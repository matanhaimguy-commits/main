"""The line table (timeline.md rows `| <PREFIX>-L01 | Section | Words |`) as lines and alignment tokens."""
from __future__ import annotations

import re


def norm(word: str) -> str:
    """Lower case, letters and inner apostrophes only: the form the pronouncing dictionary uses."""
    return re.sub(r"[^a-z']", "", word.lower()).strip("'")


def read_lines(md_text: str, prefix: str) -> list[dict]:
    """[{id, section, text, tokens}] in table order for one master (prefix O60 or O30)."""
    rows = re.findall(r"^\| (%s-L\d+) \| ([^|]+?) \| (.+?) \|\s*$" % re.escape(prefix), md_text, re.M)
    out = []
    for line_id, section, text in rows:
        tokens = [n for n in (norm(w) for w in text.split()) if n]
        out.append({"id": line_id, "section": section.strip(), "text": text.strip(), "tokens": tokens})
    return out
