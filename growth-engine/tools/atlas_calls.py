"""Atlas calls inside the generation gate: the ledger lookups atlas_rules.py needs (Shot Specs, the slice's measured
length, the file an analysis call reads). Each function takes the pipeline module as P, so this file never imports
it. Tests: growth-engine/tools/test_atlas_gate.py (OmniAndStt)."""
from __future__ import annotations

import yaml

import atlas_rules
import call_aspect


def asset_specs(P, a: dict, led: dict) -> list[dict]:
    out = []
    for s in a["shots"]:
        sp = P.spec_path(led["slug"], led["post_id"], s)
        out.append((yaml.safe_load(sp.read_text()) or {}) if sp.exists() else {"shot_id": s})
    return out


def audio_seconds(P, led: dict, value: str):
    """The measured length on the G-AUDIO PASS of the audio asset registered with this id (None when not recorded)."""
    _, ra = P.find_by_id(led["slug"], value)
    rec = P.latest(ra["gates"].get("G-AUDIO")) if ra else None
    return (rec.get("data") or {}).get("seconds") if rec and rec["status"] in P.OK_STATES else None


def checks(P, req: dict, a: dict, led: dict) -> list[str]:
    """The owner's entry applied to a generation, plus the Shot Spec aspect unless the frame follows the image."""
    why = atlas_rules.entry_checks(req, a, asset_specs(P, a, led), lambda v: audio_seconds(P, led, v))
    if req["kind"] in ("image", "video") and not req["atlas"].get("aspect_from"):
        why += call_aspect.spec_mismatch(P, a, led, req["params"], req["atlas"].get("size_for_aspect"))
    return why


def find_media(P, value: str):
    """The run and asset any client's ledger registered with this id or URL."""
    for led in P.all_ledgers():
        for a in led["assets"]:
            if value in a.get("ids", []):
                return led, a
    return None, None


def analysis(P, req: dict, e: dict):
    """An analysis call (word timings) makes nothing: no prompt, budget or review; it reads one of our registered files.
    The record goes to that file's run, marked analysis, so it never counts as a generation of the file."""
    req["analysis"] = True
    found = {m["value"]: find_media(P, m["value"]) for m in req.get("medias") or []}
    why = atlas_rules.analysis_checks(req, e, lambda v: (found.get(v) or (None, None))[1] and found[v][1]["type"])
    led, a = next(iter(found.values()), (None, None))
    return (not why), why, led, a
