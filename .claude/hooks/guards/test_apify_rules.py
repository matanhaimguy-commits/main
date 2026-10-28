"""Apify gate rules. Run: python3 -m unittest discover -s .claude/hooks/guards -p 'test_*.py'"""
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from guards.apify_rules import check  # noqa: E402

CONFIG = json.loads((Path(__file__).resolve().parents[3] / "growth-engine" / "config" / "apify-actors.json").read_text())
IG = {"directUrls": ["https://www.instagram.com/x/"], "resultsType": "posts", "resultsLimit": 20, "addParentData": False}


class ApifyRulesTest(unittest.TestCase):
    def test_the_skills_own_call_passes_with_a_charge_cap(self):
        self.assertEqual(check({"actor": "apify/instagram-scraper", "input": IG, "callOptions": {"maxTotalChargeUsd": 2}}, CONFIG), [])

    def test_unlisted_actor_is_refused(self):
        self.assertIn("not an allowed scraper", check({"actor": "someone/any-scraper", "input": {}}, CONFIG)[0])

    def test_actor_id_counts_as_the_actor(self):
        self.assertEqual(check({"actor": "shu8hvrXbJbY3Eb9W", "input": IG, "callOptions": {"maxTotalChargeUsd": 1}}, CONFIG), [])

    def test_misspelled_key_is_named_with_a_suggestion(self):
        r = check({"actor": "apify/instagram-scraper", "input": {**IG, "resultLimit": 5}, "callOptions": {"maxTotalChargeUsd": 1}}, CONFIG)
        self.assertEqual(len(r), 1)
        self.assertIn("did you mean 'resultsLimit'", r[0])

    def test_spend_cap_is_required_and_bounded(self):
        self.assertIn("maxItems does not cap it", check({"actor": "apify/instagram-scraper", "input": IG, "callOptions": {"maxItems": 400}}, CONFIG)[0])
        self.assertIn("over this scraper's cap", check({"actor": "apify/instagram-scraper", "input": IG, "callOptions": {"maxTotalChargeUsd": 50}}, CONFIG)[0])

    def test_trustpilot_cap_and_emails_off(self):
        a = "memo23/trustpilot-scraper-ppe"
        inp = {"startUrls": ["example.com"], "maxItems": 150, "enrichEmails": False}
        self.assertEqual(check({"actor": a, "input": inp, "callOptions": {"maxTotalChargeUsd": 0.5}}, CONFIG), [])
        self.assertIn("over this scraper's cap", check({"actor": a, "input": inp, "callOptions": {"maxTotalChargeUsd": 0.51}}, CONFIG)[0])
        self.assertIn("set callOptions.maxTotalChargeUsd", check({"actor": a, "input": inp, "callOptions": {}}, CONFIG)[0])
        opts = {"maxTotalChargeUsd": 0.3}
        for bad in ({"startUrls": ["example.com"]}, {**inp, "enrichEmails": True}):
            self.assertEqual(check({"actor": a, "input": bad, "callOptions": opts}, CONFIG), ["send enrichEmails: false (personal data stays off)"])

    def test_facebook_ads_cap(self):
        a = "apify/facebook-ads-scraper"
        inp = {"startUrls": [{"url": "https://www.facebook.com/ads/library/?q=x"}], "resultsLimit": 25, "onlyTotal": True}
        self.assertEqual(check({"actor": a, "input": inp, "callOptions": {"maxTotalChargeUsd": 1}}, CONFIG), [])
        self.assertIn("over this scraper's cap", check({"actor": a, "input": inp, "callOptions": {"maxTotalChargeUsd": 1.5}}, CONFIG)[0])
        self.assertIn("set callOptions.maxTotalChargeUsd", check({"actor": a, "input": inp, "callOptions": {"maxItems": 25}}, CONFIG)[0])

    def test_google_maps_personal_data_stays_off(self):
        base = {"searchStringsArray": ["water filters"], "locationQuery": "Tirana, Albania", "maxCrawledPlacesPerSearch": 20}
        opts = {"maxTotalChargeUsd": 1}
        r = check({"actor": "compass/crawler-google-places", "input": base, "callOptions": opts}, CONFIG)
        self.assertEqual(r, ["send scrapeReviewsPersonalData: false (personal data stays off)"])
        ok = {**base, "scrapeReviewsPersonalData": False}
        self.assertEqual(check({"actor": "compass/crawler-google-places", "input": ok, "callOptions": opts}, CONFIG), [])
        leads = {**ok, "maximumLeadsEnrichmentRecords": 3}
        self.assertIn("personal data", check({"actor": "compass/crawler-google-places", "input": leads, "callOptions": opts}, CONFIG)[0])

    def test_unchecked_keys_still_need_the_cap(self):
        self.assertEqual(check({"actor": "clockworks/tiktok-scraper", "input": {"anything": 1}, "callOptions": {"maxTotalChargeUsd": 1}}, CONFIG), [])


if __name__ == "__main__":
    unittest.main()
