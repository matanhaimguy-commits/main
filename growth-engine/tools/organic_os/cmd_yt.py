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
    counts = json.loads(Path(a.counts).read_text()) if a.counts else None
    items = to_items(pages, a.handle, counts)
    Path(a.out).write_text(json.dumps(items, indent=1))
    n = sum(1 for i in items if i.get("views_only"))
    print(f"wrote {len(items)} shorts for {a.handle} to {a.out}" + (f" ({n} views-only: no comment counts, so the outlier check skips them)" if n else ""))
    return 0 if items else 1
