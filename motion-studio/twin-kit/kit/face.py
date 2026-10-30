"""Where the face is in the cut-out clip, from its alpha matte, so no word lands on the eyes or mouth.

The head is the silhouette above the neck (the narrowest row between the top of the head and the shoulders). The
face band (brows to chin) is a fixed share of that head height. Sampled across the clip and unioned, in the clip's
own pixels. Output: {"src_w", "src_h", "head": [x0, y0, x1, y1], "face": [x0, y0, x1, y1], "samples": n}.
"""
import json
import subprocess

import numpy as np

SCALE_W = 270          # analyse at this width (fast, accurate to a few px at 1080)
FACE_TOP, FACE_BOTTOM = 0.28, 1.08   # share of head height (top of hair to narrowest row): brows to chin


def alpha_frames(path, every=0.5):
    probe = json.loads(subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height",
         "-of", "json", str(path)], capture_output=True, text=True, check=True).stdout)["streams"][0]
    w, h = probe["width"], probe["height"]
    sh = int(round(h * SCALE_W / w / 2) * 2)
    raw = subprocess.run(
        ["ffmpeg", "-v", "error", "-c:v", "libvpx-vp9", "-i", str(path), "-vf",
         f"fps={1 / every},alphaextract,scale={SCALE_W}:{sh}", "-f", "rawvideo", "-pix_fmt", "gray", "-"],
        capture_output=True, check=True).stdout
    frames = np.frombuffer(raw, np.uint8).reshape(-1, sh, SCALE_W)
    return w, h, frames


def head_box(mask):
    """[x0, y0, x1, y1] of the head in one boolean mask (analysis pixels), or None if nobody is there."""
    widths = mask.sum(axis=1)
    rows = np.nonzero(widths > 2)[0]
    if len(rows) == 0:
        return None
    top = rows[0]
    max_w = widths.max()
    # shoulders: first row below the top that is wider than 85% of the widest row
    below = np.nonzero(widths[top:] > 0.85 * max_w)[0]
    shoulders = top + (below[0] if len(below) else len(widths) - top)
    # neck: narrowest row between 40% of the way down and the shoulders
    lo = top + max(1, int(0.4 * (shoulders - top)))
    neck = lo + int(np.argmin(widths[lo:shoulders])) if shoulders > lo else shoulders
    head = mask[top:neck]
    cols = np.nonzero(head.any(axis=0))[0]
    return [int(cols[0]), int(top), int(cols[-1]) + 1, int(neck)]


def face_from_head(head):
    x0, y0, x1, y1 = head
    hh = y1 - y0
    return [x0, y0 + FACE_TOP * hh, x1, y0 + FACE_BOTTOM * hh]


def union(boxes):
    a = np.array(boxes, float)
    return [float(a[:, 0].min()), float(a[:, 1].min()), float(a[:, 2].max()), float(a[:, 3].max())]


def run(path, every=0.5):
    w, h, frames = alpha_frames(path, every)
    k = w / SCALE_W
    heads = [b for b in (head_box(f > 127) for f in frames) if b]
    if not heads:
        raise ValueError(f"no person found in {path}")
    head = [round(v * k) for v in union(heads)]
    face = [round(v * k) for v in union([face_from_head(b) for b in heads])]
    return {"src_w": w, "src_h": h, "head": head, "face": face, "samples": len(heads)}
