"""L19 fit: how well a format carries a Post Card's load-bearing beat (readymerce-ads-machine L19; FORMATS.md 1).

A format scores 0 (no), 1 (partly) or 2 (yes) on the six L19 properties (config formats[].l19); a beat weights the
properties it needs (config beats.needs). Fit = weighted levels / the most they could be, scaled to 0 to 5.
"""
from __future__ import annotations

from .config import CONFIG

PROPERTIES = ("face", "invisible", "order", "sound", "attention", "person")


def beats() -> list[str]:
    return list(CONFIG["beats"]["needs"])


def fit(fmt: dict, beat: str | None) -> float:
    """0 to 5. No beat named: 0, so the other signals rank (the card check warns about the missing beat)."""
    if not beat:
        return 0.0
    needs = CONFIG["beats"]["needs"].get(beat)
    if needs is None:
        raise ValueError(f"unknown load_bearing_beat {beat!r} (known: {', '.join(beats())})")
    levels = fmt.get("l19") or {}
    got = sum(w * levels.get(p, 0) for p, w in needs.items())
    return round(5 * got / (2 * sum(needs.values())), 2)


def motion_allowed_beat(beat: str | None) -> bool:
    """reel_motion carries only a list, data or a type-led idea (FORMATS.md 1)."""
    return beat in CONFIG["beats"]["motion_beats"]
