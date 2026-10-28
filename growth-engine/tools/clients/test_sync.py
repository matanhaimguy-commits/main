"""Tests for clients/sync.py and clients/body.py: the snapshot and the client-sync command."""
import datetime as dt
import unittest
from unittest import mock

from clients import body, sync
from clients.testbase import SLUG, ClientsCase

NOW = dt.datetime(2026, 10, 28, 18, 0, tzinfo=dt.timezone.utc)


class Sync(ClientsCase):
    def build(self):
        return sync.build(SLUG, root=self.root, now=NOW, registry_path=self.registry)

    def test_snapshot_shape(self):
        s = self.build()
        self.assertEqual(list(s), ["contract", "generated_at", "business", "brand", "brain", "plan", "pieces", "spend", "counts"])
        self.assertEqual((s["contract"], s["business"], s["generated_at"]), (body.CONTRACT, "acme-app", "2026-10-28T18:00:00+00:00"))
        self.assertEqual(s["brand"]["vault_folder"], "Agency OS/Clients/Acme")
        self.assertEqual(s["spend"]["month"], "2026-10")
        self.assertEqual(s["counts"], {"pieces": 2, "bank": 1, "status": {"planned": 1, "scripted": 1},
                                       "funnel_stage": {"BOF": 1, "TOF": 1}})

    def test_piece_joins_card_run_and_project(self):
        p = self.build()["pieces"][0]
        self.assertEqual((p["post_id"], p["title"], p["funnel_stage"], p["family"]), ("AC-2026-11-W1-01", "Title AC-2026-11-W1-01", "TOF", "motion"))
        self.assertEqual(p["slot"], {"local": "2026-11-02 12:00", "timezone": "America/New_York", "at": "2026-11-02T12:00:00-05:00"})
        self.assertEqual(p["hook"]["id"], "AC-B")
        self.assertEqual(p["scores"]["card_gates"], {"idea": "pass"})
        self.assertEqual(p["scores"]["project_gate_score"], 88)
        self.assertEqual(p["production"]["waiting_on_owner"], ["G-HUMAN-SPINE"])
        self.assertEqual(p["links"], {"card": "clients/acme/cards/W1/AC-01.yaml", "project": "motion-studio/projects/acme-01",
                                      "run": "clients/acme/runs/AC-2026-11-W1-01", "studio_post_id": "AC-2026-11-W1-01",
                                      "content_external_key": "AC-2026-11-W1-01", "hub_item_id": None})

    def test_piece_without_run_or_project_defaults_its_stage(self):
        p = self.build()["pieces"][1]
        self.assertEqual((p["funnel_stage"], p["production"], p["links"]["run"]), ("BOF", None, None))
        self.assertEqual(p["hook"]["spoken"], "Here's the one test.")

    def test_dry_run_calls_nothing_and_a_real_run_posts_to_clients_sync(self):
        calls = []
        call = lambda *a, **k: calls.append((a, k)) or {}
        snap = self.build()
        with mock.patch.object(sync, "build", lambda slug, month=None: snap), \
                mock.patch("builtins.print") as out:
            sync.cli([SLUG, "--dry-run"], call=call)
            self.assertEqual(calls, [])
            self.assertIn("dry run, nothing sent", out.call_args_list[0].args[0])
            sync.cli([SLUG], call=call)
        (args, kw), = calls
        self.assertEqual((args[0], args[1], kw), ("POST", "sync", {"api": "clients"}))
        self.assertEqual(args[2]["contract"], body.CONTRACT)

    def test_report_lines(self):
        text = sync.report(self.build(), sent=False)
        self.assertIn("pieces: 2 slotted + 1 bank", text)
        self.assertIn("funnel: BOF 1, TOF 1", text)
        self.assertIn("spend 2026-10: $1.25 of $50.00", text)


if __name__ == "__main__":
    unittest.main()
