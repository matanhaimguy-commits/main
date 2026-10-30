"""Weekly rules: format and job rotation, mix, B7, contrarian, CTAs (ORGANIC-OS 6.2, 6.6)."""
from __future__ import annotations

from datetime import date

from .config import CONFIG
from .issues import ERROR, WARN, issue
from .variety import counts, variety_issues


def family(card: dict) -> str:
    f = CONFIG["formats"].get(card.get("format", ""))
    return f["family"] if f else "unknown"


def week_check(cards: list[dict], brain: dict, cmap: dict | None = None) -> tuple[list[dict], dict]:
    rules = CONFIG["week_rules"]
    cards = sorted(cards, key=lambda c: c["slot"])
    issues: list[dict] = []
    for a, b in zip(cards, cards[1:]):
        if family(a) == family(b) and days_apart(a, b) <= 1:
            issues.append(issue(ERROR, "rotation", f"{a['slot'][:10]} and {b['slot'][:10]} are both {family(a)}: no format two days in a row"))
        if a["job"] == b["job"]:
            issues.append(issue(WARN, "rotation", f"{a['slot'][:10]} and {b['slot'][:10]} are both {a['job']}: no two posts in a row from the same job"))
    issues += variety_issues(cards)
    fam = {}
    for c in cards:
        fam[family(c)] = fam.get(family(c), 0) + 1
    if fam.get("image", 0) > rules["max_images"]:
        issues.append(issue(WARN, "mix", f"{fam['image']} single images this week; {rules['max_images']} at most"))
    if sum(1 for c in cards if c.get("tone") == "contrarian" or c["hook_type"] == "contrarian") < rules["min_contrarian"]:
        issues.append(issue(WARN, "tone", "no contrarian post this week (at least 1)"))
    if sum(1 for c in cards if c["belief"] == "B7") < rules["min_human_b7"]:
        issues.append(issue(WARN, "tone", "no human / B7 post this week (at least 1)"))
    run = 0
    for c in cards:
        run = 0 if c["cta_type"] in CONFIG["conversion_ctas"] else run + 1
        if run >= rules["conversion_cta_every"]:
            issues.append(issue(WARN, "cta", f"{run} posts in a row without a conversion CTA ({', '.join(CONFIG['conversion_ctas'])}) by {c['slot'][:10]}"))
            run = 0
    tier_a = [c for c in cards if CONFIG["formats"].get(c["format"], {}).get("tier") == "A"]
    if len(tier_a) > rules.get("max_tier_a_per_week", 99):
        issues.append(issue(WARN, "spend", f"{len(tier_a)} tier A pieces this week; {rules['max_tier_a_per_week']} at most (the rest of the budget feeds the daily posts)"))
    stories = [c for c in cards if c.get("story_template")]
    if len(cards) >= 5 and len(stories) < rules.get("story_reels_per_week", 0):
        issues.append(issue(WARN, "story", "no story reel this week: plan one (STORY-FORMATS.md, POV day in the buyer's life)"))
    stage = brain["package"]["account_stage"]
    target = CONFIG["stage_mix"][stage]
    jobs = {j: sum(1 for c in cards if c["job"] == j) / len(cards) for j in ("reach", "trust", "convert")} if cards else {}
    if len(cards) >= 5:
        for j, share in jobs.items():
            if abs(share - target[j]) > rules["mix_tolerance"]:
                issues.append(issue(WARN, "mix", f"{j} is {share:.0%} of the week; {stage} accounts aim for about {target[j]:.0%}"))
    cap = hard_offer_cap(target, brain)
    months: dict[str, int] = {}
    for c in cards:
        if c.get("hard_offer"):
            months[c["slot"][:7]] = months.get(c["slot"][:7], 0) + 1
    for m, n in months.items():
        if cap is not None and n > cap:
            issues.append(issue(ERROR, "offer", f"{n} hard offer posts in {m}; {stage} accounts: {cap} a month at most (about 3% of output, ORGANIC-OS 6.2)"))
    if cmap and len(cards) >= 6:
        missing = {p["name"] for p in cmap.get("pillars", [])} - {c["pillar"] for c in cards}
        if missing:
            issues.append(issue(WARN, "pillars", f"no post this week for pillar(s): {', '.join(sorted(missing))}"))
    summary = {"posts": len(cards), "families": fam, "format_families": counts(cards), "jobs": {k: round(v, 2) for k, v in jobs.items()}, "stage_target": {k: target[k] for k in ("reach", "trust", "convert")}}
    return issues, summary


def days_apart(a: dict, b: dict) -> int:
    """Calendar days between two slots: the format rule is about days, so Mon/Wed/Fri reels are not in a row."""
    return abs((date.fromisoformat(b["slot"][:10]) - date.fromisoformat(a["slot"][:10])).days)


def hard_offer_cap(target: dict, brain: dict) -> int | None:
    """Hard offer posts allowed a month: a fixed number for new accounts, else the share of the month's posts (at least 1)."""
    if "hard_offer_per_month" in target:
        return target["hard_offer_per_month"]
    if "hard_offer_share" in target:
        per_month = (brain.get("package") or {}).get("posts_per_week", 7) * 52 / 12
        return max(1, round(target["hard_offer_share"] * per_month))
    return None
