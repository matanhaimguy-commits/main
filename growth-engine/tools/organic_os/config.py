"""Paths and the config files every check reads: organic.json, the card and brain schemas, standards.json."""
from __future__ import annotations

import json
from pathlib import Path

import yaml

GE = Path(__file__).resolve().parents[2]
ROOT = GE.parent
CONFIG = json.loads((GE / "config" / "organic.json").read_text())
CARD_SCHEMA = yaml.safe_load((GE / "schemas" / "post-card.schema.yaml").read_text())
BRAIN_SCHEMA = json.loads((GE / "schemas" / "brain.schema.json").read_text())
STANDARDS = json.loads((GE / "production" / "standards.json").read_text())
LENGTHS = STANDARDS["lengths"]  # STANDARDS.md section 8 is the single source for lengths
