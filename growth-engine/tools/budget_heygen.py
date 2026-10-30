"""G-BUDGET in HeyGen credits (D-T5, Twin reel machine plan T1): the month's credits plus this piece with its retake
buffer stay under the owner's monthly credit cap (brain.json package.monthly_heygen_credit_cap), and a live credit
balance, when given, covers the piece. With no cap set it warns and the warning is logged on the G-BUDGET record; it
does not fail. Pure functions; budget_usd.run calls check() and gate_auth.budget_problem calls data_problem().
Tests: growth-engine/tools/test_budget_heygen.py."""
from __future__ import annotations

import math

KEYS = ("heygen_planned", "heygen_with_buffer", "heygen_month_spent")


def check(cap: float | None, month_spent: float, planned: float, balance: float | None, buffer: float) -> dict:
    """planned, month_spent, balance and cap in HeyGen credits. Returns {notes, warnings, data}: notes fail G-BUDGET,
    warnings are logged on the record only."""
    need = round(planned * (1 + buffer), 2)
    notes, warnings = [], []
    if planned > 0 and cap is None:
        warnings.append("no monthly HeyGen credit cap: this piece's credits are logged; the owner sets brain.json "
                        "package.monthly_heygen_credit_cap from the measured cost (D-T5)")
    elif cap is not None and month_spent + need > cap:
        notes.append(f"HeyGen month cap {cap:.0f} credits: spent {month_spent:.0f} + planned {need:.0f} with buffer is over")
    if balance is not None and need > balance:
        notes.append(f"live HeyGen balance {balance:.0f} credits can't cover {need:.0f} (planned + {buffer:.0%} retakes)")
    data = {"heygen_planned": planned, "heygen_with_buffer": need, "heygen_month_spent": round(month_spent, 2),
            "heygen_cap": cap, "heygen_balance": balance}
    return {"notes": notes, "warnings": warnings, "data": data}


def _num(v) -> bool:
    return not isinstance(v, bool) and isinstance(v, (int, float)) and math.isfinite(v) and v >= 0


def data_problem(data: dict) -> str | None:
    """Why a G-BUDGET PASS's HeyGen numbers are not ones check() passes (None: they are, or the piece has none)."""
    if not any(k in data for k in KEYS):
        return None
    bad = [k for k in KEYS if not _num(data.get(k))]
    if bad:
        return f"G-BUDGET data has no finite, non-negative {', '.join(bad)}"
    if data["heygen_with_buffer"] < data["heygen_planned"]:
        return "G-BUDGET data: heygen_with_buffer is below heygen_planned"
    cap, bal = data.get("heygen_cap"), data.get("heygen_balance")
    for name, v in (("heygen_cap", cap), ("heygen_balance", bal)):
        if v is not None and not _num(v):
            return f"G-BUDGET data: {name} is not a finite, non-negative number"
    if cap is not None and data["heygen_month_spent"] + data["heygen_with_buffer"] > cap:
        return "G-BUDGET data doesn't pass: HeyGen credits this month + planned with buffer is over the credit cap"
    if bal is not None and data["heygen_with_buffer"] > bal:
        return "G-BUDGET data doesn't pass: planned HeyGen credits with buffer are over the balance"
    return None


def priced(data) -> bool:
    """The G-BUDGET record prices this piece in HeyGen credits (a HeyGen call needs it)."""
    return isinstance(data, dict) and _num(data.get("heygen_planned")) and data["heygen_planned"] > 0
