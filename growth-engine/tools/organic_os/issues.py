"""Check results: an issue is {level, code, msg}; ERROR blocks, WARN informs."""
from __future__ import annotations

ERROR, WARN = "error", "warn"


def issue(level: str, code: str, msg: str) -> dict:
    return {"level": level, "code": code, "msg": msg}


def has_errors(issues: list[dict]) -> bool:
    return any(i["level"] == ERROR for i in issues)


def unknown(v) -> bool:
    """Empty, or a placeholder the Brain Builder left for a gap."""
    if v is None:
        return True
    if isinstance(v, str):
        s = v.strip().lower()
        return not s or s.startswith(("unknown", "tbd", "todo", "gap:"))
    if isinstance(v, (list, dict)):
        return len(v) == 0
    return False
