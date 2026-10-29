"""Dotted paths into a brain: offer.main_offer, avatars[0].situation. get returns None when a step is missing."""
import re

_STEP = re.compile(r"^([A-Za-z_][\w]*)(?:\[(\d+)\])?$")


def steps(path: str) -> list[tuple[str, int | None]]:
    out = []
    for part in path.split("."):
        m = _STEP.match(part)
        if not m:
            raise ValueError(f"bad brain path: {path}")
        out.append((m.group(1), int(m.group(2)) if m.group(2) is not None else None))
    return out


def get(brain: dict, path: str):
    cur = brain
    for key, idx in steps(path):
        cur = cur.get(key) if isinstance(cur, dict) else None
        if idx is not None:
            cur = cur[idx] if isinstance(cur, list) and idx < len(cur) else None
    return cur


def set_(brain: dict, path: str, value) -> None:
    """Sets the value, creating dicts on the way. A list index must already exist, or be the next free one."""
    st, cur = steps(path), brain
    for n, (key, idx) in enumerate(st):
        last = n == len(st) - 1
        if idx is None:
            if last:
                cur[key] = value
            else:
                cur = cur.setdefault(key, {})
            continue
        lst = cur.setdefault(key, [])
        if idx > len(lst):
            raise ValueError(f"{path}: index {idx} is past the end of {key}")
        if idx == len(lst):
            lst.append(value if last else {})
        elif last:
            lst[idx] = value
        cur = lst[idx]
