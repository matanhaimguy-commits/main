"""Writes Brand card overrides into a brain (a copy), with a source on each field. Nothing is saved here."""
import copy

from brainio import paths

from . import convert, proof
from .mapping import FIELDS

SOURCE_PREFIX = "Matan (Brand card"


def source_for(day: str) -> str:
    return f"{SOURCE_PREFIX}, {day})"


def blank_avatar() -> dict:
    u = "unknown: filled by the draft or research"
    return {"id": "AV-01", "name": u, "role": u, "situation": u, "words": [u], "fears": [u], "desires": [u]}


def apply(brain: dict, overrides: dict, day: str) -> tuple[dict, list[dict], list[str]]:
    """Returns (new brain, changes [{field, path, old, new}], problems). With any problem the caller writes nothing."""
    new, changes, problems = copy.deepcopy(brain), [], []
    src = source_for(day)
    for field in sorted(overrides):
        if field not in FIELDS:
            problems.append(f"{field}: not a Brand card field (known: {', '.join(FIELDS)})")
            continue
        path, kind = FIELDS[field]
        try:
            if kind == "proof":
                value = proof.merge(paths.get(new, path) or [], proof.items(overrides[field], src, day), SOURCE_PREFIX)
            else:
                value = convert.CONVERTERS[kind](overrides[field])
        except ValueError as e:
            problems.append(f"{field}: {e}")
            continue
        if path.startswith("avatars[0]") and not new.get("avatars"):
            new["avatars"] = [blank_avatar()]
        old = paths.get(new, path)
        if old != value:
            paths.set_(new, path, value)
            changes.append({"field": field, "path": path, "old": old, "new": value})
            new.setdefault("field_sources", {})[path] = src
        else:
            new.setdefault("field_sources", {}).setdefault(path, src)
    if new != brain:
        new["updated"] = day
    return new, changes, problems
