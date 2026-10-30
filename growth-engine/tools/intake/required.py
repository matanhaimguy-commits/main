"""O1's gate: which required answers are missing. "I don't know" counts as an answer only where the question allows it."""
UNKNOWN = ("i don't know", "i dont know", "unknown", "?", "n/a")


def filled(v) -> bool:
    if v is None:
        return False
    if isinstance(v, str):
        return bool(v.strip())
    if isinstance(v, (list, dict)):
        return any(filled(x) for x in (v.values() if isinstance(v, dict) else v))
    return True


def is_unknown(v) -> bool:
    return isinstance(v, str) and v.strip().lower() in UNKNOWN


def missing(answers: dict, questions: list[dict]) -> list[dict]:
    """[{id, label, why}] for each required question with no usable answer."""
    out = []
    for q in questions:
        qid, a = q["id"], answers.get(q["id"])
        if not q["required"]:
            continue
        if not filled(a):
            out.append({"id": qid, "label": q["label"], "why": "empty"})
        elif is_unknown(a) and not q.get("allow_unknown_when_required"):
            out.append({"id": qid, "label": q["label"], "why": "answered 'I don't know' but this one is needed"})
        elif q.get("required_any") and not any(filled((a or {}).get(f)) for f in q["required_any"]):
            out.append({"id": qid, "label": q["label"], "why": "needs at least one of: " + ", ".join(q["required_any"])})
    return out
