"""Turns a Brand card value into the type brain.json holds. Each function returns the value or raises ValueError."""
import re


def text(v) -> str:
    if not isinstance(v, str) or not v.strip():
        raise ValueError("needs a non-empty text")
    return v.strip()


def _list(v, sep: str) -> list[str]:
    parts = v if isinstance(v, list) else re.split(sep, v) if isinstance(v, str) else None
    if parts is None or not all(isinstance(p, str) for p in parts):
        raise ValueError("needs a list of texts, or one text")
    out = [p.strip().lstrip("-*• ").strip() for p in parts]
    out = [p for p in out if p]
    if not out:
        raise ValueError("needs at least one entry")
    return out


def list_commas(v) -> list[str]:
    return _list(v, r"[,\n;]")


def list_lines(v) -> list[str]:
    return _list(v, r"[\n;]")


def keyword(v) -> str:
    t = text(v)
    if re.search(r"\s", t):
        raise ValueError("a DM keyword is one word")
    return t


def usd(v):
    """A number of at least 0, or null to clear the cap."""
    if v is None:
        return None
    if isinstance(v, str) and re.fullmatch(r"\s*\d+(\.\d+)?\s*", v):
        v = float(v)
    if isinstance(v, bool) or not isinstance(v, (int, float)) or v < 0:
        raise ValueError("needs a number of 0 or more (USD), or null")
    return v


def count(v) -> int:
    if isinstance(v, str) and re.fullmatch(r"\s*\d+\s*", v):
        v = int(v)
    if isinstance(v, bool) or not isinstance(v, int) or not 1 <= v <= 21:
        raise ValueError("needs a whole number of posts a week, 1 to 21")
    return v


CONVERTERS = {"text": text, "list_commas": list_commas, "list_lines": list_lines, "keyword": keyword, "usd": usd, "count": count}
