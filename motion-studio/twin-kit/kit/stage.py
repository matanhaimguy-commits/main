"""Where the twin stands in each mode, and where its face lands on the 1080x1920 frame.

stage: cut out and small in the bottom third, the set above it. full: the clip at full width (a punch-in on the
host). off: not on screen (B-roll, UI or end card carry the frame). Modes can be tuned per EDL in twin.modes.
"""

DEFAULT_MODES = {
    # scale of the clip, and the frame y where the clip's top edge sits (x is centred)
    "stage": {"scale": 0.5, "top": 1060},
    "full": {"scale": 1.0, "top": -40},
}


def modes(edl):
    out = {k: dict(v) for k, v in DEFAULT_MODES.items()}
    for k, v in edl.get("twin", {}).get("modes", {}).items():
        out.setdefault(k, {}).update(v)
    return out


def placement(edl, mode, src_w):
    """(scale, left, top) of the clip in frame pixels, or None when the twin is off."""
    if mode == "off":
        return None
    m = modes(edl)[mode]
    s = m["scale"]
    return s, (edl["width"] - src_w * s) / 2, m["top"]


def to_frame(box, place):
    s, left, top = place
    x0, y0, x1, y1 = box
    return [left + x0 * s, top + y0 * s, left + x1 * s, top + y1 * s]


def face_on_frame(edl, mode, face):
    """The face box (brows to chin) on the frame for this mode, or None when the twin is off or no face data."""
    if not face or mode == "off":
        return None
    return to_frame(face["face"], placement(edl, mode, face["src_w"]))


def head_on_frame(edl, mode, face):
    if not face or mode == "off":
        return None
    return to_frame(face["head"], placement(edl, mode, face["src_w"]))


def overlaps(a, b):
    return a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]
