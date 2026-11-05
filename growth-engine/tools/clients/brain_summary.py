"""The brain block of the snapshot, from clients/<slug>/brain.json: offer, avatars, awareness, voice, package and the
decisions still open. Only what the dashboard shows; the brain itself stays the source."""
import json
from pathlib import Path

from .paths import client_dir


def load(root: Path, slug: str) -> dict:
    p = client_dir(root, slug) / "brain.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.is_file() else {}


def open_decisions(brain: dict) -> list[dict]:
    """Decisions with no `decided` answer yet: id and question (and the interim rule or recommendation, if any)."""
    out = []
    for d in brain.get("decisions_open") or []:
        if d.get("decided"):
            continue
        e = {"id": d.get("id"), "question": d.get("question")}
        hint = d.get("interim") or d.get("recommendation")
        if hint:
            e["interim"] = hint
        out.append(e)
    return out


def summary(brain: dict) -> dict:
    offer, voice, pkg = brain.get("offer") or {}, brain.get("voice") or {}, brain.get("package") or {}
    aw = brain.get("awareness") or {}
    return {
        "account": brain.get("account"),
        "offer": {k: offer.get(k) for k in ("main_offer", "next_step", "keyword", "delivers")},
        "avatars": [{k: a.get(k) for k in ("id", "name", "role")} for a in brain.get("avatars") or []],
        "awareness": {"stage": aw.get("stage"), "sophistication": aw.get("sophistication")},
        "voice": {"adjectives": voice.get("adjectives") or [], "banned": voice.get("banned") or []},
        "package": {k: pkg.get(k) for k in ("posts_per_week", "videos_per_month", "carousels_per_month", "platforms",
                                            "account_stage", "monthly_usd_cap", "schedule")},
        "decisions_open": open_decisions(brain),
        "updated": brain.get("updated"),
    }
