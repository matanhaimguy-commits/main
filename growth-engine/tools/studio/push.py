"""hub.py studio-push <slug> <post_id> [--title T] [--files manifest.json] [--business B] [--summary S]

Reads clients/<slug>/runs/<post_id>/ledger.json, builds the steps and gates as pipeline.py status sees them,
resolves the manifest's files and creates or updates the run on the Studio page."""
import json
import sys
import urllib.parse
from pathlib import Path

from .cli import opt, positionals
from .ledger_steps import build_steps
from .manifest import resolve_files
from .pipeline_loader import load_pipeline
from .summary import pending_queue, summarize

USAGE = "studio-push <slug> <post_id> [--title T] [--files manifest.json] [--business B] [--summary S]"


def read_manifest(path: str | None) -> tuple[dict, Path]:
    if not path:
        return {}, Path.cwd()
    p = Path(path)
    try:
        return json.loads(p.read_text(encoding="utf-8")), p.resolve().parent
    except (OSError, json.JSONDecodeError) as e:
        sys.exit(f"BAD_MANIFEST: {p}: {e}")


def run_body(led: dict, business: str, post_id: str, steps: list[dict], manifest: dict, title=None, summary=None) -> dict:
    """The POST /api/studio/runs body, files aside."""
    body = {"business": business, "post_id": post_id, "format": led.get("format"), "family": led.get("family"),
            "waiting_on_owner": bool(pending_queue(led)), "steps": steps, "ledger": led,
            "summary": (summary or manifest.get("summary") or summarize(steps, led))[:300]}
    if title or manifest.get("title"):
        body["title"] = title or manifest["title"]
    return body


def push(slug: str, post_id: str, *, call, upload, title=None, manifest_path=None, business=None, summary=None,
         pipeline=None) -> tuple[dict, int]:
    """Creates/updates the run; returns the hub's answer and how many files were uploaded."""
    P = pipeline or load_pipeline()
    try:
        led = P.load_ledger(slug, post_id)
    except P.PipelineError as e:
        sys.exit(f"NO_RUN: {e}")
    business = business or slug
    manifest, base = read_manifest(manifest_path)
    body = run_body(led, business, post_id, build_steps(P, led, manifest.get("steps")), manifest, title, summary)
    uploaded = 0
    if "files" in manifest:
        q = urllib.parse.urlencode({"business": business, "post_id": post_id})
        got = call("GET", f"runs?{q}", api="studio", missing_ok=True) or {}
        existing = {f["key"]: f for f in got.get("files", [])}
        body["files"], uploaded = resolve_files(manifest, base, business, existing, upload)
    return call("POST", "runs", body, api="studio"), uploaded


def report(res: dict, uploaded: int, hub_url: str) -> str:
    run, files = res["run"], res.get("files", [])
    steps = run.get("steps", [])
    cur = next((s for s in steps if s["n"] == run.get("current_step")), None)
    where = f"step {cur['n']} {cur['name']}" if cur else run["status"]
    done = sum(s["status"] == "done" for s in steps)
    total = sum(s["status"] != "na" for s in steps)
    return "\n".join([f"run #{run['id']} {run['business']}/{run['post_id']}: {where} ({done}/{total} done), "
                      f"{len(files)} file(s), {uploaded} uploaded", run.get("summary") or "", f"{hub_url}/studio/{run['id']}"])


def cli(rest: list[str], *, call, upload, hub_url: str) -> None:
    slug, post_id = positionals(rest, ["slug", "post_id"], USAGE)
    res, uploaded = push(slug, post_id, call=call, upload=upload, title=opt(rest, "--title"), manifest_path=opt(rest, "--files"),
                         business=opt(rest, "--business"), summary=opt(rest, "--summary"))
    print(report(res, uploaded, hub_url))
