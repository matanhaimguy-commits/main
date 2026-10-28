"""Format variety (owner, 28 Oct 2026; FORMATS.md 1): no format family more than twice in a week, at least 4 families
in a month, reel_motion at most 1 post in 6. Used by the router (filter and rank) and by week-check (issues)."""
from __future__ import annotations

from datetime import date

from .config import CONFIG
from .issues import ERROR, issue

MOTION = "reel_motion"


def format_family(card_or_fid) -> str:
    fid = card_or_fid if isinstance(card_or_fid, str) else card_or_fid.get("format", "")
    f = CONFIG["formats"].get(fid)
    return f.get("format_family", f["family"]) if f else "unknown"


def week_key(slot: str) -> tuple[int, int]:
    """ISO year and week of a slot ('2026-11-02 12:00'): Monday to Sunday."""
    return date.fromisoformat(slot[:10]).isocalendar()[:2]


def same_week(cards: list[dict], slot: str) -> list[dict]:
    return [c for c in cards if week_key(c["slot"]) == week_key(slot)]


def same_month(cards: list[dict], slot: str) -> list[dict]:
    return [c for c in cards if c["slot"][:7] == slot[:7]]


def counts(cards: list[dict]) -> dict[str, int]:
    out: dict[str, int] = {}
    for c in cards:
        out[format_family(c)] = out.get(format_family(c), 0) + 1
    return out


def motion_cap(posts: int) -> int:
    """reel_motion posts allowed among this many posts: 1 in motion_one_in, and 1 in any smaller set."""
    return max(1, posts // CONFIG["week_rules"]["motion_one_in"])


def blocked_by_plan(fid: str, slot: str, plan: list[dict]) -> str | None:
    """Why this format can't take the slot given the other planned cards (None when it can)."""
    rules = CONFIG["week_rules"]
    fam = format_family(fid)
    week = counts(same_week(plan, slot)).get(fam, 0)
    if week >= rules["max_same_format_family_per_week"]:
        return f"{fam} already {week}x this week"
    if fid == MOTION:
        month = same_month(plan, slot)
        used = sum(1 for c in month if c.get("format") == MOTION)
        if used + 1 > motion_cap(len(month) + 1):
            return f"reel_motion already {used} of {len(month) + 1} posts this month (1 in {rules['motion_one_in']})"
    return None


def month_bonus(fid: str, slot: str, plan: list[dict]) -> tuple[float, str | None]:
    """Rank toward 4+ families a month: a family not used yet this month scores up, a repeated one down."""
    used = counts(same_month(plan, slot)).get(format_family(fid), 0)
    if used == 0:
        return 1.0, "a family not used yet this month"
    return -1.0 * used, None


def variety_issues(cards: list[dict]) -> list[dict]:
    rules = CONFIG["week_rules"]
    out: list[dict] = []
    weeks: dict[tuple, list[dict]] = {}
    months: dict[str, list[dict]] = {}
    for c in cards:
        weeks.setdefault(week_key(c["slot"]), []).append(c)
        months.setdefault(c["slot"][:7], []).append(c)
    for (y, w), cs in sorted(weeks.items()):
        for fam, n in sorted(counts(cs).items()):
            if n > rules["max_same_format_family_per_week"]:
                out.append(issue(ERROR, "variety", f"{y}-W{w:02d}: {n} {fam} posts; {rules['max_same_format_family_per_week']} a week at most (FORMATS.md 1)"))
    for m, cs in sorted(months.items()):
        motion = sum(1 for c in cs if c.get("format") == MOTION)
        if motion > motion_cap(len(cs)):
            out.append(issue(ERROR, "variety", f"{m}: {motion} reel_motion of {len(cs)} posts; 1 in {rules['motion_one_in']} at most (FORMATS.md 1)"))
        fams = counts(cs)
        if len(cs) >= rules["min_posts_for_month_family_rule"] and len(fams) < rules["min_format_families_per_month"]:
            out.append(issue(ERROR, "variety", f"{m}: {len(fams)} format families ({', '.join(sorted(fams))}); at least {rules['min_format_families_per_month']} a month"))
    return out
