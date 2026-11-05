"""Tests for site_files.py: robots.txt and the sitemap, fetched from the page's own site only."""
import unittest

from testbase import SITE, stub_fetch
from page_facts.errors import Unreachable
from page_facts.site_files import read

INDEX = (f"<sitemapindex><sitemap><loc>{SITE}/a.xml</loc></sitemap><sitemap><loc>{SITE}/b.xml</loc></sitemap>"
         "<sitemap><loc>https://cdn.other.example/c.xml</loc></sitemap></sitemapindex>")


def urlset(n: int) -> str:
    return "<urlset>" + "<url><loc>x</loc></url>" * n + "</urlset>"


class SiteFiles(unittest.TestCase):
    def test_robots_names_an_index_and_its_same_site_children_are_added_up(self):
        fetch = stub_fetch({f"{SITE}/robots.txt": (200, f"User-agent: *\nDisallow:\nSitemap: {SITE}/index.xml\n"),
                            f"{SITE}/index.xml": (200, INDEX), f"{SITE}/a.xml": (200, urlset(3)), f"{SITE}/b.xml": (200, urlset(2))})
        got = read(f"{SITE}/page", fetch)
        self.assertEqual((got["robots_txt"]["present"], got["robots_txt"]["sitemaps"]), (True, [f"{SITE}/index.xml"]))
        s = got["sitemap"]
        self.assertEqual((s["url"], s["kind"], s["children"], s["children_read"], s["url_count"]),
                         (f"{SITE}/index.xml", "sitemapindex", 3, 2, 5))

    def test_no_robots_falls_back_to_sitemap_xml(self):
        got = read(SITE + "/", stub_fetch({f"{SITE}/sitemap.xml": (200, urlset(4))}))
        self.assertEqual((got["robots_txt"]["present"], got["robots_txt"]["status"]), (False, 404))
        self.assertEqual((got["sitemap"]["url"], got["sitemap"]["present"], got["sitemap"]["url_count"]),
                         (f"{SITE}/sitemap.xml", True, 4))

    def test_a_js_site_answering_html_everywhere_has_neither(self):
        shell = '<!doctype html><html><div id="root"></div></html>'
        got = read(SITE, stub_fetch({f"{SITE}/robots.txt": (200, shell), f"{SITE}/sitemap.xml": (200, shell)}))
        self.assertEqual((got["robots_txt"]["present"], got["robots_txt"]["note"]),
                         (False, "answers with an HTML page, not a robots.txt file"))
        self.assertEqual((got["sitemap"]["present"], got["sitemap"]["note"]), (False, "answers, but not with a sitemap"))

    def test_another_hosts_sitemap_is_not_fetched_and_a_dead_one_is_noted(self):
        fetch = stub_fetch({f"{SITE}/robots.txt": (200, "Sitemap: http://169.254.169.254/latest\n"),
                            f"{SITE}/sitemap.xml": Unreachable("acme.example", "no usable answer within 20s (TimeoutError)")})
        s = read(SITE, fetch)["sitemap"]
        self.assertEqual((s["url"], s["present"], s["status"]), (f"{SITE}/sitemap.xml", False, None))
        self.assertIn("TimeoutError", s["note"])


if __name__ == "__main__":
    unittest.main()
