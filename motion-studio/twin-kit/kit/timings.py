"""Word timings: the voice is the master clock. Format: {"source", "duration", "words": [{"w", "s", "e"}]}."""
import json
import re
from pathlib import Path


def load(path):
    data = json.loads(Path(path).read_text())
    words = data["words"]
    for i, w in enumerate(words):
        if not (0 <= w["s"] <= w["e"]):
            raise ValueError(f"word {i} {w['w']!r}: bad times")
        if i and w["s"] < words[i - 1]["s"]:
            raise ValueError(f"word {i} {w['w']!r} starts before the word before it")
    return data


def norm(word):
    return re.sub(r"[^a-z0-9']", "", word.lower())


def find(words, text, after=0.0):
    """The first word matching `text` (punctuation and case ignored) that starts at or after `after`."""
    target = norm(text)
    for w in words:
        if w["s"] >= after - 1e-9 and norm(w["w"]) == target:
            return w
    raise KeyError(f"{text!r} not spoken after {after:.2f} s")


def shift(words, offset):
    """The same words moved onto the film clock (the voice starts `offset` seconds in)."""
    return [{**w, "s": round(w["s"] + offset, 3), "e": round(w["e"] + offset, 3)} for w in words]


def phrases(words, gap=0.25):
    """Groups of words split at pauses longer than `gap` or at sentence punctuation."""
    out, cur = [], []
    for w in words:
        if cur and (w["s"] - cur[-1]["e"] > gap or re.search(r"[.!?]$", cur[-1]["w"])):
            out.append(cur)
            cur = []
        cur.append(w)
    if cur:
        out.append(cur)
    return out
