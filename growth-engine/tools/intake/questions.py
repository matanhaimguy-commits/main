"""The intake question set (growth-engine/onboarding/intake-questions.json)."""
import json
from pathlib import Path

QUESTIONS_FILE = Path(__file__).resolve().parents[2] / "onboarding" / "intake-questions.json"


def load(path: Path | None = None) -> list[dict]:
    return json.loads(Path(path or QUESTIONS_FILE).read_text(encoding="utf-8"))["questions"]
