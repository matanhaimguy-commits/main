"""organic.py calendar <slug> [--month YYYY-MM] [--bank]: the month's posts from the cards, as a markdown table."""
from __future__ import annotations

import datetime as dt

from .files import MissingFile, client_dir, load_cards, load_map, need
from .month_table import markdown, rows


def default_month(slug: str) -> str:
    """The content map's month (its first 7 characters), else this month."""
    try:
        m = str(load_map(slug).get("month") or "")[:7]
    except MissingFile:
        m = ""
    return m if len(m) == 7 and m[4] == "-" else dt.date.today().strftime("%Y-%m")


def calendar_cmd(a) -> int:
    month = a.month or default_month(a.slug)
    base = need(client_dir(a.slug) / "cards", "write the month's Post Cards first (content-strategist)")
    cards = load_cards([str(p) for p in sorted({f.parent for f in base.rglob("*.yaml")})])
    table = rows(cards, month, a.bank)
    print(f"{a.slug} {month}: {len(table)} post(s)")
    print(markdown(table))
    return 0
