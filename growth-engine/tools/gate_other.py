"""Gated tools of kind `other` (standards.json gated_tools): no production route, so a call runs only as the owner's
one-off test: a test asset registered for this tool, G-HUMAN-TEST from the owner, a fresh G-BUDGET (24 h), one call.
Takes the pipeline module as P. Tests: test_gate_other.py."""
from __future__ import annotations

import json

import gate_budget


def check(P, tool_name: str, ti: dict, log: bool = True) -> tuple[bool, list[str]]:
    stale = []
    for led in P.all_ledgers():
        for a in led["assets"]:
            if a["type"] != "test" or a.get("tool") != tool_name or not P.gate_ok(a["gates"].get("G-HUMAN-TEST")) \
                    or P.generated_before(led, a):
                continue
            why = gate_budget.fresh_problem(P, led)
            if why:
                stale.append(f"test asset {P.aref(a)}: {why}")
                continue
            if log:
                with P.calls_log(led).open("a") as f:
                    f.write(json.dumps({"at": P.stamp(), "tool": tool_name, "asset": P.aref(a), "decision": "ALLOW",
                                        "dry": False}) + "\n")
            return True, []
    return False, stale + [f"{tool_name} makes content outside the production pipeline. If the owner asked for it, "
                           f"register a test asset (pipeline.py asset <slug> <TEST-run> <ID> --type test --tool "
                           f"{tool_name}), record G-HUMAN-TEST with the owner's words, and G-BUDGET"]
