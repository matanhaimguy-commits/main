"""D1 (Matan, 28 Oct 2026): face-on AI people appear only as clearly staged characters, never presented as a real client,
customer or the owner (STANDARDS 7). A card for a format that shows an AI person on camera must not cast that person as
one. The one exception (D-T1, D-T2, 29 Oct): the client's own twin (brain host block) may host as the owner, and only on
a card marked twin_host. Any card that casts the owner's twin without twin_host is refused, whatever its format."""
from __future__ import annotations

import re

from .issues import ERROR, issue

# formats that put an AI person on camera (FORMATS.md 2), plus reel_strategist_prop (an on-camera presenter) and
# reel_talking_head_real (the owner's own footage, so an AI stand-in there would pass as him)
AI_PEOPLE = {"reel_ugc_talking", "reel_lived_authority", "reel_ugc_pov", "reel_podcast", "reel_drama_pov", "reel_skit",
             "reel_whiteboard", "reel_strategist_prop", "reel_talking_head_real", "reel_twin_stage"}
FIELDS = ("series_character", "notes", "hypothesis", "story_template")
CLIENT = re.compile(r"\b(?:real|actual|our|my|happy|satisfied|paying) (?:client|customer)s?\b|\btestimonials?\b"
                    r"|\b(?:as|plays?|playing) (?:the |a |our )?(?:client|customer)\b", re.I)
OWNER = re.compile(r"\b(?:as|plays?|playing) (?:the |a |our )?(?:owner|founder|matan)\b"
                   r"|\bmatan(?:'s)? (?:twin|double|lookalike|look-alike|clone|avatar|stand-in)\b"
                   r"|\b(?:digital|heygen|ai) twin\b", re.I)


def _texts(card: dict):
    for k in FIELDS:
        v = card.get(k)
        for text in (v if isinstance(v, list) else [v]):
            if isinstance(text, str):
                yield k, text


def people_issues(card: dict) -> list[dict]:
    if card.get("status") == "killed":
        return []
    twin = card.get("twin_host") is True
    on_camera = card.get("format") in AI_PEOPLE
    out = []
    for k, text in _texts(card):
        m = CLIENT.search(text) if on_camera else None
        if m:
            out.append(issue(ERROR, "ai_person", f"{k}: {m.group(0)!r}: an AI person is a staged character, never a "
                                                 "real client or customer (STANDARDS 7, D1)"))
        m = None if twin else OWNER.search(text)
        if m:
            out.append(issue(ERROR, "ai_person", f"{k}: {m.group(0)!r}: the owner appears only as his twin, and only on "
                                                 "a card marked twin_host (STANDARDS 7, D-T1)"))
    return out


def twin_issues(card: dict, brain: dict) -> list[dict]:
    """A twin_host card needs the brain's host block (the looks and voices the HeyGen gate allows)."""
    out = []
    if card.get("twin_host") is True and not (brain.get("host") or {}).get("looks"):
        out.append(issue(ERROR, "twin_host", "twin_host card, but the brain has no host block with looks and voices: "
                                             "only a client with an approved twin may use it (D-T1)"))
    if card.get("format") == "reel_twin_stage" and card.get("twin_host") is not True:
        out.append(issue(ERROR, "twin_host", "reel_twin_stage is the owner's twin: mark the card twin_host: true "
                                             "(FORMATS.md 2.18, D-T1)"))
    return out
