#!/usr/bin/env python3
"""PreToolUse hook: blocks image, video and audio generation unless the post's gates have passed.

Spec: growth-engine/production/VISUAL-QA.md section 9.2. The checks live in growth-engine/tools/pipeline.py
(check_call), so `pipeline.py check-call <tool> <input.json>` shows the same answer from the shell.
The gate fails closed: if the check itself errors, the call is blocked with the error.
"""
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "growth-engine" / "tools"))
sys.path.insert(0, str(Path(__file__).resolve().parent))


def main() -> int:
    raw = sys.stdin.read()
    try:
        data = json.loads(raw or "{}")
        import pipeline
        from guards.tool_names import canonical
        tool = canonical(data.get("tool_name", ""), pipeline.STANDARDS["gated_tools"])
        if tool not in pipeline.STANDARDS["gated_tools"]:
            return 0
        ok, reasons = pipeline.check_call(tool, data.get("tool_input") or {})
    except Exception as e:  # fail closed
        ok, reasons = False, [f"the gate check errored ({type(e).__name__}: {e}); fix growth-engine/tools/pipeline.py "
                              "or the ledger it names. The gate fails closed."]
    if ok:
        return 0
    msg = ("GENERATION BLOCKED by the production gate (growth-engine/production/VISUAL-QA.md section 9).\n- "
           + "\n- ".join(reasons)
           + "\nRun `python3 growth-engine/tools/pipeline.py status <slug> <post_id>` for the open steps.")
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny",
                                             "permissionDecisionReason": msg}}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
