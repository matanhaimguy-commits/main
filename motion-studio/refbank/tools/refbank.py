#!/usr/bin/env python3
"""Reference bank: search proven reels, pick fresh references per client, and log what each film used.

    python3 refbank/tools/refbank.py build                      # cards/*.md -> index.json (validates tags)
    python3 refbank/tools/refbank.py search [--q text] [--category c] [--tag slug] [--fit f] [--engine e]
                                            [--min-plays N] [--max-difficulty D] [--n 20]
    python3 refbank/tools/refbank.py pick --client straightscale [--fit agency] [--category c] [--q text] [--n 6]
    python3 refbank/tools/refbank.py check --client straightscale --devices a,b [--category c] [--palette dark]
    python3 refbank/tools/refbank.py log --client straightscale --project straightscale-04 --refs id1,id2
                                         --category kinetic-type --devices focus-brackets,word-stack
                                         --palette light --camera "locked, focus pulls" --engine canvas
                                         --hook question [--concept "..."] [--language sq] [--date 2026-10-20]
    python3 refbank/tools/refbank.py history --client straightscale
    python3 refbank/tools/refbank.py stats

Anti-repetition rule (enforced by `pick` and `check`): a client's next film may not reuse a reference it already
used, its previous film's category, or the signature device of any of its last 3 films, and it should share at
most one device with its last film. Paths are relative to this file, so it runs from any directory.
"""
import datetime, json, os, re, sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARDS, INDEX, LEDGER, TAGS = (os.path.join(ROOT, p) for p in ('cards', 'index.json', 'ledger.json', 'TAGS.md'))
LIST_FIELDS = ('hook', 'devices', 'palette', 'sound', 'engine', 'fit')
REQUIRED = ('id', 'title', 'url', 'platform', 'creator', 'plays', 'category', 'hook', 'devices', 'energy', 'engine',
            'fit', 'wow', 'relevance', 'difficulty')
RECENT = 3


def arg(name, default=None):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else default


def csv(name):
    v = arg(name)
    return [x.strip() for x in v.split(',') if x.strip()] if v else []


def vocab():
    """Slugs per section of TAGS.md (category table rows, then '·'-separated lists)."""
    text, out, sec = open(TAGS).read(), {}, None
    for line in text.splitlines():
        m = re.match(r'## (\w+)', line)
        if m:
            sec = m.group(1); out[sec] = set(); continue
        if not sec:
            continue
        if line.startswith('| ') and not line.startswith('| slug') and not line.startswith('|---'):
            out[sec].add(line.split('|')[1].strip())
        elif '·' in line or (line and not line.startswith(('|', '#')) and sec in ('hook', 'devices', 'energy', 'palette', 'sound', 'engine', 'fit')):
            body = line.split(':', 1)[1] if ':' in line.split('·')[0] and sec == 'devices' else line
            for s in body.split('·'):
                s = s.strip().split(' ')[0]
                if s: out[sec].add(s)
    return out


def load_cards():
    cards = []
    for f in sorted(os.listdir(CARDS)):
        if not f.endswith('.md'):
            continue
        text = open(os.path.join(CARDS, f)).read()
        m = re.match(r'---\n(.*?)\n---\n(.*)', text, re.S)
        if not m:
            print('no front matter:', f); continue
        meta = yaml.safe_load(m.group(1))
        meta['file'] = 'cards/' + f
        body = m.group(2)
        one = re.search(r'## The film in one line\n+(.+)', body)
        meta['summary'] = one.group(1).strip() if one else ''
        cards.append(meta)
    return cards


