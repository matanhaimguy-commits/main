"""A Post Card's format against its load-bearing beat (FORMATS.md 1) and the content map's blocked formats."""
from __future__ import annotations

from . import l19
from .issues import ERROR, WARN, issue
from .variety import MOTION


def beat_issues(card: dict, cmap: dict) -> list[dict]:
    out: list[dict] = []
    if card.get("status") == "killed":
        return out
    beat = card.get("load_bearing_beat")
    if card["format"] in cmap.get("blocked_formats", []):
        out.append(issue(ERROR, "format", f"{card['format']} is blocked on this month's content map (blocked_formats)"))
    if not beat:
        out.append(issue(WARN, "beat", "name the load_bearing_beat (mechanism, proof, offer, list, data or type): the format is chosen by it (FORMATS.md 1)"))
        if card["format"] == MOTION:
            out.append(issue(ERROR, "beat", "reel_motion needs a load_bearing_beat of list, data or type (FORMATS.md 1)"))
        return out
    if card["format"] == MOTION and not l19.motion_allowed_beat(beat):
        out.append(issue(ERROR, "beat", f"reel_motion carries only a list, data or a type-led idea; this card's beat is {beat}: route it (organic.py route)"))
    return out
