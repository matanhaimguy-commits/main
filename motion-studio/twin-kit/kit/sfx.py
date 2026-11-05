"""The sound on every move: cue times from the EDL, files from the Pixabay SFX kit bundled with media-use.

A cue is {"t": film seconds, "name": kit name, "file": path, "gain_db": level, "beat": id, "for": what made it}.
"""
from pathlib import Path

from .moves import MOVES, SCENES, CUTS

KIT = Path(__file__).resolve().parents[3] / ".claude/skills/media-use/audio/assets/sfx"

# levels under the voice; loud hits sit lower so no single effect jumps out of the mix
GAIN_DB = {"impact-bass-1": -9, "impact-bass-2": -9, "whoosh": -10, "whoosh-cinematic": -11, "whoosh-short": -9,
           "glitch-1": -16, "glitch-2": -18, "glitch-3": -14, "pop": -8, "click": -10, "click-soft": -8,
           "notification": -12, "ping": -12, "typing": -14, "key-press": -10, "chime": -14, "riser": -16}


def path(name):
    return KIT / f"{name}.mp3"


def exists(name):
    return path(name).is_file()


def cue(t, name, beat, what, override=None):
    name = override or name
    return {"t": round(max(0.0, t), 3), "name": name, "file": str(path(name)), "gain_db": GAIN_DB.get(name, -10),
            "beat": beat, "for": what}


def cues(edl):
    out = []
    for b in edl["beats"]:
        bid, start = b["id"], b["start"]
        if b.get("cut_in"):
            c = CUTS[b["cut_in"]]
            out.append(cue(start + c["sfx_at"], c["sfx"], bid, f"cut:{b['cut_in']}"))
        if b.get("scene"):
            s = b["scene"]
            spec = SCENES[s["move"]]
            at = start + float(s.get("vars", {}).get("at", 0))
            out.append(cue(at + spec["sfx_at"], spec["sfx"], bid, f"scene:{s['move']}", s.get("sfx")))
        if b.get("grade"):
            g = b["grade"]
            spec = MOVES[g["move"]]
            out.append(cue(start + float(g.get("vars", {}).get("at", 0)) + spec["sfx_at"], spec["sfx"], bid,
                           f"grade:{g['move']}", g.get("sfx")))
        if b.get("hero"):
            h = b["hero"]
            spec = MOVES[h["move"]]
            at = start + float(h.get("vars", {}).get("at", 0))
            out.append(cue(at + spec["sfx_at"], spec["sfx"], bid, f"hero:{h['move']}", h.get("sfx")))
    return sorted(out, key=lambda c: c["t"])
