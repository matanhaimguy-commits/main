"""organic.py score <slug> [--write]"""
from __future__ import annotations

import csv

from .config import ROOT
from .files import client_dir, need
from .learning import score


def run(a) -> int:
    p = need(client_dir(a.slug) / "analytics" / "posts.csv", "pull the post results first (analyst, ORGANIC-OS 9)")
    with p.open(newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        print("no scored posts yet")
        return 0
    res = score(rows)
    for s_ in res:
        print(f"{s_['post_id']}: {s_['metric']}={s_['value']} x{s_['x_median']} {s_['flag']} {s_['diagnosis']}".rstrip())
    if a.write:
        out = client_dir(a.slug) / "analytics" / "scored.csv"
        with out.open("w", newline="") as f:
            wr = csv.DictWriter(f, fieldnames=list(res[0].keys()))
            wr.writeheader()
            wr.writerows(res)
        print(f"wrote {out.relative_to(ROOT)}")
    return 0
