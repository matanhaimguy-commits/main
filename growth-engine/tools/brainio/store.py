"""Load and save clients/<slug>/brain.json. Saving is atomic and keeps the file's two-space layout."""
import json
import os
import sys
from pathlib import Path

from clients.paths import REPO, client_dir


def brain_path(slug: str, root: Path | None = None) -> Path:
    return client_dir(root or REPO, slug) / "brain.json"


def load(slug: str, root: Path | None = None) -> dict:
    p = brain_path(slug, root)
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        sys.exit(f"NO_BRAIN: {p}: {e}. Start from clients/_template (cp -r clients/_template clients/{slug}).")


def save(slug: str, brain: dict, root: Path | None = None) -> Path:
    p = brain_path(slug, root)
    tmp = p.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(brain, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(tmp, p)
    return p
