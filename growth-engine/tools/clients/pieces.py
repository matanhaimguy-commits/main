"""The sync's pieces: one per Post Card, joined with its run, its project and its spend."""
from pathlib import Path

from organic_os.config import CONFIG
from organic_os.funnel import stage_of

from . import body, project, runs, spend
from .cards import load as load_cards
from .slot import slot


def family_of(fmt: str | None) -> str | None:
    return (CONFIG["formats"].get(fmt or "") or {}).get("family")


def piece(root: Path, slug: str, tz: str, entry: dict, spent: dict[str, float]) -> dict:
    card = entry["card"]
    found = runs.find(root, slug, entry)
    run = runs.facts(root, found) if found else None
    return body.piece_block(entry, slot(card.get("slot"), tz)["at"], stage_of(card), family_of(card.get("format")),
                            run, project.facts(root, card), spent.get(card["post_id"]))


def build(root: Path, slug: str, tz: str) -> list[dict]:
    spent = spend.by_post(spend.rows(root, slug))
    return [piece(root, slug, tz, e, spent) for e in load_cards(root, slug)]