def build():
    v, cards, problems = vocab(), load_cards(), []
    ids = set()
    for c in cards:
        for k in REQUIRED:
            if c.get(k) in (None, '', []):
                problems.append(f"{c.get('id', c['file'])}: missing {k}")
        if c.get('id') in ids:
            problems.append(f"duplicate id {c['id']}")
        ids.add(c.get('id'))
        if c.get('category') not in v.get('category', set()):
            problems.append(f"{c['id']}: unknown category {c.get('category')}")
        for k, sec in (('hook', 'hook'), ('devices', 'devices'), ('energy', 'energy'), ('palette', 'palette'),
                       ('sound', 'sound'), ('fit', 'fit')):
            vals = c.get(k) or []
            for s in ([vals] if isinstance(vals, str) else vals):
                if s not in v.get(sec, set()):
                    problems.append(f"{c['id']}: unknown {k} '{s}' (add it to TAGS.md or use an existing slug)")
        for s in c.get('engine') or []:
            if s.split(':')[0] not in {e.split(':')[0] for e in v.get('engine', set())}:
                problems.append(f"{c['id']}: unknown engine '{s}'")
    keep = ('id', 'title', 'summary', 'url', 'platform', 'creator', 'plays', 'likes', 'shares', 'followers', 'posted',
            'duration_s', 'category', 'hook', 'devices', 'energy', 'palette', 'palette_hex', 'sound', 'voiceover',
            'text_on_screen', 'engine', 'difficulty', 'fit', 'wow', 'relevance', 'pacing', 'file')
    index = sorted(({k: c.get(k) for k in keep} for c in cards), key=lambda c: (c['category'] or '', -(c['plays'] or 0)))
    json.dump({'built': datetime.date.today().isoformat(), 'count': len(index), 'cards': index},
              open(INDEX, 'w'), indent=1, default=str)
    print(f'{len(index)} cards -> index.json')
    for p in problems:
        print('  WARN', p)
    return 0 if not problems else 1


def index():
    if not os.path.exists(INDEX):
        build()
    return json.load(open(INDEX))['cards']


def ledger():
    return json.load(open(LEDGER)) if os.path.exists(LEDGER) else {'clients': {}}


def text_of(c):
    return ' '.join(str(c.get(k) or '') for k in ('id', 'title', 'summary', 'category', 'creator')) + ' ' + \
           ' '.join(' '.join(c.get(k) or []) for k in LIST_FIELDS)


def matches(c):
    q = (arg('--q') or '').lower()
    if q and not all(w in text_of(c).lower() for w in q.split()):
        return False
    if arg('--category') and c.get('category') != arg('--category'):
        return False
    tag = arg('--tag')
    if tag and not any(tag in (c.get(k) or []) for k in LIST_FIELDS):
        return False
    if arg('--fit') and not ({arg('--fit'), 'any'} & set(c.get('fit') or [])):
        return False
    if arg('--engine') and not any(e.startswith(arg('--engine')) for e in c.get('engine') or []):
        return False
    if arg('--min-plays') and (c.get('plays') or 0) < float(arg('--min-plays')):
        return False
    if arg('--max-difficulty') and (c.get('difficulty') or 5) > int(arg('--max-difficulty')):
        return False
    return True


def show(rows, why=None):
    for c in rows:
        plays = (c.get('plays') or 0) / 1e6
        print(f"{c['id']:42} {plays:6.1f}M  {c['category']:16} wow {c.get('wow')} rel {c.get('relevance')} "
              f"diff {c.get('difficulty')}  {', '.join((c.get('devices') or [])[:3])}")
        print(f"{'':42} {c.get('summary', '')[:110]}")
        if why and why.get(c['id']):
            print(f"{'':42} note: {why[c['id']]}")


def recent(client, k=RECENT):
    films = ledger()['clients'].get(client, [])
    return sorted(films, key=lambda f: f.get('date', ''))[-k:]


def conflicts(client, category=None, devices=(), refs=()):
    films = ledger()['clients'].get(client, [])
    last = recent(client)
    out = []
    used_refs = {r for f in films for r in f.get('refs', [])}
    for r in refs:
        if r in used_refs:
            out.append(f'reference {r} was already used for {client}')
    if last and category and category == last[-1].get('category'):
        out.append(f"category {category} repeats the previous film ({last[-1].get('project')})")
    sig = {f['devices'][0]: f.get('project') for f in last if f.get('devices')}
    if devices and devices[0] in sig:
        out.append(f"signature device {devices[0]} was the signature of {sig[devices[0]]}")
    if last and devices:
        shared = set(devices) & set(last[-1].get('devices', []))
        if len(shared) > 1:
            out.append(f"shares {len(shared)} devices with {last[-1].get('project')}: {', '.join(sorted(shared))}")
    return out


