"""Tests for brand/cli.py, fetch.py and vault.py: brand-pull with fake hub responses (no network)."""
import contextlib
import io
import json
import unittest

from brainio.testbase import BrainCase
from brand import cli, fetch
from studio.testbase import Recorder

RESP = {"brand": "acme", "overrides": {"offer": "Bread subscription", "cadence": "4", "cta_keyword": "LOAF"},
        "updated_at": "2026-10-29T08:00:00Z"}


class BrandPull(BrainCase):
    def hub(self, resp=RESP):
        h = Recorder()
        h.replies[("GET", "brand-overrides")] = resp
        return h

    def pull(self, h=None, **kw):
        kw.setdefault("today", "2026-10-29")
        kw.setdefault("vault_dir", self.root / "vault")
        return cli.pull("acme", call=(h or self.hub()).call, root=self.root, **kw)

    def test_reads_by_brand_with_a_get_and_writes_brain_json(self):
        h = self.hub()
        r = self.pull(h)
        self.assertEqual((h.calls[0]["method"], h.calls[0]["path"], h.calls[0]["api"]), ("GET", "brand-overrides?brand=acme", "clients"))
        self.assertEqual(len(h.calls), 1)
        b = self.brain()
        self.assertEqual((b["offer"]["main_offer"], b["package"]["posts_per_week"], b["offer"]["keyword"]), ("Bread subscription", 4, "LOAF"))
        self.assertEqual(b["field_sources"]["offer.main_offer"], "Matan (Brand card, 2026-10-29)")
        self.assertEqual(len(r["changes"]), 3)

    def test_dry_run_writes_nothing(self):
        before = (self.dir / "brain.json").read_text()
        r = self.pull(dry_run=True)
        self.assertEqual(len(r["changes"]), 3)
        self.assertEqual((self.dir / "brain.json").read_text(), before)

    def test_a_bad_field_writes_nothing(self):
        before = (self.dir / "brain.json").read_text()
        bad = {**RESP, "overrides": {"offer": "ok", "cadence": 99}}
        with self.assertRaisesRegex(SystemExit, "BRAND_PULL_FAILED"):
            self.pull(self.hub(bad))
        self.assertEqual((self.dir / "brain.json").read_text(), before)

    def test_a_result_that_fails_the_schema_writes_nothing(self):
        b = self.brain()
        b["package"] = {"posts_per_week": 1}  # account_stage missing: the starting brain is already invalid
        self.write_brain(b)
        before = (self.dir / "brain.json").read_text()
        with self.assertRaisesRegex(SystemExit, "account_stage"):
            self.pull()
        self.assertEqual((self.dir / "brain.json").read_text(), before)

    def test_vault_note_is_regenerated_when_the_vault_exists(self):
        (self.root / "vault" / "Agency OS").mkdir(parents=True)
        r = self.pull()
        self.assertEqual(r["vault"], "vault note: regenerated")
        note = next((self.root / "vault" / "Agency OS" / "Clients").rglob("*.md")).read_text()
        self.assertIn("Bread subscription", note)

    def test_vault_missing_is_skipped_not_an_error(self):
        import brain_note
        saved = brain_note.notes_dir
        brain_note.notes_dir = lambda v, r: None
        try:
            r = self.pull()
        finally:
            brain_note.notes_dir = saved
        self.assertIn("skipped", r["vault"])
        self.assertEqual(self.brain()["offer"]["main_offer"], "Bread subscription")

    def test_second_pull_with_the_same_card_writes_nothing(self):
        self.pull()
        text = (self.dir / "brain.json").read_text()
        r = self.pull(today="2026-11-05")
        self.assertEqual(r["changes"], [])
        self.assertFalse(r["written"])
        self.assertEqual((self.dir / "brain.json").read_text(), text)

    def test_fixture_needs_no_hub(self):
        f = self.root / "resp.json"
        f.write_text(json.dumps(RESP))
        r = cli.pull("acme", fixture=str(f), root=self.root, dry_run=True)
        self.assertEqual(len(r["changes"]), 3)

    def test_wrong_brand_or_shape_stops(self):
        with self.assertRaisesRegex(SystemExit, "BAD_BRAND_OVERRIDES"):
            fetch.from_hub(self.hub({"brand": "other", "overrides": {}}).call, "acme")
        with self.assertRaisesRegex(SystemExit, "BAD_BRAND_OVERRIDES"):
            fetch.from_hub(self.hub({"brand": "acme"}).call, "acme")

    def test_cli_prints_the_changed_fields(self):
        out = io.StringIO()
        saved = cli.pull
        cli.pull = lambda slug, **kw: saved(slug, today="2026-10-29", vault_dir=self.root / "v", root=self.root, **kw)
        try:
            with contextlib.redirect_stdout(out):
                cli.cli(["acme"], call=self.hub().call)
        finally:
            cli.pull = saved
        self.assertIn("offer -> offer.main_offer", out.getvalue())
