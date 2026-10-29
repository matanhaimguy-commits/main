"""A card's motion-studio project: its stage and gate score from PROJECT.md, the hook text from docs/hooks.json and
the hub item's external_key from hub/item.json."""
import json
import re
from pathlib import Path

MASTER = re.compile(r"master ([A-Z]{2,5}\d*-[A-Z0-9]+)")
SCORE = re.compile(r"gate (\d{2,3})/100")
NOTE_HOOK = re.compile(r"(Text hook|Spoken hook)[^:']*: '(.+?)'(?=[\s.,;:)]|$)")


def _read_json(p: Path):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


def status(doc: Path) -> dict:
    """`Stage:` and the first `gate NN/100` of the Status section in PROJECT.md."""
    if not doc.is_file():
        return {}
    text = doc.read_text(encoding="utf-8")
    sec = text.split("## Status", 1)[1].split("\n## ", 1)[0] if "## Status" in text else ""
    out = {}
    m = re.search(r"^Stage:\s*(.+)$", sec, re.M)
    if m:
        out["stage"] = m.group(1).strip()
    s = SCORE.search(sec)
    if s:
        out["gate_score"] = int(s.group(1))
    return out


def hook(proj: Path | None, card: dict) -> dict | None:
    """The master hook in docs/hooks.json (the id the card's source_ref names as master, else the first), else the
    hook written in the card's notes."""
    hooks = _read_json(proj / "docs" / "hooks.json") if proj else None
    if isinstance(hooks, list) and hooks:
        m = MASTER.search(card.get("source_ref") or "")
        h = next((h for h in hooks if m and h.get("id") == m.group(1)), hooks[0])
        out = {"id": h.get("id"), "text": h.get("text"), "spoken": h.get("spoken"), "source": "docs/hooks.json"}
        return {**out, "grade": h["grade"]} if h.get("grade") else out
    m = NOTE_HOOK.search(card.get("notes") or "")
    if m:
        key = "text" if m.group(1) == "Text hook" else "spoken"
        return {"id": None, key: m.group(2), "source": "card notes"}
    return None


def facts(root: Path, card: dict) -> dict:
    rel_dir = card.get("project")
    proj = Path(root) / rel_dir if rel_dir else None
    if proj and not proj.is_dir():
        proj = None
    item = _read_json(proj / "hub" / "item.json") if proj else None
    return {"project": rel_dir if proj else None, **(status(proj / "PROJECT.md") if proj else {}),
            "hook": hook(proj, card), "content_external_key": (item or {}).get("external_key")}
