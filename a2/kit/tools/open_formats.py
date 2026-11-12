#!/usr/bin/env python3
"""Poly: convert one explicitly chosen local copy with installed open-source tools."""
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

TOOLS = {'pdf-text': 'pdftotext', 'scan-text': 'tesseract', 'document': 'pandoc', 'audio': 'ffmpeg'}
LIMIT = 64 * 1024 * 1024


def doctor():
    # Discovery is not a functional test, licence check or permission to install.
    return {'product': 'Poly A2', 'installed': {action: bool(shutil.which(tool)) for action, tool in TOOLS.items()},
            'functionalTestPassed': False, 'installationPerformed': False}


def convert(action, source, destination, language='eng'):
    if action not in TOOLS:
        raise ValueError('Choose pdf-text, scan-text, document or audio.')
    original = Path(source).absolute()
    target = Path(destination).absolute()
    if original.is_symlink() or not original.is_file() or original.stat().st_size > LIMIT:
        raise ValueError('Choose a local file copy up to 64 MB, not a link.')
    if target.exists() or target.is_symlink() or not target.parent.is_dir():
        raise ValueError('Choose a new output filename in an existing folder.')
    extensions = {'pdf-text': {'.pdf'}, 'scan-text': {'.png', '.jpg', '.jpeg', '.tif', '.tiff'},
                  'document': {'.md', '.txt'}, 'audio': {'.wav', '.mp3', '.m4a', '.mp4', '.mov', '.ogg', '.flac'}}
    if original.suffix.lower() not in extensions[action]:
        raise ValueError('Unsupported input format for this action.')
    wanted = {'.docx', '.html'} if action == 'document' else {'.wav'} if action == 'audio' else {'.txt'}
    if target.suffix.lower() not in wanted:
        raise ValueError('Choose the expected output extension: ' + ', '.join(sorted(wanted)))
    binary = shutil.which(TOOLS[action])
    if not binary:
        raise ValueError('Required tool is not installed: ' + TOOLS[action] + '. Ask before installing it, or use the current AI with this file.')
    if not language.isascii() or not language.replace('+', '').isalpha() or len(language) > 40:
        raise ValueError('Choose installed OCR languages, for example eng or eng+rus.')
    # Stage only in our temporary folder. Copy to final output with exclusive creation.
    with tempfile.TemporaryDirectory(prefix='poly-a2-format-') as folder:
        staged = Path(folder) / ('result' + target.suffix.lower())
        if action == 'pdf-text':
            command = [binary, '-layout', str(original), str(staged)]
        elif action == 'scan-text':
            command = [binary, str(original), str(staged.with_suffix('')), '-l', language, '--psm', '6']
        elif action == 'document':
            command = [binary, '--sandbox', '--from=markdown-raw_html-raw_tex', '--standalone', '--to=' + ('docx' if target.suffix.lower() == '.docx' else 'html'), str(original), '--output', str(staged)]
        else:
            command = [binary, '-nostdin', '-v', 'error', '-n', '-protocol_whitelist', 'file,pipe', '-i', str(original), '-vn', '-c:a', 'pcm_s16le', str(staged)]
        with open(Path(folder) / 'log', 'w+b') as log:
            result = subprocess.run(command, stdin=subprocess.DEVNULL, stdout=log, stderr=log, timeout=60, cwd=folder, check=False)
            if result.returncode:
                log.seek(0)
                raise ValueError('Conversion failed; no output was saved. ' + log.read(1600).decode('utf8', errors='replace'))
        if not staged.is_file() or not 0 < staged.stat().st_size <= LIMIT:
            raise ValueError('No usable output up to 64 MB. A scanned PDF may need OCR first.')
        if action in ('pdf-text', 'scan-text') and not staged.read_text(encoding='utf8').strip():
            raise ValueError('No text was recognised. Try a clearer copy or an appropriate OCR language; no output was saved.')
        created = False
        try:
            with target.open('xb') as output:
                created = True
                os.chmod(target, 0o600)
                with staged.open('rb') as incoming:
                    shutil.copyfileobj(incoming, output)
        except BaseException:
            if created:
                target.unlink(missing_ok=True)
            raise
    return {'product': 'Poly A2', 'action': action, 'source': original.name, 'output': str(target),
            'bytes': target.stat().st_size, 'sourceCheckRequired': True, 'inputChanged': False,
            'installationPerformed': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['doctor', *TOOLS])
    parser.add_argument('--input'); parser.add_argument('--output'); parser.add_argument('--language', default='eng')
    args = parser.parse_args()
    try:
        if args.action == 'doctor':
            result = doctor()
        else:
            if not args.input or not args.output:
                raise ValueError('Choose --input and a new --output filename.')
            result = convert(args.action, args.input, args.output, args.language)
    except (ValueError, OSError, subprocess.TimeoutExpired) as error:
        parser.exit(1, str(error) + '\n')
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
