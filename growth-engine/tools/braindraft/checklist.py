"""The drafter's internal checklist: for each of the 38 questions, what the brain holds now."""
import json
from pathlib import Path

from brainio import paths
from brainio.unknown import is_placeholder

from .targets import TARGETS

QUESTIONS = Path(__file__).resolve().parents[2] / "onboarding" / "intake-questions.json"


def state(brain: dict, target: str) -> str:
    if target.startswith("research/"):
        return "file"
    v = paths.get(brain, target)
    if is_placeholder(v):
        return "open"
    return "sourced" if (brain.get("field_sources") or {}).get(target) or target in ("proof_bank", "belief_ladder", "contrarian_vault") else "no source"


def build(brain: dict) -> list[dict]:
    qs = json.loads(QUESTIONS.read_text(encoding="utf-8"))["questions"]
    out = []
    for q in qs:
        targets, where = TARGETS[q["id"]]
        out.append({"id": q["id"], "question": q["label"], "targets": {t: state(brain, t) for t in targets}, "look_in": where})
    return out


def render(rows: list[dict]) -> str:
    lines = []
    for r in rows:
        t = ", ".join(f"{k} [{v}]" for k, v in r["targets"].items())
        lines.append(f"{r['id']:<3} {r['question'][:60]:<60} -> {t}  (look in: {', '.join(r['look_in'])})")
    return "\n".join(lines)
