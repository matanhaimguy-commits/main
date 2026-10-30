"""Letter grades of the Hook Lab rubric as an order: A+ best, F worst. Tests: test_hook_rule.py."""
from __future__ import annotations

LADDER = ["F", "D-", "D", "D+", "C-", "C", "C+", "B-", "B", "B+", "A-", "A", "A+"]


def rank(grade) -> int | None:
    """Position on the ladder (higher is better); None for n/a or anything that is not a grade."""
    g = str(grade or "").strip().upper()
    return LADDER.index(g) if g in LADDER else None
