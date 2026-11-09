#!/usr/bin/env python3
"""Poly A2 local text library. Python/SQLite; no network, telemetry or external AI."""
import hashlib
import argparse
import json
import os
from pathlib import Path
import sqlite3

MAX_BYTES=2_000_000
EXTENSIONS={'.txt','.md','.csv'}
def index(folder,database):
    root=Path(folder).resolve(strict=True)
    if not root.is_dir():raise ValueError('Choose a folder with copies of your materials.')
    db=Path(database).resolve()
    if db.exists():raise ValueError('Choose a new index filename; existing files are kept.')
    candidates=[];sources=[];total_bytes=0
    for path in sorted(root.rglob('*')):
        if not path.is_symlink() and not path.is_file():continue
        item={'file':str(path.relative_to(root)),'status':'skipped','reason':None}
        sources.append(item)
        if len(sources)>1000:raise ValueError('Choose a smaller folder (up to 1000 files).')
        if path.is_symlink():item['reason']='symbolic-link';continue
        if not path.resolve().is_relative_to(root):item['reason']='outside-folder';continue
        if path.suffix.lower() not in EXTENSIONS:item['reason']='unsupported-format';continue
        if path.stat().st_size>MAX_BYTES:item['reason']='file-too-large';continue
        total_bytes+=path.stat().st_size
        if total_bytes>20_000_000:raise ValueError('Choose a smaller folder (up to 20 MB of text in total).')
        candidates.append((path,item))
    # Read first, so an unreadable source is explicitly reported, not silently omitted.
    rows=[]
    for path,item in candidates:
        try:
            data=path.read_bytes()
            if len(data)>MAX_BYTES:item['reason']='file-too-large';continue
            text=data.decode('utf-8-sig')
        except UnicodeError:item['reason']='not-utf8';continue
        except OSError:item['reason']='cannot-read';continue
        lines=text.splitlines()
        item.update(status='indexed',reason=None,sha256=hashlib.sha256(data).hexdigest(),lines=len(lines),truncatedLines=sum(len(line)>10000 for line in lines))
        for number,line in enumerate(lines,1):
            if line.strip():rows.append((item['file'],number,line[:10000]))
    db.parent.mkdir(parents=True,exist_ok=True)
    fd=os.open(db,os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o600);os.close(fd)
    with sqlite3.connect(db) as con:
        con.execute('CREATE TABLE lines (file TEXT, line INTEGER, text TEXT)')
        con.executemany('INSERT INTO lines VALUES (?,?,?)',rows)
        con.execute('CREATE TABLE inventory (file TEXT PRIMARY KEY, record TEXT)')
        con.executemany('INSERT INTO inventory VALUES (?,?)',[(item['file'],json.dumps(item)) for item in sources])
    return {'product':'Poly A2','indexedFiles':sum(item['status']=='indexed' for item in sources),'lines':len(rows),'skippedFiles':sum(item['status']=='skipped' for item in sources),'sources':sources,'database':str(db),'networkUsed':False,'sourceCheckRequired':True}
def verify(folder,database):
    root=Path(folder).resolve(strict=True)
    if not root.is_dir():raise ValueError('Choose the original folder of copies.')
    db=Path(database).resolve(strict=True)
    with sqlite3.connect(db.as_uri()+'?mode=ro',uri=True) as con:
        if not con.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='inventory'").fetchone():raise ValueError('This older index has no source inventory. Create a new index; the old file is kept.')
        sources=[json.loads(row[0]) for row in con.execute('SELECT record FROM inventory ORDER BY file')]
    results=[]
    for item in sources:
        if item['status']!='indexed':continue
        rel=Path(item['file'])
        if rel.is_absolute() or '..' in rel.parts:raise ValueError('The index contains an invalid source path.')
        path=root/rel;status='unchanged'
        if path.is_symlink() or not path.resolve().is_relative_to(root):status='not-checked'
        else:
            try:
                if not path.is_file():status='missing'
                elif path.stat().st_size>MAX_BYTES:status='changed'
                elif hashlib.sha256(path.read_bytes()).hexdigest()!=item['sha256']:status='changed'
            except OSError:status='not-checked'
        results.append({'file':item['file'],'status':status})
    known={item['file'] for item in sources}
    added=[]
    for path in root.rglob('*'):
        if path.is_file() and path.resolve()!=db and str(path.relative_to(root)) not in known:
            added.append(str(path.relative_to(root)))
            if len(added)>1000:raise ValueError('Choose a smaller folder (up to 1000 added files).')
    return {'product':'Poly A2','sources':results,'addedFiles':sorted(added),'allIndexedSourcesUnchanged':all(item['status']=='unchanged' for item in results),'sourceContentsVerified':False,'networkUsed':False}
def search(database,query,folder=None):
    if not query.strip() or len(query)>300:raise ValueError('Use a search phrase of 1–300 characters.')
    db=Path(database).resolve(strict=True)
    with sqlite3.connect(db.as_uri()+'?mode=ro',uri=True) as con:
        # Unicode-aware matching through Python, not SQLite ASCII-only lower(). Literal search, not SQL or a regex.
        found=[]
        for file,line,text in con.execute('SELECT file,line,text FROM lines ORDER BY file,line'):
            if query.casefold() in text.casefold():
                found.append({'file':file,'line':line,'text':text})
                if len(found)==30:break
    result={'product':'Poly A2','matches':found,'limit':30,'sourceCheckRequired':True,
            'matchLimitReached':len(found)==30,'sourceLinesChecked':False}
    if folder is None:
        for match in found:match['sourceStatus']='not-checked'
        return result
    root=Path(folder).resolve(strict=True)
    freshness=verify(root,db)
    statuses={item['file']:item['status'] for item in freshness['sources']}
    checked=[];withheld=[];originals={}
    for match in found:
        file=match['file'];status=statuses.get(file,'not-checked')
        if status=='unchanged':
            if file not in originals:
                path=root/file
                try:
                    # Re-read the original, not the saved snippet. Reject a changed path.
                    if path.is_symlink() or not path.resolve().is_relative_to(root) or path.stat().st_size>MAX_BYTES:
                        originals[file]=None
                    else:originals[file]=path.read_bytes().decode('utf-8-sig').splitlines()
                except (OSError,UnicodeError):originals[file]=None
            lines=originals[file];number=match['line']
            if lines is None:status='not-checked'
            elif not isinstance(number,int) or number<1 or number>len(lines) or lines[number-1][:10000]!=match['text']:
                status='line-mismatch'
            else:
                checked.append({**match,'sourceStatus':'line-matched','truncated':len(lines[number-1])>10000})
                continue
        withheld.append({'file':file,'line':match['line'],'sourceStatus':status})
    result.update(matches=checked,withheldMatches=withheld,sourceLinesChecked=True,
                  freshness=freshness,sourceMeaningVerified=False)
    return result
def main():
    parser=argparse.ArgumentParser(description=__doc__);sub=parser.add_subparsers(dest='action',required=True)
    a=sub.add_parser('index');a.add_argument('--folder',required=True);a.add_argument('--database',required=True)
    v=sub.add_parser('verify');v.add_argument('--folder',required=True);v.add_argument('--database',required=True)
    b=sub.add_parser('search');b.add_argument('--database',required=True);b.add_argument('--query',required=True);b.add_argument('--folder')
    args=parser.parse_args()
    try:result=index(args.folder,args.database) if args.action=='index' else verify(args.folder,args.database) if args.action=='verify' else search(args.database,args.query,args.folder)
    except (ValueError,OSError,sqlite3.Error) as error:parser.exit(1,str(error)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
