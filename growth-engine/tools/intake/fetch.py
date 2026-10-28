"""Reads a submitted intake from the hub app (agent-start-spark src/server/clients/api-intakes.server.ts).

GET clients/intakes?brand=<brand slug> (studio token) ->
  {"intakes": [{id, brand, answers: {<question id>: value}, files: [{name, url, type?, size?}], status: "submitted",
                submits, submitted_at, expires_at, created_at}], "confirmations": [...]}
Only submitted rows, newest first: intakes[0] is the latest. The answer ids are intake-questions.json's. A fixture is a
saved copy of that response. A 404 or any other HTTP error stops (hub.call exits); it is never read as "not submitted"."""
import json
import sys
import urllib.parse
from pathlib import Path


def from_hub(call, slug: str) -> dict:
    return call("GET", "intakes?" + urllib.parse.urlencode({"brand": slug}), api="clients")


def from_fixture(path: str) -> dict:
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        sys.exit(f"BAD_FIXTURE: {path}: {e}")


def latest(resp: dict) -> dict:
    """The newest submitted intake, as {answers, files, submitted_at}."""
    rows = resp.get("intakes") if isinstance(resp, dict) else None
    if not rows:
        sys.exit("NOT_SUBMITTED: the client has not submitted the intake yet (the hub has no submitted intake for this brand)")
    row = rows[0]
    if not isinstance(row.get("answers"), dict) or not isinstance(row.get("files") or [], list):
        sys.exit("BAD_INTAKE: answers must be an object and files a list")
    return {"answers": row["answers"], "files": row.get("files") or [], "submitted_at": row.get("submitted_at") or row.get("created_at")}
