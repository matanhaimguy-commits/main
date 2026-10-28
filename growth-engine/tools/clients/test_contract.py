"""Tests for clients/contract.py, against the example in C1's docs/client-os.md (agent-start-spark, claude/client-os-c1)."""
import copy
import unittest

from clients.contract import problems

DOC_EXAMPLE = {
    "brand": {"slug": "maya-quilts", "name": "Maya Quilts", "status": "active", "business": "acme", "language": "en",
              "account_stage": "warm-up", "timezone": "Europe/Tirane",
              "cadence": {"per_week": 5, "formats": {"reel": 4, "carousel": 1}}, "monthly_usd_cap": 150},
    "snapshots": {"brain": {"offer": "Custom memory quilts from old clothes", "icp": "Mothers 35-55 keeping a child's clothes"},
                  "plan": {"month": "2026-11", "pillars": ["memory", "craft", "proof"]}},
    "pieces": [
        {"post_id": "MQ-EN-01", "status": "produced", "slot": "2099-11-03T18:00:00+02:00", "funnel_stage": "TOF",
         "job": "stop the scroll", "belief": "old clothes can become an heirloom", "format": "reel_song",
         "format_family": "song", "title": "The onesie quilt", "hook_text": "She kept every onesie for 18 years.",
         "hook_grades": [{"hook": "She kept every onesie for 18 years.", "grade": "A", "by": "hook-lab"}],
         "script_score": 86, "gates": [{"gate": "G-SCRIPT", "status": "PASS", "score": 86}], "project": "november-launch",
         "studio_post_id": None, "content_external_key": "acme:MQ-EN-01", "usd_spent": 4.2, "notes": None},
        {"post_id": "MQ-EN-02", "status": "planned", "slot": "2099-11-05T18:00:00+02:00", "funnel_stage": "BOF",
         "title": "How to order"}]}


class Contract(unittest.TestCase):
    def changed(self, fn):
        b = copy.deepcopy(DOC_EXAMPLE)
        fn(b)
        return problems(b)

    def test_the_doc_example_is_valid(self):
        self.assertEqual(problems(DOC_EXAMPLE), [])
        self.assertEqual(self.changed(lambda b: b.pop("pieces")), [])

    def test_brand_rules(self):
        self.assertIn("brand.slug", self.changed(lambda b: b["brand"].update(slug="Maya Quilts"))[0])
        self.assertIn("brand.status", self.changed(lambda b: b["brand"].update(status="archived"))[0])
        self.assertIn("not in the contract", self.changed(lambda b: b["brand"].update(vault_folder="x"))[0])

    def test_snapshot_rules(self):
        self.assertIn("kinds are", self.changed(lambda b: b["snapshots"].update(counts={}))[0])
        self.assertIn("a JSON object", self.changed(lambda b: b["snapshots"].update(plan=[1]))[0])
        self.assertIn("over 500 KB", self.changed(lambda b: b["snapshots"].update(brain={"x": "y" * 500_001}))[0])

    def test_piece_rules(self):
        self.assertIn("twice", self.changed(lambda b: b["pieces"][1].update(post_id="MQ-EN-01"))[0])
        self.assertIn("slot", self.changed(lambda b: b["pieces"][0].update(slot="2099-11-03 18:00"))[0])
        self.assertIn("funnel_stage", self.changed(lambda b: b["pieces"][0].update(funnel_stage="TOP"))[0])
        self.assertIn("status", self.changed(lambda b: b["pieces"][0].update(status="drafted"))[0])
        self.assertIn("not in the contract", self.changed(lambda b: b["pieces"][0].update(bank=True))[0])
        self.assertEqual(self.changed(lambda b: b["pieces"][0].update(slot=None, funnel_stage=None)), [])


if __name__ == "__main__":
    unittest.main()
