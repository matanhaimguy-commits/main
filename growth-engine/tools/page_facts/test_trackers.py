"""Tests for trackers.py and signatures.py: exact signatures, captured ids, and no loose matches."""
import unittest

from testbase import doc
from page_facts.htmldoc import parse
from page_facts.trackers import detect, haystack


def by_name(found: list[dict]) -> dict:
    return {t["name"]: t for t in found}


def scan_html(html: str) -> dict:
    return by_name(detect({"html": haystack(parse(html))}))


class Trackers(unittest.TestCase):
    def test_pixel_and_gtm_with_their_ids_and_a_commented_out_tag_ignored(self):
        t = by_name(detect({"html": haystack(doc("pixel_gtm_form.html"))}))
        self.assertEqual((t["Meta Pixel"]["found"], t["Meta Pixel"]["ids"]), (True, ["123456789012345"]))
        self.assertIn("fbevents.js", t["Meta Pixel"]["evidence"])
        self.assertEqual((t["Google Tag Manager"]["found"], t["Google Tag Manager"]["ids"]), (True, ["GTM-ABC1234"]))
        for name in ("GA4", "Google Ads", "TikTok Pixel", "Microsoft Clarity", "Hotjar"):
            self.assertFalse(t[name]["found"], name)

    def test_the_word_facebook_in_text_scripts_and_links_is_not_a_pixel(self):
        t = by_name(detect({"html": haystack(doc("facebook_text_only.html"))}))
        self.assertEqual([n for n, v in t.items() if v["found"]], [])
        self.assertEqual(len(t), 7)

    def test_each_other_tracker_by_its_snippet(self):
        t = scan_html("""<script async src="https://www.googletagmanager.com/gtag/js?id=G-AB12CD34EF"></script>
            <script>gtag('config', 'G-AB12CD34EF'); gtag('config', 'AW-123456789');
            gtag('event', 'conversion', {'send_to': 'AW-123456789/abcDEF'});
            ttq.load('C4ABCDEFGHIJ1234567'); ttq.page();
            (function(c,l,a,r,i,t,y){t=l.createElement(r);t.src="https://www.clarity.ms/tag/"+i;
            })(window, document, "clarity", "script", "k3x9abcd1");
            (function(h,o,t,j,a,r){h._hjSettings={hjid:3456789,hjsv:6};r.src=t+h._hjSettings.hjid+j;
            })(window,document,'https://static.hotjar.com/c/hotjar-','.js?sv=');</script>
            <script src="https://analytics.tiktok.com/i18n/pixel/events.js"></script>""")
        self.assertEqual(t["GA4"]["ids"], ["G-AB12CD34EF"])
        self.assertEqual(t["Google Ads"]["ids"], ["AW-123456789"])
        self.assertEqual(t["TikTok Pixel"]["ids"], ["C4ABCDEFGHIJ1234567"])
        self.assertEqual(t["Microsoft Clarity"]["ids"], ["k3x9abcd1"])
        self.assertEqual(t["Hotjar"]["ids"], ["3456789"])
        self.assertFalse(t["Meta Pixel"]["found"])

    def test_a_bare_quoted_id_proves_nothing_without_the_loader(self):
        t = scan_html("<script>var container = 'GTM-ABC1234'; var hjid = {hjid: 1234567};</script>")
        self.assertFalse(t["Google Tag Manager"]["found"])
        self.assertFalse(t["Hotjar"]["found"])

    def test_a_pixel_loaded_through_gtm_shows_in_the_requests_only(self):
        requests = "\n".join(["https://www.googletagmanager.com/gtm.js?id=GTM-ZZZ9999",
                              "https://connect.facebook.net/en_US/fbevents.js",
                              "https://connect.facebook.net/signals/config/998877665544332?v=2.9.1",
                              "https://www.google-analytics.com/g/collect?v=2&tid=G-REQ12345&cid=1"])
        t = by_name(detect({"html": haystack(parse("<p>shell</p>")), "requests": requests}))
        self.assertEqual((t["Meta Pixel"]["seen_in"], t["Meta Pixel"]["ids"]), (["requests"], ["998877665544332"]))
        self.assertEqual(t["Google Tag Manager"]["ids"], ["GTM-ZZZ9999"])
        self.assertEqual(t["GA4"]["ids"], ["G-REQ12345"])


if __name__ == "__main__":
    unittest.main()
