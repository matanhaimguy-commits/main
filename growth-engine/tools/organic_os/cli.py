"""Organic Growth OS: the checks and numbers behind growth-engine (see growth-engine/ORGANIC-OS.md).

  organic.py brain-check <slug> [--write]          Client Brain: schema, blocking fields, gaps report (section 4)
  organic.py card-check <slug> <card|dir> ...      Post Cards against the brain and the content map (7.1, 7.2, 7.5)
  organic.py week-check <slug> <dir|cards> ...     weekly rules: format and job rotation, mix, B7, contrarian, CTAs (6.2, 6.6)
  organic.py route <slug> <card> [--prev-family F] format router within the monthly budget (7.7)
  organic.py ledger <slug> [--month YYYY-MM]       Atlas USD and minutes spent vs the monthly USD cap (7.7)
  organic.py ledger-add <slug> --post ID --format F --usd N [--minutes N] [--note TEXT]   (--credits, --el: history)
  organic.py outliers <dataset.json> [--days 90] [--out file.csv]   the 4 outlier checks per account (5.1)
  organic.py hooks <slug> <hooks.json> [--library F] [--phrases F]   hook stacks: proven format, buyers' words, plain English
  organic.py yt-import <@handle> <page.json...> --out items.json   YouTube Shorts pages -> outlier items
  organic.py score <slug> [--write]                scorecard: job metric vs median, candidate/template, diagnosis (9)

Exit code 1 when a blocking check fails, so the daily run can stop on it.
"""
from __future__ import annotations

import argparse
import datetime as dt
import sys

from . import cmd_brain, cmd_cards, cmd_hooks, cmd_ledger, cmd_outliers, cmd_score, cmd_yt
from .files import MissingFile

COMMANDS = {
    "brain-check": cmd_brain.run,
    "card-check": cmd_cards.card_check_cmd,
    "week-check": cmd_cards.week_check_cmd,
    "route": cmd_cards.route_cmd,
    "ledger": cmd_ledger.ledger_cmd,
    "ledger-add": cmd_ledger.ledger_add_cmd,
    "outliers": cmd_outliers.run,
    "hooks": cmd_hooks.run,
    "score": cmd_score.run,
    "yt-import": cmd_yt.run,
}


def parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("brain-check"); b.add_argument("slug"); b.add_argument("--write", action="store_true")
    c = sub.add_parser("card-check"); c.add_argument("slug"); c.add_argument("paths", nargs="+")
    w = sub.add_parser("week-check"); w.add_argument("slug"); w.add_argument("paths", nargs="+")
    r = sub.add_parser("route"); r.add_argument("slug"); r.add_argument("card"); r.add_argument("--prev-family")
    l = sub.add_parser("ledger"); l.add_argument("slug"); l.add_argument("--month")
    la = sub.add_parser("ledger-add"); la.add_argument("slug"); la.add_argument("--post", required=True); la.add_argument("--format", required=True)
    la.add_argument("--usd", type=float, required=True); la.add_argument("--minutes", type=float, default=0)
    la.add_argument("--credits", type=float, default=0); la.add_argument("--el", type=float, default=0)
    la.add_argument("--note", default=""); la.add_argument("--date", default=dt.date.today().isoformat())
    o = sub.add_parser("outliers"); o.add_argument("dataset"); o.add_argument("--days", type=int, default=90); o.add_argument("--out")
    h = sub.add_parser("hooks"); h.add_argument("slug"); h.add_argument("hooks"); h.add_argument("--library"); h.add_argument("--phrases")
    y = sub.add_parser("yt-import"); y.add_argument("handle"); y.add_argument("pages", nargs="+"); y.add_argument("--out", required=True)
    s = sub.add_parser("score"); s.add_argument("slug"); s.add_argument("--write", action="store_true")
    return ap


def main(argv=None) -> int:
    a = parser().parse_args(argv)
    try:
        return COMMANDS[a.cmd](a)
    except MissingFile as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
