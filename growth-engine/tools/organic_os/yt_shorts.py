"""YouTube Shorts listings (TranscriptAPI list_channel_videos, tab=shorts) -> rows the outlier checks read.

Organic proof without Apify: the same creators post their reels as Shorts, and a Shorts page carries the view count.
"""
from __future__ import annotations

import re

MULT = {"": 1, "K": 1_000, "M": 1_000_000, "B": 1_000_000_000}


def parse_views(text: str | None) -> int | None:
    """'36K views' -> 36000, '1.2M views' -> 1200000, 'No views' or hidden -> None."""
    m = re.match(r"\s*([\d.,]+)\s*([KMB]?)", text or "", re.I)
    if not m:
        return None
    return int(float(m.group(1).replace(",", "")) * MULT[m.group(2).upper()])


def to_items(pages: list[dict], handle: str) -> list[dict]:
    """Each page is one list_channel_videos response ({'results': [...]} or {'content': {'results': [...]}})."""
    out = []
    for page in pages:
        for v in (page.get("content") or page).get("results", []):
            views = parse_views(v.get("viewCountText"))
            if views is None or v.get("members_only"):
                continue
            out.append({"ownerUsername": handle.lstrip("@"), "url": f"https://www.youtube.com/shorts/{v['videoId']}",
                        "type": "Video", "videoViewCount": views, "caption": v.get("title", ""), "platform": "youtube"})
    return out
