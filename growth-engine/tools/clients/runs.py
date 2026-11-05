"""A card's production run (clients/<x>/runs/<id>/ledger.json) and what the dashboard shows of it: steps done,
the current step, the latest record of each gate and the checkpoints waiting on the owner."""
import json
import re
from pathlib import Path

from studio.gates import gate_entry
from studio.summary import pending_queue

from .paths import client_dir, rel

RUN_REF = re.compile(r"clients/[\w.-]+/runs/[\w.-]+")


def _ledger(d: Path) -> Path | None:
    p = d / "ledger.json"
    return p if p.is_file() else None


def by_card_path(root: Path, card_path: str) -> Path | None:
    """A run whose ledger names this card."""
    for p in sorted(Path(root).glob("clients/*/runs/*/ledger.json")):
        try:
            if json.loads(p.read_text(encoding="utf-8")).get("card") == card_path:
                return p
        except (OSError, ValueError):
            continue
    return None


def by_project(root: Path, project: str | None) -> Path | None:
    """The first run the project's PROJECT.md names (`clients/<slug>/runs/<id>`)."""
    doc = Path(root) / project / "PROJECT.md" if project else None
    if not doc or not doc.is_file():
        return None
    for m in RUN_REF.finditer(doc.read_text(encoding="utf-8")):
        found = _ledger(Path(root) / m.group(0))
        if found:
            return found
    return None


def find(root: Path, slug: str, entry: dict) -> Path | None:
    """The card's run ledger: its `run` field, then clients/<slug>/runs/<post_id>, then a ledger naming the card,
    then the run its project names. None when the piece has no run yet."""
    card = entry["card"]
    if card.get("run"):
        found = _ledger(Path(root) / card["run"].rstrip("/"))
        if found:
            return found
    return (_ledger(client_dir(root, slug) / "runs" / card["post_id"]) or by_card_path(root, entry["path"])
            or by_project(root, card.get("project")))


def latest_gates(led: dict) -> list[dict]:
    """The last record of each run gate, as the Studio page shows a gate."""
    return [gate_entry(g, recs[-1]) for g, recs in led.get("run_gates", {}).items() if recs]


def facts(root: Path, ledger_path: Path) -> dict:
    led = json.loads(ledger_path.read_text(encoding="utf-8"))
    steps = sorted(((int(n), s.get("status")) for n, s in led.get("steps", {}).items()), key=lambda x: x[0])
    live = [(n, st) for n, st in steps if st != "na"]
    cur = next((n for n, st in live if st != "done"), None)
    return {"run": rel(root, ledger_path.parent), "post_id": led.get("post_id"), "slug": led.get("slug"),
            "format": led.get("format"), "family": led.get("family"),
            "steps_done": sum(st == "done" for _, st in live), "steps_total": len(live), "current_step": cur,
            "waiting_on_owner": sorted({q["checkpoint"] for q in pending_queue(led)}), "gates": latest_gates(led)}
