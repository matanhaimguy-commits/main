"""The spend block: a month's Atlas USD from clients/<slug>/ledger.csv against the brand's monthly cap."""
import csv
from pathlib import Path

from organic_os import router

from .paths import client_dir


def rows(root: Path, slug: str) -> list[dict]:
    p = client_dir(root, slug) / "ledger.csv"
    if not p.is_file():
        return []
    with p.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def month(root: Path, slug: str, ym: str, cap) -> dict:
    all_rows = rows(root, slug)
    got = router.month_spend(all_rows, ym)
    return {"month": ym, "usd": got["usd"], "cap_usd": cap, "left_usd": None if cap is None else round(cap - got["usd"], 2),
            "minutes": got["minutes"], "pieces": sum(d["pieces"] for d in got["by_format"].values()),
            "by_format": {k: {"pieces": d["pieces"], "usd": round(d["usd"], 2)} for k, d in got["by_format"].items()},
            "has_ledger": bool(all_rows)}
