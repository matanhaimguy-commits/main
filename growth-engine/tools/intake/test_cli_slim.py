"""Tests for intake-pull on the slim shape (cli.py, write.py): fixture, hub with fake responses, documents, privacy."""
import json
import subprocess
import unittest
from pathlib import Path

from intake import cli
from intake.test_slim import slim_row
from intake.testbase import FIXTURE, IntakeCase, response
from studio.testbase import Recorder

SLIM = FIXTURE.parent / "slim-intake.json"


class SlimPull(IntakeCase):
    def hub(self):
        h = Recorder()
        h.replies[("GET", "intakes")] = slim_row()
        return h

    def run_pull(self, **kw):
        kw.setdefault("get", lambda u: b"hello world" if "guide" in u else b"12345")
        return cli.pull("sample-bakery", root=self.root, **kw)

    def test_reads_the_slim_shape_from_the_hub_and_downloads_docs(self):
        h = self.hub()
        got, bad, paths = self.run_pull(call=h.call)
        self.assertEqual(h.calls[0]["path"], "intakes?brand=sample-bakery")
        self.assertEqual(bad, [])
        d = self.root / "clients" / "sample-bakery"
        self.assertEqual((d / "foundation" / "brand-guide.pdf").read_bytes(), b"hello world")
        self.assertTrue((d / "foundation" / "prices.xlsx").exists())  # the ../ in the name is dropped
        slim = json.loads((d / "intake" / "slim.json").read_text())
        self.assertEqual(slim["business_name"], "Sample Bakery")
        self.assertEqual(slim["competitors"], ["Corner Loaf", "https://rival-bakery.example"])
        self.assertNotIn("signed_url", json.dumps(slim))
        self.assertEqual([p.name for p in paths], ["slim.json"])

    def test_fixture_makes_no_network_calls_and_downloads_nothing(self):
        got, bad, _ = self.run_pull(fixture=str(SLIM), get=lambda u: self.fail("no download from a fixture"))
        self.assertEqual(bad, [])
        self.assertFalse((self.root / "clients" / "sample-bakery" / "foundation").exists())

    def test_dry_run_writes_nothing(self):
        _, _, paths = self.run_pull(call=self.hub().call, dry_run=True, get=lambda u: self.fail("no download"))
        self.assertEqual(paths, [])
        self.assertFalse((self.root / "clients").exists())

    def test_expired_link_fails_the_gate_with_the_document_name(self):
        def get(u):
            raise OSError("link expired")
        _, bad, _ = self.run_pull(call=self.hub().call, get=get)
        self.assertEqual([m["id"] for m in bad], ["doc:brand-guide.pdf", "doc:../prices.xlsx"])

    def test_one_unsigned_doc_does_not_lose_the_others_and_the_gate_names_it(self):
        row = slim_row()
        row["docs"][0]["signed_url"] = None
        h = Recorder()
        h.replies[("GET", "intakes")] = row
        _, bad, _ = self.run_pull(call=h.call)
        self.assertEqual([m["id"] for m in bad], ["doc:brand-guide.pdf"])
        self.assertIn("no signed link", bad[0]["why"])
        self.assertTrue((self.root / "clients" / "sample-bakery" / "foundation" / "prices.xlsx").exists())

    def test_a_404_says_there_is_no_submitted_intake(self):
        h = Recorder()  # no reply set and missing_ok: answers None, like a 404
        with self.assertRaisesRegex(SystemExit, "no submitted intake for sample-bakery"):
            self.run_pull(call=h.call)

    def test_the_hub_token_is_never_sent_to_the_storage_host(self):
        seen = []
        self.run_pull(call=self.hub().call, get=lambda u: seen.append(u) or b"x")
        self.assertEqual(len(seen), 2)  # fetch takes only a URL, so no header can carry the token

    def test_old_shape_still_works(self):
        h = Recorder()
        h.replies[("GET", "intakes")] = response()
        got, bad, paths = self.run_pull(call=h.call)
        self.assertEqual(got["shape"], "legacy")
        self.assertEqual({p.name for p in paths}, {"answers.json", "files.json"})

    def test_cli_exits_1_when_not_ready(self):
        row = {**slim_row(), "business_name": ""}
        h = Recorder()
        h.replies[("GET", "intakes")] = row
        with self.assertRaises(SystemExit) as e:
            cli.cli(["sample-bakery", "--dry-run"], call=h.call)
        self.assertEqual(e.exception.code, 1)


class Privacy(unittest.TestCase):
    def test_foundation_folders_are_gitignored(self):
        repo = Path(__file__).resolve().parents[3]
        r = subprocess.run(["git", "check-ignore", "clients/acme/foundation/brand-guide.pdf"], cwd=repo, capture_output=True)
        self.assertEqual(r.returncode, 0)


if __name__ == "__main__":
    unittest.main()