def pick():
    client = arg('--client') or sys.exit('pick needs --client')
    films = ledger()['clients'].get(client, [])
    used = {r for f in films for r in f.get('refs', [])}
    last = recent(client)
    last_devices = {d for f in last for d in f.get('devices', [])}
    last_sigs = {f['devices'][0] for f in last if f.get('devices')}
    last_cat = last[-1].get('category') if last else None
    scored, why = [], {}
    for c in index():
        if not matches(c) or c['id'] in used:
            continue
        devs = c.get('devices') or []
        if devs and devs[0] in last_sigs:
            continue
        score = 2 * (c.get('relevance') or 0) + 1.5 * (c.get('wow') or 0) - 0.8 * (c.get('difficulty') or 3)
        score -= 1.2 * len(set(devs) & last_devices)
        if c.get('category') == last_cat:
            score -= 4
        scored.append((score, c))
        notes = []
        if set(devs) & last_devices:
            notes.append('overlaps recent devices: ' + ', '.join(sorted(set(devs) & last_devices)))
        if c.get('category') == last_cat:
            notes.append('same category as the last film (only as a secondary reference)')
        why[c['id']] = '; '.join(notes)
    scored.sort(key=lambda x: -x[0])
    n = int(arg('--n', 6))
    print(f"{client}: {len(films)} films logged; avoiding refs {sorted(used) or '-'}, signatures {sorted(last_sigs) or '-'}, "
          f"last category {last_cat or '-'}")
    show([c for _, c in scored[:n]], why)


def log():
    client = arg('--client') or sys.exit('log needs --client')
    entry = {
        'project': arg('--project'), 'date': arg('--date', datetime.date.today().isoformat()),
        'concept': arg('--concept', ''), 'refs': csv('--refs'), 'category': arg('--category'),
        'devices': csv('--devices'), 'hook': csv('--hook'), 'palette': csv('--palette'),
        'palette_hex': csv('--palette-hex'), 'camera': arg('--camera', ''), 'engine': csv('--engine'),
        'music': arg('--music', ''), 'language': csv('--language'),
    }
    for w in conflicts(client, entry['category'], entry['devices'], entry['refs']):
        print('  WARN', w)
    L = ledger()
    L['clients'].setdefault(client, []).append(entry)
    json.dump(L, open(LEDGER, 'w'), indent=1, ensure_ascii=False)
    print(f"logged {entry['project']} for {client}")


def check():
    client = arg('--client') or sys.exit('check needs --client')
    w = conflicts(client, arg('--category'), csv('--devices'), csv('--refs'))
    print('\n'.join('  WARN ' + x for x in w) if w else 'ok: no repeats against the last films')
    return 1 if w else 0


def history():
    client = arg('--client') or sys.exit('history needs --client')
    for f in sorted(ledger()['clients'].get(client, []), key=lambda f: f.get('date', '')):
        print(f"{f.get('date')}  {f.get('project'):22} {f.get('category') or '-':16} sig {(f.get('devices') or ['-'])[0]:18} "
              f"refs {','.join(f.get('refs') or []) or '-'}  | {f.get('concept', '')[:70]}")


def stats():
    from collections import Counter
    cards = index()
    print(len(cards), 'cards')
    for k in ('category', 'energy', 'platform'):
        print(k, dict(Counter(c.get(k) for c in cards).most_common()))
    print('top devices', Counter(d for c in cards for d in c.get('devices') or []).most_common(25))
    print('engines', Counter((c.get('engine') or ['-'])[0] for c in cards).most_common())


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    if cmd == 'build': sys.exit(build())
    elif cmd == 'search': show([c for c in index() if matches(c)][: int(arg('--n', 20))])
    elif cmd == 'pick': pick()
    elif cmd == 'log': log()
    elif cmd == 'check': sys.exit(check())
    elif cmd == 'history': history()
    elif cmd == 'stats': stats()
    else: sys.exit(__doc__)
