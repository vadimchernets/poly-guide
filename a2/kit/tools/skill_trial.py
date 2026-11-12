#!/usr/bin/env python3
"""Poly: blind comparison of actual saved answers; no model or network calls."""
import argparse
import json
import math
import secrets
from pathlib import Path
from quality_skill import digest, load_rules, read_json, read_text, save_json, verify_review


def prepare(args):
    config = read_json(args.cases)
    rules = load_rules(args.rules)
    cases = config.get('cases', [])
    if len(cases) != 3 or {c.get('kind') for c in cases} != {'ordinary', 'edge', 'unrelated'}:
        raise ValueError('three-real-cases-required')
    # Load before creating output. One agreed task/source pair applies to both answers.
    loaded = []
    for case in cases:
        if case.get('expected_use') not in ('use', 'skip'):
            raise ValueError('expected-use-required')
        values = {key: read_text(case[key]) for key in ('task', 'source', 'without', 'with')}
        times = case.get('seconds', {})
        if set(times) - {'with', 'without'} or any(type(t) not in (float, int) or not math.isfinite(t) or t <= 0 for t in times.values()):
            raise ValueError('invalid-measured-seconds')
        loaded.append((case, values))
    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=False, mode=0o700)
    public = out / 'BLIND'
    private = out / 'PRIVATE'
    public.mkdir(mode=0o700)
    private.mkdir(mode=0o700)
    save_json(public / 'rules.json', rules)
    mapping, files, original = {}, {}, {}
    for number, (case, values) in enumerate(loaded, 1):
        key = str(number)
        folder = public / key
        folder.mkdir(mode=0o700)
        roles = ['with', 'without']
        secrets.SystemRandom().shuffle(roles)
        mapping[key] = dict(zip(('A', 'B'), roles))
        original[key] = {'kind': case['kind'], 'expected_use': case['expected_use'],
                         'seconds': case.get('seconds', {}),
                         'provenance': case.get('provenance', 'not-recorded'),
                         'originals': {k: {'path': str(Path(case[k]).resolve()), 'sha256': digest(v)} for k, v in values.items()}}
        for filename, text in [('TASK.txt', values['task']), ('SOURCE.txt', values['source']),
                               ('A.txt', values[roles[0]]), ('B.txt', values[roles[1]])]:
            path = folder / filename
            path.write_text(text, encoding='utf-8')
    for path in sorted(public.rglob('*')):
        if path.is_file():
            files[str(path.relative_to(public))] = digest(read_text(path))
    save_json(private / 'KEY.json', {'product': 'Poly A2', 'mapping': mapping,
                                     'cases': original, 'files': files,
                                     'rules_original': {'path': str(Path(args.rules).resolve()), 'sha256': digest(read_text(args.rules))}})
    return {'product': 'Poly A2', 'blind_folder': str(public), 'cases': 3, 'choice': 'pending'}


def intact(out):
    key = read_json(out / 'PRIVATE/KEY.json')
    public = out / 'BLIND'
    actual = {str(p.relative_to(public)): digest(read_text(p)) for p in public.rglob('*') if p.is_file()}
    if actual != key['files']:
        raise ValueError('blind-files-changed')
    if digest(read_text(key['rules_original']['path'])) != key['rules_original']['sha256']:
        raise ValueError('rules-original-changed')
    for case in key['cases'].values():
        for original in case['originals'].values():
            if digest(read_text(original['path'])) != original['sha256']:
                raise ValueError('original-changed')
    return key


def decide(args):
    out = Path(args.folder)
    key = intact(out)
    decision = read_json(args.decision)
    rows = decision.get('cases', [])
    if len(rows) != 3 or {str(c.get('id')) for c in rows} != set(key['mapping']):
        raise ValueError('all-three-decisions-required')
    rules = load_rules(out / 'BLIND/rules.json')
    receipts = {}
    for row in rows:
        number = str(row['id'])
        if row.get('choice') not in ('A', 'B', 'tie', 'undecided') or not str(row.get('reason', '')).strip():
            raise ValueError('choice-and-reason-required')
        receipts[number] = {}
        for label in ('A', 'B'):
            source = read_text(out / 'BLIND' / number / (label + '.txt'))
            review = row.get('reviews', {}).get(label)
            receipts[number][label] = verify_review(rules, source, review)
            if row.get('activation', {}).get(label) not in ('use', 'skip', 'unknown'):
                raise ValueError('activation-observation-required')
    save_json(out / 'DECISION.json', {'product': 'Poly A2', 'decision': decision, 'receipts': receipts,
              'blind_hashes': key['files'], 'semantic_verdict': 'not-verified',
              'decider': decision.get('decider', 'not-recorded')})
    return {'product': 'Poly A2', 'decision_saved': True, 'origins_revealed': False}


def reveal(args):
    out = Path(args.folder)
    key = intact(out)
    decision = read_json(out / 'DECISION.json')
    if decision['blind_hashes'] != key['files']:
        raise ValueError('decision-inputs-changed')
    results = []
    for row in decision['decision']['cases']:
        number = str(row['id'])
        case = key['cases'][number]
        results.append({'id': number, 'kind': case['kind'], 'choice': row['choice'],
                        'selected_origin': key['mapping'][number].get(row['choice'], row['choice']),
                        'origins': key['mapping'][number], 'seconds': case['seconds'],
                        'expected_use': case['expected_use'], 'activation': row['activation'],
                        'provenance': case['provenance'], 'reason': row['reason']})
    result = {'product': 'Poly A2', 'cases': results, 'semantic_verdict': 'not-verified',
              'decider': decision['decider'], 'usefulness': 'requires-persons-judgment'}
    save_json(out / 'RESULT.json', result)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    prepare_parser = sub.add_parser('prepare')
    for name in ('cases', 'rules', 'output'):
        prepare_parser.add_argument('--' + name, required=True)
    decide_parser = sub.add_parser('decide')
    decide_parser.add_argument('--folder', required=True)
    decide_parser.add_argument('--decision', required=True)
    reveal_parser = sub.add_parser('reveal')
    reveal_parser.add_argument('--folder', required=True)
    args = parser.parse_args()
    try:
        print(json.dumps(globals()[args.command](args), ensure_ascii=False))
        return 0
    except (OSError, ValueError, TypeError, KeyError, AttributeError) as error:
        print(json.dumps({'product': 'Poly A2', 'error': str(error)}, ensure_ascii=False))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
