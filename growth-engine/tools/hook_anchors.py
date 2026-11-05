"""The 2 proven winner hooks (anchors) that ride in every G-HOOK grading run. Tests: test_hook_rule.py."""
from __future__ import annotations

import json
from pathlib import Path

ANCHOR_FILE = Path(__file__).resolve().parents[1] / "production" / "hook-calibration" / "anchors.json"
PACKET = "packet-v2"
CHANNELS = ("visual", "text", "spoken")


def load(path: Path = ANCHOR_FILE) -> list[dict]:
    anchors = json.loads(Path(path).read_text())["anchors"]
    if len(anchors) != 2:
        raise ValueError("the hook rule uses exactly 2 anchors")
    return anchors


def anchor_ids(path: Path = ANCHOR_FILE) -> list[str]:
    return [a["id"] for a in load(path)]
