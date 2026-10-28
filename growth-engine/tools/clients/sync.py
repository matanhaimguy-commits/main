"""hub.py client-sync <slug> [--dry-run] [--json] [--month YYYY-MM]

Builds the brand's snapshot (registry.json + brain.json + content-map.json + Post Cards + runs + projects +
ledger.csv) and POSTs it to the hub's /api/clients/sync. --dry-run builds and reports it without calling the hub;
--json prints the whole body. --month picks the spend month (default: this month, UTC)."""
import datetime as dt
import json
from pathlib import Path

from studio.cli import opt, positionals

from . import body, brain_summary, plan, registry, spend
from .counts import counts
from .paths import REPO
from .pieces import build as build_pieces

USAGE = "client-sync <slug> [--dry-run] [--json] [--month YYYY-MM]"


def build(slug: str, root: Path | None = None, now: dt.datetime | None = None, month: str | None = None,
          registry_path: Path | None = None) -> dict:
    root = Path(root or REPO)
    now = now or dt.datetime.now(dt.timezone.utc)
    entry = registry.brand(slug, registry_path)
    pieces = build_pieces(root, slug, entry["timezone"])
    return body.snapshot(entry, now.replace(microsecond=0).isoformat(),
                         brain_summary.summary(brain_summary.load(root, slug)), plan.summary(plan.load(root, slug)),
                         pieces, spend.month(root, slug, month or now.strftime("%Y-%m"), entry["monthly_usd_cap"]),
                         counts(pieces))


def report(snap: dict, sent: bool) -> str:
    c, s, b = snap["counts"], snap["spend"], snap["brand"]
    fmt = lambda d: ", ".join(f"{k} {v}" for k, v in d.items()) or "none"
    cap = f" of ${s['cap_usd']:.2f}" if s["cap_usd"] is not None else " (no cap)"
    return "\n".join([
        f"{b['slug']} -> hub business {snap['business']} ({b['status']}): " + ("sent" if sent else "dry run, nothing sent"),
        f"pieces: {c['pieces']} slotted + {c['bank']} bank",
        f"status: {fmt(c['status'])}",
        f"funnel: {fmt(c['funnel_stage'])}",
        f"spend {s['month']}: ${s['usd']:.2f}{cap}" + ("" if s["has_ledger"] else " (no ledger.csv yet)"),
        f"open decisions: {len(snap['brain'].get('decisions_open', []))}",
    ])


def cli(rest: list[str], *, call, upload=None, hub_url: str = "") -> None:
    (slug,) = positionals(rest, ["slug"], USAGE)
    snap = build(slug, month=opt(rest, "--month"))
    dry = "--dry-run" in rest
    if not dry:
        call("POST", "sync", snap, api="clients")
    print(report(snap, sent=not dry))
    if "--json" in rest:
        print(json.dumps(snap, ensure_ascii=False, indent=1))
