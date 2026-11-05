"""The evidence a hook must cite: a proven format from the Hook Library and the buyers' own phrases."""
from __future__ import annotations

import re
from pathlib import Path

from .hook_plain import words

ENTRY = re.compile(r"^\s*- `(H[FLA]-\d+)`(.*)")  # entry lines only; ids are also cited inside other entries
DAYS = re.compile(r"(\d+) days")
BREAKOUT = re.compile(r"(\d+(?:\.\d+)?)x\b")
PHRASE = re.compile(r"^\s*- `(Q-[A-Z]+-\d+)`\s*(.*)")
MIN_BREAKOUT = 3.0  # STORY-FORMATS / ORGANIC-OS outlier bar; 10x+ for copying a structure
MIN_DAYS = 30       # Hook Lab H1: an ad still running after 30+ days is a winner


def library(path: Path) -> dict[str, float]:
    """Format id -> its proof: breakout over the creator's median (HF, HL) or days running (HA, ads).
    Losers (HL-) are kept so a citation of one fails loudly."""
    out = {}
    for line in path.read_text().splitlines():
        m = ENTRY.search(line)
        if m:
            b = (DAYS if m.group(1).startswith("HA-") else BREAKOUT).search(m.group(2))
            out[m.group(1)] = float(b.group(1)) if b else 0.0
    return out


def phrases(path: Path) -> dict[str, str]:
    """Phrase id -> the buyer's verbatim words."""
    out = {}
    for line in path.read_text().splitlines():
        m = PHRASE.search(line)
        if m:
            out[m.group(1)] = m.group(2)
    return out


def buyer_vocab(ph: dict[str, str]) -> set[str]:
    return {w for text in ph.values() for w in words(text)}


def source_issues(stack: dict, lib: dict[str, float], ph: dict[str, str]) -> list[str]:
    out = []
    fmt = stack.get("format_id")
    if not fmt:
        out.append("no proven format cited (format_id)")
    elif fmt not in lib:
        out.append(f"format {fmt} is not in the Hook Library")
    elif fmt.startswith("HL-"):
        out.append(f"format {fmt} is a loser in the Hook Library")
    elif fmt.startswith("HA-") and lib[fmt] < MIN_DAYS:
        out.append(f"ad {fmt} ran {lib[fmt]:.0f} days, under the {MIN_DAYS}-day bar")
    elif fmt.startswith("HF-") and lib[fmt] < MIN_BREAKOUT:
        out.append(f"format {fmt} is {lib[fmt]}x, under the {MIN_BREAKOUT}x outlier bar")
    ids = stack.get("voc_ids") or []
    if not ids:
        out.append("no buyer phrase cited (voc_ids)")
    missing = [i for i in ids if i not in ph]
    if missing:
        out.append(f"buyer phrase ids not found: {', '.join(missing)}")
    cited = {w for i in ids if i in ph for w in words(ph[i]) if len(w) > 3}
    said = {w for w in words(stack.get("spoken", "") + " " + stack.get("text", "")) if len(w) > 3}
    if ids and not missing and not (cited & said):
        out.append("the hook uses none of the cited buyers' words")
    return out
