"""Tests for intake/shape.py and slim.py: telling the two shapes apart, cleaning the slim row, O1's slim gate."""
import copy
import unittest

from intake import shape, slim
from intake.testbase import FIXTURE, IntakeCase, response, sample
import json


def slim_row() -> dict:
    return json.loads((FIXTURE.parent / "slim-intake.json").read_text())


class Shapes(unittest.TestCase):
    def test_slim_row_is_the_response_itself(self):
        r = slim_row()
        self.assertIs(shape.row_of(r), r)
        self.assertEqual(shape.kind(r), "slim")

    def test_old_response_takes_the_newest_row(self):
        self.assertEqual(shape.kind(shape.row_of(response())), "legacy")
        self.assertIsNone(shape.row_of({"intakes": []}))
        self.assertIsNone(shape.row_of({}))

    def test_a_slim_row_inside_intakes_also_works(self):
        self.assertEqual(shape.kind(shape.row_of({"intakes": [slim_row()]})), "slim")


class Normalize(IntakeCase):
    def test_cleans_fields_and_drops_blank_competitors(self):
        s = slim.normalize(slim_row())
        self.assertEqual(s["competitors"], ["Corner Loaf", "https://rival-bakery.example"])
        self.assertEqual(s["consents"], {"ai_people": False, "proof": True})
        self.assertEqual(s["docs"][0]["signed_url"], "https://storage.example/sign/brand-guide?t=abc")

    def test_wrong_types_stop(self):
        for k, v in (("competitors", "Corner Loaf"), ("docs", {}), ("consents", [])):
            bad = {**slim_row(), k: v}
            with self.assertRaisesRegex(SystemExit, "BAD_INTAKE"):
                slim.normalize(bad)
        bad = copy.deepcopy(slim_row())
        del bad["docs"][0]["name"]
        with self.assertRaisesRegex(SystemExit, "BAD_INTAKE"):
            slim.normalize(bad)

    def test_a_doc_with_a_null_signed_url_is_kept(self):
        row = copy.deepcopy(slim_row())
        row["docs"][0]["signed_url"] = None
        s = slim.normalize(row)
        self.assertEqual(len(s["docs"]), 2)
        self.assertIsNone(s["docs"][0]["signed_url"])

    def test_gate_ready_and_not(self):
        s = slim.normalize(slim_row())
        self.assertEqual(slim.gate(s, []), [])
        s["business_name"], s["website"], s["instagram"], s["docs"] = "", "", "", []
        s["consents"]["proof"] = None
        ids = [m["id"] for m in slim.gate(s, [])]
        self.assertEqual(ids, ["business_name", "sources", "consents.proof"])

    def test_gate_names_a_document_that_failed(self):
        s = slim.normalize(slim_row())
        bad = slim.gate(s, [{"name": "brand-guide.pdf", "error": "link expired"}])
        self.assertEqual(bad[0]["id"], "doc:brand-guide.pdf")
