"""organic.py outliers <dataset.json> [--days 90] [--out file.csv]"""
from __future__ import annotations

import csv
import json
from pathlib import Path

from .research import outliers

COLUMNS = ["account", "url", "type", "timestamp", "basis", "views", "likes", "likes_hidden", "comments", "x_median",
           "comments_per_1k", "account_comments_per_1k", "engagement", "views_3x", "comments_above_rate",
           "likes_in_proportion", "engagement_2pct", "trusted", "partial_outlier"]


def run(a) -> int:
    items = json.loads(Path(a.dataset).read_text())
    rows = outliers(items, a.days)
    if a.out:
        with open(a.out, "w", newline="") as f:
            wr = csv.DictWriter(f, fieldnames=COLUMNS, extrasaction="ignore")
            wr.writeheader()
            wr.writerows(rows)
        print(f"wrote {a.out}")
    trusted = [r for r in rows if r.get("trusted")]
    print(f"{len(rows)} posts, {len(trusted)} trusted outliers (all 4 checks)")
    for r_ in trusted[:15]:
        print(f"  {r_['x_median']}x  @{r_['account']}  {r_['url']}")
    by_hand = [r for r in rows if r.get("likes_hidden") and r.get("partial_outlier")]
    if by_hand:
        print(f"{len(by_hand)} more pass views and comments but hide their likes: check them by hand")
        for r_ in by_hand[:10]:
            print(f"  {r_['x_median']}x  @{r_['account']}  {r_['url']}")
    return 0
