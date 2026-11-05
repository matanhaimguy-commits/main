"""The twin in the router (FORMATS.md 2.18): reel_twin_stage exists only on a card marked twin_host for a brain with a
host block, and a slot is re-routed to the twin only where the twin ranks first with the flag on (D-T1)."""
from __future__ import annotations

from .config import CONFIG


def twin_only(fid: str) -> bool:
    return CONFIG["formats"][fid].get("twin_only") is True


def twin_allowed(card: dict, brain: dict) -> bool:
    return card.get("twin_host") is True and bool((brain.get("host") or {}).get("looks"))


def reroute(card: dict, brain: dict, run) -> dict | None:
    """The twin option if it would rank first for this card with twin_host on, else None. `run(card)` is the router.
    A card that is already a twin card, or a brain with no host block, has nothing to re-route."""
    if card.get("twin_host") is True or not (brain.get("host") or {}).get("looks"):
        return None
    opts = run({**card, "twin_host": True})
    return opts[0] if opts and twin_only(opts[0]["format"]) else None
