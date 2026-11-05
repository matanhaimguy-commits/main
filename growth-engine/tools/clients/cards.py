"""A brand's Post Cards: every clients/<slug>/cards/**/*.yaml, with its path and whether it sits in the bank."""
from pathlib import Path

import yaml

from .paths import client_dir, rel


def load(root: Path, slug: str) -> list[dict]:
    """[{path, bank, card}] sorted by slot then post_id; a file that is not a card (no post_id) is skipped."""
    base = client_dir(root, slug) / "cards"
    out = []
    for f in sorted(base.rglob("*.yaml")) if base.is_dir() else []:
        card = yaml.safe_load(f.read_text(encoding="utf-8"))
        if isinstance(card, dict) and card.get("post_id"):
            out.append({"path": rel(root, f), "bank": "bank" in f.relative_to(base).parts[:-1], "card": card})
    return sorted(out, key=lambda c: (str(c["card"].get("slot") or ""), c["card"]["post_id"]))
