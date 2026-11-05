"""hub.py studio-synced <decision_id>

Marks an answer as taken into the studio, after it was recorded in the run. The hub refuses (HUB_HTTP_409) a
question the owner hasn't answered yet."""
import sys

from .cli import positionals


def mark_synced(decision_id: int, *, call) -> bool:
    """True when it was marked now, False when it already was."""
    res = call("POST", "synced", {"ids": [decision_id]}, api="studio")
    return decision_id in res.get("synced", [])


def cli(rest: list[str], *, call, upload=None, hub_url: str = "") -> None:
    (raw,) = positionals(rest, ["decision_id"], "studio-synced <decision_id>")
    if not raw.isdigit():
        sys.exit("usage: hub.py studio-synced <decision_id> (a number from studio-answers)")
    did = int(raw)
    print(f"decision #{did} {'synced' if mark_synced(did, call=call) else 'was already synced'}")
