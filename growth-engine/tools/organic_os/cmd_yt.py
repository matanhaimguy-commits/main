"""organic.py yt-import <@handle> <page.json> [page.json ...] --out items.json

Turns saved TranscriptAPI Shorts pages into the item list `organic.py outliers` reads (no likes or comments in a
listing: the outlier rows come out with basis "views"; fetch metadata only for the top outliers).
"""
from __future__ import annotations

import json
from pathlib import Path

from .yt_shorts import to_items


def run(a) -> int:
    pages = [json.loads(Path(p).read_text()) for p in a.pages]
    items = to_items(pages, a.handle)
    Path(a.out).write_text(json.dumps(items, indent=1))
    print(f"wrote {len(items)} shorts for {a.handle} to {a.out}")
    return 0 if items else 1
