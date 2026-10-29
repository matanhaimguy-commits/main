"""Reads a submitted intake from the hub app (agent-start-spark src/server/clients/api-intakes.server.ts).

Slim shape (docs-first, Quick onboarding): GET clients/intakes?brand=<slug> -> {brand, business_name, website, instagram,
offer_line, competitors: [str], consents: {ai_people, proof}, docs: [{name, mime, size, signed_url}], submitted_at}.
Old shape (38 questions):
GET clients/intakes?brand=<brand slug> (studio token) ->
  {"intakes": [{id, brand, answers: {<question id>: value}, files: [{name, url, type?, size?}], status: "submitted",
                submits, submitted_at, expires_at, created_at}], "confirmations": [...]}
Only submitted rows, newest first: intakes[0] is the latest. The answer ids are intake-questions.json's. A fixture is a
saved copy of that response. A 404 or any other HTTP error stops (hub.call exits); it is never read as "not submitted"."""
import json
import sys
import urllib.parse
from pathlib import Path

from . import shape, slim


def from_hub(call, slug: str) -> dict:
    return call("GET", "intakes?" + urllib.parse.urlencode({"brand": slug}), api="clients")


def from_fixture(path: str) -> dict:
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        sys.exit(f"BAD_FIXTURE: {path}: {e}")


def latest(resp: dict) -> dict:
    """The newest submitted intake. Old shape: {shape: "legacy", answers, files, submitted_at}. Slim shape:
    {shape: "slim", slim: {...}, submitted_at} (see slim.py)."""
    row = shape.row_of(resp)
    if not row:
        sys.exit("NOT_SUBMITTED: the client has not submitted the intake yet (the hub has no submitted intake for this brand)")
    if shape.kind(row) == "slim":
        s = slim.normalize(row)
        return {"shape": "slim", "slim": s, "submitted_at": s["submitted_at"]}
    if not isinstance(row.get("answers"), dict) or not isinstance(row.get("files") or [], list):
        sys.exit("BAD_INTAKE: answers must be an object and files a list")
    return {"shape": "legacy", "answers": row["answers"], "files": row.get("files") or [],
            "submitted_at": row.get("submitted_at") or row.get("created_at")}
