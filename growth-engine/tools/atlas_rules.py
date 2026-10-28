"""The owner's Atlas entries (standards.json models.atlas.allowed) and how the gate applies them to one call.

Pure functions: pipeline.py loads the ledger, the Shot Specs and the audio lengths and passes them in.
Tests: growth-engine/tools/test_atlas_rules.py. Entry keys: growth-engine/tools/atlas/README.md.
"""
from __future__ import annotations

import json

SRC = "standards.json models.atlas.allowed"
ENTRY_KEYS = {"id", "kind", "use", "params", "params_one_of", "params_if_given", "min_s", "max_s", "text_fields",
              "note", "duration_from", "aspect_from", "size_for_aspect", "prop_subjects_only", "analysis", "reads"}
SHAPE = "each entry is an object {id, kind, use, params, params_one_of, params_if_given, min_s, max_s, text_fields}"


def entry_problem(e) -> str | None:
    """Why the gate can't read an entry (None: it can). One unreadable entry blocks every Atlas call."""
    if not isinstance(e, dict) or not isinstance(e.get("id"), str) or set(e) - ENTRY_KEYS:
        return SHAPE
    if e.get("kind") not in ("image", "video", "audio"):
        return "kind is image, video or audio (no asset type makes 3D)"
    for k in ("params", "params_one_of", "params_if_given"):
        if not isinstance(e.get(k, {}), dict):
            return f"{k} is an object"
    if any(not isinstance(v, list) for k in ("params_one_of", "params_if_given") for v in (e.get(k) or {}).values()):
        return "params_one_of and params_if_given map each key to a list of values"
    for k in ("use", "text_fields", "reads"):
        if not isinstance(e.get(k, []), list) or not all(isinstance(x, str) for x in e.get(k, [])):
            return f"{k} is a list of names"
    for k in ("min_s", "max_s"):
        if k in e and (isinstance(e[k], bool) or not isinstance(e[k], (int, float))):
            return f"{k} is a number of seconds"
    for k in ("prop_subjects_only", "analysis"):
        if k in e and not isinstance(e[k], bool):
            return f"{k} is true or false"
    if e.get("duration_from", "audio") != "audio":
        return "duration_from is \"audio\" (the length is the audio reference's)"
    sfa = e.get("size_for_aspect", {})
    if not isinstance(sfa, dict) or any(not isinstance(v, list) or not all(isinstance(x, str) for x in v)
                                        for v in sfa.values()):
        return "size_for_aspect maps a Shot Spec aspect (\"4:5\") to the sizes that make it ([\"1024x1536\"])"
    if sfa and e.get("aspect_from"):
        return "size_for_aspect and aspect_from don't mix (the frame follows the image)"
    if e.get("aspect_from", "image") != "image":
        return "aspect_from is \"image\" (the frame follows the image reference)"
    if e["kind"] == "video" and not ("min_s" in e and "max_s" in e):
        return "a video entry sets min_s and max_s (the clip length rules)"
    if e.get("duration_from") and not ("min_s" in e and "max_s" in e):
        return "duration_from needs min_s and max_s (bounds on the audio's measured length)"
    if e.get("analysis"):
        if e["kind"] != "audio" or not e.get("reads") or e.get("text_fields") or e.get("use"):
            return "an analysis entry is kind audio, lists the asset types it reads in reads, and has no use or text_fields"
    elif "reads" in e:
        return "reads is for analysis entries"
    return None


def find_entry(allowed: list, model, kind: str) -> tuple[dict | None, list[str]]:
    """The owner's entry for an Atlas model. Only that list opens Atlas; G-EXCEPTION does not (STANDARDS.md 1)."""
    for e in allowed:
        bad = entry_problem(e)
        if bad:
            return None, [f"growth-engine/production/{SRC} has an entry the gate can't read "
                          f"({json.dumps(e)[:120]}): {bad} (growth-engine/tools/atlas/README.md)"]
    if kind == "3d":
        return None, ["Atlas 3d calls are blocked: no asset type in standards.json makes 3D"]
    named = [e["id"] for e in allowed]
    e = next((x for x in allowed if x["id"] == model), None)
    if e is None:
        return None, [f"Atlas model {model} is not on the owner's list: growth-engine/production/{SRC} "
                      f"({', '.join(named) if named else 'empty: no Atlas model is named yet'}). "
                      "Only the owner adds a model there, by its exact id (STANDARDS.md 1)"]
    if e["kind"] != kind:
        return None, [f"Atlas model {model} is named for {e['kind']} calls, not {kind}"]
    return e, []


def review_text(req: dict, e: dict) -> str:
    """The text the Prompt Reviewer reviews: the prompt, then each of the entry's text_fields the call sets, as a
    `[field]` line and its text, in the entry's order."""
    text = req.get("prompt") or ""
    for k in e.get("text_fields") or []:
        v = req["params"].get(k)
        if isinstance(v, str):
            text += f"\n\n[{k}]\n{v}"
    return text


REF_KINDS = ("image", "video", "audio")


def ref_object(v, refs=()) -> bool:
    """A reference given as an object, as H3 reference-to-video's refers takes it: {"url": a reference, "type":
    image|video|audio (optional)}. Its keys and type are structure, not text."""
    return isinstance(v, dict) and v.get("url") in refs and set(v) <= {"url", "type"} \
        and v.get("type", "image") in REF_KINDS


def strings(v, refs=()):
    if isinstance(v, str):
        yield v
    elif isinstance(v, (list, tuple)):
        for x in v:
            yield from strings(x, refs)
    elif ref_object(v, refs):
        yield v["url"]
    elif isinstance(v, dict):
        for k, x in v.items():
            yield str(k)
            yield from strings(x, refs)


