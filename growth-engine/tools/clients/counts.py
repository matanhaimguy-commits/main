"""Totals for the dry-run report: pieces per status and per funnel stage (slotted pieces; unslotted bank cards apart)."""
from collections import Counter


def counts(pieces: list[dict]) -> dict:
    slotted = [p for p in pieces if p["slot"]]
    return {"pieces": len(slotted), "unslotted": len(pieces) - len(slotted),
            "status": dict(sorted(Counter(p["status"] for p in slotted).items())),
            "funnel_stage": dict(sorted(Counter(p["funnel_stage"] or "none" for p in slotted).items()))}
