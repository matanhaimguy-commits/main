"""The G-HOOK record data (what pipeline.py gate stores with a G-HOOK PASS): the twin hook rule's run and its verdict.
`python3 hook_record.py run.json` prints the --data JSON for a run. Tests: test_hook_record.py."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import hook_rule
from hook_anchors import PACKET, anchor_ids

SOURCE = "hook_rule"


def make(run: dict) -> dict:
    """The data a G-HOOK record carries: the grades of both graders for the hook and both anchors, and the verdict."""
    v = hook_rule.judge(run)
    return {"source": SOURCE, "packet": run.get("packet"), "anchors": anchor_ids(), "graders": run.get("graders") or [],
            "verdict": "pass" if v["pass"] else "fail", "why": v["why"]}


def pass_problem(data) -> str | None:
    """Why a G-HOOK PASS's data is not a passing twin-rule run (None: it is). The verdict is recomputed from the grades,
    never trusted."""
    if not isinstance(data, dict) or data.get("source") != SOURCE:
        return (f"a G-HOOK PASS carries the twin hook rule's data (source {SOURCE}, packet {PACKET}): build it with "
                "python3 hook_record.py <run.json> and pass it as --data")
    if data.get("anchors") != anchor_ids():
        return "the G-HOOK data does not carry the 2 anchors of the grading run"
    v = hook_rule.judge({"packet": data.get("packet"), "graders": data.get("graders")})
    return None if v["pass"] else "the hook is below an anchor or fails a check: " + "; ".join(v["why"])


if __name__ == "__main__":
    print(json.dumps(make(json.loads(Path(sys.argv[1]).read_text()))))
