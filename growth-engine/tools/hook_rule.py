"""The twin hook rule (Matan, 29 Oct 2026). A hook passes when, in one blind run, BOTH fresh graders score it at least as
well as BOTH anchors (2 proven winner hooks that rode in the same packet) on EVERY channel (visual, text, spoken), and
it fails none of the 9 checks (gates) for either grader. Each grader is compared with its own grades of the anchors, so
a harsh or kind grader moves the hook and the anchors together. A channel with no real grade, for the hook or for an
anchor, cannot pass. Pure functions. Tests: test_hook_rule.py.

A run is {"packet": "packet-v2", "graders": [{"hook": {"visual","text","spoken","gates_failed"},
"anchors": {"<anchor id>": {"visual","text","spoken","gates_failed"}}}, ...]}."""
from __future__ import annotations

from hook_anchors import CHANNELS, PACKET, anchor_ids
from hook_grades import rank

GRADERS = 2


def grader_problems(n: int, g: dict, ids: list[str]) -> list[str]:
    """Why grader n's read does not clear the rule (empty: it clears it)."""
    hook, anchors, why = g.get("hook") or {}, g.get("anchors") or {}, []
    if not isinstance(hook.get("gates_failed"), list):
        why.append(f"grader {n}: no list of failed checks for the hook (an empty list means none failed)")
    elif hook["gates_failed"]:
        why.append(f"grader {n}: the hook fails check(s) {hook['gates_failed']}")
    for ch in CHANNELS:
        mine = rank(hook.get(ch))
        if mine is None:
            why.append(f"grader {n}: no {ch} grade for the hook")
            continue
        for aid in ids:
            theirs = rank((anchors.get(aid) or {}).get(ch))
            if theirs is None:
                why.append(f"grader {n}: no {ch} grade for {aid}, so the hook cannot be compared")
            elif mine < theirs:
                why.append(f"grader {n}: {ch} {hook[ch]} is below {aid} ({anchors[aid][ch]})")
    return why


def judge(run: dict, ids: list[str] | None = None) -> dict:
    """{"pass": bool, "why": [...]}: one reason per shortfall; empty `why` means pass."""
    ids, graders, why = ids or anchor_ids(), run.get("graders") or [], []
    if run.get("packet") != PACKET:
        why.append(f"the run did not use {PACKET}")
    if len(graders) != GRADERS:
        why.append(f"the rule needs {GRADERS} fresh graders in one run, got {len(graders)}")
    if len(graders) == GRADERS and graders[0] == graders[1]:
        why.append("the 2 graders' reads are identical: one read counted twice is not 2 fresh graders")
    for n, g in enumerate(graders, 1):
        why += grader_problems(n, g, ids)
    return {"pass": not why, "why": why}
