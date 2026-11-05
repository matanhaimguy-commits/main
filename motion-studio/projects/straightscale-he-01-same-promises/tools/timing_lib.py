"""Shared helpers for the film's ONE timing file, film/timing.json (lines, words, cues, tail).

Only "lines" and "source" are ever rewritten by the tools. "cues" (what happens on which word) and "tail" (end-card
hold) are design data: edit them by hand, the tools keep them.
"""
import json
import re
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
SCRIPT = PROJECT / "docs" / "script.md"
TIMING = PROJECT / "film" / "timing.json"
ROW = re.compile(r"^\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*[^|]*\|\s*([\d.]+)-([\d.]+)\s*\|")


def script_lines():
    """[(id, hebrew_text, start, end)] from the table in section 2 of docs/script.md."""
    text = SCRIPT.read_text(encoding="utf-8")
    body = text.split("## 2.", 1)[1].split("## 3.", 1)[0]
    out = []
    for row in body.splitlines():
        m = ROW.match(row)
        if m:
            out.append((int(m.group(1)), m.group(2), float(m.group(3)), float(m.group(4))))
    return out


def letters(word):
    """The word without punctuation or quotes, for matching and for length."""
    return re.sub(r"[^\w֐-׿]", "", word)


def load():
    if TIMING.exists():
        return json.loads(TIMING.read_text(encoding="utf-8"))
    return {"version": 1, "source": "", "tail": 2.4, "lines": [], "cues": {}}


def save(data):
    """One cue or word per line, so a retime shows up as a readable diff."""
    j = lambda v: json.dumps(v, ensure_ascii=False)
    cues = ",\n".join(f"  {j(k)}: {j(v)}" for k, v in data["cues"].items())
    lines = []
    for line in data["lines"]:
        head = {k: v for k, v in line.items() if k != "words"}
        words = ",\n".join(f"    {j(w)}" for w in line["words"])
        lines.append(f"  {j(head)[:-1]}, \"words\": [\n{words}\n  ]}}")
    TIMING.write_text(
        f"{{\n \"version\": {data.get('version', 1)},\n \"source\": {j(data['source'])},\n \"tail\": {data['tail']},\n"
        f" \"cues\": {{\n{cues}\n }},\n \"lines\": [\n" + ",\n".join(lines) + "\n ]\n}\n", encoding="utf-8")
