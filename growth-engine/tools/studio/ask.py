"""hub.py studio-ask <slug> <post_id> <decision.json> [--business B]

Puts a checkpoint question to the owner on the Studio page. The run must have been pushed first. --business
defaults to the client brain's hub.business, else <slug>."""
import json
import sys
from pathlib import Path

from .business import business_for
from .cli import opt, positionals

USAGE = "studio-ask <slug> <post_id> <decision.json> [--business B]"


def read_decision(path: str) -> dict:
    """The decision JSON, with "context_file" (relative to it) read into "context"."""
    p = Path(path)
    try:
        d = json.loads(p.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        sys.exit(f"BAD_DECISION: {p}: {e}")
    if not isinstance(d, dict) or not d.get("checkpoint") or not d.get("question"):
        sys.exit("BAD_DECISION: it needs at least \"checkpoint\" and \"question\"")
    cf = d.pop("context_file", None)
    if cf:
        cp = (p.resolve().parent / cf).resolve()
        if not cp.is_file():
            sys.exit(f"NO_FILE: {cp}")
        d["context"] = cp.read_text(encoding="utf-8")
    return d


def ask(slug: str, post_id: str, path: str, *, call, business=None, root=None) -> dict:
    d = read_decision(path)
    d.update({"business": business_for(slug, root, business), "post_id": post_id})
    return call("POST", "decisions", d, api="studio")


def cli(rest: list[str], *, call, upload=None, hub_url: str) -> None:
    slug, post_id, path = positionals(rest, ["slug", "post_id", "decision.json"], USAGE)
    res = ask(slug, post_id, path, call=call, business=opt(rest, "--business"))
    d = res["decision"]
    print(f"decision #{d['id']} {'updated' if res.get('updated') else 'asked'} ({d['key']}): {d['question']}")
    print(f"{hub_url}/studio/{d['run_id']}")
