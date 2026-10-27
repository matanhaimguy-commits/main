"""Tests for js_built.py: a client-rendered shell is flagged, with the evidence."""
import unittest

from testbase import doc
from page_facts.htmldoc import parse
from page_facts.js_built import check


class JsBuilt(unittest.TestCase):
    def test_a_vite_lovable_shell_is_flagged(self):
        c = check(doc("js_shell.html"))
        self.assertTrue(c["flagged"])
        self.assertEqual((c["body_text_chars"], c["mount_points"], c["bundle_scripts"]), (0, ["#root"], ["/assets/index-B7xQ2kLm.js"]))

    def test_a_page_with_text_is_not_flagged_even_with_a_root_div(self):
        self.assertFalse(check(doc("pixel_gtm_form.html"))["flagged"])
        self.assertFalse(check(parse('<div id="app"><p>' + "Real words here. " * 30 + '</p></div><script src="/assets/app-abc12345.js"></script>'))["flagged"])

    def test_a_thin_page_without_a_mount_point_or_bundle_is_not_flagged(self):
        self.assertFalse(check(parse('<body><img src="/coming-soon.jpg"><script src="/js/analytics.js"></script></body>'))["flagged"])
        self.assertTrue(check(parse('<app-root></app-root><script src="/main.4f3a9c2b1d.js"></script>'))["flagged"])


if __name__ == "__main__":
    unittest.main()
