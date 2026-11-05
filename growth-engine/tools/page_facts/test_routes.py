"""Tests for routes.py: booking, form, messaging and direct routes by exact host, with where they appear."""
import unittest

from testbase import doc
from page_facts.routes import classify, find


class Routes(unittest.TestCase):
    def test_whatsapp_calendly_page(self):
        got = [(r["service"], r["where"], r["via"], r["url"]) for r in find(doc("whatsapp_calendly.html"))]
        self.assertEqual(got, [
            ("Phone", "header", "link", "tel:+972501234567"),
            ("Typeform", "body", "link", "https://form.typeform.com/to/AbC123"),
            ("WhatsApp", "footer", "link", "https://wa.me/972501234567?text=Hi%20Dana"),
            ("Messenger", "footer", "link", "https://m.me/danalash"),
            ("Instagram DM", "footer", "link", "https://ig.me/m/danalash"),
            ("Calendly", "body", "iframe", "https://calendly.com/dana-lash/intro?embed_type=Inline"),
            ("Calendly", "body", "embed", "https://calendly.com/dana-lash/follow-up"),
        ])
        whatsapp = next(r for r in find(doc("whatsapp_calendly.html")) if r["service"] == "WhatsApp")
        self.assertEqual((whatsapp["kind"], whatsapp["text"]), ("messaging", "WhatsApp us"))

    def test_hosts_match_exactly_never_as_substrings(self):
        self.assertEqual(classify("https://app.cal.com/acme"), ("booking", "Cal.com"))
        self.assertEqual(classify("https://acme.as.me/schedule.php"), ("booking", "Acuity"))
        self.assertEqual(classify("//meetings.hubspot.com/dana"), ("booking", "HubSpot meetings"))
        self.assertEqual(classify("https://api.whatsapp.com/send?phone=972"), ("messaging", "WhatsApp"))
        self.assertEqual(classify("MAILTO:hi@acme.example"), ("direct", "Email"))
        for url in ("https://notcalendly.com/x", "https://calendly.com.evil.example/x", "https://example.com/?u=wa.me",
                    "https://www.facebook.com/acme", "/contact", "javascript:void(0)"):
            self.assertIsNone(classify(url), url)


if __name__ == "__main__":
    unittest.main()
