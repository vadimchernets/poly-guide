#!/usr/bin/env python3
"""Poly: portable personal review rules; offline, Python standard library."""
import argparse
import hashlib
import json
import re
from pathlib import Path

COPY = json.loads(Path(__file__).with_name('QUALITY-TEXT.json').read_text(encoding='utf-8'))
MAX_BYTES = 2_000_000


def read_text(path):
    path = Path(path)
    if not path.is_file() or path.stat().st_size > MAX_BYTES:
        raise ValueError('input-missing-or-too-large')
    return path.read_bytes().decode('utf-8')


def digest(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def read_json(path):
    return json.loads(read_text(path))


def save_json(path, value):
    with Path(path).open('x', encoding='utf-8') as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2, allow_nan=False)
        stream.write('\n')


def load_rules(path):
    rules = read_json(path)
    if not isinstance(rules, dict) or not isinstance(rules.get('use_when'), str) or not rules['use_when'].strip():
        raise ValueError('use-when-required')
    criteria = rules.get('criteria')
    if not isinstance(criteria, list) or not 5 <= len(criteria) <= 8:
        raise ValueError('five-to-eight-rules-required')
    ids = []
    for rule in criteria:
        if not isinstance(rule, dict) or not re.fullmatch(r'[a-z0-9-]{1,48}', str(rule.get('id', ''))):
            raise ValueError('invalid-rule-id')
        if not isinstance(rule.get('text'), str) or not rule['text'].strip():
            raise ValueError('rule-text-required')
        ids.append(rule['id'])
    if len(set(ids)) != len(ids):
        raise ValueError('duplicate-rule-id')
    return rules


def verify_review(rules, source, review):
    """Verify coverage and quote locations, never the model's semantic verdict."""
    if not isinstance(review, dict) or review.get('source_sha256') != digest(source):
        raise ValueError('source-hash-mismatch')
    rows = review.get('checks')
    ids = [rule['id'] for rule in rules['criteria']]
    if not isinstance(rows, list) or len(rows) != len(ids) or {r.get('id') for r in rows if isinstance(r, dict)} != set(ids):
        raise ValueError('rule-coverage-mismatch')
    lines = source.splitlines()
    located = 0
    for row in rows:
        if row.get('verdict') not in ('pass', 'fail', 'unclear'):
            raise ValueError('invalid-verdict')
        if not isinstance(row.get('reason'), str) or not row['reason'].strip():
            raise ValueError('reason-required')
        if not isinstance(row.get('suggestion'), str):
            raise ValueError('suggestion-required')
        if row['verdict'] == 'fail' and not row['suggestion'].strip():
            raise ValueError('failed-rule-needs-suggestion')
        quote = row.get('quote')
        start, end = row.get('start_line'), row.get('end_line')
        if quote == '' and row['verdict'] == 'unclear' and start is None and end is None:
            continue
        if (not isinstance(quote, str) or not quote.strip() or type(start) is not int
                or type(end) is not int or not 1 <= start <= end <= len(lines)):
            raise ValueError('quote-and-lines-required')
        if quote not in '\n'.join(lines[start - 1:end]):
            raise ValueError('quote-not-at-lines')
        located += 1
    return {'rules_checked': len(ids), 'quotes_located': located,
            'traceability': 'checked', 'semantic_verdict': 'not-verified',
            'human_acceptance': 'not-recorded'}


def create(args):
    rules = load_rules(args.rules)
    source = read_text(args.source)
    copy = COPY[args.locale]
    if len('Poly. ' + rules['use_when']) > 1024 or any(c in rules['use_when'] for c in '<>'):
        raise ValueError('use-when-too-long-or-invalid')
    out = Path(args.output)
    # Validate every input before creating anything; never merge into an existing skill.
    out.mkdir(parents=True, exist_ok=False, mode=0o700)
    save_json(out / 'rules.json', rules)
    (out / 'EXAMPLE.txt').write_text(source, encoding='utf-8')
    description = 'Poly. ' + rules['use_when']
    skill = ('---\nname: poly-a2-quality-rules\ndescription: ' + json.dumps(description, ensure_ascii=False)
             + '\n---\n\n# Poly — ' + copy['standardTitle'] + '\n\n' + copy['skillBody']
             + '\n\n' + '\n'.join(f"- {r['id']}: {r['text']}" for r in rules['criteria']) + '\n')
    skill += '\n\n<!-- Poly: technical procedure; explicit saved audit only. Never include in recipient text. -->\nOnly for an explicitly requested saved audit: copy REVIEW-TEMPLATE.json; source_sha256 = SHA256(exact UTF-8 input). Fill every checks[].id, verdict (pass/fail/unclear), reason, suggestion and exact quote with 1-based start_line/end_line. No evidence: unclear, empty quote, null lines. Run from this folder: `python3 scripts/quality_skill.py check --rules rules.json --source /path/to/actual.txt --review /path/to/review.json --output /path/to/new-receipt.json`. Inspect judgments separately; exit 0 confirms coverage and quote locations only. Keep audit files and all status information separate from recipient text.\n'
    (out / 'SKILL.md').write_text(skill, encoding='utf-8')
    (out / 'scripts').mkdir(mode=0o700)
    for name in ('quality_skill.py', 'QUALITY-TEXT.json'):
        (out / 'scripts' / name).write_bytes(Path(__file__).with_name(name).read_bytes())
    save_json(out / 'REVIEW-TEMPLATE.json', {'source_sha256': digest(source), 'checks': [
        {'id': r['id'], 'verdict': 'unclear', 'reason': '', 'suggestion': '',
         'quote': '', 'start_line': None, 'end_line': None} for r in rules['criteria']]})
    save_json(out / 'MANIFEST.json', {'product': 'Poly A2', 'locale': args.locale,
              'files': {name: digest(read_text(out / name)) for name in ('SKILL.md', 'rules.json', 'EXAMPLE.txt', 'REVIEW-TEMPLATE.json', 'scripts/quality_skill.py', 'scripts/QUALITY-TEXT.json')},
              'source_sha256': digest(source), 'installed': False,
              'usefulness': 'not-verified'})
    return {'product': 'Poly A2', 'created': str(out), 'installed': False}


def check(args):
    rules = load_rules(args.rules)
    source = read_text(args.source)
    review = read_json(args.review)
    result = verify_review(rules, source, review)
    result.update(product='Poly A2', source_sha256=digest(source), review_sha256=digest(read_text(args.review)))
    save_json(args.output, result)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    make = sub.add_parser('create')
    make.add_argument('--rules', required=True)
    make.add_argument('--source', required=True)
    make.add_argument('--output', required=True)
    make.add_argument('--locale', choices=COPY, default='en')
    verify = sub.add_parser('check')
    for flag in ('rules', 'source', 'review', 'output'):
        verify.add_argument('--' + flag, required=True)
    args = parser.parse_args()
    try:
        print(json.dumps(create(args) if args.command == 'create' else check(args), ensure_ascii=False))
        return 0
    except (OSError, ValueError, TypeError, KeyError, AttributeError) as error:
        print(json.dumps({'product': 'Poly A2', 'error': str(error)}, ensure_ascii=False))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
