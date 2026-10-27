"""Tests for sitemap.py: URL counts, sitemap indexes, and text that is not a sitemap."""
import unittest

import testbase  # noqa: F401
from page_facts.sitemap import parse

URLSET = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">
<url><loc>https://acme.example/</loc><image:image><image:loc>https://acme.example/a.jpg</image:loc></image:image></url>
<url>
  <loc>https://acme.example/services</loc>
</url>
<url><loc>https://acme.example/contact</loc></url>
</urlset>"""


class Sitemap(unittest.TestCase):
    def test_counts_urls(self):
        self.assertEqual(parse(URLSET), {"kind": "urlset", "url_count": 3, "children": []})
        self.assertEqual(parse('<ns:urlset xmlns:ns="x"><ns:url><ns:loc>a</ns:loc></ns:url></ns:urlset>')["url_count"], 1)

    def test_an_index_lists_its_children(self):
        text = ("<sitemapindex><sitemap><loc> https://acme.example/post-sitemap.xml </loc></sitemap>"
                "<sitemap><loc>https://acme.example/page-sitemap.xml?a=1&amp;b=2</loc></sitemap></sitemapindex>")
        self.assertEqual(parse(text), {"kind": "sitemapindex", "url_count": None,
                                       "children": ["https://acme.example/post-sitemap.xml", "https://acme.example/page-sitemap.xml?a=1&b=2"]})

    def test_not_a_sitemap(self):
        self.assertEqual(parse("<!doctype html><html><body>Not found</body></html>")["kind"], None)


if __name__ == "__main__":
    unittest.main()
