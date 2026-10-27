"""Tests for facts.py: the assembled JSON object, static and rendered, and pages that are not pages."""
import json
import unittest
from datetime import datetime, timezone

from testbase import SITE, fixture, stub_fetch
from page_facts.errors import PageError
from page_facts.facts import collect
from page_facts.fetch import Page

CLOCK = lambda: datetime(2026, 10, 27, 18, 5, tzinfo=timezone.utc)  # noqa: E731


class Facts(unittest.TestCase):
    def test_static_facts_have_every_section(self):
        f = collect(SITE, fetch=stub_fetch({SITE: (200, fixture("pixel_gtm_form.html"))}), clock=CLOCK)
        self.assertEqual(list(f), ["url", "final_url", "status", "mode", "checked_at", "truncated", "js_built", "trackers",
                                   "forms", "routes", "basics", "jsonld", "robots_txt", "sitemap"])
        self.assertEqual((f["mode"], f["checked_at"], f["js_built"]["flagged"]), ("static", "2026-10-27T18:05:00Z", False))
        self.assertEqual([t["name"] for t in f["trackers"] if t["found"]], ["Meta Pixel", "Google Tag Manager"])
        self.assertEqual(len(f["forms"]), 2)
        self.assertEqual([r["service"] for r in f["routes"]], ["Email"])
        json.dumps(f)

    def test_rendered_mode_reads_the_rendered_page_and_its_requests(self):
        def render(url):
            return {"html": fixture("whatsapp_calendly.html"), "final_url": url, "status": 200, "idle": True,
                    "requests": ["https://connect.facebook.net/en_US/fbevents.js", "https://www.facebook.com/tr/?id=555666777888999&ev=PageView"]}
        f = collect(SITE, fetch=stub_fetch({SITE: (200, fixture("js_shell.html"))}), render=render, clock=CLOCK)
        pixel = f["trackers"][0]
        self.assertEqual((pixel["found"], pixel["ids"], pixel["seen_in"]), (True, ["555666777888999"], ["requests"]))
        self.assertTrue(f["js_built"]["flagged"])
        self.assertEqual(f["basics"]["title"], "Dana Lash Studio")
        self.assertEqual((f["mode"], f["rendered"]), ("rendered", {"requests_seen": 2, "network_idle": True}))

    def test_an_error_page_or_a_pdf_is_not_read(self):
        with self.assertRaises(PageError) as e:
            collect(SITE, fetch=stub_fetch({SITE: (403, "Attention required")}))
        self.assertTrue(str(e.exception).startswith("PAGE_HTTP_403"))
        pdf = lambda url: Page(url, url, 200, "application/pdf", "%PDF-1.7", False)  # noqa: E731
        with self.assertRaises(PageError) as e:
            collect(SITE, fetch=pdf)
        self.assertTrue(str(e.exception).startswith("NOT_HTML"))


if __name__ == "__main__":
    unittest.main()
