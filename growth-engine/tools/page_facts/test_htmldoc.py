"""Tests for htmldoc.py: one pass over the HTML into elements, scripts and visible text."""
import unittest

import testbase  # noqa: F401  (puts growth-engine/tools on sys.path)
from page_facts.htmldoc import parse


class HtmlDoc(unittest.TestCase):
    def test_regions_follow_header_footer_role_and_id(self):
        d = parse('<header><a href="/a">A</a></header><div role="contentinfo"><a href="/b">B</a></div>'
                  '<div id="header"><span><a href="/c">C</a></span></div><p><a href="/d">D</a></p><footer><a href="/e">E</a></footer>')
        self.assertEqual([(a["attrs"]["href"], a["where"]) for a in d.find("a")],
                         [("/a", "header"), ("/b", "footer"), ("/c", "header"), ("/d", "body"), ("/e", "footer")])

    def test_fields_know_their_form_and_scripts_keep_their_bodies(self):
        d = parse('<input name="loose"><form><input name="a"></form><form><textarea name="b"></textarea></form>'
                  '<script src="/x.js"></script><script>var a = "<b>not a tag</b>";</script>')
        self.assertEqual([(el["attrs"]["name"], el["form"]) for el in d.find("input", "textarea")],
                         [("loose", None), ("a", 0), ("b", 1)])
        self.assertEqual([s["body"] for s in d.scripts], ["", 'var a = "<b>not a tag</b>";'])
        self.assertEqual(d.find("b"), [])

    def test_visible_text_skips_code_title_and_comments(self):
        d = parse("<title>T</title><style>p{}</style><p>Hello <!-- hidden --> <b>world</b></p>"
                  "<noscript>enable JS</noscript><template><p>later</p></template><script>x()</script>")
        self.assertEqual(d.text, "Hello world")
        self.assertEqual(d.find("title")[0]["text"], "T")

    def test_captured_text_includes_nested_tags_and_bad_html_does_not_break(self):
        d = parse("<h1>Book a <em>same-day</em>\n visit</h1></div></span><a href='/x'>Go <b>now")
        self.assertEqual(d.find("h1")[0]["text"], "Book a same-day visit")
        self.assertEqual(d.find("a")[0]["text"], "Go now")


if __name__ == "__main__":
    unittest.main()
