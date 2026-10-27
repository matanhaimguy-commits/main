"""Tests for say_site.py: robots.txt and sitemap lines."""
import unittest

import testbase  # noqa: F401
from page_facts.say_site import robots_line, sitemap_line


class SaySite(unittest.TestCase):
    def test_robots_lines(self):
        self.assertEqual(robots_line({"present": True, "sitemaps": ["a"], "blocks_all": True, "status": 200}),
                         "- robots.txt: present, declares 1 sitemap; it blocks every crawler (Disallow: / for User-agent: *)")
        self.assertEqual(robots_line({"present": False, "status": 404}), "- robots.txt: missing (HTTP 404)")

    def test_sitemap_lines(self):
        self.assertEqual(sitemap_line({"url": "u", "present": True, "kind": "urlset", "url_count": 42}), "- Sitemap u: present, 42 URLs")
        self.assertEqual(sitemap_line({"url": "u", "present": True, "kind": "sitemapindex", "url_count": 5, "children": 3, "children_read": 2}),
                         "- Sitemap u: an index of 3 sitemaps; 5 URLs in the 2 read")
        self.assertEqual(sitemap_line({"url": "u", "present": False, "status": 200, "note": "gzipped; not read"}),
                         "- Sitemap u: not usable (gzipped; not read)")


if __name__ == "__main__":
    unittest.main()
