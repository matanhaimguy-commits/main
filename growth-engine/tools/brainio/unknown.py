"""The "unknown: <what is missing>" convention."""


def is_unknown(v) -> bool:
    return v is None or v == "" or v == [] or (isinstance(v, str) and v.strip().lower().startswith("unknown"))


def is_placeholder(v) -> bool:
    """True when a value is only a placeholder list or string: every part unknown."""
    if isinstance(v, list):
        return all(is_placeholder(x) for x in v)
    return is_unknown(v)
