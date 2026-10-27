"""hub.py studio-answers [--slug S]

The owner's answers from the Studio page that the studio hasn't taken in yet, as JSON. Record each in the run
(pipeline.py approve/gate, --by the owner's name), then mark it with studio-synced <id>."""
import json
import urllib.parse

from .cli import opt


def answers(*, call, slug=None) -> list[dict]:
    q = urllib.parse.urlencode({"status": "answered", **({"business": slug} if slug else {})})
    out = []
    for d in call("GET", f"decisions?{q}", api="studio")["decisions"]:
        a = d.get("answer") or {}
        out.append({"id": d["id"], "business": d["business"], "post_id": d["post_id"], "checkpoint": d["checkpoint"],
                    "key": d["key"], "step": d.get("step"), "question": d["question"], "choices": a.get("choices", []),
                    "note": a.get("note", ""), "by": a.get("by"), "answered_at": a.get("at") or d.get("answered_at")})
    return out


def cli(rest: list[str], *, call, upload=None, hub_url: str = "") -> None:
    print(json.dumps(answers(call=call, slug=opt(rest, "--slug")), ensure_ascii=False, indent=1))
