"""Totals the dashboard shows: pieces per status and per funnel stage (slotted pieces; bank cards counted apart)."""
from collections import Counter


def counts(pieces: list[dict]) -> dict:
    slotted = [p for p in pieces if not p["bank"]]
    return {"pieces": len(slotted), "bank": len(pieces) - len(slotted),
            "status": dict(sorted(Counter(p["status"] for p in slotted).items())),
            "funnel_stage": dict(sorted(Counter(p["funnel_stage"] or "none" for p in slotted).items()))}
