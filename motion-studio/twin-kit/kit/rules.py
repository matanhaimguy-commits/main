"""The edit rules, checked on the EDL before anything renders (T3 in the twin reel machine plan).

1. one hero move per beat            4. a visual change every 2 to 3 s (never more than MAX_GAP without one)
2. every move, scene and cut has a sound from the kit   5. the twin on screen 50% of the time or less
3. hero text readable in under 1 s (few words, on screen >= 1 s)   6. no word or object over the eyes or mouth
Plus: text stays inside the 9:16 safe zone (top 250 px, bottom 400 px).
Returns a list of findings: (level, rule, message), level FAIL or WARN.
"""
from . import sfx, stage
from .moves import MOVES, SCENES, CUTS

MAX_GAP = 3.0           # seconds without a visual change
MAX_TWIN_SHARE = 0.5
MAX_HERO_WORDS = 4
MIN_HERO_TIME = 1.0
SAFE_TOP, SAFE_BOTTOM = 250, 400
FRONT_LAYERS = ("words-front", "split")


def hero_at(beat):
    return beat["start"] + float(beat["hero"].get("vars", {}).get("at", 0)) if beat.get("hero") else None


def words_in(value):
    return len(str(value).replace("|", " ").split())


def text_box(edl, move, v):
    """A conservative box [x0, y0, x1, y1] around a front move's text or object, or None if it has none."""
    w = edl["width"]
    if move == "two-tone":
        size = float(v.get("size", 150))
        y = float(v.get("y", 400))
        return [60, y - size * 1.05, w - 60, y + size * 1.05]
    if move == "pop3d":
        size, x, y = float(v.get("size", 300)), float(v.get("x", w / 2)), float(v.get("y", 600))
        return [x - size / 2, y - size / 2, x + size / 2, y + size / 2 + (90 if v.get("label") else 0)]
    if move == "end-card":
        return None
    return None


def caption_box(edl):
    c = edl.get("captions")
    if not c:
        return None
    size, y = float(c.get("size", 64)), float(c.get("y", 1380))
    return [90, y - size * 0.8, edl["width"] - 90, y + size * 0.8]


def check(edl, face=None):
    out = []

    def add(level, rule, msg):
        out.append((level, rule, msg))

    dur = edl["duration"]
    events = [0.0]
    twin_time = 0.0
    cap = caption_box(edl)
    if cap and (cap[1] < SAFE_TOP or cap[3] > edl["height"] - SAFE_BOTTOM):
        add("FAIL", "safe-zone", f"captions band {cap[1]:.0f}-{cap[3]:.0f} px leaves the safe zone")

    for b in edl["beats"]:
        bid, length = b["id"], b["end"] - b["start"]
        events.append(b["start"])
        mode = b.get("twin", "off")
        if mode != "off":
            twin_time += length
        hero, scene, cut = b.get("hero"), b.get("scene"), b.get("cut_in")
        # 1. one hero move per beat
        if isinstance(hero, list):
            add("FAIL", "one-hero", f"{bid}: {len(hero)} hero moves (one per beat)")
            continue
        if not hero and not scene and not cut:
            add("WARN", "one-hero", f"{bid}: no hero move, scene or cut")
        # 2. every move with a sound
        grade = b.get("grade")
        for item, table in ((hero, MOVES), (grade, MOVES), (scene, SCENES), ({"move": cut} if cut else None, CUTS)):
            if not item:
                continue
            kind = item["move"]
            name = item.get("sfx", table[kind]["sfx"])
            if not name or not sfx.exists(name):
                add("FAIL", "sound", f"{bid}: {kind} has no sound from the kit ({name!r})")
        if grade:
            events.append(b["start"] + float(grade.get("vars", {}).get("at", 0)))
        if scene:
            events.append(b["start"] + float(scene.get("vars", {}).get("at", 0)))
        if hero:
            v = hero.get("vars", {})
            events.append(hero_at(b))
            # 3. readable in under 1 s
            spec = MOVES[hero["move"]]
            for key in spec["text"]:
                if key not in v:
                    continue
                if hero["move"] == "orbit":
                    long_items = [s for s in str(v[key]).split("|") if words_in(s) > 2]
                    if long_items:
                        add("FAIL", "readable", f"{bid}: orbit items over 2 words: {long_items}")
                elif hero["move"] == "two-tone":
                    pass
                elif words_in(v[key]) > MAX_HERO_WORDS:
                    add("FAIL", "readable", f"{bid}: {key} has {words_in(v[key])} words (max {MAX_HERO_WORDS})")
            if hero["move"] == "two-tone":
                n = words_in(v.get("lead", "")) + words_in(v.get("key", ""))
                if n > MAX_HERO_WORDS:
                    add("FAIL", "readable", f"{bid}: two-tone has {n} words (max {MAX_HERO_WORDS})")
            on_screen = b["end"] - hero_at(b)
            if on_screen < MIN_HERO_TIME - 1e-6:
                add("FAIL", "readable", f"{bid}: {hero['move']} is on screen {on_screen:.2f} s (min {MIN_HERO_TIME})")
            # 6. never over the eyes or mouth (front layers only: behind-twin words are hidden by the twin)
            box = text_box(edl, hero["move"], v)
            fbox = stage.face_on_frame(edl, mode, face)
            if box and spec["layer"] in FRONT_LAYERS:
                if box[1] < SAFE_TOP or box[3] > edl["height"] - SAFE_BOTTOM:
                    add("FAIL", "safe-zone", f"{bid}: {hero['move']} band {box[1]:.0f}-{box[3]:.0f} px leaves the safe zone")
                if fbox and stage.overlaps(box, fbox):
                    add("FAIL", "face", f"{bid}: {hero['move']} covers the face ({_fmt(box)} vs face {_fmt(fbox)})")
        if cap and mode != "off" and not b.get("no_captions"):
            fbox = stage.face_on_frame(edl, mode, face)
            if fbox and stage.overlaps(cap, fbox):
                add("FAIL", "face", f"{bid}: captions cover the face in twin mode {mode!r}")
        if face is None and mode != "off":
            add("WARN", "face", f"{bid}: no face data, face rule not checked")

    # 4. a visual change every 2 to 3 s
    events = sorted(set(round(e, 3) for e in events)) + [dur]
    gaps = [(b - a, a) for a, b in zip(events, events[1:])]
    worst = max(gaps)
    if worst[0] > MAX_GAP + 1e-6:
        add("FAIL", "pacing", f"{worst[0]:.2f} s without a visual change from {worst[1]:.2f} s (max {MAX_GAP})")
    # 5. twin on screen 50% or less
    share = twin_time / dur
    if share > MAX_TWIN_SHARE + 1e-6:
        add("FAIL", "twin-share", f"twin on screen {share:.0%} of the film (max {MAX_TWIN_SHARE:.0%})")
    return out


def _fmt(box):
    return "[" + ", ".join(f"{v:.0f}" for v in box) + "]"


def summary(edl, face=None):
    """Numbers for the report: twin share, longest gap between visual changes, hero count."""
    dur = edl["duration"]
    twin = sum(b["end"] - b["start"] for b in edl["beats"] if b.get("twin", "off") != "off")
    return {"twin_share": round(twin / dur, 3), "beats": len(edl["beats"]),
            "heroes": sum(1 for b in edl["beats"] if b.get("hero"))}
