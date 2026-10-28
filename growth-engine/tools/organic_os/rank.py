"""One format's score for one Post Card (FORMATS.md 1): L19 fit to the load-bearing beat, the funnel stage, what wins
with the client's buyers, the story template, and variety. Cost is not here: it only filters (router.py)."""
from __future__ import annotations

from . import l19
from .config import CONFIG
from .variety import month_bonus

PROVEN_CONVERT = ("reel_strategist_prop", "reel_podcast", "carousel_comparison")


def score(fid: str, f: dict, card: dict, cmap: dict, plan: list[dict]) -> tuple[float, list[str]]:
    why: list[str] = []
    beat = card.get("load_bearing_beat")
    s = l19.fit(f, beat)
    if beat:
        why.append(f"L19 fit {s} for the {beat} beat")
    stage = CONFIG["beats"]["funnel_by_job"].get(card["job"])
    funnel = f.get("funnel", [])
    if funnel[:1] == [stage]:
        s += 1; why.append(f"built for {stage}")
    elif stage in funnel:
        s += 0.5; why.append(f"fits {stage}")
    if fid in cmap.get("buyer_formats", []):
        s += 3; why.append("wins with this client's buyers (research)")
    if card["job"] == "convert" and fid in PROVEN_CONVERT:
        s += 2; why.append("proven convert format")
    if card.get("story_template"):
        s += 2; why.append(f"renders the {card['story_template']} story")
    if f["family"] == "image":
        s -= 2
    bonus, note = month_bonus(fid, card["slot"], plan)
    s += bonus
    if note:
        why.append(note)
    return round(s, 2), why
