"""organic.py ledger | ledger-add: Atlas USD and minutes spent against the monthly cap (ORGANIC-OS 7.7)."""
from __future__ import annotations

import datetime as dt

from .config import CONFIG
from .files import client_dir, load_brain
from .ledger_file import append_row
from .spend import ledger_rows, month_spend, usd_cap


def ledger_cmd(a) -> int:
    rows = ledger_rows(a.slug)
    month = a.month or dt.date.today().strftime("%Y-%m")
    sp = month_spend(rows, month)
    cap = usd_cap(load_brain(a.slug))
    share = f" ({sp['usd'] / cap:.0%})" if cap else ""
    print(f"{month}: ${sp['usd']:.2f} / " + (f"${cap:.2f} Atlas USD{share}" if cap is not None else
          "no USD cap set (brain.json package.monthly_usd_cap, the owner's)")
          + f", {sp['minutes']:.0f} production minutes")
    if sp["credits"] or sp["elevenlabs"]:
        print(f"  history: {sp['credits']:.0f} Higgsfield credits, {sp['elevenlabs']:.0f} ElevenLabs credits")
    for f_, v in sorted(sp["by_format"].items()):
        print(f"  {f_}: {v['pieces']} pieces, ${v['usd']:.2f}, {v['minutes']:.0f} min")
    if cap and sp["usd"] > cap / 1.25:
        print("  over 80% of the cap: keep the 25% retake buffer, move remaining slots to tier C")
    return 0


def ledger_add_cmd(a) -> int:
    fmt = CONFIG["formats"].get(a.format)
    append_row(client_dir(a.slug) / "ledger.csv",
               {"date": a.date, "post_id": a.post, "format": a.format, "tier": fmt["tier"] if fmt else "",
                "atlas_usd": a.usd, "higgsfield_credits": a.credits, "elevenlabs_credits": a.el, "minutes": a.minutes,
                "note": a.note})
    print(f"logged {a.post} in clients/{a.slug}/ledger.csv")
    return 0
