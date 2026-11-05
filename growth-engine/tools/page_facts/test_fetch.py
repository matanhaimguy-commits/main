"""Tests for fetch.py: honest User-Agent, size cap, HTTP errors as pages, and the unreachable paths."""
import socket
import unittest
import urllib.error

from testbase import SITE, StubOpener
from page_facts.errors import BadUrl, Unreachable
from page_facts.fetch import fetch


class Fetch(unittest.TestCase):
    def test_a_page_with_an_honest_user_agent_and_a_timeout(self):
        opener = StubOpener({SITE: (200, "<h1>Hi</h1>", "text/html; charset=utf-8")})
        page = fetch(SITE, opener=opener, timeout=7)
        self.assertEqual((page.status, page.text, page.final_url, page.truncated), (200, "<h1>Hi</h1>", SITE, False))
        ua = opener.calls[0]["user_agent"]
        self.assertIn("page-facts", ua)
        self.assertNotIn("Chrome", ua)
        self.assertNotIn("Mozilla", ua)
        self.assertEqual(opener.calls[0]["timeout"], 7)

    def test_size_cap_and_header_charset(self):
        page = fetch(SITE, opener=StubOpener({SITE: (200, "é".encode("latin-1") + b"x" * 20, "text/html; charset=iso-8859-1")}), cap=10)
        self.assertEqual((page.text, page.truncated), ("é" + "x" * 9, True))

    def test_an_http_error_comes_back_as_a_page(self):
        page = fetch(SITE + "/robots.txt", opener=StubOpener({}))
        self.assertEqual((page.status, page.text), (404, "not found"))

    def test_proxy_refusal_dns_failure_and_timeout_are_unreachable(self):
        cases = [(urllib.error.URLError(OSError("Tunnel connection failed: 403 Forbidden")), "the network proxy refused the connection: 403 Forbidden"),
                 (urllib.error.URLError(socket.gaierror(-2, "Name or service not known")), "DNS lookup failed"),
                 (TimeoutError("timed out"), "no usable answer within 20s (TimeoutError)")]
        for error, reason in cases:
            with self.assertRaises(Unreachable) as e:
                fetch(SITE, opener=StubOpener({SITE: error}))
            self.assertEqual((e.exception.host, e.exception.reason), ("acme.example", reason))

    def test_local_and_non_web_addresses_are_never_fetched(self):
        opener = StubOpener({})
        for url in ("file:///etc/passwd", "http://127.0.0.1/", "http://169.254.169.254/latest", "http://localhost:8080"):
            with self.assertRaises(BadUrl):
                fetch(url, opener=opener)
        self.assertEqual(opener.calls, [])


if __name__ == "__main__":
    unittest.main()
