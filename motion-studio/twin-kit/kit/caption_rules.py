"""Caption cards, grouped exactly as templates/captions.html groups them, and checked as one line each.

A card is at most max_words words and max_chars characters, split at pauses over 0.25 s and after , . ! ?.
The template draws each card on one line (no wrapping) and splits a card that would still be too wide, so here a
card whose estimated width passes the band is a FAIL: it would mean a second line and a card past the bottom zone.
"""
import re
from pathlib import Path

from . import timings, zones

CAPS_W = 0.70           # width of an average bold capital, in font sizes (Montserrat 700, uppercase)


def cards(words, max_words=3, max_chars=11):
    out, cur = [], []
    for w in words:
        if cur:
            chars = len(" ".join(c["w"] for c in cur)) + 1 + len(w["w"])
            prev = cur[-1]
            if len(cur) >= max_words or chars > max_chars or w["s"] - prev["e"] > 0.25 or re.search(r"[.!?,]$", prev["w"]):
                out.append(cur)
                cur = []
        cur.append(w)
    if cur:
        out.append(cur)
    return out


def text(card):
    return " ".join(re.sub(r"[.,!?;:]+$", "", w["w"]) for w in card).upper()


def card_findings(edl):
    cap = edl.get("captions")
    if not cap:
        return []
    words = timings.shift(timings.load(Path(edl["_dir"]) / edl["voice"]["words"])["words"],
                          float(edl["voice"].get("start", 0)))
    size = float(cap.get("size", 88))
    box = zones.caption_box(cap)
    band = box[2] - box[0]
    out = []
    for c in cards(words, int(cap.get("max_words", 3)), int(cap.get("max_chars", 11))):
        width = len(text(c)) * size * CAPS_W
        lines = max(1, -(-int(width) // int(band)))
        bottom = float(cap.get("y", 1130)) - size * 0.6 + lines * size * 1.2
        if lines > 1:
            out.append(("FAIL", "captions", f'"{text(c)}" needs {lines} lines ({width:.0f} px in a {band:.0f} px band); '
                                            f"its bottom would be {bottom:.0f} px (limit {zones.H - zones.BOTTOM})"))
    return out
