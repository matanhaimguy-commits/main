"""Reading a client's files: brain.json, the content map, the demand map and Post Cards."""
from __future__ import annotations

import csv
import json
from pathlib import Path

import yaml

from .config import ROOT


def client_dir(slug: str) -> Path:
    return ROOT / "clients" / slug


def load_brain(slug: str) -> dict:
    return json.loads((client_dir(slug) / "brain.json").read_text())


def load_map(slug: str) -> dict:
    return json.loads((client_dir(slug) / "content-map.json").read_text())


def load_demand(slug: str, brain: dict | None = None) -> list[dict]:
    rel = (brain or {}).get("demand_map_file") or "research/demand-map.csv"
    p = client_dir(slug) / rel
    if not p.exists():
        return []
    with p.open(newline="") as f:
        return [r for r in csv.DictReader(f)]


def load_cards(paths: list[str]) -> list[tuple[str, dict]]:
    out = []
    for p in paths:
        pp = Path(p)
        files = sorted(pp.glob("*.yaml")) if pp.is_dir() else [pp]
        for f in files:
            out.append((str(f), yaml.safe_load(f.read_text())))
    return out
