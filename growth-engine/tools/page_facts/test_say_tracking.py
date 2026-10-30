"""Tests for say_tracking.py: the tracker lines."""
import unittest

import testbase  # noqa: F401
from page_facts.say_tracking import line

STATIC = {"mode": "static"}


def tracker(name, ids=(), seen=("html",), evidence="x"):
    return {"name": name, "found": bool(seen), "ids": list(ids), "evidence": evidence if seen else None, "seen_in": list(seen)}


class SayTracking(unittest.TestCase):
    def test_found_lines_name_the_ids_and_the_code(self):
        self.assertEqual(line(tracker("GA4", ["G-A1B2C3D4", "G-Z9Y8X7W6"], evidence="gtag/js?id=G-A1B2C3D4"), STATIC),
                         "- GA4: found (measurement IDs G-A1B2C3D4, G-Z9Y8X7W6) in the page's HTML; the code: `gtag/js?id=G-A1B2C3D4`")
        self.assertEqual(line(tracker("Hotjar", seen=("rendered", "requests"), evidence="a`b"), {"mode": "rendered"}),
                         "- Hotjar: found (no site ID in the code) in the rendered page and the network requests; the code: `a'b`")

    def test_not_found_says_where_it_looked(self):
        self.assertEqual(line(tracker("TikTok Pixel", seen=()), STATIC), "- TikTok Pixel: not found in the page's HTML")


if __name__ == "__main__":
    unittest.main()
