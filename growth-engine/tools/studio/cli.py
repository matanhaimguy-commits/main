"""Argument helpers shared by the studio commands (same style as hub.py: positionals first, then --name value)."""
import sys


def opt(rest: list[str], name: str, default=None):
    if name in rest:
        i = rest.index(name)
        if i + 1 >= len(rest):
            sys.exit(f"{name} needs a value")
        return rest[i + 1]
    return default


def positionals(rest: list[str], names: list[str], usage: str) -> list[str]:
    if len(rest) < len(names) or any(r.startswith("--") for r in rest[: len(names)]):
        sys.exit(f"usage: hub.py {usage}")
    return rest[: len(names)]
