"""Tests for clients/slot.py and clients/counts.py."""
import unittest

from clients.counts import counts
from clients.slot import slot


class SlotCounts(unittest.TestCase):
    def test_slot_carries_the_offset_of_its_date(self):
        self.assertEqual(slot("2026-11-02 12:00", "America/New_York")["at"], "2026-11-02T12:00:00-05:00")
        self.assertEqual(slot("2026-10-30 12:00", "America/New_York")["at"], "2026-10-30T12:00:00-04:00")
        self.assertIsNone(slot("someday", "America/New_York")["at"])

    def test_counts_leave_the_bank_apart(self):
        ps = [{"bank": False, "status": "planned", "funnel_stage": "TOF"},
              {"bank": False, "status": "produced", "funnel_stage": None},
              {"bank": True, "status": "planned", "funnel_stage": "MOF"}]
        self.assertEqual(counts(ps), {"pieces": 2, "bank": 1, "status": {"planned": 1, "produced": 1},
                                      "funnel_stage": {"TOF": 1, "none": 1}})


if __name__ == "__main__":
    unittest.main()
