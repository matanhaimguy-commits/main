"""clients/<slug>/ledger.csv: one row per finished piece. atlas_usd is what Atlas charged; the Higgsfield and
ElevenLabs credit columns are kept for the pieces made before the move to Atlas (owner, 28 Oct 2026)."""
from __future__ import annotations

import csv
import os
from pathlib import Path

HEADER = ["date", "post_id", "format", "tier", "atlas_usd", "higgsfield_credits", "elevenlabs_credits", "minutes", "note"]


def append_row(path: Path, row: dict) -> None:
    """Appends one row. A ledger from before atlas_usd is rewritten once with the new header (old rows keep their
    values; their atlas_usd stays empty), through a temp file, so a row that can't be written leaves it untouched."""
    rows: list[dict] = []
    if path.exists():
        with path.open(newline="") as f:
            rd = csv.DictReader(f)
            old = list(rd.fieldnames or [])
            rows = list(rd)
        extra = [k for k in old if k not in HEADER]
        if extra:
            raise ValueError(f"{path} has columns this tool does not know: {extra}")
        if old == HEADER:
            with path.open("a", newline="") as f:
                csv.DictWriter(f, HEADER).writerow(row)
            return
    tmp = path.with_name(f".{path.name}.tmp")
    try:
        with tmp.open("w", newline="") as f:
            wr = csv.DictWriter(f, HEADER, restval="")
            wr.writeheader()
            wr.writerows(rows)
            wr.writerow(row)
        os.replace(tmp, path)  # the old ledger stays whole until the new one is complete
    finally:
        tmp.unlink(missing_ok=True)
