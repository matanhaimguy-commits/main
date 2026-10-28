"""Conditional entry keys in the owner's Atlas list: params_when (a dearer value only for the shots that need it) and
test_only (a model named for a G-HUMAN-TEST comparison, not yet for production).

Pure functions: atlas_rules.py calls them with the call, the asset and its Shot Specs. Tests: test_atlas_rules.py
(Conditions). Entry keys: growth-engine/tools/atlas/README.md.
"""
from __future__ import annotations

SRC = "standards.json models.atlas.allowed"
# Matan, 28 Oct 2026 (FORMATS.md 5, F5): realistic people are these asset types on these Shot Spec formats.
# "presenter" is his word: today a presenter shot is a talking_head spec; the name is kept for a future format.
PEOPLE_TYPES = ("character_sheet", "start_frame", "still")
PEOPLE_FORMATS = ("ugc", "talking_head", "podcast", "drama", "presenter")
SHEET_FORMATS = ("character_sheet", "prop_sheet", "set_sheet", "storyboard_panel", "style_reference")


def face_or_mouth(a: dict, specs: list[dict]) -> str | None:
    """None when a Shot Spec the asset serves has a face region (kind face, or a region named for a mouth)."""
    for sp in specs:
        for r in sp.get("regions") or []:
            if r.get("kind") == "face" or "mouth" in (r.get("name") or ""):
                return None
    return "no Shot Spec it serves has a face or mouth region (regions: kind face)"


def realistic_people(a: dict, specs: list[dict]) -> str | None:
    """None for a realistic-people asset: a character_sheet, start_frame or still whose Shot Specs are ugc,
    talking_head, podcast, drama or presenter. A character sheet's own SHEET- spec is skipped, so the sheet is
    registered with the people shots it serves (pipeline.py asset ... --shots SHEET-CH-X,S30-SEQ01-SH1)."""
    if a.get("type") not in PEOPLE_TYPES:
        return f"a {a.get('type')} is not a realistic-people asset ({', '.join(PEOPLE_TYPES)})"
    shots = [sp for sp in specs if sp.get("format") not in SHEET_FORMATS]
    off = [f"{sp.get('shot_id')} ({sp.get('format')})" for sp in shots if sp.get("format") not in PEOPLE_FORMATS]
    if not shots or off:
        return (f"every Shot Spec it serves is {', '.join(PEOPLE_FORMATS)}: "
                f"{', '.join(off) if off else 'it serves no such shot'}")
    return None


CONDITIONS = {"face_or_mouth": face_or_mouth, "realistic_people": realistic_people}


def when_problem(pw) -> str | None:
    """Why params_when can't be read: {param: {value: condition}} with known conditions."""
    if not isinstance(pw, dict) or any(not isinstance(v, dict) for v in pw.values()):
        return "params_when maps a parameter to {value: condition} ({\"resolution\": {\"1440p-sr\": \"face_or_mouth\"}})"
    bad = sorted({c for v in pw.values() for c in v.values() if c not in CONDITIONS})
    if bad:
        return f"params_when conditions are {', '.join(CONDITIONS)} (not {', '.join(map(str, bad))})"
    return None


def when_checks(req: dict, e: dict, a: dict, specs: list[dict]) -> list[str]:
    """Each params_when value the call passes needs its condition to hold on the asset and its Shot Specs."""
    why, p = [], req["params"]
    for k, vals in (e.get("params_when") or {}).items():
        cond = vals.get(p.get(k)) if isinstance(p.get(k), (str, int, float, bool)) else None
        if cond:
            miss = CONDITIONS[cond](a, specs)
            if miss:
                why.append(f"{e['id']}: {k} {p[k]!r} is only for {cond.replace('_', ' ')} ({SRC}): {miss}")
    return why


def test_only_checks(e: dict, a: dict) -> list[str]:
    """A test_only model makes test assets only (pipeline.py asset ... --type test, with G-HUMAN-TEST)."""
    if e.get("test_only") and a.get("type") != "test":
        return [f"{e['id']} is named for a G-HUMAN-TEST comparison only, not a {a.get('type')}: the owner names it for "
                f"production after the test ({SRC})"]
    return []
