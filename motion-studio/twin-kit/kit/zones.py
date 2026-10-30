"""Safe zones and text boxes (growth-engine/production/STANDARDS.md section 6, which overrules the motion-reel house zone).

At 1080x1920: top 269 px and bottom 672 px clear, side margins 65 px, and the right 227 px clear in the lower half.
Faces sit 15% to 55% from the top. Captions 80 to 100 px, placed 55% to 62% down. Body text never under 44 px.
Every box here is a conservative estimate from the move's variables, [x0, y0, x1, y1] in frame pixels.
"""
import json

W, H = 1080, 1920
TOP, BOTTOM, SIDE, RIGHT_LOWER = 269, 672, 65, 227
FACE_TOP, FACE_BOTTOM = 0.15, 0.55
CAPTION_TOP, CAPTION_BOTTOM = 0.55, 0.62
CAPTION_MIN, CAPTION_MAX = 80, 100
MIN_TEXT = 44
CHAR_W = 0.68            # width of an average capital, in font sizes (bold sans and display serif)


def breaches(box):
    """Plain-English reasons a box leaves the safe zone (empty when it is inside)."""
    x0, y0, x1, y1 = box
    out = []
    if y0 < TOP:
        out.append(f"top {y0:.0f} < {TOP}")
    if y1 > H - BOTTOM:
        out.append(f"bottom {y1:.0f} > {H - BOTTOM}")
    if x0 < SIDE:
        out.append(f"left {x0:.0f} < {SIDE}")
    if x1 > W - SIDE:
        out.append(f"right {x1:.0f} > {W - SIDE}")
    if y1 > H / 2 and x1 > W - RIGHT_LOWER:
        out.append(f"right {x1:.0f} > {W - RIGHT_LOWER} in the lower half")
    return out


def face_band_breach(face_box):
    lo, hi = FACE_TOP * H, FACE_BOTTOM * H
    if face_box[1] < lo or face_box[3] > hi:
        return f"face {face_box[1]:.0f}-{face_box[3]:.0f} px, must sit inside {lo:.0f}-{hi:.0f} (15-55% from the top)"
    return None


def centred(width, y0, y1, cx=W / 2):
    return [cx - width / 2, y0, cx + width / 2, y1]


def text_width(text, size):
    return len(str(text)) * size * CHAR_W


def caption_box(cap):
    size, y = float(cap.get("size", 88)), float(cap.get("y", 1130))
    return [float(cap.get("left", SIDE)), y - size * 0.75, W - float(cap.get("right", RIGHT_LOWER)), y + size * 0.75]


def move_box(kind, v, beat=None, head=None):
    """The text or object box of a move or scene, or None when it carries none."""
    if kind == "behind-word":
        size, y = float(v.get("size", 300)), float(v.get("y", 540))
        w = min(float(v.get("max_w", 950)), text_width(v.get("text", ""), size))
        return centred(w, y - size * 0.45, y + size * 0.45)
    if kind == "two-tone":
        size, y = float(v.get("size", 190)), float(v.get("y", 520))
        w = max(text_width(v.get("lead", ""), size * 0.42), text_width(v.get("key", ""), size))
        return centred(min(w, W - 2 * SIDE), y - size * 0.95, y + size * 0.75)
    if kind == "orbit":
        size = float(v.get("size", 58))
        words = [s for s in str(v.get("words", "")).split("|") if s]
        half = max([text_width(s, size) for s in words] or [0]) / 2
        cx, cy = float(v.get("cx", W / 2)), float(v.get("cy", 800))
        rx, ry = float(v.get("rx", 300)), float(v.get("ry", 110))
        return [cx - rx - half, cy - ry - size, cx + rx + half, cy + ry + size]
    if kind == "pop3d":
        size, x, y = float(v.get("size", 300)), float(v.get("x", W / 2)), float(v.get("y", 600))
        return [x - size / 2, y - size / 2, x + size / 2, y + size / 2 + (90 if v.get("label") else 0)]
    if kind == "end-card":
        top = float(v.get("top", 420))
        return [RIGHT_LOWER, top, W - RIGHT_LOWER, top + 520]
    if kind == "ui-notification":
        y = float(v.get("y", 380))
        n = len(json.loads(v.get("items", "[]")))
        return [70, y, W - 70, y + n * 250]
    if kind == "ui-chat":
        y = float(v.get("y", 440))
        n = len(json.loads(v.get("messages", "[]")))
        return [70, 290, W - 70, y + n * 150]
    if kind == "ui-prompt":
        y = float(v.get("y", 620))
        return [70, y - 80, W - 70, y + 320]
    return None


def text_sizes(kind, v):
    """(name, px) of every text size a move sets, for the 44 px floor."""
    if kind == "orbit":
        return [("orbit words", float(v.get("size", 58)))]
    if kind == "two-tone":
        return [("two-tone lead", float(v.get("size", 190)) * 0.42)]
    return []