def param_checks(req: dict, e: dict) -> list[str]:
    """params, params_one_of, params_if_given, text fields, and no parameter carrying text the entry does not list."""
    model, p, why = req.get("model"), req["params"], []
    for k, v in (e.get("params") or {}).items():
        if p.get(k) != v:
            why.append(f"{model}: pass {k}: {v!r} ({SRC})")
    for k, opts in (e.get("params_one_of") or {}).items():
        if p.get(k) not in opts:
            why.append(f"{model}: pass {k} as one of {opts} ({SRC}), not {p.get(k)!r}")
    for k, opts in (e.get("params_if_given") or {}).items():
        if k in p and p[k] not in opts:
            why.append(f"{model}: {k} must be one of {opts} ({SRC})")
    texts = e.get("text_fields") or []
    for k in texts:
        if k in p and not isinstance(p[k], str):
            why.append(f"{model}: {k} is a text field: pass it as text, reviewed with the prompt")
    listed = set(e.get("params") or {}) | set(e.get("params_one_of") or {}) | set(e.get("params_if_given") or {}) \
        | set(texts)
    refs = {m["value"] for m in req.get("medias") or []}
    for k, v in p.items():
        loose = [s for s in strings(v, refs) if s not in refs]
        if k not in listed and loose:
            why.append(f"{model}: {k} carries text no review covers ({loose[0][:40]!r}): drop it, or the owner lists {k} "
                       f"in the model's entry (params, params_one_of, params_if_given, or text_fields, which are reviewed "
                       f"with the prompt) ({SRC})")
    return why


def length_checks(req: dict, e: dict, audio_seconds) -> list[str]:
    """The call's duration within min_s to max_s, or, for duration_from audio, the audio reference's measured length.
    audio_seconds(value) -> seconds recorded on that audio's G-AUDIO PASS, or None."""
    model, p = req.get("model"), req["params"]
    lo, hi = e.get("min_s", 0), e.get("max_s", float("inf"))
    if e.get("duration_from") != "audio":
        d = p.get("duration")
        if isinstance(d, bool) or not isinstance(d, (int, float)) or not lo <= d <= hi:
            return [f"duration {d!r} outside {lo} to {hi} s ({SRC}; STANDARDS.md clip rules)"]
        return []
    if "duration" in p:
        return [f"{model} has no duration setting: its length is the audio's; drop duration ({SRC})"]
    audios = [m["value"] for m in req.get("medias") or [] if m["role"] == "audio"]
    if len(audios) != 1:
        return [f"{model} takes its length from exactly one audio reference ({len(audios)} in the call)"]
    s = audio_seconds(audios[0])
    if isinstance(s, bool) or not isinstance(s, (int, float)):
        return [f"the audio {audios[0]} has no measured length: record it on its G-AUDIO PASS "
                "(pipeline.py gate ... G-AUDIO --data '{\"seconds\": N}'); it sets the clip's length and price"]
    if not lo <= s <= hi:
        return [f"the audio is {s} s: {model} clips run {lo} to {hi} s ({SRC}; STANDARDS.md clip rules)"]
    return []


def subject_checks(e: dict, specs: list[dict]) -> list[str]:
    """prop_subjects_only: every Shot Spec the asset serves shows only props as subjects (a talking object, never a
    person or a character)."""
    if not e.get("prop_subjects_only"):
        return []
    if not specs:
        return [f"{e['id']} is for talking-object clips: the asset serves no Shot Spec to check ({SRC})"]
    why = []
    for sp in specs:
        ids = [s.get("id", "") for s in sp.get("subjects") or []]
        people = [i for i in ids if not i.startswith("PR-")]
        if not ids or people:
            why.append(f"{e['id']} is for talking-object clips only: shot {sp.get('shot_id')} has subjects "
                       f"{ids or 'none'} (every subject is a PR- prop) ({SRC})")
    return why


def entry_checks(req: dict, a: dict, specs: list[dict], audio_seconds) -> list[str]:
    """The owner's entry applied to a generation (not the Shot Spec aspect, which pipeline.py checks)."""
    e, why = req["atlas"], []
    if e.get("use") and a["type"] not in e["use"]:
        why.append(f"{req.get('model')} is named for {', '.join(e['use'])}, not a {a['type']} ({SRC})")
    why += param_checks(req, e)
    if "min_s" in e or "max_s" in e or e.get("duration_from"):
        why += length_checks(req, e, audio_seconds)
    return why + subject_checks(e, specs)


def analysis_checks(req: dict, e: dict, read_type) -> list[str]:
    """An analysis call (xai/stt-v1 word timings): no prompt, one reference that is a registered asset of a type the
    entry reads, and the entry's parameters. read_type(value) -> the asset type registered with that id, or None."""
    model, why = req.get("model"), []
    if (req.get("prompt") or "").strip():
        why.append(f"{model} reads audio and takes no prompt: drop it ({SRC})")
    medias = req.get("medias") or []
    if len(medias) != 1 or medias[0]["role"] != "audio":
        why.append(f"{model} reads exactly one reference, as --audio ({len(medias)} in the call)")
    for m in medias:
        t = read_type(m["value"])
        if t is None:
            why.append(f"{m['value']} is not registered on any asset (pipeline.py media ... --id URL): "
                       f"{model} only reads our own files")
        elif t not in e["reads"]:
            why.append(f"{model} reads {', '.join(e['reads'])}, not a {t} ({SRC})")
    return why + param_checks(req, e)
