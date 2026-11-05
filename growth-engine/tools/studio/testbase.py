"""Shared by the studio tests: a temporary repo root for pipeline.py runs, and recorders for the hub calls."""
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))
import pipeline as P  # noqa: E402

SLUG, POST = "acme", "AC-2026-10-W4-01"


class Recorder:
    """Stands in for hub.call / hub.upload: records every call and answers from `replies[(method, path)]`."""

    def __init__(self):
        self.calls, self.uploads, self.replies = [], [], {}

    def call(self, method, path, body=None, timeout=120, api="content", missing_ok=False):
        self.calls.append({"method": method, "path": path, "body": body, "api": api})
        reply = self.replies.get((method, path.split("?")[0]))
        if callable(reply):
            return reply(body)
        if reply is None and missing_ok:
            return None
        return reply if reply is not None else {}

    def upload(self, slug, file):
        self.uploads.append((slug, Path(file).name))
        return f"https://storage.example/{slug}/{Path(file).name}"


class StudioCase(unittest.TestCase):
    """A temporary repo root with one client, and a fresh Recorder."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self._root, self._out = P.ROOT, P.OUT
        P.ROOT, P.OUT = self.root, self.root / "growth-engine" / "production"
        (self.root / "clients" / SLUG).mkdir(parents=True)
        self.hub = Recorder()

    def tearDown(self):
        P.ROOT, P.OUT = self._root, self._out
        self.tmp.cleanup()

    def song_run(self) -> dict:
        """A song piece at step 1: brief done, the idea failed once, and the owner owes a song listen."""
        P.init_run(SLUG, POST, "reel_song")
        P.record_gate(SLUG, POST, "G-BRIEF", "PASS", "claude", note="brief from brain.json")
        P.close_step(SLUG, POST, 0, "done")
        P.record_gate(SLUG, POST, "G-IDEA", "FAIL", "organic-director", note="picture too abstract")
        led = P.load_ledger(SLUG, POST)
        P._queue_add(led, "G-HUMAN-SONG", "Listen to the song master")
        P.save_ledger(led)
        return P.load_ledger(SLUG, POST)
