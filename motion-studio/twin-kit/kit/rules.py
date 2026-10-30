"""The edit rules, checked on the EDL before anything renders (T3 in the twin reel machine plan, STANDARDS 6).

1. one hero move per beat                  5. the twin on screen 50% of the time or less
2. every move, scene, grade and cut has a sound from the kit
3. hero text readable in under 1 s (few words, on screen >= 1 s)
4. a visual change at least every MAX_GAP s
6. no front word, object or caption on the face; the face sits 15-55% from the top
7. every text layer (behind-twin words, UI and captions too) inside the safe zone; captions 80-100 px; text >= 44 px
   at its smallest on-screen scale; no two text layers overlap; a word behind the head never has a letter covered
   (kit/text_rules.py)
Returns a list of findings: (level, rule, message), level FAIL or WARN.
"""
from . import sfx, stage, text_rules, zones
from .moves import MOVES, SCENES, CUTS

MAX_GAP = 3.0
MAX_TWIN_SHARE = 0.5
MAX_HERO_WORDS = 4
MIN_HERO_TIME = 1.0
FRONT_LAYERS = ("words-front", "split")


def hero_at(beat):
    return beat["start"] + float(beat["hero"].get("vars", {}).get("at", 0)) if beat.get("hero") else None


def words_in(value):
    return len(str(value).replace("|", " ").split())


def hero_vars(edl, beat, face):
    """The hero's variables as the film will mount them (orbit gets its ring from the head)."""
    v = dict(beat["hero"].get("vars", {}))
    if beat["hero"]["move"] == "orbit":
        v = stage.orbit_geometry(edl, beat, v, face)
    return v


def check(edl, face=None):
    out = []

    def add(level, rule, msg):
        out.append((level, rule, msg))

    dur = edl["duration"]
    events, twin_time = [0.0], 0.0
    cap = edl.get("captions")
    cap_box = zones.caption_box(cap) if cap else None
    if cap:
        size = float(cap.get("size", 88))
        if not zones.CAPTION_MIN <= size <= zones.CAPTION_MAX:
            add("FAIL", "size", f"captions {size:.0f} px (want {zones.CAPTION_MIN}-{zones.CAPTION_MAX})")
        for why in zones.breaches(cap_box):
            add("FAIL", "safe-zone", f"captions: {why}")
        y = float(cap.get("y", 1130)) / zones.H
        if not zones.CAPTION_TOP <= y <= zones.CAPTION_BOTTOM:
            add("WARN", "safe-zone", f"captions centred {y:.0%} down (want 55-62%)")

    for b in edl["beats"]:
        bid, length = b["id"], b["end"] - b["start"]
        events.append(b["start"])
        mode = b.get("twin", "off")
        fbox = stage.face_on_frame(edl, mode, face)
        if mode != "off":
            twin_time += length
            if face is None:
                add("WARN", "face", f"{bid}: no face data, face rules not checked")
            elif zones.face_band_breach(fbox):
                add("FAIL", "face-band", f"{bid}: {zones.face_band_breach(fbox)}")
        hero, scene, grade, cut = b.get("hero"), b.get("scene"), b.get("grade"), b.get("cut_in")
        if isinstance(hero, list):
            add("FAIL", "one-hero", f"{bid}: {len(hero)} hero moves (one per beat)")
            continue
        if not hero and not scene and not cut:
            add("WARN", "one-hero", f"{bid}: no hero move, scene or cut")
        for item, table in ((hero, MOVES), (grade, MOVES), (scene, SCENES), ({"move": cut} if cut else None, CUTS)):
            if item:
                name = item.get("sfx", table[item["move"]]["sfx"])
                if not name or not sfx.exists(name):
                    add("FAIL", "sound", f"{bid}: {item['move']} has no sound from the kit ({name!r})")
        for item in (grade, scene):
            if item:
                events.append(b["start"] + float(item.get("vars", {}).get("at", 0)))
        if scene:
            out += [(lv, r, f"{bid}: {m}") for lv, r, m in text_rules.scene_findings(scene)]
        hv = hero_vars(edl, b, face) if hero else {}
        if hero:
            events.append(hero_at(b))
            out += [(lv, r, f"{bid}: {m}") for lv, r, m in hero_findings(edl, b, mode, fbox, face)]
            if hero["move"] == "behind-word":
                out += [(lv, r, f"{bid}: {m}") for lv, r, m in text_rules.head_clear_findings(edl, b, hv, face)]
        layers = text_rules.text_layers(edl, b, hv, cap_box)
        out += [(lv, r, f"{bid}: {m}") for lv, r, m in text_rules.overlap_findings(layers)]
        if cap_box and fbox and not b.get("no_captions") and stage.overlaps(cap_box, fbox):
            add("FAIL", "face", f"{bid}: captions cover the face in twin mode {mode!r}")

    events = sorted(set(round(e, 3) for e in events)) + [dur]
    gap, at = max((b - a, a) for a, b in zip(events, events[1:]))
    if gap > MAX_GAP + 1e-6:
        add("FAIL", "pacing", f"{gap:.2f} s without a visual change from {at:.2f} s (max {MAX_GAP})")
    if twin_time / dur > MAX_TWIN_SHARE + 1e-6:
        add("FAIL", "twin-share", f"twin on screen {twin_time / dur:.0%} of the film (max {MAX_TWIN_SHARE:.0%})")
    return out


def hero_findings(edl, b, mode, fbox, face):
    hero = b["hero"]
    kind, spec = hero["move"], MOVES[hero["move"]]
    v = hero_vars(edl, b, face)
    out = []
    if kind == "orbit":
        long_items = [s for s in str(v.get("words", "")).split("|") if words_in(s) > 2]
        if long_items:
            out.append(("FAIL", "readable", f"orbit items over 2 words: {long_items}"))
    else:
        n = sum(words_in(v[k]) for k in spec["text"] if k in v)
        if n > MAX_HERO_WORDS:
            out.append(("FAIL", "readable", f"{kind} has {n} words (max {MAX_HERO_WORDS})"))
    on_screen = b["end"] - hero_at(b)
    if on_screen < MIN_HERO_TIME - 1e-6:
        out.append(("FAIL", "readable", f"{kind} is on screen {on_screen:.2f} s (min {MIN_HERO_TIME})"))
    for name, px in zones.text_sizes(kind, v):
        if px < zones.MIN_TEXT:
            out.append(("FAIL", "size", f"{name} {px:.0f} px (min {zones.MIN_TEXT})"))
    box = zones.move_box(kind, v)
    if box:
        out += [("FAIL", "safe-zone", f"{kind}: {why}") for why in zones.breaches(box)]
        # orbit near words skip the face box themselves; other front moves must stay off it
        if fbox and spec["layer"] == "words-front" and stage.overlaps(box, fbox):
            out.append(("FAIL", "face", f"{kind} covers the face ({_fmt(box)} vs face {_fmt(fbox)})"))
    return out


def _fmt(box):
    return "[" + ", ".join(f"{v:.0f}" for v in box) + "]"


def summary(edl, face=None):
    """Numbers for the report: twin share, beats, hero count."""
    dur = edl["duration"]
    twin = sum(b["end"] - b["start"] for b in edl["beats"] if b.get("twin", "off") != "off")
    return {"twin_share": round(twin / dur, 3), "beats": len(edl["beats"]),
            "heroes": sum(1 for b in edl["beats"] if b.get("hero"))}
