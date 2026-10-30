"""Tests for hub.py's dispatch of the studio commands (the commands themselves: growth-engine/tools/studio/test_*.py).

    python3 -m unittest growth-engine/tools/test_hub.py
    python3 -m unittest discover -s growth-engine/tools/studio -t growth-engine/tools

No network: hub.call and hub.upload are replaced by a recorder.
"""
import contextlib
import io
import json
import os
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import hub as H  # noqa: E402
from studio.testbase import POST, SLUG, StudioCase  # noqa: E402

FAKE_TOKEN = "ssk_fake-token-never-printed-1234567890"


class Dispatch(StudioCase):
    def setUp(self):
        super().setUp()
        self._call, self._upload, self._env = H.call, H.upload, os.environ.get("HUB_TOKEN")
        H.call, H.upload = self.hub.call, self.hub.upload
        os.environ["HUB_TOKEN"] = FAKE_TOKEN

    def tearDown(self):
        H.call, H.upload = self._call, self._upload
        if self._env is None:
            os.environ.pop("HUB_TOKEN", None)
        else:
            os.environ["HUB_TOKEN"] = self._env
        super().tearDown()

    def run_cli(self, *args):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            H.main([str(a) for a in args])
        return out.getvalue()

    def test_every_studio_command_goes_to_its_module_with_hubs_call(self):
        self.song_run()
        self.hub.replies[("POST", "runs")] = lambda body: {"run": {"id": 7, "business": body["business"], "post_id": body["post_id"],
                                                                   "current_step": 1, "status": "active", "summary": body["summary"],
                                                                   "steps": body["steps"]}}
        self.hub.replies[("POST", "decisions")] = lambda body: {"decision": {"id": 3, "run_id": 7, "key": "GATE-4",
                                                                             "question": body["question"]}}
        self.hub.replies[("GET", "decisions")] = {"decisions": []}
        self.hub.replies[("POST", "synced")] = {"synced": [3]}
        q = self.root / "q.json"
        q.write_text(json.dumps({"checkpoint": "GATE-4", "question": "Which spine?"}))
        out = "".join([self.run_cli("studio-push", SLUG, POST), self.run_cli("studio-ask", SLUG, POST, q),
                       self.run_cli("studio-answers"), self.run_cli("studio-synced", "3")])
        self.assertEqual([(c["method"], c["path"].split("?")[0]) for c in self.hub.calls],
                         [("POST", "runs"), ("POST", "decisions"), ("GET", "decisions"), ("POST", "synced")])
        self.assertIn(f"{H.HUB_URL}/studio/7", out)
        self.assertIn("decision #3 asked (GATE-4): Which spine?", out)
        self.assertIn("decision #3 synced", out)
        self.assertNotIn(FAKE_TOKEN, out)

    def test_a_client_folder_posts_as_its_brains_hub_business(self):
        d = self.root / "clients" / "acme-en"
        d.mkdir(parents=True)
        (d / "brain.json").write_text(json.dumps({"hub": {"business": "acme"}}))
        import studio.business as B
        repo, B.REPO = B.REPO, self.root
        try:
            self.hub.replies[("GET", "results")] = {"results": []}
            self.hub.replies[("POST", "items")] = lambda body: {"items": [{"id": 1, "status": "draft", "kind": "reel",
                                                                           "business": body["items"][0]["business"]}]}
            item = self.root / "item.json"
            item.write_text(json.dumps({"business": "acme-en", "kind": "reel", "caption": "c", "media": []}))
            self.run_cli("results", "acme-en")
            self.run_cli("push", item)
            self.run_cli("results", "acme-en", "--days", "7")
        finally:
            B.REPO = repo
        self.assertEqual(self.hub.calls[0]["path"], "results?business=acme&days=30")
        self.assertEqual(self.hub.calls[1]["body"]["items"][0]["business"], "acme")

    def test_help_lists_the_studio_commands(self):
        out = self.run_cli("--help")
        for cmd in ("studio-push", "studio-ask", "studio-answers", "studio-synced"):
            self.assertIn(f"hub.py {cmd}", out)


if __name__ == "__main__":
    unittest.main()
