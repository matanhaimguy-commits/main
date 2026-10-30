"""Builds one blind G-HOOK grading folder: packet-v2 (rubric, instructions) plus the hook stack(s) and the 2 anchors,
shuffled under neutral labels, and the key that maps a grader's labels back. Graders never see the key.
Tests: test_hook_packet.py."""
from __future__ import annotations

import json
import random
import shutil
from pathlib import Path

from hook_anchors import PACKET, load

PACKET_DIR = Path(__file__).resolve().parents[1] / "production" / "hook-calibration" / PACKET
ADDENDUM = ("\n\nVISUAL: a stack with a FRAME line has a real concept frame; open that image and grade it (frame 1 as a phone "
            "viewer sees it). A stack whose frame is not made yet gets \"n/a\". Return \"visual\" next to \"text\" and "
            "\"spoken\" for every stack.\n")


def _block(label: str, s: dict, root: Path) -> str:
    frame = f"FRAME: {(root / s['frame']).resolve()}" if s.get("frame") else "VISUAL: frame not made yet"
    return f'## {label}\n- TARGET BUYER: {s["buyer"]}\n- {frame}\n- TEXT: "{s["text"]}"\n- SPOKEN: "{s["spoken"]}"\n'


def build(folder, hooks: list[dict], seed: int | None = None, root=".") -> dict:
    """Write folder/{instructions.md, rubric.md, stacks.md}; return the key {label: stack id} (keep it out of the folder).
    hooks: {"id", "buyer", "text", "spoken", "frame": path or None}. The anchors are added here, always."""
    folder, root = Path(folder), Path(root)
    folder.mkdir(parents=True, exist_ok=True)
    stacks = [dict(h) for h in hooks] + load()
    random.Random(seed).shuffle(stacks)
    key = {f"S{i:02d}": s["id"] for i, s in enumerate(stacks, 1)}
    shutil.copy(PACKET_DIR / "rubric.md", folder / "rubric.md")
    (folder / "instructions.md").write_text((PACKET_DIR / "instructions.md").read_text() + ADDENDUM)
    body = "\n".join(_block(label, s, root) for label, s in zip(key, stacks))
    (folder / "stacks.md").write_text("# Stacks to grade\n\n" + body)
    return key


def to_run(key: dict, hook_id: str, reads: list[dict]) -> dict:
    """The graders' JSON outputs ({"stacks": [{"id": label, ...}]}) as a hook_rule run for one hook."""
    graders = []
    for out in reads:
        by_id = {key[s["id"]]: s for s in out["stacks"] if s["id"] in key}
        pick = lambda sid: {k: by_id.get(sid, {}).get(k) for k in ("visual", "text", "spoken", "gates_failed")}  # noqa: E731
        graders.append({"hook": pick(hook_id),
                        "anchors": {a["id"]: pick(a["id"]) for a in load()}})
    return {"packet": PACKET, "graders": graders}


def key_text(key: dict) -> str:
    return json.dumps(key, indent=1)
