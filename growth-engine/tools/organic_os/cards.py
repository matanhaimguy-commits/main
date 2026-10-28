"""Post Card check against the brain and the content map (ORGANIC-OS 7.1, 7.2, 7.5)."""
from __future__ import annotations

import jsonschema

from .card_cta import cta_issues
from .card_format import beat_issues
from .config import CARD_SCHEMA, CONFIG, LENGTHS
from .issues import ERROR, WARN, has_errors, issue, unknown


def card_check(card: dict, brain: dict, cmap: dict, demand: list[dict]) -> list[dict]:
    issues = [issue(ERROR, "schema", f"{'/'.join(map(str, e.path)) or 'card'}: {e.message}")
              for e in jsonschema.Draft202012Validator(CARD_SCHEMA).iter_errors(card)]
    if has_errors(issues):
        return issues
    fmt = CONFIG["formats"].get(card["format"])
    belief = CONFIG["beliefs"][card["belief"]]
    job = card["job"]

    if card["client"] != brain["client"]:
        issues.append(issue(ERROR, "client", f"card is for {card['client']}, brain is {brain['client']}"))
    if card["account_language"] != brain["market"]["language"]:
        issues.append(issue(ERROR, "language", f"one language per account: {brain['market']['language']}, card says {card['account_language']}"))
    pillars = {p["name"] for p in cmap.get("pillars", [])}
    if card["pillar"] not in pillars:
        issues.append(issue(ERROR, "map", f"pillar {card['pillar']!r} is not on the map ({', '.join(sorted(pillars))})"))
    series = {s["name"]: s for s in cmap.get("series", [])}
    if card.get("series") and card["series"] not in series:
        issues.append(issue(ERROR, "map", f"series {card['series']!r} is not on the map"))
    if card["avatar"] not in {a["id"] for a in brain.get("avatars", [])}:
        issues.append(issue(ERROR, "map", f"avatar {card['avatar']} is not in the brain"))
    if job not in belief["jobs"]:
        issues.append(issue(WARN, "belief_job", f"{card['belief']} usually serves {'/'.join(belief['jobs'])}, card says {job}"))
    if card["awareness"] not in belief["awareness"]:
        issues.append(issue(WARN, "awareness", f"{card['belief']} fits {'/'.join(belief['awareness'])}, card says {card['awareness']}"))

    phrase = card["demand_phrase"].strip().lower()
    hit = next((r for r in demand if r.get("phrase", "").strip().lower() == phrase), None)
    if hit is None:
        issues.append(issue(WARN, "demand", "demand phrase is not in the demand map yet: add it with a tag and a source"))
    elif hit.get("tag") == "off_map":
        issues.append(issue(ERROR, "demand", "demand phrase is tagged off_map: drop the idea"))

    if fmt is None:
        issues.append(issue(ERROR, "format", f"unknown format {card['format']!r}; see config/organic.json"))
    else:
        if fmt["tier"] != card["format_tier"]:
            issues.append(issue(ERROR, "format", f"{card['format']} is tier {fmt['tier']}, card says {card['format_tier']}"))
        if job not in fmt["jobs"]:
            issues.append(issue(WARN, "format_job", f"{card['format']} is not a usual {job} format"))
        if card["belief"] not in fmt["beliefs"]:
            issues.append(issue(WARN, "format_belief", f"{card['format']} is not a usual format for {card['belief']}"))
        issues += budget_issues(card, fmt)
        issues += beat_issues(card, cmap)
        if fmt.get("needs_real_human") and not brain["visual"].get("real_footage"):
            issues.append(issue(ERROR, "format", f"{card['format']} needs real photos or footage of real people; the brain has none yet"))
        if fmt.get("needs_proof") and not card.get("proof_used"):
            issues.append(issue(ERROR, "truth", f"{card['format']} needs a proof bank item"))
        if fmt["family"] == "image":
            issues.append(issue(WARN, "format", "single images are the weakest format: only a strong self-check question, a real review quote or an announcement, 1 a week at most"))
        if fmt["family"] == "reel" and card.get("length_target_s"):
            issues += length_issues(card["format"], card["length_target_s"])
        if fmt["family"] == "carousel" and card.get("slides") and not 7 <= card["slides"] <= 10:
            issues.append(issue(WARN, "slides", f"carousels: 7 to 10 slides (the hub takes at most 10 files; card: {card['slides']})"))
    if fmt is not None:
        st, style = card.get("story_template"), card.get("animation_style")
        if st:
            if st not in CONFIG["story_templates"] or st.startswith("_"):
                issues.append(issue(ERROR, "story", f"unknown story_template {st!r}; see config/organic.json story_templates"))
            else:
                t = CONFIG["story_templates"][st]
                if st not in fmt.get("story_templates", []):
                    issues.append(issue(ERROR, "story", f"{card['format']} doesn't render {st} (it renders: {', '.join(fmt.get('story_templates', [])) or 'no story templates'})"))
                elif card["belief"] not in t["beliefs"]:
                    issues.append(issue(WARN, "story", f"{st} usually carries {'/'.join(t['beliefs'])}, card says {card['belief']}"))
                vis = brain["visual"]
                if t.get("needs_real_footage") and (vis.get("face") == "ai_character" or not vis.get("real_footage")):
                    issues.append(issue(ERROR, "truth", f"{st} is someone's real story: it needs real footage of the real person, never an AI person "
                                                        f"(STANDARDS 7; the brain has face {vis.get('face')}, real_footage {bool(vis.get('real_footage'))})"))
        elif fmt.get("story_templates") and fmt["tier"] in ("A", "B") and card["format"] not in ("reel_podcast",):
            issues.append(issue(WARN, "story", f"{card['format']} is a story format: name a story_template (STORY-FORMATS.md)"))
        if fmt.get("styles"):
            if not style:
                issues.append(issue(ERROR, "style", f"{card['format']} needs an animation_style ({', '.join(fmt['styles'])})"))
            elif style not in fmt["styles"]:
                issues.append(issue(ERROR, "style", f"animation_style {style!r} is not one of {', '.join(fmt['styles'])}"))
        elif style:
            issues.append(issue(WARN, "style", f"{card['format']} is not animated; animation_style is ignored"))
    if card["format_tier"] == "A" and not (card["angle_proven"] or card.get("wildcard")):
        issues.append(issue(ERROR, "spend", "tier A needs a proven angle (beat the median in a cheaper format) or the month's wildcard"))

    issues += cta_issues(card, brain, job)

    permitted = {p["id"] for p in brain.get("proof_bank", []) if p.get("permission") == "yes"}
    for pid in card.get("proof_used") or []:
        if pid not in permitted:
            issues.append(issue(ERROR, "truth", f"proof {pid} is not in the proof bank with permission"))
    if card["belief"] == "B6" and not card.get("proof_used") and card.get("series") != "The Build":
        issues.append(issue(ERROR, "truth", "B6 needs proof from the proof bank, or the 'The Build' series (7.6)"))
    if card.get("hard_offer") and card["job"] != "convert":
        issues.append(issue(ERROR, "offer", "a hard offer post is a convert-job post (organic.json stage_mix note)"))
    if card["belief"] == "B8" and unknown((brain.get("offer") or {}).get("delivers")):
        issues.append(issue(WARN, "truth", "B8 while the brain's offer.delivers is not written: state only the offer facts the brain holds, "
                                           "no post on what the offer includes until the owner writes it (brain decisions_open)"))
    return issues


