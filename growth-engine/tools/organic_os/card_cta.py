"""The card's one ask: it fits the job, a keyword has a live and checked lead magnet, and reach posts don't beg for a
word (ORGANIC-OS 6.2, 8.5)."""
from __future__ import annotations

from .config import CONFIG
from .issues import ERROR, WARN, issue, unknown

CHECKS = [k for k in CONFIG["lead_magnet_checks"] if not k.startswith("_")]
REACH_KEYWORD = ("Instagram says it won't recommend posts that ask people to comment a specific word to non-followers "
                 "(Instagram @creators, June 2024; ORGANIC-OS 8.5). On a reach post prefer send, save or follow; keep the "
                 "keyword where its resource is the point")


def lead_magnet_issues(kw: str, lm: dict) -> list[dict]:
    if not lm.get("live"):
        return [issue(ERROR, "conversion", f"keyword {kw} has no live flow and resource yet")]
    out = []
    checks = lm.get("checks") or {}
    failed = [c for c in CHECKS if checks.get(c) is False]
    open_ = [c for c in CHECKS if c not in checks]
    if failed:
        out.append(issue(ERROR, "conversion", f"keyword {kw}'s resource fails the lead-magnet checks: {', '.join(failed)}"))
    elif open_:
        out.append(issue(WARN, "conversion", f"keyword {kw}'s resource hasn't been through the lead-magnet checks "
                                             f"({', '.join(open_)}): Conversion Agent"))
    if unknown(lm.get("delivers")):
        out.append(issue(WARN, "conversion", f"keyword {kw}: what the person gets (delivers) isn't written, so the post "
                                             "can't promise it"))
    return out


def cta_issues(card: dict, brain: dict, job: str) -> list[dict]:
    issues = []
    cta, ctas = card["cta_type"], CONFIG["jobs"][job]["ctas"]
    if cta not in ctas:
        why = " ('book' is for convert posts only, said as the keyword or DM path, never a link)" if cta == "book" else ""
        issues.append(issue(ERROR, "cta", f"CTA {cta} does not fit the {job} job ({', '.join(ctas)}){why}"))
    if cta == "comment" and card.get("cta_keyword"):
        issues.append(issue(WARN, "cta", f"a comment CTA is an answer to a question the post asks; a keyword ({card['cta_keyword']}) is cta_type keyword"))
    if cta == "keyword" and job == "reach":
        issues.append(issue(WARN, "reach", REACH_KEYWORD))
    if cta == "keyword" or (cta == "book" and card.get("cta_keyword")):
        kw = (card.get("cta_keyword") or "").upper()
        lm = next((m for m in brain.get("lead_magnets", []) if m["keyword"].upper() == kw), None)
        if not kw:
            issues.append(issue(ERROR, "conversion", "keyword CTA without a keyword"))
        elif lm is None:
            issues.append(issue(ERROR, "conversion", f"keyword {kw} has no lead magnet in the brain"))
        else:
            issues += lead_magnet_issues(kw, lm)
    return issues
