"""hub.py client-sync <slug> [--dry-run] [--json] [--month YYYY-MM]

Builds the brand's sync body (registry.json + brain.json + content-map.json + Post Cards + runs + projects +
ledger.csv), checks it against the hub's contract (contract.py) and POSTs it to /api/clients/sync. --dry-run builds,
checks and reports without calling the hub; --json prints the whole body. --month picks the spend month (default:
this month, UTC)."""
import datetime as dt
import json
import sys
from pathlib import Path

from studio.cli import opt, positionals

from . import body, brain_summary, plan, registry, spend
from .contract import problems
from .counts import counts
from .paths import REPO
from .pieces import build as build_pieces

USAGE = "client-sync <slug> [--dry-run] [--json] [--month YYYY-MM]"


def build(slug: str, root: Path | None = None, month: str | None = None, registry_path: Path | None = None,
          now: dt.datetime | None = None) -> dict:
    root = Path(root or REPO)
    ym = month or (now or dt.datetime.now(dt.timezone.utc)).strftime("%Y-%m")
    entry = registry.brand(slug, registry_path)
    return body.snapshot(entry, brain_summary.summary(brain_summary.load(root, slug)), plan.summary(plan.load(root, slug)),
                         spend.month(root, slug, ym, entry["monthly_usd_cap"]), build_pieces(root, slug, entry["timezone"]))


def report(snap: dict, sent: dict | None) -> str:
    c, s, b = counts(snap["pieces"]), snap["snapshots"]["spend"], snap["brand"]
    fmt = lambda d: ", ".join(f"{k} {v}" for k, v in d.items()) or "none"
    cap = f" of ${s['cap_usd']:.2f}" if s["cap_usd"] is not None else " (no cap)"
    head = (f"sent: {sent.get('pieces')} live piece(s), snapshots added {sent.get('snapshots_added')}, "
            f"removed {sent.get('removed')}") if sent is not None else "dry run, nothing sent"
    return "\n".join([
        f"{b['slug']} -> hub business {b['business']} ({b['status']}): {head}",
        f"pieces: {c['pieces']} slotted + {c['unslotted']} unslotted (bank)",
        f"status: {fmt(c['status'])}",
        f"funnel: {fmt(c['funnel_stage'])}",
        f"spend {s['month']}: ${s['usd']:.2f}{cap}" + ("" if s["has_ledger"] else " (no ledger.csv yet)"),
        f"open decisions: {len(snap['snapshots']['brain'].get('decisions_open', []))}",
    ])


def cli(rest: list[str], *, call, upload=None, hub_url: str = "") -> None:
    (slug,) = positionals(rest, ["slug"], USAGE)
    snap = build(slug, month=opt(rest, "--month"))
    bad = problems(snap)
    if bad:
        sys.exit("BAD_SYNC_BODY:\n  " + "\n  ".join(bad))
    sent = None if "--dry-run" in rest else (call("POST", "sync", snap, api="clients") or {})
    print(report(snap, sent))
    if "--json" in rest:
        print(json.dumps(snap, ensure_ascii=False, indent=1))
