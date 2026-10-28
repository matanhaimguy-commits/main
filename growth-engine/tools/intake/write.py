"""Writes clients/<slug>/intake/answers.json and files.json. Files are listed (name, url, type, size), not downloaded."""
import json
from pathlib import Path

from clients.paths import REPO, client_dir


def write(slug: str, got: dict, bad: list[dict], root: Path | None = None) -> list[Path]:
    out = client_dir(root or REPO, slug) / "intake"
    out.mkdir(parents=True, exist_ok=True)
    answers = {"slug": slug, "submitted_at": got["submitted_at"], "missing_required": [m["id"] for m in bad],
               "answers": got["answers"]}
    files = [{k: f.get(k) for k in ("name", "url", "type", "size")} for f in got.get("files") or []]
    paths = []
    for name, data in (("answers.json", answers), ("files.json", files)):
        p = out / name
        p.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        paths.append(p)
    return paths
