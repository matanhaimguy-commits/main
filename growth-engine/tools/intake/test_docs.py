"""Tests for intake/docs.py: safe names and downloading with a fake fetcher (no network)."""
import json
import unittest
import urllib.error

from intake import docs
from intake.testbase import IntakeCase


class Names(unittest.TestCase):
    def test_no_path_parts_and_unique(self):
        taken = set()
        self.assertEqual(docs.safe_name("../../etc/passwd", taken), "passwd")
        self.assertEqual(docs.safe_name("a/b/guide.pdf", taken), "guide.pdf")
        self.assertEqual(docs.safe_name("GUIDE.pdf", taken), "GUIDE-2.pdf")
        self.assertEqual(docs.safe_name("", taken), "document")


class Download(IntakeCase):
    def doc(self, name, size=None, url=None):
        return {"name": name, "mime": "application/pdf", "size": size, "signed_url": url or f"https://s.example/{name}?sig=SECRET"}

    def test_saves_files_and_manifest_has_no_signed_url(self):
        out = docs.download([self.doc("a.pdf", 5)], self.root / "foundation", get=lambda u: b"hello")
        self.assertEqual((self.root / "foundation" / "a.pdf").read_bytes(), b"hello")
        self.assertEqual(out[0]["error"], None)
        m = (self.root / "foundation" / "manifest.json").read_text()
        self.assertNotIn("SECRET", m)
        self.assertEqual(json.loads(m)[0]["bytes"], 5)

    def test_an_expired_link_is_reported_and_the_rest_are_saved(self):
        def get(url):
            if "bad" in url:
                raise urllib.error.HTTPError(url, 403, "Forbidden", {}, None)
            return b"ok"
        out = docs.download([self.doc("bad.pdf"), self.doc("good.pdf")], self.root / "f", get=get)
        self.assertIn("could not download", out[0]["error"])
        self.assertIsNone(out[0]["saved_as"])
        self.assertTrue((self.root / "f" / "good.pdf").exists())

    def test_an_unsigned_doc_is_skipped_with_an_error_and_the_others_are_saved(self):
        unsigned = {"name": "x.pdf", "mime": None, "size": 3, "signed_url": None}
        out = docs.download([unsigned, self.doc("good.pdf")], self.root / "f", get=lambda u: self.assertNotIn("x.pdf", u) or b"ok")
        self.assertIn("no signed link", out[0]["error"])
        self.assertIsNone(out[0]["saved_as"])
        self.assertTrue((self.root / "f" / "good.pdf").exists())

    def test_a_size_mismatch_is_flagged_but_kept(self):
        out = docs.download([self.doc("a.pdf", 99)], self.root / "f", get=lambda u: b"abc")
        self.assertIn("the intake said 99", out[0]["error"])
        self.assertTrue((self.root / "f" / "a.pdf").exists())

    def test_two_documents_with_one_name_do_not_overwrite(self):
        docs.download([self.doc("a.pdf"), self.doc("a.pdf")], self.root / "f", get=lambda u: u.encode())
        self.assertEqual(sorted(p.name for p in (self.root / "f").glob("a*.pdf")), ["a-2.pdf", "a.pdf"])
