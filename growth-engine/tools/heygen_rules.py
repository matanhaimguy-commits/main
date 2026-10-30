"""The twin route's call checks (D-T4, Twin reel machine plan T1): pure functions over the HeyGen call, the brain's host
block and standards.json models.heygen. heygen_gate.py does the ledger lookups. Tests: test_heygen_rules.py."""
from __future__ import annotations


def host_problem(host) -> str | None:
    """The brain has a usable HeyGen twin."""
    if not isinstance(host, dict) or host.get("engine") != "heygen":
        return "the client's brain has no HeyGen host block (brain.json host, engine heygen): no twin to call"
    if not host.get("looks") or not host.get("voices"):
        return "the brain's host block has no looks or no voices"
    return None


def look_for(host: dict, look_id) -> dict | None:
    return next((x for x in host.get("looks") or [] if x.get("id") == look_id), None)


def voice_ids(host: dict) -> list[str]:
    return [v.get("id") for v in host.get("voices") or []]


def speech_checks(ti: dict, host: dict, rule: dict) -> list[str]:
    """create_speech: one of the twin's voices, plain text (the released script is checked by the caller)."""
    why = []
    if ti.get("voiceId") not in voice_ids(host):
        why.append(f"voiceId {ti.get('voiceId')!r} is not one of the twin's voices in the brain's host block "
                   f"({', '.join(voice_ids(host))})")
    if not isinstance(ti.get("text"), str) or not ti["text"].strip():
        why.append("no text: the speech is the released script, word for word")
    if (ti.get("inputType") or "text") not in rule["input_types"]:
        why.append(f"inputType {ti.get('inputType')!r}: only {rule['input_types']} (the text must match the script)")
    return why


def _set(v) -> bool:
    return v not in (None, "", [], {})


def video_checks(ti: dict, host: dict, rule: dict) -> tuple[list[str], str | None]:
    """create_video_from_avatar: one of the twin's looks, 9:16, cover for a landscape look, driven only by audio.
    Returns (why, the audio value the call names, or None)."""
    why = []
    look = look_for(host, ti.get("avatarId"))
    if not look:
        why.append(f"avatarId {ti.get('avatarId')!r} is not one of the twin's looks in the brain's host block "
                   f"({', '.join(x.get('id', '') for x in host.get('looks') or [])})")
    if ti.get("aspectRatio") != rule["aspect_ratio"]:
        why.append(f"aspectRatio {ti.get('aspectRatio')!r}: a reel is {rule['aspect_ratio']} (pass it; auto keeps a "
                   "landscape look landscape)")
    if look:
        fits = rule["fit_by_orientation"].get(look.get("orientation"), [None, "cover"])
        if ti.get("fit") not in fits:
            why.append(f"fit {ti.get('fit')!r} for the {look.get('orientation')} look {look.get('name')!r}: use "
                       f"{' or '.join('omit' if f is None else f for f in fits)} (a landscape twin in 9:16 is cover, "
                       "never contain)")
    ref = (ti.get("engine") or {}).get("reference_look_id") if isinstance(ti.get("engine"), dict) else None
    if _set(ref) and not look_for(host, ref):
        why.append(f"engine.reference_look_id {ref!r} is not one of the twin's looks")
    refused = [k for k in rule["refused_keys"] if _set(ti.get(k))]
    if refused:
        why.append(f"{', '.join(refused)} on the call: the video is driven only by the gated voice asset, with no "
                   "script text or other prompt")
    audio = [k for k in rule["audio_keys"] if _set(ti.get(k))]
    if len(audio) != 1:
        why.append(f"name exactly one audio source ({' or '.join(rule['audio_keys'])}): the twin's voice asset with "
                   f"{rule['audio_gate']} PASS")
    cap = ti.get("caption")
    if isinstance(cap, dict) and _set(cap.get("style")):
        why.append("caption.style burns captions in: captions are made in the edit")
    if (ti.get("outputFormat") or "mp4") not in rule["output_formats"]:
        why.append(f"outputFormat {ti.get('outputFormat')!r}: one of {rule['output_formats']}")
    value = ti.get(audio[0]) if len(audio) == 1 else None
    return why, value if isinstance(value, str) else None
