"""organic.py ledger | ledger-add: credits and minutes spent against the monthly cap (ORGANIC-OS 7.7)."""
from __future__ import annotations

import csv
import datetime as dt

from .config import CONFIG
from .files import client_dir, load_brain
from .router import ledger_rows, month_spend


def ledger_cmd(a) -> int:
    rows = ledger_rows(a.slug)
    month = a.month or dt.date.today().strftime("%Y-%m")
    sp = month_spend(rows, month)
    cap = load_brain(a.slug)["package"]["monthly_credit_cap"]
    print(f"{month}: {sp['credits']:.0f} / {cap} Higgsfield credits ({sp['credits'] / cap:.0%}), "
          f"{sp['elevenlabs']:.0f} ElevenLabs credits, {sp['minutes']:.0f} production minutes")
    for f_, v in sorted(sp["by_format"].items()):
        print(f"  {f_}: {v['pieces']} pieces, {v['credits']:.0f} credits, {v['minutes']:.0f} min")
    if sp["credits"] > cap / 1.25:
        print("  over 80% of the cap: keep the 25% retake buffer, move remaining slots to tier C")
    return 0


def ledger_add_cmd(a) -> int:
    p = client_dir(a.slug) / "ledger.csv"
    new = not p.exists()
    fmt = CONFIG["formats"].get(a.format)
    with p.open("a", newline="") as f:
        wr = csv.writer(f)
        if new:
            wr.writerow(["date", "post_id", "format", "tier", "higgsfield_credits", "elevenlabs_credits", "minutes", "note"])
        wr.writerow([a.date, a.post, a.format, fmt["tier"] if fmt else "", a.credits, a.el, a.minutes, a.note])
    print(f"logged {a.post} in clients/{a.slug}/ledger.csv")
    return 0
