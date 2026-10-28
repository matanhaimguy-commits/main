"""Who may record a gate by hand (pipeline.py gate / approve): the human checkpoints of standards.json
human_checkpoints, delegated owner checkpoints (plan of 28 Oct, A1), and G-BUDGET's data. Pure functions;
pipeline.record_gate raises PipelineError with the message. Tests: growth-engine/tools/test_gate_auth.py."""
from __future__ import annotations

import re

# A delegated owner checkpoint names the fresh evaluator's report: a review file in the note.
REPORT = re.compile(r"[\w./-]+\.(?:json|md)\b")
BUDGET_KEYS = ("planned", "with_buffer", "balance", "month_spent", "cap")


def is_human(by: str, humans: list[str]) -> bool:
    return by.strip() in humans


def delegate(hc: dict, by: str) -> str | None:
    """The delegate name this record uses, when the checkpoint names one (hc["delegate"]["by"])."""
    d = (hc.get("delegate") or {}).get("by")
    return d if d and by.strip() == d else None


def checkpoint_problem(gate: str, hc: dict, by: str, note: str | None, humans: list[str]) -> str | None:
    """Why `by` may not record this human checkpoint (None: it may)."""
    human = is_human(by, humans)
    if hc["mode"] == "delegable" and not human:
        if not by.startswith("claude (delegated)"):
            return f"{gate} is the owner's call; Claude may take it only as 'claude (delegated)' with a --note"
    elif hc["mode"] == "director" and not (human or by.startswith("organic-director")):
        return f"{gate} is the Director's call (organic-director agent) or the owner's"
    elif hc["mode"] not in ("delegable", "director") and not human:
        d = (hc.get("delegate") or {}).get("by")
        if d and by.strip() == d:
            if not note or not REPORT.search(note):
                return (f"{gate} delegated: --note names the fresh evaluator's report (its file, e.g. "
                        f"reviews/hookboard.v1.review.json) and what it found")
        else:
            also = f", or {d!r} with a --note naming the evaluator's report" if d else ""
            return (f"{gate} is a human checkpoint: --by must be one of {humans}{also} "
                    f"(record what the owner said; never approve on their behalf)")
    if not note:
        return f"{gate}: say what was decided and where (--note)"
    return None


def is_delegated(hc: dict, by: str, humans: list[str]) -> bool:
    """Recorded by Claude on the owner's behalf: an FYI goes to the owner's queue."""
    return not is_human(by, humans) and (hc["mode"] == "delegable" or delegate(hc, by) is not None)


def budget_problem(status: str, data) -> str | None:
    """A G-BUDGET PASS carries what budget_usd.run writes: unit usd, the numbers, and they add up under the cap and
    the balance. Use `pipeline.py budget`; a bare PASS is refused."""
    if status != "PASS":
        return None
    how = "run pipeline.py budget <slug> <post_id> --planned USD --balance USD (it records the numbers)"
    if not isinstance(data, dict) or data.get("unit") != "usd":
        return f"a G-BUDGET PASS carries budget_usd's data (unit usd, {', '.join(BUDGET_KEYS)}): {how}"
    bad = [k for k in BUDGET_KEYS if isinstance(data.get(k), bool) or not isinstance(data.get(k), (int, float))]
    if bad:
        return f"G-BUDGET data lacks {', '.join(bad)} as numbers: {how}"
    if data["month_spent"] + data["with_buffer"] > data["cap"] or data["with_buffer"] > data["balance"]:
        return f"G-BUDGET data doesn't pass: month spend + planned with buffer is over the cap, or over the balance"
    return None


def budget_ok(rec: dict | None, ok_states=("PASS", "OVERRIDE")) -> bool:
    """A G-BUDGET record the gate counts: an owner's OVERRIDE, or a PASS carrying its data."""
    if not rec or rec.get("status") not in ok_states:
        return False
    return rec["status"] != "PASS" or budget_problem("PASS", rec.get("data")) is None
