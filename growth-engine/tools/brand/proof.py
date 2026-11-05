"""The Brand card's proof bank into brain.json's proof_bank items.

The card's entries are texts or {text, type?, permission?, date?}. Each becomes {id, type, text, source, permission, date}.
Permission is the card's own, else "pending": a proof line is not public until its permission is yes. Items that an
earlier brand-pull wrote and the card no longer holds are removed; items from documents are kept."""
import re

PERMISSIONS = ("yes", "no", "pending", "internal_only")


def items(value, source: str, today: str) -> list[dict]:
    if not isinstance(value, list) or not value:
        raise ValueError("needs a list of proof entries")
    out = []
    for n, e in enumerate(value, 1):
        e = {"text": e} if isinstance(e, str) else e
        if not isinstance(e, dict) or not isinstance(e.get("text"), str) or not e["text"].strip():
            raise ValueError(f"entry {n} needs a text")
        perm = e.get("permission", "pending")
        if perm not in PERMISSIONS:
            raise ValueError(f"entry {n}: permission must be one of {', '.join(PERMISSIONS)}")
        out.append({"type": str(e.get("type") or "claim"), "text": e["text"].strip(), "source": source,
                    "permission": perm, "date": str(e.get("date") or today)})
    return out


def merge(existing: list[dict], new: list[dict], source_prefix: str) -> list[dict]:
    """Document proof is kept. Proof an earlier brand-pull wrote stays (with its id, date and source) while the card
    still holds its text, taking the card's type and permission, and goes when the card drops it. New lines are added
    with ids that continue after the highest."""
    by_text = {p["text"]: p for p in new}
    out = []
    for p in existing:
        card = str(p.get("source", "")).startswith(source_prefix)
        if not card:
            out.append(p)
        elif p["text"] in by_text:
            out.append({**p, "type": by_text[p["text"]]["type"], "permission": by_text[p["text"]]["permission"]})
    have = {p["text"] for p in out}
    top = max([int(m.group(1)) for p in out if (m := re.fullmatch(r"P-(\d+)", str(p.get("id", ""))))] or [0])
    for p in new:
        if p["text"] not in have:
            top += 1
            out.append({"id": f"P-{top:02d}", **p})
    return out
