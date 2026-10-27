"""Tests for studio/push.py: studio-push."""
import json
import unittest

from studio.push import push, report
from studio.testbase import POST, SLUG, StudioCase


def echo_run(body):
    """What the hub answers to POST runs: the run as pushed, with an id."""
    return {"run": {"id": 7, "business": body["business"], "post_id": body["post_id"], "current_step": 1, "status": "active",
                    "summary": body["summary"], "steps": body["steps"]}, "files": body.get("files", [])}


class Push(StudioCase):
    def manifest(self):
        d = self.root / "project"
        (d / "docs").mkdir(parents=True)
        (d / "docs" / "script.md").write_text("# Script\n", encoding="utf-8")
        (d / "song.mp3").write_bytes(b"ID3")
        p = d / "studio.json"
        p.write_text(json.dumps({"title": "Maya's quilt", "summary": "Song made; waiting on the listen.", "files": [
            {"step": 3, "label": "Speech script", "path": "docs/script.md"},
            {"step": 4, "label": "Song master v1", "path": "song.mp3"}]}), encoding="utf-8")
        return p

    def test_push_sends_the_run_with_its_steps_ledger_and_files(self):
        self.song_run()
        self.hub.replies[("POST", "runs")] = echo_run
        res, uploaded = push(SLUG, POST, call=self.hub.call, upload=self.hub.upload, manifest_path=str(self.manifest()),
                             business="acme-app")
        get, post = self.hub.calls
        self.assertEqual((get["method"], get["path"]), ("GET", f"runs?business=acme-app&post_id={POST}"))
        body = post["body"]
        self.assertEqual((body["business"], body["title"], body["format"], body["family"], body["waiting_on_owner"]),
                         ("acme-app", "Maya's quilt", "reel_song", "song", True))
        self.assertEqual(body["summary"], "Song made; waiting on the listen.")
        self.assertEqual(body["ledger"]["post_id"], POST)
        self.assertEqual(len(body["steps"]), 16)
        self.assertEqual([f["key"] for f in body["files"]], ["docs/script.md", "song.mp3"])
        self.assertEqual((uploaded, self.hub.uploads), (1, [("acme-app", "song.mp3")]))
        self.assertTrue(all(c["api"] == "studio" for c in self.hub.calls))
        out = report(res, uploaded, "https://hub.example")
        self.assertEqual(out.splitlines()[0], f"run #7 acme-app/{POST}: step 1 Idea, angle and THE PICTURE (1/16 done), 2 file(s), 1 uploaded")
        self.assertEqual(out.splitlines()[-1], "https://hub.example/studio/7")

    def test_without_a_manifest_the_files_stay_as_they_are(self):
        self.song_run()
        self.hub.replies[("POST", "runs")] = echo_run
        push(SLUG, POST, call=self.hub.call, upload=self.hub.upload, title="Song 1")
        self.assertEqual([c["method"] for c in self.hub.calls], ["POST"])
        body = self.hub.calls[0]["body"]
        self.assertNotIn("files", body)
        self.assertEqual((body["title"], body["summary"]), ("Song 1", "Step 1 Idea, angle and THE PICTURE. Waiting on you: G-HUMAN-SONG."))

    def test_a_missing_run_or_manifest_stops_with_a_reason(self):
        with self.assertRaises(SystemExit) as e:
            push(SLUG, "NOPE", call=self.hub.call, upload=self.hub.upload)
        self.assertIn("NO_RUN", str(e.exception))
        self.song_run()
        with self.assertRaises(SystemExit) as e:
            push(SLUG, POST, call=self.hub.call, upload=self.hub.upload, manifest_path=str(self.root / "none.json"))
        self.assertIn("BAD_MANIFEST", str(e.exception))


if __name__ == "__main__":
    unittest.main()
