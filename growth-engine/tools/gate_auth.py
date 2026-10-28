"""Who may record a gate by hand (pipeline.py gate / approve): the human checkpoints of standards.json
human_checkpoints, delegated owner checkpoints (plan of 28 Oct, A1), and G-BUDGET's data. Pure functions;
pipeline.record_gate raises PipelineError with the message. Tests: growth-engine/tools/test_gate_auth.py."""
from __future__ import annotations

import math
import re
from pathlib import Path

# A delegated owner checkpoint names the fresh evaluator's report: a review file in the note.
REPORT = re.compile(r"[\w./-]+\.(?:json|md)\b")
BUDGET_KEYS = ("planned", "with_buffer", "balance", "month_spent", "cap")


def is_human(by: str, humans: list[str]) -> bool:
    return by.strip() in humans


def delegate(hc: dict, by: str) -> str | None:
    """The delegate name this record uses, when the checkpoint names one (hc["delegate"]["by"])."""
    d = (hc.get("delegate") or {}).get("by")
    return d if d and by.strip() == d else None


def report_problem(note: str | None, root: Path) -> str | None:
    """The delegated note names an existing review file inside the repo (a relative path)."""
    m = REPORT.search(note or "")
    if not m:
        return "--note names the fresh evaluator's report (its repo path, e.g. clients/<slug>/runs/<post>/qa/hookboard.v1.review.json)"
    p = (Path(root) / m.group(0)).resolve()
    if not p.is_relative_to(Path(root).resolve()) or not p.is_file():
        return f"the evaluator's report {m.group(0)} is not a file in the repo (give its path from the repo root)"
    return None


def checkpoint_problem(gate: str, hc: dict, by: str, note: str | None, humans: list[str], root: Path) -> str | None:
    """Why `by` may not record this human checkpoint (None: it may). root: the repo, where a delegate's report lives."""
    human = is_human(by, humans)
    if hc["mode"] == "delegable" and not human:
        if not by.startswith("claude (delegated)"):
            return f"{gate} is the owner's call; Claude may take it only as 'claude (delegated)' with a --note"
    elif hc["mode"] == "director" and not (human or by.startswith("organic-director")):
        return f"{gate} is the Director's call (organic-director agent) or the owner's"
    elif hc["mode"] not in ("delegable", "director") and not human:
        d = (hc.get("delegate") or {}).get("by")
        if d and by.strip() == d:
            why = report_problem(note, root)
            if why:
                return f"{gate} delegated: {why}"
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


def hand_budget_problem(status: str) -> str | None:
    """pipeline.py gate never writes a G-BUDGET PASS: only budget_usd.run does, with the numbers it computed. A FAIL
    can be recorded by hand; the owner's way past a FAIL is an OVERRIDE with a reason."""
    if status == "PASS":
        return ("a G-BUDGET PASS is written only by pipeline.py budget <slug> <post_id> --planned USD --balance USD "
                "(budget_usd computes the numbers); the owner may OVERRIDE with a reason")
    return None


def budget_problem(data) -> str | None:
    """Why a PASS's data is not what budget_usd.run writes (None: it is): its marker, unit usd, finite non-negative
    numbers that pass under the cap and the balance."""
    if not isinstance(data, dict) or data.get("source") != "budget_usd" or data.get("unit") != "usd":
        return "the G-BUDGET data is not budget_usd's (source budget_usd, unit usd): run pipeline.py budget"
    bad = [k for k in BUDGET_KEYS if isinstance(data.get(k), bool) or not isinstance(data.get(k), (int, float))
           or not math.isfinite(data[k]) or data[k] < 0]
    if bad:
        return f"G-BUDGET data has no finite, non-negative {', '.join(bad)}"
    if data["with_buffer"] < data["planned"]:
        return "G-BUDGET data: with_buffer is below planned"
    if data["month_spent"] + data["with_buffer"] > data["cap"] or data["with_buffer"] > data["balance"]:
        return "G-BUDGET data doesn't pass: month spend + planned with buffer is over the cap, or over the balance"
    return None


def budget_ok(rec: dict | None, ok_states=("PASS", "OVERRIDE")) -> bool:
    """A G-BUDGET record the gate counts: an owner's OVERRIDE, or a PASS carrying budget_usd's data."""
    if not rec or rec.get("status") not in ok_states:
        return False
    return rec["status"] != "PASS" or budget_problem(rec.get("data")) is None
