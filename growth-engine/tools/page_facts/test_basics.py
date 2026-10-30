"""Tests for basics.py: title, description, every H1, canonical, lang, viewport and og: tags."""
import unittest

from testbase import doc
from page_facts.basics import read


class Basics(unittest.TestCase):
    def test_reads_what_the_html_says(self):
        b = read(doc("pixel_gtm_form.html"))
        self.assertEqual(b["title"], "Acme Plumbing | Same-day repairs")
        self.assertEqual(b["meta_description"], "Leak? We fix it today. Licensed plumbers in Tel Aviv.")
        self.assertEqual(b["h1"], ["Leaks fixed today", "Book a same-day visit"])
        self.assertEqual((b["canonical"], b["lang"]), ("https://acme-plumbing.example/", "en"))
        self.assertEqual(b["viewport"], "width=device-width, initial-scale=1")
        self.assertEqual(b["og"], {"og:title": "Acme Plumbing", "og:image": "https://acme-plumbing.example/og.jpg"})

    def test_missing_is_none_never_a_guess(self):
        b = read(doc("facebook_text_only.html"))
        self.assertEqual((b["meta_description"], b["canonical"], b["lang"], b["viewport"], b["og"]), (None, None, None, None, {}))
        self.assertEqual(b["h1"], ["Fresh bread every morning"])


if __name__ == "__main__":
    unittest.main()
