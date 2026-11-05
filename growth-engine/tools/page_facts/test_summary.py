"""Tests for summary.py: the markdown for the leak scorecard, with its caveats first."""
import unittest
from datetime import datetime, timezone

from testbase import SITE, fixture, stub_fetch
from page_facts.facts import collect
from page_facts.summary import markdown

CLOCK = lambda: datetime(2026, 10, 27, 18, 5, tzinfo=timezone.utc)  # noqa: E731


def summary_of(name: str, **kw) -> str:
    return markdown(collect(SITE, fetch=stub_fetch({SITE: (200, fixture(name))}), clock=CLOCK, **kw))


class Summary(unittest.TestCase):
    def test_pixel_page(self):
        md = summary_of("pixel_gtm_form.html")
        self.assertTrue(md.startswith("# Page facts: acme.example\nChecked https://acme.example on 2026-10-27 18:05:00 UTC"))
        self.assertIn("- Meta Pixel: found (id 123456789012345) in the page's HTML; the code: `", md)
        self.assertIn("- Google Tag Manager: found (container GTM-ABC1234)", md)
        self.assertIn("- GA4: not found in the page's HTML", md)
        self.assertNotIn("Incomplete", md)
        for word in ("score", "grade", "/10", "%"):
            self.assertNotIn(word, md.lower())

    def test_facebook_in_text_is_reported_not_found(self):
        self.assertIn("- Meta Pixel: not found in the page's HTML", summary_of("facebook_text_only.html"))

    def test_js_shell_carries_the_caveat_first(self):
        md = summary_of("js_shell.html")
        caveat = md.split("\n\n")[1]
        self.assertTrue(caveat.startswith("> **Incomplete:** the static HTML is a JavaScript-built shell (0 characters of text; #root, /assets/index-B7xQ2kLm.js)"))
        self.assertIn("--render", caveat)

    def test_rendered_wording(self):
        render = lambda url: {"html": fixture("js_shell.html"), "requests": [], "final_url": url, "status": 200, "idle": False}  # noqa: E731
        md = summary_of("js_shell.html", render=render)
        self.assertIn("the facts below come from the rendered page and its network requests", md)
        self.assertIn("never went quiet", md)
        self.assertIn("- Hotjar: not found in the page's HTML, the rendered page or its network requests", md)


if __name__ == "__main__":
    unittest.main()
