#!/usr/bin/env python3
"""Poly: turn an approved CSV copy into a calendar draft, without importing it.
Python standard library only. No network, login, installation or calendar access.
"""
import argparse,csv,datetime,hashlib,json,os
from pathlib import Path

def escaped(value):
 return value.replace('\\','\\\\').replace('\r\n','\n').replace('\r','\n').replace('\n','\\n').replace(';','\\;').replace(',','\\,')

def folded(line):
 lines=[];part=''
 for char in line:
  if len((part+char).encode('utf-8'))>75:lines.append(part);part=' '+char
  else:part+=char
 return '\r\n'.join(lines+[part])

def instant(value):
 try:d=datetime.datetime.fromisoformat(value.strip().replace('Z','+00:00'))
 except ValueError:raise ValueError('Use an ISO date/time with an explicit timezone offset, for example 2026-11-10T09:00:00-05:00.') from None
 if d.tzinfo is None:raise ValueError('Timezone is missing. Ask the person; never guess the timezone.')
 return d.astimezone(datetime.timezone.utc)

def plan(source,output):
 source=Path(source);output=Path(output)
 if source.is_symlink() or not source.is_file() or source.stat().st_size>2_000_000:raise ValueError('Choose a CSV copy up to 2 MB, not a link.')
 if output.suffix.lower()!='.ics':raise ValueError('Choose a new .ics file; do not overwrite an existing calendar.')
 original=source.read_bytes();digest=hashlib.sha256(original).hexdigest();events=[]
 with source.open(encoding='utf-8-sig',newline='') as f:
  reader=csv.DictReader(f,strict=True)
  fields=reader.fieldnames or []
  if len(fields)!=len(set(fields)) or not {'title','start','end','source'}.issubset(fields):raise ValueError('Unique title, start, end and source columns are required; notes is optional.')
  previous_line=reader.line_num
  for row in reader:
   source_line=previous_line+1;previous_line=reader.line_num
   if len(events)>=500:raise ValueError('Choose up to 500 events.')
   if None in row or any(value is None for value in row.values()):raise ValueError('A row has the wrong number of columns.')
   title=row['title'].strip();citation=row['source'].strip();notes=row.get('notes','')
   if not title or not citation or any(len(v)>4000 for v in [title,citation,notes]):raise ValueError('Every event needs a title and source reference, up to 4000 characters per field.')
   start=instant(row['start']);end=instant(row['end'])
   if end<=start:raise ValueError('Event end must be after start.')
   events.append({'line':source_line,'title':title,'source':citation,'notes':notes,'start':start,'end':end})
 if not events:raise ValueError('No events found.')
 conflicts=[]
 for index,a in enumerate(events):
  for b in events[index+1:]:
   if max(a['start'],b['start'])<min(a['end'],b['end']):conflicts.append({'lines':[a['line'],b['line']],'issue':'overlap'})
 lines=['BEGIN:VCALENDAR','VERSION:2.0','PRODID:-//Poly A2//Calendar draft//EN','CALSCALE:GREGORIAN']
 stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
 for event in events:
  uid=hashlib.sha256(f"{digest}:{event['line']}".encode()).hexdigest()+'@polyhelper.ai'
  description=event['notes']+'\nSource: '+event['source']+f"\nCSV line: {event['line']}"
  lines+=['BEGIN:VEVENT','UID:'+uid,'DTSTAMP:'+stamp,'DTSTART:'+event['start'].strftime('%Y%m%dT%H%M%SZ'),'DTEND:'+event['end'].strftime('%Y%m%dT%H%M%SZ'),'SUMMARY:'+escaped(event['title']),'DESCRIPTION:'+escaped(description),'END:VEVENT']
 lines+=['END:VCALENDAR'];content='\r\n'.join(folded(line) for line in lines)+'\r\n'
 # Exclusive creation prevents accidental replacement, including links at the output path.
 descriptor=os.open(output,os.O_CREAT|os.O_EXCL|os.O_WRONLY,0o600)
 with os.fdopen(descriptor,'w',encoding='utf-8',newline='') as f:f.write(content)
 return {'product':'Poly A2','events':len(events),'sourceSHA256':digest,'sourceLines':[e['line'] for e in events],'conflicts':conflicts,'output':str(output),'draftOnly':True,'calendarChanged':False,'networkUsed':False,'sourceCheckRequired':True,'next':'Review every title, source, local time and overlap before deciding whether to import the draft.'}

def main():
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('source',type=Path);parser.add_argument('output',type=Path);args=parser.parse_args()
 try:print(json.dumps(plan(args.source,args.output),ensure_ascii=False,indent=2));return 0
 except (OSError,ValueError,csv.Error,UnicodeError):print(json.dumps({'product':'Poly A2','status':'not-created','message':'Check the CSV columns, explicit timezones, dates and output path. No calendar was changed.'}));return 2
if __name__=='__main__':raise SystemExit(main())
