"""Where the twin stands in each mode, and where its face lands on the 1080x1920 frame.

stage: cut out and small, the set around it, the face 15-55% from the top (STANDARDS 6) and the clip's edges faded
into the set (fade_x, fade_y: share of the clip's width and height) so its box edges never show. full: the clip at full width (a punch-in on the
host). off: not on screen (B-roll, UI or end card carry the frame). Modes can be tuned per EDL in twin.modes.
"""

DEFAULT_MODES = {
    # scale of the clip, the frame y where the clip's top edge sits (x is centred), and the soft-edge shares
    "stage": {"scale": 0.5, "top": 520, "fade_x": 0.16, "fade_y": 0.24},
    "full": {"scale": 1.0, "top": -40, "fade_x": 0.0, "fade_y": 0.0},
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


def fades(edl, mode):
    m = modes(edl).get(mode, {})
    return float(m.get("fade_x", 0)), float(m.get("fade_y", 0))


def orbit_geometry(edl, beat, v, face):
    """Orbit variables with the ring centred on the head and the face box passed in (EDL values win)."""
    out = dict(v)
    mode = beat.get("twin", "off")
    head, fbox = head_on_frame(edl, mode, face), face_on_frame(edl, mode, face)
    if head:
        # a halo at forehead height: the far side passes behind the crown, the near side stays above the brows
        hh = head[3] - head[1]
        out.setdefault("cx", round((head[0] + head[2]) / 2))
        out.setdefault("cy", round(head[1] + hh * 0.11))
        out.setdefault("rx", round((head[2] - head[0]) * 0.95))
        out.setdefault("ry", round(hh * 0.09))
    if fbox:
        out["face"] = ",".join(str(round(x)) for x in fbox)
    return out
