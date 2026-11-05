"""The month's calendar from a brand's Post Cards: one row per slotted card, in slot order (bank cards apart)."""
from __future__ import annotations

import datetime as dt

from .card_title import title_of
from .funnel import stage_of

COLUMNS = ("date", "time", "funnel", "job", "format", "status", "title", "project")


def rows(cards: list[tuple[str, dict]], month: str, bank: bool = False) -> list[dict]:
    """cards: (path, card). Cards in a bank/ folder are left out unless bank is set."""
    out = []
    for path, c in cards:
        slot = str(c.get("slot") or "")
        if not slot.startswith(month) or (not bank and "/bank/" in path.replace("\\", "/")):
            continue
        day = dt.datetime.strptime(slot, "%Y-%m-%d %H:%M")
        out.append({"date": day.strftime("%a %d %b"), "time": day.strftime("%H:%M"), "funnel": stage_of(c) or "",
                    "job": c.get("job", ""), "format": c.get("format", ""), "status": c.get("status", ""),
                    "title": title_of(c, 48), "project": (c.get("project") or "").rsplit("/", 1)[-1],
                    "_sort": (slot, c["post_id"])})
    out.sort(key=lambda r: r.pop("_sort"))
    return out


def markdown(rows_: list[dict]) -> str:
    head = "| " + " | ".join(COLUMNS) + " |\n|" + "---|" * len(COLUMNS)
    return "\n".join([head] + ["| " + " | ".join(str(r[k]).replace("|", "/") for k in COLUMNS) + " |" for r in rows_])
