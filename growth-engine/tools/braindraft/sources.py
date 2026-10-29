"""Every fact in the brain has a source or says what is missing. Checks the fields the drafter fills."""
import re

from brainio import paths
from brainio.unknown import is_placeholder

SCALAR = ["client", "account", "business_model.sells", "business_model.price_notes", "business_model.margin",
          "business_model.capacity", "business_model.sales_process", "offer.main_offer", "offer.next_step", "offer.keyword",
          "offer.delivers", "awareness.stage", "awareness.sophistication", "mechanism.ump", "mechanism.ums",
          "voice.adjectives", "voice.banned", "voice.language", "voice.register", "market.language", "market.country",
          "market.city", "constraints.cannot_say", "constraints.approver", "visual.face", "baseline.client_sources"]
PER_AVATAR = ["role", "situation", "words", "fears", "desires"]
# Optional paths: only checked when the brain holds a value for them.
OPTIONAL = {"business_model.price_notes", "business_model.margin", "offer.keyword", "offer.delivers", "voice.banned",
            "market.city", "constraints.approver", "visual.face", "baseline.client_sources"}
UNKNOWN_WITH_REASON = re.compile(r"^unknown\s*:\s*\S.{2,}", re.I)


def fields(brain: dict) -> list[str]:
    return SCALAR + [f"avatars[{i}].{k}" for i in range(len(brain.get("avatars") or [])) for k in PER_AVATAR]


def _says_what_is_missing(v) -> bool:
    if isinstance(v, list):
        return bool(v) and all(_says_what_is_missing(x) for x in v)
    return isinstance(v, str) and bool(UNKNOWN_WITH_REASON.match(v.strip()))


def problems(brain: dict) -> list[dict]:
    """[{path, problem}] for each drafted field with no source and no 'unknown: <what>'."""
    src, out = brain.get("field_sources") or {}, []
    for path in fields(brain):
        v = paths.get(brain, path)
        if is_placeholder(v):
            if v is None and path in OPTIONAL:
                continue
            if not _says_what_is_missing(v):
                out.append({"path": path, "problem": "empty: write 'unknown: <what is missing>' or give a source"})
        elif not str(src.get(path, "")).strip():
            out.append({"path": path, "problem": "filled but no source in field_sources"})
    for n, p in enumerate(brain.get("proof_bank") or []):
        if not str(p.get("source", "")).strip():
            out.append({"path": f"proof_bank[{n}]", "problem": "proof line with no source"})
    return out
