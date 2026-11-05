"""The spend ledger, the owner's monthly USD cap and the HeyGen credit cap (ORGANIC-OS 7.7). Budgets are Atlas USD, plus
HeyGen credits for the twin (D-T5); the ledger's Higgsfield and ElevenLabs credit columns stay readable for history."""
from __future__ import annotations

import csv

from .files import client_dir
from .issues import WARN, issue


def ledger_rows(slug: str) -> list[dict]:
    p = client_dir(slug) / "ledger.csv"
    if not p.exists():
        return []
    with p.open(newline="") as f:
        return list(csv.DictReader(f))


def month_spend(rows: list[dict], month: str) -> dict:
    sel = [r for r in rows if r["date"].startswith(month)]
    num = lambda r, k: float(r.get(k) or 0)
    by_fmt: dict[str, dict] = {}
    for r in sel:
        d = by_fmt.setdefault(r["format"], {"pieces": 0, "usd": 0.0, "credits": 0.0, "minutes": 0.0})
        d["pieces"] += 1
        d["usd"] += num(r, "atlas_usd")
        d["credits"] += num(r, "higgsfield_credits")
        d["minutes"] += num(r, "minutes")
    return {"month": month, "usd": round(sum(num(r, "atlas_usd") for r in sel), 2),
            "credits": sum(num(r, "higgsfield_credits") for r in sel),
            "elevenlabs": sum(num(r, "elevenlabs_credits") for r in sel),
            "heygen": sum(num(r, "heygen_credits") for r in sel),
            "minutes": sum(num(r, "minutes") for r in sel), "by_format": by_fmt}


def usd_cap(brain: dict) -> float | None:
    """The owner's monthly Atlas cap in USD (brain.json package.monthly_usd_cap); None when not set."""
    cap = (brain.get("package") or {}).get("monthly_usd_cap")
    return None if isinstance(cap, bool) or not isinstance(cap, (int, float)) else cap


def heygen_cap(brain: dict) -> float | None:
    """The owner's monthly HeyGen credit cap (brain.json package.monthly_heygen_credit_cap); None when not set."""
    cap = (brain.get("package") or {}).get("monthly_heygen_credit_cap")
    return None if isinstance(cap, bool) or not isinstance(cap, (int, float)) else cap


def route_issues(brain: dict) -> list[dict]:
    if usd_cap(brain) is None:
        return [issue(WARN, "budget", "no monthly_usd_cap set (Matan): formats are routed with no budget filter")]
    return []
