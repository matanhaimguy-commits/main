"""Tests for braindraft/sources.py and finish.py: a source or 'unknown: <what>' on every field; O2 queued only then."""
import json
import unittest

from brainio.testbase import BrainCase
from braindraft import cli, finish, sources


class Sources(BrainCase):
    def test_the_template_passes_because_every_field_says_what_is_missing(self):
        probs = [p["path"] for p in sources.problems(self.brain())]
        self.assertEqual(probs, ["client", "constraints.cannot_say", "visual.face"])  # "_template" and "faceless" have no source; [] says nothing

    def test_a_filled_field_needs_a_source(self):
        b = self.brain()
        b["offer"]["main_offer"] = "Bread subscription"
        self.assertIn({"path": "offer.main_offer", "problem": "filled but no source in field_sources"}, sources.problems(b))
        b["field_sources"] = {"offer.main_offer": "https://sample-bakery.example/subscribe"}
        self.assertNotIn("offer.main_offer", [p["path"] for p in sources.problems(b)])

    def test_a_bare_unknown_is_not_enough(self):
        b = self.brain()
        b["offer"]["next_step"] = "unknown"
        self.assertIn("offer.next_step", [p["path"] for p in sources.problems(b)])

    def test_avatar_fields_and_proof_lines_are_checked(self):
        b = self.brain()
        b["avatars"][0]["situation"] = "Busy families"
        b["proof_bank"] = [{"id": "P-01", "type": "claim", "text": "x", "source": " ", "permission": "pending"}]
        paths = [p["path"] for p in sources.problems(b)]
        self.assertIn("avatars[0].situation", paths)
        self.assertIn("proof_bank[0]", paths)

    def test_optional_fields_may_be_absent(self):
        b = self.brain()
        del b["market"]["city"]
        self.assertNotIn("market.city", [p["path"] for p in sources.problems(b)])


class Finish(BrainCase):
    def good(self):
        b = self.brain()
        b["client"] = "Sample Bakery"
        b["constraints"]["cannot_say"] = ["unknown: nothing found in the docs; ask Matan"]
        b["field_sources"] = {"client": "brand-guide.pdf p.1", "visual.face": "client intake: consent, no AI-made people"}
        return b

    def test_pass_queues_o2(self):
        errs, q = finish.check(self.slug, self.good(), self.root, "2026-10-29")
        self.assertEqual(errs, [])
        data = json.loads(q.read_text())
        self.assertEqual((data["status"], data["queued_at"]), ("queued", "2026-10-29"))

    def test_fail_queues_nothing(self):
        errs, q = finish.check(self.slug, self.brain(), self.root)
        self.assertTrue(errs)
        self.assertIsNone(q)
        self.assertFalse((self.dir / "research" / "o2-queue.json").exists())

    def test_schema_errors_also_fail(self):
        b = self.good()
        b["package"]["monthly_usd_cap"] = -1
        errs, q = finish.check(self.slug, b, self.root)
        self.assertTrue(any("monthly_usd_cap" in e for e in errs))
        self.assertIsNone(q)

    def test_cli_seed_then_checklist_then_check(self):
        (self.dir / "intake").mkdir(exist_ok=True)
        from intake.test_slim import slim_row
        from intake import slim
        s = {k: v for k, v in slim.normalize(slim_row()).items() if k != "docs"}
        (self.dir / "intake" / "slim.json").write_text(json.dumps(s))
        self.assertEqual(cli.run("seed", self.slug, self.root), 0)
        self.assertEqual(self.brain()["client"], "Sample Bakery")
        self.assertEqual(json.loads((self.dir / "research" / "seeds.json").read_text())["website"], "https://sample-bakery.example")
        self.assertEqual(cli.run("checklist", self.slug, self.root), 0)

    def test_seed_without_an_intake_stops(self):
        (self.dir / "intake").mkdir(exist_ok=True)
        with self.assertRaisesRegex(SystemExit, "NO_INTAKE"):
            cli.run("seed", self.slug, self.root)
