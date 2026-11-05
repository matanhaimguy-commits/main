"""Tests for clients/cards.py."""
import unittest

from clients import cards
from clients.testbase import SLUG, ClientsCase


class Cards(ClientsCase):
    def test_cards_in_slot_order_with_the_bank_marked(self):
        got = cards.load(self.root, SLUG)
        self.assertEqual([(c["card"]["post_id"], c["bank"]) for c in got],
                         [("AC-2026-11-W1-01", False), ("AC-2026-11-W1-02", False), ("AC-2026-11-W9-01", True)])
        self.assertEqual(got[0]["path"], "clients/acme/cards/W1/AC-01.yaml")

    def test_a_yaml_that_is_not_a_card_is_skipped(self):
        self.write(self.root / "clients" / SLUG / "cards" / "notes.yaml", "just: notes\n")
        self.assertEqual(len(cards.load(self.root, SLUG)), 3)


if __name__ == "__main__":
    unittest.main()
