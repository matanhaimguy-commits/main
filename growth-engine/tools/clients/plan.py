"""The plan block of the snapshot, from clients/<slug>/content-map.json: month, theme, mix, cadence, pillars, series,
calendar lines, keywords, rules and who approved it."""
import json
from pathlib import Path

from .paths import client_dir

KEEP = ("month", "theme", "belief_focus", "stage", "mix", "mix_planned", "formats_per_week", "cadence", "calendar",
        "keywords", "rules", "spend", "approved_by")


def load(root: Path, slug: str) -> dict:
    p = client_dir(root, slug) / "content-map.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.is_file() else {}


def summary(cmap: dict) -> dict:
    out = {k: cmap.get(k) for k in KEEP if k in cmap}
    out["pillars"] = [p.get("name") for p in cmap.get("pillars") or []]
    out["series"] = [{k: s.get(k) for k in ("name", "kind", "format", "job", "target_episodes", "status")}
                     for s in cmap.get("series") or []]
    return out
