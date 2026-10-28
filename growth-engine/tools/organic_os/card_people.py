"""D1 (Matan, 28 Oct 2026): face-on AI people appear only as clearly staged characters with Instagram's AI label, never
presented as a real client, customer or the owner (STANDARDS 7). A card for a format that shows an AI person on camera
must not cast that person as one."""
from __future__ import annotations

import re

from .issues import ERROR, issue

# formats that put an AI person on camera (FORMATS.md 2); reel_talking_head_real is the owner's own footage
AI_PEOPLE = {"reel_ugc_talking", "reel_lived_authority", "reel_ugc_pov", "reel_podcast", "reel_drama_pov", "reel_skit",
             "reel_whiteboard"}
FIELDS = ("series_character", "notes", "hypothesis", "story_template")
CAST = re.compile(r"\b(?:real|actual|our|my|happy|satisfied|paying) (?:client|customer)s?\b|\btestimonials?\b"
                  r"|\b(?:as|plays?|playing) (?:the |a |our )?(?:owner|founder|client|customer|matan)\b"
                  r"|\bmatan(?:'s)? (?:twin|double|lookalike|look-alike|clone|avatar|stand-in)\b", re.I)


def people_issues(card: dict) -> list[dict]:
    if card.get("format") not in AI_PEOPLE or card.get("status") == "killed":
        return []
    out = []
    for k in FIELDS:
        v = card.get(k)
        for text in (v if isinstance(v, list) else [v]):
            m = CAST.search(text) if isinstance(text, str) else None
            if m:
                out.append(issue(ERROR, "ai_person", f"{k}: {m.group(0)!r}: an AI person is a staged character with the "
                                                     "AI label, never a real client, customer or the owner (STANDARDS 7, D1)"))
    return out
