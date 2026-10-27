"""Tests for urls.py: normalizing, checking and comparing addresses."""
import unittest

import testbase  # noqa: F401
from page_facts.errors import BadUrl
from page_facts.urls import check_url, host_of, normalize, origin, same_site


class Urls(unittest.TestCase):
    def test_normalize_host_and_origin(self):
        self.assertEqual(normalize(" acme.example "), "https://acme.example")
        self.assertEqual(normalize("http://acme.example/x"), "http://acme.example/x")
        self.assertEqual((host_of("https://WWW.Acme.example:443/a"), origin("https://acme.example:8443/a?b")),
                         ("www.acme.example", "https://acme.example:8443"))

    def test_only_public_web_addresses_pass(self):
        self.assertEqual(check_url("https://8.8.8.8/"), "https://8.8.8.8/")
        for bad in ("ftp://acme.example", "javascript:alert(1)", "https://", "http://[::1]/", "http://192.168.1.1",
                    "http://printer.local/", "http://metadata.google.internal/"):
            with self.assertRaises(BadUrl, msg=bad):
                check_url(bad)

    def test_same_site_ignores_www_only(self):
        self.assertTrue(same_site("https://www.acme.example/a", "http://acme.example/b"))
        self.assertFalse(same_site("https://cdn.acme.example/a", "https://acme.example/"))


if __name__ == "__main__":
    unittest.main()
