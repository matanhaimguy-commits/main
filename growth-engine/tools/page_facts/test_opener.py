"""Tests for opener.py: http(s) only, verified TLS, and redirects only to public addresses."""
import ssl
import unittest
import urllib.request

import testbase  # noqa: F401
from page_facts.errors import BadUrl
from page_facts.opener import SafeRedirects, build_opener, tls_context


class Opener(unittest.TestCase):
    def test_no_file_ftp_or_data_handlers(self):
        kinds = {type(h) for h in build_opener().handlers}
        self.assertTrue({urllib.request.FileHandler, urllib.request.FTPHandler, urllib.request.DataHandler}.isdisjoint(kinds))
        self.assertIn(urllib.request.ProxyHandler, kinds)

    def test_tls_is_verified(self):
        ctx = tls_context()
        self.assertEqual((ctx.verify_mode, ctx.check_hostname), (ssl.CERT_REQUIRED, True))

    def test_redirects_to_local_addresses_are_refused(self):
        req = urllib.request.Request("https://acme.example/")
        for target in ("file:///etc/passwd", "http://10.0.0.5/admin"):
            with self.assertRaises(BadUrl):
                SafeRedirects().redirect_request(req, None, 302, "Found", {}, target)
        self.assertEqual(SafeRedirects().redirect_request(req, None, 302, "Found", {}, "https://www.acme.example/").full_url,
                         "https://www.acme.example/")


if __name__ == "__main__":
    unittest.main()
