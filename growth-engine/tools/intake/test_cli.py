"""Tests for intake/cli.py and write.py: intake-pull from a fixture, from the hub, and dry run."""
import contextlib
import io
import json
import unittest

from intake import cli
from intake.testbase import FIXTURE, IntakeCase, sample
from studio.testbase import Recorder


class IntakePull(IntakeCase):
    def run_pull(self, **kw):
        return cli.pull("sample-bakery", root=self.root, **kw)

    def test_fixture_writes_answers_and_files_without_network(self):
        got, bad, paths = self.run_pull(fixture=str(FIXTURE))
        self.assertEqual(bad, [])
        d = self.root / "clients" / "sample-bakery" / "intake"
        self.assertEqual({p.name for p in paths}, {"answers.json", "files.json"})
        a = json.loads((d / "answers.json").read_text())
        self.assertEqual(a["answers"]["A1"], "Sample Bakery")
        self.assertEqual(a["missing_required"], [])
        self.assertEqual(json.loads((d / "files.json").read_text())[0]["name"], "logo.png")

    def test_dry_run_writes_nothing(self):
        _, _, paths = self.run_pull(fixture=str(FIXTURE), dry_run=True)
        self.assertEqual(paths, [])
        self.assertFalse((self.root / "clients").exists())

    def test_reads_the_hub_for_the_clients_business(self):
        hub = Recorder()
        hub.replies[("GET", "intake")] = sample()
        self.run_pull(call=hub.call, business="bakery-app")
        self.assertEqual(hub.calls[0]["path"], "intake?business=bakery-app")
        self.assertEqual(hub.calls[0]["api"], "studio")

    def test_an_unsubmitted_intake_stops(self):
        hub = Recorder()
        hub.replies[("GET", "intake")] = {"answers": {}, "submitted_at": None}
        with self.assertRaisesRegex(SystemExit, "NOT_SUBMITTED"):
            self.run_pull(call=hub.call)

    def test_cli_reports_missing_answers_and_exits_1(self):
        bad = sample()
        del bad["answers"]["G1"]
        p = self.root / "partial.json"
        p.write_text(json.dumps(bad))
        out = io.StringIO()
        with contextlib.redirect_stdout(out), self.assertRaises(SystemExit) as e:
            cli.cli(["sample-bakery", "--fixture", str(p), "--dry-run"], call=None)
        self.assertEqual(e.exception.code, 1)
        self.assertIn("G1", out.getvalue())
        self.assertIn("NOT READY", out.getvalue())

    def test_cli_ready_message(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            cli.cli(["sample-bakery", "--fixture", str(FIXTURE), "--dry-run"], call=None)
        self.assertIn("ready", out.getvalue())


if __name__ == "__main__":
    unittest.main()
