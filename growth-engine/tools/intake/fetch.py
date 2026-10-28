"""Reads a submitted intake from the hub app. Contract (the app's /intake/$token, built in parallel; change this one
file when its API is final): GET studio/intake?business=<slug> ->
  {"business", "submitted_at" (ISO or null when not submitted), "answers": {"A1": ..., "G1": ...},
   "files": [{"question": "F5", "name": "logo.png", "url": "https://...", "mime": "image/png", "size": 1234}]}"""
import json
import sys
import urllib.parse
from pathlib import Path


def from_hub(call, business: str) -> dict:
    return call("GET", "intake?" + urllib.parse.urlencode({"business": business}), api="studio", missing_ok=True) or {}


def from_fixture(path: str) -> dict:
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        sys.exit(f"BAD_FIXTURE: {path}: {e}")


def check(got: dict) -> dict:
    if not isinstance(got.get("answers"), dict) or not got.get("submitted_at"):
        sys.exit("NOT_SUBMITTED: the client has not submitted the intake yet (no answers or no submitted_at)")
    if not isinstance(got.get("files", []), list):
        sys.exit("BAD_INTAKE: files must be a list")
    return got
