"""Client Brain check: schema, blocking fields and the gaps report (ORGANIC-OS section 4)."""
from __future__ import annotations

import datetime as dt

import jsonschema

from .config import BRAIN_SCHEMA, CONFIG
from .issues import ERROR, issue, unknown

LM_CHECKS = [k for k in CONFIG["lead_magnet_checks"] if not k.startswith("_")]


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

    cap = get("package.monthly_usd_cap")
    if isinstance(cap, bool) or not isinstance(cap, (int, float)):
        gap("package.monthly_usd_cap", "the monthly Atlas generation cap in USD; until it is set G-BUDGET fails every "
            "paid generation and only free formats route", "owner decision (STANDARDS.md 10 prices each format)")
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
        elif set(LM_CHECKS) - set(lm.get("checks") or {}):
            gap(f"lead_magnets[{lm.get('keyword')}].checks", "the five lead-magnet checks are not recorded (8.5)", "Conversion Agent")
    if (brain.get("messaging") or {}).get("status", "").split(" ")[0] != "approved":
        gap("messaging", "one-liner, pitch, 3 value props and boilerplate the bot, site and captions reuse, approved",
            "draft from the brain's mechanism and offer; owner approves")
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
