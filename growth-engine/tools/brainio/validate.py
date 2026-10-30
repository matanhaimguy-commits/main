"""Schema check for a brain (growth-engine/schemas/brain.schema.json). Schema errors only; brain-check adds the rest."""
import json
from pathlib import Path

import jsonschema

SCHEMA = json.loads((Path(__file__).resolve().parents[2] / "schemas" / "brain.schema.json").read_text(encoding="utf-8"))


def errors(brain: dict) -> list[str]:
    return [f"{'/'.join(map(str, e.path)) or 'brain'}: {e.message}" for e in jsonschema.Draft202012Validator(SCHEMA).iter_errors(brain)]
