"""The hook a post opens with: the first spoken sentence from its transcript, else the caption's first line.

A row says which it is (`hook_source`: "transcript" or "caption"), because a caption line is text only, not what
was said on camera.
"""
from __future__ import annotations

import re

TRANSCRIPT_KEYS = ("transcript", "transcription", "transcriptText", "speech")
SENTENCE_END = re.compile(r"(?<=[.?!])\s+")


def _transcript(post: dict) -> str:
    for k in TRANSCRIPT_KEYS:
        v = post.get(k)
        if isinstance(v, list):  # segments: [{"text": ...}] or plain strings
            v = " ".join(s.get("text", "") if isinstance(s, dict) else str(s) for s in v)
        if isinstance(v, str) and v.strip():
            return " ".join(v.split())
    return ""


def first_sentence(text: str) -> str:
    text = " ".join(text.split())
    return SENTENCE_END.split(text, maxsplit=1)[0] if text else ""


def hook_of(post: dict) -> dict:
    spoken = _transcript(post)
    if spoken:
        return {"hook": first_sentence(spoken), "hook_source": "transcript"}
    lines = [ln.strip() for ln in (post.get("caption") or "").splitlines() if ln.strip()]
    return {"hook": lines[0] if lines else "", "hook_source": "caption" if lines else "none"}


def add_hooks(rows: list[dict], items: list[dict]) -> list[dict]:
    """Joins each outlier row (keyed by url or shortCode) to its post's opening line."""
    by_key = {}
    for it in items:
        for k in (it.get("url"), it.get("shortCode")):
            if k:
                by_key[k] = it
    for r in rows:
        r.update(hook_of(by_key.get(r.get("url"), {})))
    return rows
