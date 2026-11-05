"""Plain spoken English: words an owner would never say out loud in a reel, unless the buyers wrote them first."""
from __future__ import annotations

import re

# Written-register and marketing words (owner, 28 Oct 2026: "who says quote?"). A word the buyers themselves use
# (it appears in buyer-phrases-en.md) is allowed.
STIFF = {
    "quote", "quoted", "quoting", "solution", "solutions", "leverage", "optimize", "optimise", "utilize", "utilise",
    "ensure", "framework", "mechanism", "ecosystem", "synergy", "streamline", "robust", "holistic", "seamless",
    "unlock", "elevate", "empower", "transform", "journey", "landscape", "navigate", "compounding", "scalable",
    "patchwork", "funnel", "qualified", "agency", "done-for-you", "growth", "prospect", "prospects", "conversion",
    "conversions", "proposal", "regarding", "therefore", "thus", "whereas", "furthermore",
}
TEASERS = ("watch this", "wait till", "wait until", "sound familiar", "check this out", "you won't believe")


def words(text: str) -> list[str]:
    return re.findall(r"[a-z][a-z'\-]*", text.lower())


def syllables(word: str) -> int:
    groups = re.findall(r"[aeiouy]+", word.lower())
    n = len(groups) - (1 if word.endswith("e") and len(groups) > 1 else 0)
    return max(n, 1)


def plain_issues(text: str, buyer_words: set[str]) -> list[str]:
    """Problems that make a line sound written, not said. Empty list = plain."""
    out, low = [], text.lower()
    for w in words(text):
        if w in buyer_words:
            continue
        if w in STIFF:
            out.append(f"stiff word '{w}' (not in the buyers' words)")
        elif syllables(w) >= 4:
            out.append(f"long word '{w}' (4+ syllables, not in the buyers' words)")
    out += [f"teaser '{t}'" for t in TEASERS if t in low]
    if "—" in text:
        out.append("em dash")
    return out
