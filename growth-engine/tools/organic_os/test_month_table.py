"""organic.py calendar: the month table. Run: python3 -m unittest discover -s growth-engine/tools/organic_os -t growth-engine/tools"""
import unittest

from organic_os.month_table import COLUMNS, markdown, rows
from organic_os.testbase import card

CARDS = [
    ("c/cards/W2/b.yaml", card(post_id="AC-2026-11-W2-01", slot="2026-11-09 12:00", job="trust", funnel_stage=None, status="scripted",
                                 narrow_product="Second: why it matters", project="motion-studio/projects/acme-02")),
    ("c/cards/W1/a.yaml", card(post_id="AC-2026-11-W1-01", slot="2026-11-02 19:30", funnel_stage="TOF")),
    ("c/cards/bank/z.yaml", card(post_id="AC-2026-11-W9-01", slot="2026-11-30 12:00")),
    ("c/cards/W5/old.yaml", card(post_id="AC-2026-10-W5-01", slot="2026-10-30 12:00")),
]


class MonthTableTest(unittest.TestCase):
    def test_rows_are_the_month_in_slot_order_without_the_bank(self):
        got = rows(CARDS, "2026-11")
        self.assertEqual([r["date"] for r in got], ["Mon 02 Nov", "Mon 09 Nov"])
        self.assertEqual(got[1], {"date": "Mon 09 Nov", "time": "12:00", "funnel": "MOF", "job": "trust",
                                  "format": "reel_quote_broll", "status": "scripted", "title": "Second",
                                  "project": "acme-02"})

    def test_bank_on_request(self):
        self.assertEqual(len(rows(CARDS, "2026-11", bank=True)), 3)

    def test_markdown_has_a_header_and_one_line_per_row(self):
        lines = markdown(rows(CARDS, "2026-11")).splitlines()
        self.assertEqual(lines[0], "| " + " | ".join(COLUMNS) + " |")
        self.assertEqual(len(lines), 4)
        self.assertIn("| Mon 02 Nov | 19:30 | TOF | reach |", lines[2])


if __name__ == "__main__":
    unittest.main()
