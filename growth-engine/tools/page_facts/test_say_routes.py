"""Tests for say_routes.py: route lines in kind order, and the kinds that are missing."""
import unittest

import testbase  # noqa: F401
from page_facts.say_routes import section


class SayRoutes(unittest.TestCase):
    def test_lines_and_missing_kinds(self):
        routes = [{"kind": "messaging", "service": "WhatsApp", "url": "https://wa.me/1", "where": "footer", "via": "link", "text": "Chat"},
                  {"kind": "booking", "service": "Calendly", "url": "https://calendly.com/a", "where": "body", "via": "iframe"}]
        self.assertEqual(section({"mode": "static", "routes": routes}), [
            "## Contact and booking routes",
            "- Calendly (body, iframe): https://calendly.com/a",
            '- WhatsApp (footer, link, "Chat"): https://wa.me/1',
            "- Not in the page's HTML: Typeform/Tally form; phone or email link."])

    def test_nothing_found(self):
        lines = section({"mode": "static", "routes": []})
        self.assertEqual(len(lines), 2)
        self.assertTrue(lines[1].startswith("- Not in the page's HTML: booking link; "))


if __name__ == "__main__":
    unittest.main()
