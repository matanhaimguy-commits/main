"""Tests for robots.py: declared sitemaps, blocking every crawler, and HTML pretending to be robots.txt."""
import unittest

import testbase  # noqa: F401
from page_facts.robots import looks_like_html, parse


class Robots(unittest.TestCase):
    def test_sitemaps_and_an_open_site(self):
        r = parse("# hello\nUser-agent: *\nDisallow: /admin  # private\nAllow: /\n"
                  "Sitemap: https://acme.example/sitemap_index.xml\nsitemap:https://acme.example/news.xml\n")
        self.assertEqual(r, {"sitemaps": ["https://acme.example/sitemap_index.xml", "https://acme.example/news.xml"],
                             "blocks_all": False})

    def test_blocks_all_only_for_the_star_group(self):
        self.assertFalse(parse("User-agent: Googlebot\nDisallow: /\n\nUser-agent: *\nDisallow:\n")["blocks_all"])
        self.assertTrue(parse("User-agent: Googlebot\nUser-agent: *\nDisallow: /\n")["blocks_all"])
        self.assertFalse(parse("User-agent: *\nDisallow: /tmp\nUser-agent: Bingbot\nDisallow: /\n")["blocks_all"])

    def test_html_is_not_a_robots_file(self):
        self.assertTrue(looks_like_html('\n<!doctype html><html><div id="root"></div>'))
        self.assertFalse(looks_like_html("User-agent: *\nDisallow:"))


if __name__ == "__main__":
    unittest.main()
