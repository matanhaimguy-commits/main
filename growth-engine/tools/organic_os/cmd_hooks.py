"""organic.py hooks <slug> <hooks.json> [--library F] [--phrases F]

hooks.json is a list of stacks: {"id", "text", "spoken", "visual", "format_id", "voc_ids": [...], "story": false}.
A stack passes only with a proven format (3x+), the buyers' own words, and plain spoken English.
A grader's opinion comes after this check, never instead of it.
"""
from __future__ import annotations

import json
from pathlib import Path

from .files import client_dir
from .hook_rules import form_issues
from .hook_sources import buyer_vocab, library, phrases, source_issues


def check_stacks(stacks: list[dict], lib: dict, ph: dict) -> dict[str, list[str]]:
    vocab = buyer_vocab(ph)
    return {s.get("id", f"#{i + 1}"): source_issues(s, lib, ph) + form_issues(s, vocab) for i, s in enumerate(stacks)}


def run(a) -> int:
    base = client_dir(a.slug) / "research"
    lib_p = Path(a.library) if a.library else base / "hook-library-en.md"
    ph_p = Path(a.phrases) if a.phrases else base / "buyer-phrases-en.md"
    for p in (lib_p, ph_p):
        if not p.exists():
            print(f"FAIL missing {p}: no hook can pass without the library and the buyer phrases")
            return 1
    stacks = json.loads(Path(a.hooks).read_text())
    results = check_stacks(stacks, library(lib_p), phrases(ph_p))
    for sid, issues in results.items():
        print(f"{'PASS' if not issues else 'FAIL'} {sid}")
        for i in issues:
            print(f"   - {i}")
    passed = sum(1 for v in results.values() if not v)
    print(f"{passed} of {len(results)} stacks pass")
    return 0 if passed else 1
