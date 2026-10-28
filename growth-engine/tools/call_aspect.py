"""The frame shape a generation call asks for, against its Shot Spec's camera.aspect (the gate's aspect check).

A model sets the shape one of three ways: `aspect_ratio` or `ratio` ("9:16"), or `size` ("1152x2048"). Every one the
call passes must match the spec. An Atlas entry's `size_for_aspect` names the sizes that make a spec aspect the model
has no exact size for (gpt-image-2 has no 4:5 size: a 4:5 slide is made at 1024x1536 and cropped to 4:5 at export).
Tests: growth-engine/tools/test_call_aspect.py.
"""
from __future__ import annotations

import re
from fractions import Fraction

SHAPE_KEYS = ("aspect_ratio", "ratio", "size")
_PAIR = re.compile(r"\s*(\d+)\s*[:xX]\s*(\d+)\s*$")


def ratio(text) -> Fraction | None:
    """'9:16' or '1152x2048' as width/height; None for anything else ('adaptive', missing, zero)."""
    m = _PAIR.match(text) if isinstance(text, str) else None
    if not m or not int(m.group(1)) or not int(m.group(2)):
        return None
    return Fraction(int(m.group(1)), int(m.group(2)))


def mismatch(params: dict, aspect: str, size_for_aspect: dict | None = None) -> list[str]:
    """Why the call's shape differs from the spec's aspect (empty: it matches)."""
    given = [k for k in SHAPE_KEYS if k in params]
    if not given:
        return [f"no aspect_ratio, ratio or size in the call: the Shot Spec is {aspect} (pass the one the model takes)"]
    why = []
    for k in given:
        v = params[k]
        if k == "size" and size_for_aspect:
            sizes = size_for_aspect.get(aspect) or []
            if v not in sizes:
                why.append(f"size {v} differs from the Shot Spec ({aspect}): this model makes {aspect} at "
                           f"{' or '.join(sizes) if sizes else 'no size (size_for_aspect)'}")
        elif ratio(v) is None or ratio(v) != ratio(aspect):
            why.append(f"{k} {v} differs from the Shot Spec ({aspect})")
    return why
