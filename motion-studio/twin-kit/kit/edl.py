"""Load and validate an edit list (EDL): the JSON that says which move plays on which beat.

Shape (times in seconds on the film clock):
  {"width":1080,"height":1920,"fps":30,"duration":10.8,
   "brand":{...}, "twin":{"src":..., "face":...}, "voice":{"src":...,"start":0.2,"words":...},
   "music":{"src":...,"gain_db":-20}, "captions":{"y":1380},
   "beats":[{"id":"b1","start":0,"end":2.3,"twin":"stage","hero":{"move":"behind-word","vars":{...}},
             "scene":{"move":"ui-notification","vars":{...}}, "cut_in":"whip"}]}
"""
import json
from pathlib import Path

from .moves import MOVES, CUTS, SCENES

TWIN_MODES = ("stage", "full", "off")


class EDLError(ValueError):
    pass


def load(path):
    path = Path(path)
    edl = json.loads(path.read_text())
    edl["_dir"] = str(path.parent.resolve())
    validate(edl)
    return edl


def resolve(edl, rel):
    """A path in the EDL, relative to the EDL's own folder."""
    p = Path(rel)
    return p if p.is_absolute() else Path(edl["_dir"]) / p


def validate(edl):
    for key in ("width", "height", "fps", "duration", "beats", "twin", "voice", "brand"):
        if key not in edl:
            raise EDLError(f"missing key: {key}")
    beats = edl["beats"]
    if not beats:
        raise EDLError("no beats")
    prev_end = 0.0
    seen = set()
    for b in beats:
        bid = b.get("id")
        if not bid or bid in seen:
            raise EDLError(f"beat id missing or repeated: {bid!r}")
        seen.add(bid)
        if not (0 <= b["start"] < b["end"] <= edl["duration"] + 1e-6):
            raise EDLError(f"{bid}: start/end out of range")
        if abs(b["start"] - prev_end) > 1e-6:
            raise EDLError(f"{bid}: starts at {b['start']}, previous beat ends at {prev_end} (beats must tile the film)")
        prev_end = b["end"]
        if b.get("twin", "off") not in TWIN_MODES:
            raise EDLError(f"{bid}: twin must be one of {TWIN_MODES}")
        hero = b.get("hero")
        if hero is not None and hero.get("move") not in MOVES:
            raise EDLError(f"{bid}: unknown hero move {hero.get('move')!r}")
        scene = b.get("scene")
        if scene is not None and scene.get("move") not in SCENES:
            raise EDLError(f"{bid}: unknown scene {scene.get('move')!r}")
        grade = b.get("grade")
        if grade is not None and grade.get("move") != "bw-grain":
            raise EDLError(f"{bid}: grade must be bw-grain")
        if b.get("cut_in") not in (None, *CUTS):
            raise EDLError(f"{bid}: unknown cut_in {b.get('cut_in')!r}")
    if abs(prev_end - edl["duration"]) > 1e-6:
        raise EDLError(f"beats end at {prev_end}, film is {edl['duration']} s")
    return True
