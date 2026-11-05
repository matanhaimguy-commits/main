"""Tests for charset.py: header charset, then <meta charset>, then UTF-8."""
import unittest

import testbase  # noqa: F401
from page_facts.charset import decode


class Charset(unittest.TestCase):
    def test_header_then_meta_then_utf8(self):
        self.assertEqual(decode("שלום".encode("cp1255"), "windows-1255"), "שלום")
        self.assertEqual(decode('<meta charset="iso-8859-1"><p>café'.encode("latin-1")), '<meta charset="iso-8859-1"><p>café')
        self.assertEqual(decode("café".encode("utf-8")), "café")

    def test_an_unknown_charset_falls_back_and_bad_bytes_never_raise(self):
        self.assertEqual(decode(b"ok\xff", "no-such-charset"), "ok�")


if __name__ == "__main__":
    unittest.main()
