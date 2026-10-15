#!/usr/bin/env python3
"""Organic Growth OS: the checks and numbers behind growth-engine (see growth-engine/ORGANIC-OS.md).

  organic.py brain-check <slug> [--write]          Client Brain: schema, blocking fields, gaps report (section 4)
  organic.py card-check <slug> <card|dir> ...      Post Cards against the brain and the content map (7.1, 7.2, 7.5)
  organic.py week-check <slug> <dir|cards> ...     weekly rules: format and job rotation, mix, B7, contrarian, CTAs (6.2, 6.6)
  organic.py route <slug> <card> [--prev-family F] format router within the monthly budget (7.7)
  organic.py ledger <slug> [--month YYYY-MM]       credits and minutes spent vs the monthly cap (7.7)
  organic.py ledger-add <slug> --post ID --format F --credits N [--el N] [--minutes N] [--note TEXT]
  organic.py outliers <dataset.json> [--days 90] [--out file.csv]   the 4 outlier checks per account (5.1)
  organic.py score <slug> [--write]                scorecard: job metric vs median, candidate/template, diagnosis (9)

Exit code 1 when a blocking check fails, so the daily run can stop on it.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import statistics
import sys
from pathlib import Path

import jsonschema
import yaml

GE = Path(__file__).resolve().parents[1]
ROOT = GE.parent
CONFIG = json.loads((GE / "config" / "organic.json").read_text())
CARD_SCHEMA = yaml.safe_load((GE / "schemas" / "post-card.schema.yaml").read_text())
BRAIN_SCHEMA = json.loads((GE / "schemas" / "brain.schema.json").read_text())

ERROR, WARN = "error", "warn"


def issue(level: str, code: str, msg: str) -> dict:
    return {"level": level, "code": code, "msg": msg}


def has_errors(issues: list[dict]) -> bool:
    return any(i["level"] == ERROR for i in issues)


def unknown(v) -> bool:
    """Empty, or a placeholder the Brain Builder left for a gap."""
    if v is None:
        return True
    if isinstance(v, str):
        s = v.strip().lower()
        return not s or s.startswith(("unknown", "tbd", "todo", "gap:"))
    if isinstance(v, (list, dict)):
        return len(v) == 0
    return False


# ---- files -------------------------------------------------------------------------------------

def client_dir(slug: str) -> Path:
    return ROOT / "clients" / slug


def load_brain(slug: str) -> dict:
    return json.loads((client_dir(slug) / "brain.json").read_text())


def load_map(slug: str) -> dict:
    return json.loads((client_dir(slug) / "content-map.json").read_text())


def load_demand(slug: str, brain: dict | None = None) -> list[dict]:
    rel = (brain or {}).get("demand_map_file") or "research/demand-map.csv"
    p = client_dir(slug) / rel
    if not p.exists():
        return []
    with p.open(newline="") as f:
        return [r for r in csv.DictReader(f)]


def load_cards(paths: list[str]) -> list[tuple[str, dict]]:
    out = []
    for p in paths:
        pp = Path(p)
        files = sorted(pp.glob("*.yaml")) if pp.is_dir() else [pp]
        for f in files:
            out.append((str(f), yaml.safe_load(f.read_text())))
    return out


# ---- brain (section 4) ---------------------------------------------------------------------------

def brain_check(brain: dict, demand: list[dict]) -> tuple[list[dict], list[dict]]:
    """Returns (issues, gaps). Errors block production; gaps are required onboarding work."""
    issues: list[dict] = []
    for e in jsonschema.Draft202012Validator(BRAIN_SCHEMA).iter_errors(brain):
        issues.append(issue(ERROR, "schema", f"{'/'.join(map(str, e.path)) or 'brain'}: {e.message}"))

    def get(path: str):
        cur = brain
        for k in path.split("."):
            cur = cur.get(k) if isinstance(cur, dict) else None
        return cur

    blocking = {
        "offer.main_offer": "the one offer content points to",
        "offer.next_step": "the single next step for a viewer",
        "mechanism.ump": "problem name (UMP)",
        "mechanism.ums": "solution name (UMS)",
        "voice.language": "account language",
        "constraints.cannot_say": "the never-say list",
    }
    for path, what in blocking.items():
        if unknown(get(path)):
            issues.append(issue(ERROR, "blocking", f"{path} is empty: {what}. Nothing is produced until it is filled."))
    if not brain.get("avatars"):
        issues.append(issue(ERROR, "blocking", "avatars: at least one avatar is required."))

    gaps: list[dict] = []

    def gap(field, missing, how):
        gaps.append({"field": field, "missing": missing, "how_to_get": how})

    if unknown(get("business_model.capacity")):
        gap("business_model.capacity", "how many new clients a month the business can take", "ask the owner")
    good = [r for r in demand if (r.get("tag") or "").strip() in ("direct", "bridge")]
    if len(good) < 20:
        gap("demand_map", f"{len(good)} usable buyer phrases (direct or bridge); 20 to 40 needed",
            "comments and DMs in the hub inbox, sales calls, competitor comments, search suggestions")
    for k in ("stage", "sophistication"):
        if unknown(get(f"awareness.{k}")):
            gap(f"awareness.{k}", "where most buyers are / how often they heard the claims", "research + sales calls")
    if len(brain.get("contrarian_vault") or []) < 5:
        gap("contrarian_vault", f"{len(brain.get('contrarian_vault') or [])} positions; 5 to 10 needed", "15-20 minute owner ramble (voice note)")
    for lm in brain.get("lead_magnets") or []:
        if unknown(lm.get("delivers")):
            gap(f"lead_magnets[{lm.get('keyword')}].delivers", "exactly what the person gets, how long it takes", "owner; write it before more keyword CTAs")
        if not lm.get("live"):
            gap(f"lead_magnets[{lm.get('keyword')}]", "resource or keyword flow not live yet", "Conversion Agent builds it; no posts may use the keyword until then")
    if len((brain.get("voice") or {}).get("samples") or []) < 3:
        gap("voice.samples", "3 to 5 real samples of how the owner talks", "owner ramble, past posts")
    if (get("voice.register") or "").split(" ")[0] not in ("ti", "ju"):
        gap("voice.register", "ju or ti not decided", "owner decision (section 13.3)")
    if (get("visual.face") in ("ai_character", "mixed")) and unknown(get("visual.ai_label")):
        gap("visual.ai_label", "how the AI character is labeled", "owner decision (section 13.1)")
    if unknown(get("baseline.followers")) or unknown(get("baseline.as_of")):
        gap("baseline", "followers, 30-day reach, median views, where clients come from", "account audit (Insights) + owner")
    if get("constraints.turnaround_hours") in (None, ""):
        gap("constraints.turnaround_hours", "approval contact and turnaround", "contract / owner")
    if any((b.get("state") == "unknown") for b in brain.get("belief_ladder") or []):
        gap("belief_ladder.state", "which beliefs the audience already holds", "comments, DMs, sales calls; update monthly")
    if not [p for p in brain.get("proof_bank") or [] if p.get("permission") == "yes"]:
        gap("proof_bank", "no public proof yet: B6 posts only through 'The Build' / process (7.6)", "film the first clients from day one, with permission")
    return issues, gaps


def brain_report(slug: str, brain: dict, issues: list[dict], gaps: list[dict]) -> str:
    lines = [f"# {slug} · Client Brain gaps", "", f"Checked {dt.date.today().isoformat()} by `organic.py brain-check`.", ""]
    if issues:
        lines += ["## Blocking (nothing is produced until fixed)", ""] + [f"- {i['msg']}" for i in issues] + [""]
    else:
        lines += ["## Blocking", "", "None: production may run.", ""]
    lines += ["## Gaps to fill (required, not blocking)", "", "| Field | Missing | How to get it |", "|---|---|---|"]
    lines += [f"| {g['field']} | {g['missing']} | {g['how_to_get']} |" for g in gaps]
    dec = brain.get("decisions_open") or []
    if dec:
        lines += ["", "## Decisions for the owner", ""]
        for d in dec:
            lines.append(f"- **{d['id']}** {d['question']}" + (f" Recommended: {d['recommendation']}" if d.get("recommendation") else "")
                         + (f" Until then: {d['interim']}" if d.get("interim") else ""))
    return "\n".join(lines) + "\n"


# ---- post card (7.1, 7.2, 7.5) ---------------------------------------------------------------------

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
        lo, hi = fmt["credits"]
        if card["credit_budget"] > hi * 1.25:
            issues.append(issue(WARN, "budget", f"budget {card['credit_budget']} is above {card['format']}'s range {lo}-{hi} plus 25%"))
        if fmt.get("needs_real_human") and not brain["visual"].get("real_footage"):
            issues.append(issue(ERROR, "format", f"{card['format']} needs real photos or footage of real people; the brain has none yet"))
        if fmt.get("needs_proof") and not card.get("proof_used"):
            issues.append(issue(ERROR, "truth", f"{card['format']} needs a proof bank item"))
        if fmt["family"] == "image":
            issues.append(issue(WARN, "format", "single images are the weakest format: only a strong self-check question, a real review quote or an announcement, 1 a week at most"))
        if fmt["family"] == "reel" and card.get("length_target_s"):
            n = card["length_target_s"]
            if n > 180:
                issues.append(issue(ERROR, "length", "reels over 3 minutes are not recommended to non-followers"))
            elif job == "reach" and not 10 <= n <= 60:
                issues.append(issue(WARN, "length", f"reach reels work best at 30 to 60 s (card: {n} s)"))
        if fmt["family"] == "carousel" and card.get("slides") and not 7 <= card["slides"] <= 12:
            issues.append(issue(WARN, "slides", f"carousels: 7 to 12 slides (card: {card['slides']})"))
    if fmt is not None:
        st, style = card.get("story_template"), card.get("animation_style")
        if st:
            if st not in CONFIG["story_templates"] or st.startswith("_"):
                issues.append(issue(ERROR, "story", f"unknown story_template {st!r}; see config/organic.json story_templates"))
            elif st not in fmt.get("story_templates", []):
                issues.append(issue(ERROR, "story", f"{card['format']} doesn't render {st} (it renders: {', '.join(fmt.get('story_templates', [])) or 'no story templates'})"))
            else:
                t = CONFIG["story_templates"][st]
                if card["belief"] not in t["beliefs"]:
                    issues.append(issue(WARN, "story", f"{st} usually carries {'/'.join(t['beliefs'])}, card says {card['belief']}"))
                if t.get("needs_real_or_labelled") and brain["visual"].get("face") == "ai_character" and not brain["visual"].get("real_footage"):
                    issues.append(issue(WARN, "truth", f"{st} is first person: with an AI character it needs the AI label (decision D1) and no invented results"))
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

    if card["cta_type"] not in CONFIG["jobs"][job]["ctas"]:
        issues.append(issue(ERROR, "cta", f"CTA {card['cta_type']} does not fit the {job} job ({', '.join(CONFIG['jobs'][job]['ctas'])})"))
    if card["cta_type"] == "keyword":
        kw = (card.get("cta_keyword") or "").upper()
        lm = next((m for m in brain.get("lead_magnets", []) if m["keyword"].upper() == kw), None)
        if not kw:
            issues.append(issue(ERROR, "conversion", "keyword CTA without a keyword"))
        elif lm is None:
            issues.append(issue(ERROR, "conversion", f"keyword {kw} has no lead magnet in the brain"))
        elif not lm.get("live"):
            issues.append(issue(ERROR, "conversion", f"keyword {kw} has no live flow and resource yet"))

    permitted = {p["id"] for p in brain.get("proof_bank", []) if p.get("permission") == "yes"}
    for pid in card.get("proof_used") or []:
        if pid not in permitted:
            issues.append(issue(ERROR, "truth", f"proof {pid} is not in the proof bank with permission"))
    if card["belief"] == "B6" and not card.get("proof_used") and card.get("series") != "The Build":
        issues.append(issue(ERROR, "truth", "B6 needs proof from the proof bank, or the 'The Build' series (7.6)"))
    if card.get("hard_offer") and card["job"] != "convert":
        issues.append(issue(WARN, "offer", "hard offer posts belong to the convert job"))
    return issues


# ---- week (6.2, 6.6) -------------------------------------------------------------------------------

def family(card: dict) -> str:
    f = CONFIG["formats"].get(card.get("format", ""))
    return f["family"] if f else "unknown"


def week_check(cards: list[dict], brain: dict, cmap: dict | None = None) -> tuple[list[dict], dict]:
    rules = CONFIG["week_rules"]
    cards = sorted(cards, key=lambda c: c["slot"])
    issues: list[dict] = []
    for a, b in zip(cards, cards[1:]):
        if family(a) == family(b):
            issues.append(issue(ERROR, "rotation", f"{a['slot'][:10]} and {b['slot'][:10]} are both {family(a)}: no format two days in a row"))
        if a["job"] == b["job"]:
            issues.append(issue(WARN, "rotation", f"{a['slot'][:10]} and {b['slot'][:10]} are both {a['job']}: no two posts in a row from the same job"))
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
            issues.append(issue(WARN, "cta", f"{run} posts in a row without a conversion CTA (keyword, DM, book) by {c['slot'][:10]}"))
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
    if stage == "new":
        months: dict[str, int] = {}
        for c in cards:
            if c.get("hard_offer"):
                months[c["slot"][:7]] = months.get(c["slot"][:7], 0) + 1
        for m, n in months.items():
            if n > target["hard_offer_per_month"]:
                issues.append(issue(ERROR, "offer", f"{n} hard offer posts in {m}; new accounts: {target['hard_offer_per_month']} a month at most"))
    if cmap and len(cards) >= 6:
        missing = {p["name"] for p in cmap.get("pillars", [])} - {c["pillar"] for c in cards}
        if missing:
            issues.append(issue(WARN, "pillars", f"no post this week for pillar(s): {', '.join(sorted(missing))}"))
    summary = {"posts": len(cards), "families": fam, "jobs": {k: round(v, 2) for k, v in jobs.items()}, "stage_target": {k: target[k] for k in ("reach", "trust", "convert")}}
    return issues, summary


# ---- router and ledger (7.7) -----------------------------------------------------------------------

def ledger_rows(slug: str) -> list[dict]:
    p = client_dir(slug) / "ledger.csv"
    if not p.exists():
        return []
    with p.open(newline="") as f:
        return list(csv.DictReader(f))


def month_spend(rows: list[dict], month: str) -> dict:
    sel = [r for r in rows if r["date"].startswith(month)]
    num = lambda r, k: float(r.get(k) or 0)
    by_fmt: dict[str, dict] = {}
    for r in sel:
        d = by_fmt.setdefault(r["format"], {"pieces": 0, "credits": 0.0, "minutes": 0.0})
        d["pieces"] += 1
        d["credits"] += num(r, "higgsfield_credits")
        d["minutes"] += num(r, "minutes")
    return {"month": month, "credits": sum(num(r, "higgsfield_credits") for r in sel),
            "elevenlabs": sum(num(r, "elevenlabs_credits") for r in sel),
            "minutes": sum(num(r, "minutes") for r in sel), "by_format": by_fmt}


def route(card: dict, brain: dict, cmap: dict, prev_family: str | None = None, spent: float = 0.0) -> list[dict]:
    cap = brain["package"]["monthly_credit_cap"]
    remaining = cap - spent
    permitted_proof = any(p.get("permission") == "yes" for p in brain.get("proof_bank", []))
    buyer_formats = cmap.get("buyer_formats", [])
    out = []
    for fid, f in CONFIG["formats"].items():
        if card["job"] not in f["jobs"] or card["belief"] not in f["beliefs"]:
            continue
        why = []
        if f["tier"] == "A" and not (card.get("angle_proven") or card.get("wildcard")):
            continue
        if f.get("needs_real_human") and not brain["visual"].get("real_footage"):
            continue
        if f.get("needs_proof") and not permitted_proof:
            continue
        if prev_family and f["family"] == prev_family:
            continue
        if f["credits"][1] > remaining:
            continue
        score = 0.0
        if fid in buyer_formats:
            score += 3; why.append("wins with this client's buyers (research)")
        if card["job"] == "reach" and f["family"] == "reel":
            score += 2; why.append("reels lead reach for small accounts")
        if card["job"] == "trust" and f["family"] == "carousel":
            score += 2; why.append("carousels earn saves")
        if card["job"] == "convert" and fid in ("reel_strategist_prop", "reel_podcast", "carousel_comparison"):
            score += 2; why.append("proven convert format")
        st = card.get("story_template")
        if st:
            if st not in f.get("story_templates", []):
                continue
            score += 2; why.append(f"renders the {st} story")
            if f["tier"] == "B" and not (card.get("angle_proven") or card.get("wildcard")):
                score += 1; why.append("story lab: test the angle at tier B before a tier A piece")
        if card.get("animation_style") and card["animation_style"] not in f.get("styles", []):
            continue
        if f["tier"] == "C":
            score += 0.5; why.append("cheap: test the angle first")
        if f["family"] == "image":
            score -= 2
        out.append({"format": fid, "tier": f["tier"], "family": f["family"], "credits": f["credits"], "score": score,
                    "why": "; ".join(why) or "fits job and belief", "skill": f.get("skill")})
    return sorted(out, key=lambda r: -r["score"])


# ---- research (5.1) ----------------------------------------------------------------------------------

def _views(it: dict):
    v = it.get("videoViewCount") or it.get("videoPlayCount") or it.get("views")
    return float(v) if v else None


def outliers(items: list[dict], days: int | None = 90, now: dt.datetime | None = None) -> list[dict]:
    now = now or dt.datetime.now(dt.timezone.utc)
    if days:
        def recent(it):
            ts = it.get("timestamp")
            if not ts:
                return True
            t = dt.datetime.fromisoformat(ts.replace("Z", "+00:00"))
            return (now - t).days <= days
        items = [it for it in items if recent(it)]
    accounts: dict[str, list[dict]] = {}
    for it in items:
        if it.get("isPinned"):
            continue
        accounts.setdefault(it.get("ownerUsername") or "?", []).append(it)
    rows = []
    for acct, posts in accounts.items():
        vid = [p for p in posts if _views(p)]
        med_views = statistics.median([_views(p) for p in vid]) if vid else None
        tot_v = sum(_views(p) for p in vid)
        acct_cpk = (sum(p.get("commentsCount") or 0 for p in vid) / tot_v * 1000) if tot_v else None
        lpk = [((p.get("likesCount") or 0) / _views(p) * 1000) for p in vid if (p.get("likesCount") or 0) >= 0]
        med_lpk = statistics.median(lpk) if lpk else None
        med_likes = statistics.median([max(p.get("likesCount") or 0, 0) for p in posts]) if posts else 0
        for p in posts:
            likes = max(p.get("likesCount") or 0, 0)
            comments = p.get("commentsCount") or 0
            v = _views(p)
            row = {"account": acct, "url": p.get("url") or p.get("shortCode"), "type": p.get("type") or p.get("productType"),
                   "timestamp": p.get("timestamp"), "views": v, "likes": likes, "comments": comments}
            if v and med_views:
                cpk = comments / v * 1000
                ratio_l = (likes / v * 1000) / med_lpk if med_lpk else None
                eng = (likes + comments) / v
                checks = {
                    "views_3x": v >= 3 * med_views,
                    "comments_above_rate": acct_cpk is not None and cpk > acct_cpk,
                    "likes_in_proportion": ratio_l is not None and 0.25 <= ratio_l <= 4,
                    "engagement_2pct": eng >= 0.02,
                }
                row.update({"basis": "views", "x_median": round(v / med_views, 2), "comments_per_1k": round(cpk, 2),
                            "account_comments_per_1k": round(acct_cpk, 2) if acct_cpk is not None else None,
                            "engagement": round(eng, 4), **checks, "trusted": all(checks.values())})
            else:
                x = likes / med_likes if med_likes else None
                row.update({"basis": "likes_only", "x_median": round(x, 2) if x else None, "trusted": False,
                            "partial_outlier": bool(x and x >= 3)})
            rows.append(row)
    return sorted(rows, key=lambda r: -(r.get("x_median") or 0))


# ---- learning (9) --------------------------------------------------------------------------------------

def _f(v):
    try:
        return float(v) if v not in (None, "") else None
    except ValueError:
        return None


def _div(a, b):
    return a / b if a is not None and b else None


def _median(vals):
    vals = [v for v in vals if v is not None]
    return statistics.median(vals) if vals else None


def score(rows: list[dict]) -> list[dict]:
    d = []
    for r in rows:
        reach, views = _f(r.get("reach")), _f(r.get("views"))
        x = {k: _f(r.get(k)) for k in ("likes", "comments", "saves", "sends", "profile_visits", "follows", "skip_rate", "avg_watch_s",
                                       "keyword_comments", "dms", "qualified_dms", "booked")}
        m = {"sends_per_reach": _div(x["sends"], reach), "saves_per_reach": _div(x["saves"], reach),
             "follows_per_1k_reach": (_div(x["follows"], reach) or 0) * 1000 if reach and x["follows"] is not None else None,
             "profile_per_reach": _div(x["profile_visits"], reach),
             "comments_per_1k_views": (_div(x["comments"], views) or 0) * 1000 if views and x["comments"] is not None else None,
             "engagement": _div((x["likes"] or 0) + (x["comments"] or 0), views) if views else None,
             "qualified_dms": x["qualified_dms"] if x["qualified_dms"] is not None else x["dms"]}
        d.append({"row": r, "x": x, "m": m, "reach": reach, "views": views})
    med = {k: _median([e["m"][k] for e in d]) for k in d[0]["m"]} if d else {}
    med.update({"reach": _median([e["reach"] for e in d]), "views": _median([e["views"] for e in d]),
                "skip_rate": _median([e["x"]["skip_rate"] for e in d]), "avg_watch_s": _median([e["x"]["avg_watch_s"] for e in d])})
    job_med = {}
    for job, cfg in CONFIG["jobs"].items():
        job_med[job] = _median([e["m"].get(cfg["metric"]) for e in d if e["row"].get("job") == job])
    out = []
    for e in d:
        r, m, x = e["row"], e["m"], e["x"]
        job = r.get("job") or "reach"
        metric = CONFIG["jobs"][job]["metric"]
        val, base = m.get(metric), job_med.get(job)
        ratio = (val / base) if val is not None and base else None
        checks = {
            "views_3x": bool(e["views"] and med["views"] and e["views"] >= 3 * med["views"]),
            "comments_above_rate": bool(m["comments_per_1k_views"] is not None and med["comments_per_1k_views"] is not None and m["comments_per_1k_views"] > med["comments_per_1k_views"]),
            "saves_sends_good": bool((m["saves_per_reach"] or 0) >= (med["saves_per_reach"] or 0) and (m["sends_per_reach"] or 0) >= (med["sends_per_reach"] or 0)),
            "engagement_2pct": bool(m["engagement"] is not None and m["engagement"] >= 0.02),
        }
        booked = (x["booked"] or 0) > 0
        flag = "template" if booked or (ratio and ratio >= CONFIG["templates"]["template_x"] and all(checks.values())) \
            else "candidate" if ratio and ratio >= CONFIG["templates"]["candidate_x"] else ""
        out.append({"post_id": r.get("post_id"), "job": job, "metric": metric, "value": val, "job_median": base,
                    "x_median": round(ratio, 2) if ratio else None, "flag": flag, "diagnosis": diagnose(e, med, r)})
    return out


def diagnose(e: dict, med: dict, r: dict) -> str:
    """The first step of the 9.4 ladder that the numbers point at, or '' when nothing stands out."""
    m, x = e["m"], e["x"]
    low = lambda v, base, f=0.7: v is not None and base is not None and v < base * f
    if low(e["reach"], med.get("reach")) and x["skip_rate"] is not None and med.get("skip_rate") is not None and x["skip_rate"] > med["skip_rate"] * 1.15:
        return "low reach, high skip rate: the hook or first frame failed; rewrite hooks, test with trial reels"
    if x["avg_watch_s"] is not None and med.get("avg_watch_s") and x["avg_watch_s"] >= med["avg_watch_s"] and \
            low((m["sends_per_reach"] or 0) + (m["saves_per_reach"] or 0), (med.get("sends_per_reach") or 0) + (med.get("saves_per_reach") or 0)):
        return "good hold, low sends/saves: value not unique or not usable; narrow to level 4, add a usable step"
    if e["views"] and med.get("views") and e["views"] >= med["views"] and low(m["profile_per_reach"], med.get("profile_per_reach"), 0.5):
        return "views but few profile visits: angle off-target; back to the demand map"
    if m["profile_per_reach"] and med.get("profile_per_reach") and m["profile_per_reach"] >= med["profile_per_reach"] and \
            x["follows"] is not None and x["profile_visits"] and low(x["follows"] / x["profile_visits"], 0.1, 1):
        return "profile visits but few follows: profile or series promise weak; fix bio, pinned posts, series"
    if (x["follows"] or 0) > 0 and r.get("cta_keyword") and x["dms"] == 0:
        return "follows but no DMs: CTA or lead magnet weak"
    if (x["dms"] or 0) > 0 and x["qualified_dms"] is not None and x["qualified_dms"] / x["dms"] < 0.3:
        return "DMs but few qualified: wrong viewer; tighten avatar and pillars, 'who it is not for' posts"
    if (x["qualified_dms"] or 0) > 0 and x["booked"] == 0:
        return "qualified DMs but no bookings: an offer or sales problem, not content"
    return ""


# ---- CLI ------------------------------------------------------------------------------------------------

def _print_issues(label: str, issues: list[dict]) -> None:
    if not issues:
        print(f"OK  {label}")
        return
    for i in issues:
        print(f"{'FAIL' if i['level'] == ERROR else 'warn'} {label}: [{i['code']}] {i['msg']}")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("brain-check"); b.add_argument("slug"); b.add_argument("--write", action="store_true")
    c = sub.add_parser("card-check"); c.add_argument("slug"); c.add_argument("paths", nargs="+")
    w = sub.add_parser("week-check"); w.add_argument("slug"); w.add_argument("paths", nargs="+")
    r = sub.add_parser("route"); r.add_argument("slug"); r.add_argument("card"); r.add_argument("--prev-family")
    l = sub.add_parser("ledger"); l.add_argument("slug"); l.add_argument("--month")
    la = sub.add_parser("ledger-add"); la.add_argument("slug"); la.add_argument("--post", required=True); la.add_argument("--format", required=True)
    la.add_argument("--credits", type=float, required=True); la.add_argument("--el", type=float, default=0); la.add_argument("--minutes", type=float, default=0)
    la.add_argument("--note", default=""); la.add_argument("--date", default=dt.date.today().isoformat())
    o = sub.add_parser("outliers"); o.add_argument("dataset"); o.add_argument("--days", type=int, default=90); o.add_argument("--out")
    s = sub.add_parser("score"); s.add_argument("slug"); s.add_argument("--write", action="store_true")
    a = ap.parse_args(argv)

    if a.cmd == "brain-check":
        brain = load_brain(a.slug)
        issues, gaps = brain_check(brain, load_demand(a.slug, brain))
        _print_issues("brain", issues)
        print(f"{len(gaps)} gaps to fill")
        for g in gaps:
            print(f"  - {g['field']}: {g['missing']}")
        if a.write:
            (client_dir(a.slug) / "brain-gaps.md").write_text(brain_report(a.slug, brain, issues, gaps))
            print(f"wrote clients/{a.slug}/brain-gaps.md")
        return 1 if has_errors(issues) else 0

    if a.cmd in ("card-check", "week-check", "route"):
        brain, cmap = load_brain(a.slug), load_map(a.slug)
        demand = load_demand(a.slug, brain)
        if a.cmd == "card-check":
            bad = False
            for path, card in load_cards(a.paths):
                iss = card_check(card, brain, cmap, demand)
                _print_issues(Path(path).name, iss)
                bad |= has_errors(iss)
            return 1 if bad else 0
        if a.cmd == "week-check":
            cards = [c for _, c in load_cards(a.paths)]
            iss, summary = week_check(cards, brain, cmap)
            print(json.dumps(summary))
            _print_issues("week", iss)
            return 1 if has_errors(iss) else 0
        card = yaml.safe_load(Path(a.card).read_text())
        month = card["slot"][:7]
        spent = month_spend(ledger_rows(a.slug), month)["credits"]
        opts = route(card, brain, cmap, a.prev_family, spent)
        print(f"budget {month}: {spent:.0f} of {brain['package']['monthly_credit_cap']} credits spent")
        for o_ in opts[:3]:
            print(f"- {o_['format']} (tier {o_['tier']}, {o_['credits'][0]}-{o_['credits'][1]} credits): {o_['why']} · {o_['skill']}")
        return 0 if opts else 1

    if a.cmd == "ledger":
        rows = ledger_rows(a.slug)
        month = a.month or dt.date.today().strftime("%Y-%m")
        sp = month_spend(rows, month)
        cap = load_brain(a.slug)["package"]["monthly_credit_cap"]
        print(f"{month}: {sp['credits']:.0f} / {cap} Higgsfield credits ({sp['credits'] / cap:.0%}), "
              f"{sp['elevenlabs']:.0f} ElevenLabs credits, {sp['minutes']:.0f} production minutes")
        for f_, v in sorted(sp["by_format"].items()):
            print(f"  {f_}: {v['pieces']} pieces, {v['credits']:.0f} credits, {v['minutes']:.0f} min")
        if sp["credits"] > cap / 1.25:
            print("  over 80% of the cap: keep the 25% retake buffer, move remaining slots to tier C")
        return 0

    if a.cmd == "ledger-add":
        p = client_dir(a.slug) / "ledger.csv"
        new = not p.exists()
        fmt = CONFIG["formats"].get(a.format)
        with p.open("a", newline="") as f:
            wr = csv.writer(f)
            if new:
                wr.writerow(["date", "post_id", "format", "tier", "higgsfield_credits", "elevenlabs_credits", "minutes", "note"])
            wr.writerow([a.date, a.post, a.format, fmt["tier"] if fmt else "", a.credits, a.el, a.minutes, a.note])
        print(f"logged {a.post} in clients/{a.slug}/ledger.csv")
        return 0

    if a.cmd == "outliers":
        items = json.loads(Path(a.dataset).read_text())
        rows = outliers(items, a.days)
        cols = ["account", "url", "type", "timestamp", "basis", "views", "likes", "comments", "x_median", "comments_per_1k",
                "account_comments_per_1k", "engagement", "views_3x", "comments_above_rate", "likes_in_proportion", "engagement_2pct", "trusted", "partial_outlier"]
        if a.out:
            with open(a.out, "w", newline="") as f:
                wr = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
                wr.writeheader()
                wr.writerows(rows)
            print(f"wrote {a.out}")
        trusted = [r for r in rows if r.get("trusted")]
        print(f"{len(rows)} posts, {len(trusted)} trusted outliers (all 4 checks)")
        for r_ in trusted[:15]:
            print(f"  {r_['x_median']}x  @{r_['account']}  {r_['url']}")
        return 0

    if a.cmd == "score":
        p = client_dir(a.slug) / "analytics" / "posts.csv"
        with p.open(newline="") as f:
            rows = list(csv.DictReader(f))
        if not rows:
            print("no scored posts yet")
            return 0
        res = score(rows)
        for s_ in res:
            print(f"{s_['post_id']}: {s_['metric']}={s_['value']} x{s_['x_median']} {s_['flag']} {s_['diagnosis']}".rstrip())
        if a.write:
            out = client_dir(a.slug) / "analytics" / "scored.csv"
            with out.open("w", newline="") as f:
                wr = csv.DictWriter(f, fieldnames=list(res[0].keys()))
                wr.writeheader()
                wr.writerows(res)
            print(f"wrote {out.relative_to(ROOT)}")
        return 0
    return 2


if __name__ == "__main__":
    sys.exit(main())
