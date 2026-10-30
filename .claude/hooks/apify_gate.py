#!/usr/bin/env python3
"""PreToolUse hook on mcp__Apify__call-actor: only the scrapers in growth-engine/config/apify-actors.json, with their
real input keys, a spend cap per run and no personal-data add-ons. The rules live in guards/apify_rules.py.
It fails closed (a run costs money): if the check errors, the call is blocked with the error.
"""
import json
import sys
from pathlib import Path

HOOKS = Path(__file__).resolve().parent
sys.path.insert(0, str(HOOKS))
from guards.apify_rules import check  # noqa: E402
from guards.deny import deny  # noqa: E402

CONFIG = HOOKS.parents[1] / "growth-engine" / "config" / "apify-actors.json"


def main() -> int:
    try:
        data = json.loads(sys.stdin.read() or "{}")
        reasons = check(data.get("tool_input") or {}, json.loads(CONFIG.read_text()))
    except Exception as e:  # fail closed
        reasons = [f"the Apify gate errored ({type(e).__name__}: {e}); fix .claude/hooks/guards/apify_rules.py or {CONFIG.name}"]
    if reasons:
        print(deny("APIFY RUN BLOCKED (growth-engine/config/apify-actors.json).\n- " + "\n- ".join(reasons)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
