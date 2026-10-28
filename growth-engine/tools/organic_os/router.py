"""Format router (ORGANIC-OS 7.7, FORMATS.md 1): which formats can take a Post Card, best first.

Filters: job and belief, tier A rules, real footage, proof, the story template and style, the content map's
blocked_formats and zero formats_per_week, the variety rules against the other planned cards, reel_motion's beats, and the monthly USD cap.
Ranking: rank.score. Cost only filters against the cap; it never ranks."""
from __future__ import annotations

from . import l19
from .config import CONFIG
from .rank import score
from .spend import ledger_rows, month_spend, route_issues, usd_cap  # noqa: F401  (re-exported for older imports)
from .variety import MOTION, blocked_by_plan, format_family


def route(card: dict, brain: dict, cmap: dict, prev_family: str | None = None, spent: float = 0.0,
          plan: list[dict] | None = None) -> list[dict]:
    """spent: Atlas USD spent this month. plan: the other planned cards (any month; the card itself is skipped).
    prev_family: the format family (or surface family) of the post before, never repeated."""
    plan = [c for c in plan or [] if c.get("post_id") != card.get("post_id")]
    cap = usd_cap(brain)
    remaining = float("inf") if cap is None else cap - spent
    out = []
    for fid, f in CONFIG["formats"].items():
        why_not = excluded(fid, f, card, brain, cmap, prev_family, remaining, plan)
        if why_not:
            continue
        s, why = score(fid, f, card, cmap, plan)
        out.append({"format": fid, "tier": f["tier"], "family": f["family"], "format_family": format_family(fid),
                    "usd": f["usd"], "credits": f["credits"], "score": s,
                    "why": "; ".join(why) or "fits job and belief", "skill": f.get("skill")})
    return sorted(out, key=lambda r: -r["score"])


def excluded(fid: str, f: dict, card: dict, brain: dict, cmap: dict, prev_family: str | None, remaining: float,
             plan: list[dict]) -> str | None:
    if card["job"] not in f["jobs"] or card["belief"] not in f["beliefs"]:
        return "job or belief"
    if f["tier"] == "A" and not (card.get("angle_proven") or card.get("wildcard")):
        return "tier A needs a proven angle or the wildcard"
    if f.get("needs_real_human") and not brain["visual"].get("real_footage"):
        return "needs real footage"
    if f.get("needs_proof") and not any(p.get("permission") == "yes" for p in brain.get("proof_bank", [])):
        return "needs proof"
    if fid in cmap.get("blocked_formats", []):
        return "blocked on the content map"
    if (cmap.get("formats_per_week") or {}).get(f["family"]) == 0:
        return f"the content map plans no {f['family']} posts"
    if prev_family and prev_family in (f["family"], format_family(fid)):
        return "same family as the post before"
    st = card.get("story_template")
    if st and st not in f.get("story_templates", []):
        return f"doesn't render {st}"
    if card.get("animation_style") and card["animation_style"] not in f.get("styles", []):
        return "style"
    if fid == MOTION and not l19.motion_allowed_beat(card.get("load_bearing_beat")):
        return "reel_motion carries only a list, data or a type-led idea"
    if blocked_by_plan(fid, card["slot"], plan):
        return blocked_by_plan(fid, card["slot"], plan)
    if f["usd"][1] > remaining:
        return "over the month's USD cap"
    return None
