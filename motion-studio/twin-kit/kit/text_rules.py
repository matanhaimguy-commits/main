"""Text-layer rules that look at more than one layer at once (round 2 of the kit review).

- Text layers in one beat never overlap (hero, UI scene, captions), unless an EDL item sets "overlap_ok": true.
- A word behind the head keeps its letters at least HEAD_CLEAR px above the head: the head may cover only the space
  behind or between words, never a letter.
- UI scenes keep their smallest text at the floor and their box inside the safe zone.
Each function returns (level, rule, message) findings.
"""
from . import stage, zones

TEXT_HEROES = ("behind-word", "two-tone", "orbit", "end-card", "pop3d")


def scene_findings(scene):
    kind, v = scene["move"], scene.get("vars", {})
    out = []
    box = zones.move_box(kind, v)
    out += [("FAIL", "safe-zone", f"{kind}: {why}") for why in (zones.breaches(box) if box else [])]
    out += [("FAIL", "size", f"{name} {px:.0f} px (min {zones.MIN_TEXT})")
            for name, px in zones.text_sizes(kind, v) if px < zones.MIN_TEXT]
    return out


def head_clear_findings(edl, beat, v, face):
    """The behind-word's letters must clear the head top by HEAD_CLEAR px wherever they share its width."""
    head = stage.head_on_frame(edl, beat.get("twin", "off"), face)
    box = zones.move_box("behind-word", v)
    if not head or not box or box[2] <= head[0] or box[0] >= head[2]:
        return []
    bottom = zones.letters_bottom(v)
    if bottom > head[1] - zones.HEAD_CLEAR:
        return [("FAIL", "head", f"behind-word letters reach {bottom:.0f} px, the head starts at {head[1]:.0f} px "
                                 f"(keep {zones.HEAD_CLEAR} px clear)")]
    return []


def text_layers(edl, beat, hero_v, cap_box):
    """(name, box, overlap_ok) for every text layer on screen in this beat."""
    out = []
    hero, scene = beat.get("hero"), beat.get("scene")
    if hero and hero["move"] in TEXT_HEROES:
        if hero["move"] == "orbit":
            out += [(f"orbit lane {i}", b, hero.get("overlap_ok", False))
                    for i, b in enumerate(zones.orbit_lanes(hero_v))]
        elif hero["move"] != "pop3d" or hero_v.get("label"):
            box = zones.move_box(hero["move"], hero_v)
            if box:
                out.append((hero["move"], box, hero.get("overlap_ok", False)))
    if scene:
        box = zones.move_box(scene["move"], scene.get("vars", {}))
        if box:
            out.append((scene["move"], box, scene.get("overlap_ok", False)))
    if cap_box and not beat.get("no_captions"):
        out.append(("captions", cap_box, False))
    return out


def overlap_findings(layers):
    out = []
    for i, (na, a, oka) in enumerate(layers):
        for nb, b, okb in layers[i + 1:]:
            if not (oka or okb) and stage.overlaps(a, b):
                out.append(("FAIL", "overlap", f"{na} and {nb} overlap"))
    return out
