"""Client Brain check. Run: python3 -m unittest discover -s growth-engine/tools/organic_os -p 'test_*.py'"""
import copy
import unittest

import organic_os as o
from organic_os.testbase import BRAIN, DEMAND, codes


class BrainTest(unittest.TestCase):
    def test_complete_enough_brain_has_no_blockers_but_lists_gaps(self):
        issues, gaps = o.brain_check(BRAIN, DEMAND)
        self.assertEqual(codes(issues, o.ERROR), [])
        fields = [g["field"] for g in gaps]
        for f in ("business_model.capacity", "demand_map", "contrarian_vault", "visual.ai_label", "baseline", "lead_magnets[TEST]"):
            self.assertIn(f, fields)

    def test_missing_offer_blocks(self):
        b = copy.deepcopy(BRAIN)
        b["offer"]["main_offer"] = "TBD"
        issues, _ = o.brain_check(b, DEMAND)
        self.assertIn("blocking", codes(issues, o.ERROR))


if __name__ == "__main__":
    unittest.main()
