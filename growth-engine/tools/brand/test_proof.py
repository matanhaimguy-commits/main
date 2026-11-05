"""Tests for brand/proof.py."""
import unittest

from brand import proof

SRC = "Matan (Brand card, 2026-10-29)"


class Proof(unittest.TestCase):
    def test_strings_and_objects_become_items_with_pending_by_default(self):
        out = proof.items(["500 loaves a week", {"text": "Five stars", "type": "review", "permission": "yes", "date": "2026-09-01"}], SRC, "2026-10-29")
        self.assertEqual(out[0], {"type": "claim", "text": "500 loaves a week", "source": SRC, "permission": "pending", "date": "2026-10-29"})
        self.assertEqual((out[1]["type"], out[1]["permission"], out[1]["date"]), ("review", "yes", "2026-09-01"))

    def test_bad_entries(self):
        for bad in ([], "text", [{"text": ""}], [{"text": "x", "permission": "maybe"}], [3]):
            with self.assertRaises(ValueError):
                proof.items(bad, SRC, "2026-10-29")

    def test_merge_keeps_document_proof_and_replaces_earlier_card_proof(self):
        old = [{"id": "P-01", "type": "claim", "text": "from doc", "source": "brand-guide.pdf p.3", "permission": "yes"},
               {"id": "P-02", "type": "claim", "text": "old card line", "source": "Matan (Brand card, 2026-10-01)", "permission": "yes"}]
        new = proof.items(["from doc", "new card line"], SRC, "2026-10-29")
        out = proof.merge(old, new, "Matan (Brand card")
        self.assertEqual([(p["id"], p["text"]) for p in out], [("P-01", "from doc"), ("P-02", "new card line")])

    def test_same_card_again_changes_nothing_but_a_permission_change_is_taken(self):
        first = proof.merge([], proof.items(["a", "b"], SRC, "2026-10-29"), "Matan (Brand card")
        again = proof.merge(first, proof.items(["a", "b"], "Matan (Brand card, 2026-11-05)", "2026-11-05"), "Matan (Brand card")
        self.assertEqual(again, first)
        changed = proof.merge(first, proof.items([{"text": "a", "permission": "yes"}, "b"], SRC, "2026-11-05"), "Matan (Brand card")
        self.assertEqual([p["permission"] for p in changed], ["yes", "pending"])
        self.assertEqual(changed[0]["date"], "2026-10-29")
