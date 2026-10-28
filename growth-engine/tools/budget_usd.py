"""G-BUDGET in Atlas USD (STANDARDS.md 10): the month's spend plus this piece with its retake buffer stays under the
owner's monthly USD cap, and the live Atlas balance covers the piece. check() is pure; run() records it on the run.
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


def run(P, slug: str, post_id: str, planned: float, balance: float, el: float = 0.0) -> dict:
    """Records G-BUDGET on the run (P: the pipeline module): the brain's monthly_usd_cap, the ledger's atlas_usd this
    month, the live balance. el: ElevenLabs credits, kept on the record for history."""
    import sys
    sys.path.insert(0, str(P.GE / "tools"))
    from organic_os import files as organic_files, router as organic_router  # noqa: E402
    organic_files.ROOT = P.ROOT  # client_dir() reads this module's ROOT
    brain = organic_files.load_brain(slug)
    spent = organic_router.month_spend(organic_router.ledger_rows(slug), P.now().strftime("%Y-%m"))
    r = check(organic_router.usd_cap(brain), spent["usd"], planned, balance, P.STANDARDS["gate_policy"]["retake_buffer"])
    data = {**r["data"], "el_planned": el}
    led = P.load_ledger(slug, post_id)
    P.add_record(led["run_gates"], "G-BUDGET", {"status": r["status"], "by": "pipeline.py budget", "data": data,
                                                "note": "; ".join(r["notes"])})
    P.save_ledger(led)
    return {"status": r["status"], "notes": r["notes"], **data}