def length_issues(fmt: str, n: int) -> list[dict]:
    """A reel's length against STANDARDS.md section 8 (standards.json lengths): the card's tier decides the check."""
    if n > LENGTHS["max_s"]:
        return [issue(ERROR, "length", f"{n} s is over {LENGTHS['max_s']} s, the longest reel until the owner confirms a longer limit (STANDARDS 8)")]
    if fmt == "reel_podcast":
        lo, hi = LENGTHS["podcast_C45"]["s"]
        return [] if lo <= n <= hi else [issue(WARN, "length", f"podcast runs only at C45, {lo} to {hi} s (STANDARDS 8; card: {n} s)")]
    tiers = {k: v for k, v in LENGTHS.items() if k.startswith("O") and isinstance(v, list)}
    if any(lo <= n <= hi for lo, hi in tiers.values()):
        return []
    names = ", ".join(f"{k} {lo}-{hi}" for k, (lo, hi) in tiers.items())
    return [issue(WARN, "length", f"{n} s fits no STANDARDS 8 tier ({names} s): pick the tier, the script gate checks against it")]


def budget_issues(card: dict, fmt: dict) -> list[dict]:
    """usd_budget against the format's Atlas USD range; a card from before 28 Oct with only credit_budget is read
    against the old credit range (history)."""
    unit, key, (lo, hi) = ("$", "usd_budget", fmt["usd"]) if "usd_budget" in card else ("", "credit_budget", fmt["credits"])
    if card.get(key) is None or card[key] <= hi * 1.25:
        return []
    return [issue(WARN, "budget", f"budget {unit}{card[key]} is above {card['format']}'s range {unit}{lo}-{hi} plus 25%")]
