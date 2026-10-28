"""G-BUDGET in Atlas USD (STANDARDS.md 10): the month's spend plus this piece with its retake buffer stays under the
owner's monthly USD cap, and the live Atlas balance covers the piece. Pure function; pipeline.py records the result.
Tests: growth-engine/tools/test_budget_usd.py."""
from __future__ import annotations


def check(cap: float | None, month_spent: float, planned: float, balance: float, buffer: float) -> dict:
    """planned and balance in USD. Returns {status, notes, data}; data goes on the G-BUDGET record."""
    need = round(planned * (1 + buffer), 2)
    notes = []
    if cap is None:
        notes.append("no monthly USD cap: the owner sets brain.json package.monthly_usd_cap (STANDARDS.md 10)")
    elif month_spent + need > cap:
        notes.append(f"month cap ${cap:.2f}: spent ${month_spent:.2f} + planned ${need:.2f} with buffer is over")
    if need > balance:
        notes.append(f"live Atlas balance ${balance:.2f} can't cover ${need:.2f} (planned + {buffer:.0%} retakes)")
    data = {"unit": "usd", "planned": planned, "with_buffer": need, "balance": balance,
            "month_spent": round(month_spent, 2), "cap": cap}
    return {"status": "FAIL" if notes else "PASS", "notes": notes, "data": data}
