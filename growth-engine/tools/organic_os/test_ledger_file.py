"""The spend ledger: atlas_usd column, old credit columns kept. Run: python3 -m unittest discover -s growth-engine/tools/organic_os -t growth-engine/tools"""
import csv
import tempfile
import unittest
from pathlib import Path

from organic_os import ledger_file, router, spend

OLD = ("date,post_id,format,tier,higgsfield_credits,elevenlabs_credits,minutes,note\n"
       "2026-10-15,SS-1,reel_quote_broll,C,26.75,708.0,45.0,old run\n")


class LedgerFileTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.p = Path(self.tmp.name) / "ledger.csv"

    def tearDown(self):
        self.tmp.cleanup()

    def rows(self):
        with self.p.open(newline="") as f:
            return list(csv.DictReader(f))

    def test_new_ledger_and_append(self):
        ledger_file.append_row(self.p, {"date": "2026-10-28", "post_id": "A", "format": "x", "atlas_usd": 1.5})
        ledger_file.append_row(self.p, {"date": "2026-10-29", "post_id": "B", "format": "x", "atlas_usd": 0.5})
        self.assertEqual(self.p.read_text().splitlines()[0], ",".join(ledger_file.HEADER))
        self.assertEqual([r["atlas_usd"] for r in self.rows()], ["1.5", "0.5"])

    def test_an_old_ledger_is_rewritten_once_and_keeps_its_credits(self):
        self.p.write_text(OLD)
        ledger_file.append_row(self.p, {"date": "2026-10-28", "post_id": "A", "format": "x", "atlas_usd": 2})
        rows = self.rows()
        self.assertEqual(rows[0]["higgsfield_credits"], "26.75")
        self.assertEqual(rows[0]["atlas_usd"], "")
        self.assertEqual(rows[1]["atlas_usd"], "2")
        sp = router.month_spend(rows, "2026-10")
        self.assertEqual((sp["usd"], sp["credits"], sp["elevenlabs"]), (2.0, 26.75, 708.0))
        self.assertEqual(sp["by_format"]["reel_quote_broll"]["credits"], 26.75)

    def test_unknown_columns_stop_the_write(self):
        self.p.write_text("date,post_id,format,cost\n")
        with self.assertRaises(ValueError):
            ledger_file.append_row(self.p, {"date": "2026-10-28"})

    def test_a_malformed_old_row_leaves_the_ledger_untouched(self):
        bad = OLD + "2026-10-16,SS-2,image_question,C,1.0,0,10.0,note,an extra field\n"
        self.p.write_text(bad)
        with self.assertRaises(ValueError):
            ledger_file.append_row(self.p, {"date": "2026-10-28", "post_id": "A", "format": "x", "atlas_usd": 2})
        self.assertEqual(self.p.read_text(), bad)
        self.assertEqual([x.name for x in self.p.parent.iterdir()], ["ledger.csv"])

    def test_heygen_credits_column_and_cap(self):
        self.p.write_text(OLD)
        ledger_file.append_row(self.p, {"date": "2026-10-30", "post_id": "T", "format": "x", "atlas_usd": 1,
                                        "heygen_credits": 120})
        rows = self.rows()
        self.assertEqual((rows[0]["heygen_credits"], rows[1]["heygen_credits"]), ("", "120"))
        self.assertEqual(router.month_spend(rows, "2026-10")["heygen"], 120.0)
        self.assertEqual(spend.heygen_cap({"package": {"monthly_heygen_credit_cap": 900}}), 900)
        for pkg in ({}, {"monthly_heygen_credit_cap": None}, {"monthly_heygen_credit_cap": True}):
            self.assertIsNone(spend.heygen_cap({"package": pkg}))

    def test_usd_cap(self):
        self.assertEqual(router.usd_cap({"package": {"monthly_usd_cap": 40}}), 40)
        for pkg in ({}, {"monthly_usd_cap": None}, {"monthly_usd_cap": True}, {"monthly_credit_cap": 1300}):
            self.assertIsNone(router.usd_cap({"package": pkg}))


if __name__ == "__main__":
    unittest.main()
