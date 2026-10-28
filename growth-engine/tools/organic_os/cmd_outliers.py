"""organic.py outliers <dataset.json|.jsonl> [--days 90, 0 = all] [--out file.csv]: the 4 checks plus each post's opening line."""
from __future__ import annotations

import csv
import json
from pathlib import Path

from .first_line import add_hooks
from .research import outliers

COLUMNS = ["account", "url", "type", "timestamp", "basis", "views", "likes", "likes_hidden", "comments", "x_median",
           "comments_per_1k", "account_comments_per_1k", "engagement", "views_3x", "comments_above_rate",
           "likes_in_proportion", "engagement_2pct", "trusted", "partial_outlier", "hook_source", "hook"]


def run(a) -> int:
    text = Path(a.dataset).read_text()
    items = [json.loads(ln) for ln in text.split("\n") if ln.strip()] if a.dataset.endswith(".jsonl") else json.loads(text)
    rows = add_hooks(outliers(items, a.days or None), items)
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
