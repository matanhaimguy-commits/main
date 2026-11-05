"""Checks a sync body against C1's rules (docs/client-os.md) before it is sent, so a bad body stops here and not as
a 400 from the hub. Returns the problems; an empty list is a valid body."""
import datetime as dt
import json
import re

from .body import BRAND_KEYS, PIECE_KEYS

SLUG = re.compile(r"^[a-z0-9][a-z0-9-]{0,63}$")
BRAND_STATUS = ("onboarding", "research", "active", "paused")
PIECE_STATUS = ("planned", "scripted", "produced", "approved", "scheduled", "live", "scored", "killed")
SNAPSHOT_KINDS = ("brain", "plan", "onboarding", "spend")
MAX_SNAPSHOT, MAX_PIECES, MAX_GRADES, MAX_GATES = 500_000, 1000, 50, 100


def iso_with_offset(v) -> bool:
    try:
        return dt.datetime.fromisoformat(str(v)).utcoffset() is not None
    except ValueError:
        return False


def brand_problems(b) -> list[str]:
    if not isinstance(b, dict):
        return ["brand: an object is required"]
    out = [f"brand.{k}: not in the contract" for k in b if k not in BRAND_KEYS]
    if not SLUG.match(str(b.get("slug") or "")):
        out.append("brand.slug: required, ^[a-z0-9][a-z0-9-]{0,63}$")
    if not b.get("name"):
        out.append("brand.name: required")
    if b.get("status") not in BRAND_STATUS:
        out.append(f"brand.status: one of {', '.join(BRAND_STATUS)}")
    return out


def snapshot_problems(s) -> list[str]:
    if s is None:
        return []
    if not isinstance(s, dict):
        return ["snapshots: an object"]
    out = []
    for kind, data in s.items():
        if kind not in SNAPSHOT_KINDS:
            out.append(f"snapshots.{kind}: kinds are {', '.join(SNAPSHOT_KINDS)}")
        elif not isinstance(data, dict):
            out.append(f"snapshots.{kind}: a JSON object")
        elif len(json.dumps(data, ensure_ascii=False).encode()) > MAX_SNAPSHOT:
            out.append(f"snapshots.{kind}: over 500 KB")
    return out


def piece_problems(i: int, p: dict) -> list[str]:
    at = f"pieces[{i}]"
    out = [f"{at}.{k}: not in the contract" for k in p if k not in PIECE_KEYS]
    if not p.get("post_id"):
        out.append(f"{at}.post_id: required")
    if p.get("status") not in PIECE_STATUS:
        out.append(f"{at}.status: one of {', '.join(PIECE_STATUS)}")
    if p.get("slot") is not None and not iso_with_offset(p["slot"]):
        out.append(f"{at}.slot: ISO date-time with offset, or null")
    if p.get("funnel_stage") not in (None, "TOF", "MOF", "BOF"):
        out.append(f"{at}.funnel_stage: TOF, MOF, BOF or null")
    return out + grade_problems(at, p)


def grade_problems(at: str, p: dict) -> list[str]:
    """hook_grades and gates are lists of objects, never null (the hub's `z.array(z.record(...)).default([])`)."""
    out = []
    for k, cap in (("hook_grades", MAX_GRADES), ("gates", MAX_GATES)):
        v = p.get(k, [])
        if not isinstance(v, list) or len(v) > cap or not all(isinstance(x, dict) for x in v):
            out.append(f"{at}.{k}: a list of at most {cap} objects (use [] for none, not null)")
    return out


def problems(body: dict) -> list[str]:
    out = brand_problems(body.get("brand")) + snapshot_problems(body.get("snapshots"))
    pieces = body.get("pieces")
    if pieces is None:
        return out
    if not isinstance(pieces, list) or len(pieces) > MAX_PIECES:
        return out + [f"pieces: a list of at most {MAX_PIECES}"]
    ids = [p.get("post_id") for p in pieces]
    if len(set(ids)) != len(ids):
        out.append("pieces: a post_id is listed twice")
    for i, p in enumerate(pieces):
        out += piece_problems(i, p) if isinstance(p, dict) else [f"pieces[{i}]: an object"]
    return out
