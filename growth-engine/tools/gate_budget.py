"""The budget a gated call needs: a G-BUDGET the gate counts (gate_auth.budget_ok) and recorded in the last
gate_policy.budget_fresh_hours (24 h). Used by the twin route (heygen_gate.py) and owner test calls (gate_other.py).
Takes the pipeline module as P. Tests: test_heygen_gate.py, test_gate_other.py."""
from __future__ import annotations

import datetime as dt

import gate_auth


def fresh_problem(P, led: dict) -> str | None:
    """Why the run's latest G-BUDGET doesn't cover a call now (None: it does)."""
    b = P.latest(led["run_gates"].get("G-BUDGET"))
    if not gate_auth.budget_ok(b, P.OK_STATES):
        return (f"no G-BUDGET PASS for {led['post_id']} (pipeline.py budget {led['slug']} {led['post_id']} "
                "--planned USD --balance USD)")
    hours = P.STANDARDS["gate_policy"]["budget_fresh_hours"]
    if P.now() - P.parse_ts(b["at"]) > dt.timedelta(hours=hours):
        return f"G-BUDGET for {led['post_id']} is older than {hours} h: check the live balance again (it is shared)"
    return None
