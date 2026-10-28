"""The hub business a client folder posts to: brain.json `hub.business`, else the folder's own slug.

clients/straightscale-en is the English account, posted through the hub's only business, `straightscale`; its brain
says so, so hub.py and the studio commands need no --business for it. An explicit --business still wins."""
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]


def business_for(slug: str, root: Path | None = None, given: str | None = None) -> str:
    if given:
        return given
    p = Path(root or REPO) / "clients" / slug / "brain.json"
    try:
        hub = json.loads(p.read_text(encoding="utf-8")).get("hub") or {}
    except (OSError, ValueError, AttributeError):
        return slug
    b = hub.get("business") if isinstance(hub, dict) else None
    return b if isinstance(b, str) and b else slug
