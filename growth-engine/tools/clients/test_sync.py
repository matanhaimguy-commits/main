"""Tests for clients/sync.py and clients/body.py: the sync body as C1's contract takes it, and the command."""
import datetime as dt
import unittest
from unittest import mock

from clients import body, sync
from clients.contract import problems
from clients.testbase import SLUG, ClientsCase

NOW = dt.datetime(2026, 10, 28, 18, 0, tzinfo=dt.timezone.utc)


class Sync(ClientsCase):
    def build(self):
        return sync.build(SLUG, root=self.root, now=NOW, registry_path=self.registry)

    def test_body_shape_follows_the_contract(self):
        s = self.build()
        self.assertEqual(list(s), ["brand", "snapshots", "pieces"])
        self.assertEqual(problems(s), [])
        self.assertEqual(s["brand"], {"slug": "acme", "name": "Acme", "status": "active", "business": "acme-app",
                                      "language": "en", "account_stage": "new", "timezone": "America/New_York",
                                      "cadence": {"per_week": 2, "days": ["Mon", "Thu"]}, "monthly_usd_cap": 50})
        self.assertEqual(list(s["snapshots"]), ["brain", "plan", "spend"])
        self.assertEqual(s["snapshots"]["brain"]["studio"], {"vault_folder": "Agency OS/Clients/Acme"})
        self.assertEqual(s["snapshots"]["spend"]["month"], "2026-10")

    def test_snapshots_hold_no_timestamp_so_a_rebuild_is_identical(self):
        later = sync.build(SLUG, root=self.root, now=NOW + dt.timedelta(hours=1), registry_path=self.registry)
        self.assertEqual(later["snapshots"], self.build()["snapshots"])

    def test_piece_joins_card_run_project_and_spend(self):
        p = self.build()["pieces"][0]
        self.assertEqual(list(p), list(body.PIECE_KEYS))
        self.assertEqual((p["post_id"], p["title"], p["funnel_stage"], p["format_family"]),
                         ("AC-2026-11-W1-01", "Title AC-2026-11-W1-01", "TOF", "motion"))
        self.assertEqual((p["slot"], p["hook_text"], p["script_score"], p["usd_spent"]),
                         ("2026-11-02T12:00:00-05:00", "second", 88, 1.25))
        self.assertEqual([(g["gate"], g["status"]) for g in p["gates"]], [("card:idea", "PASS"), ("G-SCRIPT", "PASS")])
        self.assertEqual((p["project"], p["studio_post_id"], p["content_external_key"]),
                         ("motion-studio/projects/acme-01", None, "AC-2026-11-W1-01"))

    def test_piece_without_run_or_project_and_the_unslotted_bank_card(self):
        _, second, bank = self.build()["pieces"]
        self.assertEqual((second["funnel_stage"], second["project"], second["script_score"], second["usd_spent"]),
                         ("BOF", None, None, None))
        self.assertEqual(second["hook_text"], "Here's the one test.")
        self.assertIsNone(bank["slot"])
        self.assertTrue(bank["notes"].startswith("Bank card (spare)"))

    def test_studio_post_id_only_when_the_run_has_another_id(self):
        e = {"card": {"post_id": "A-1", "status": "planned"}, "bank": False, "path": "x"}
        p = body.piece_block(e, None, None, None, {"post_id": "RUN-9", "gates": []}, {}, None)
        self.assertEqual(p["studio_post_id"], "RUN-9")

    def test_dry_run_calls_nothing_and_a_real_run_posts_to_clients_sync(self):
        calls = []
        call = lambda *a, **k: calls.append((a, k)) or {"pieces": 3, "snapshots_added": ["brain"], "removed": []}
        snap = self.build()
        with mock.patch.object(sync, "build", lambda slug, month=None: snap), mock.patch("builtins.print") as out:
            sync.cli([SLUG, "--dry-run"], call=call)
            self.assertEqual(calls, [])
            self.assertIn("dry run, nothing sent", out.call_args_list[0].args[0])
            sync.cli([SLUG], call=call)
            self.assertIn("sent: 3 live piece(s)", out.call_args_list[1].args[0])
        (args, kw), = calls
        self.assertEqual((args[0], args[1], kw), ("POST", "sync", {"api": "clients"}))
        self.assertIs(args[2], snap)

    def test_a_bad_body_stops_before_the_hub(self):
        snap = self.build()
        snap["pieces"][0]["status"] = "drafted"
        with mock.patch.object(sync, "build", lambda slug, month=None: snap), self.assertRaises(SystemExit) as e:
            sync.cli([SLUG], call=lambda *a, **k: self.fail("called the hub"))
        self.assertIn("pieces[0].status", str(e.exception))

    def test_report_lines(self):
        text = sync.report(self.build(), None)
        self.assertIn("pieces: 2 slotted + 1 unslotted (bank)", text)
        self.assertIn("funnel: BOF 1, TOF 1", text)
        self.assertIn("spend 2026-10: $1.25 of $50.00", text)


if __name__ == "__main__":
    unittest.main()
