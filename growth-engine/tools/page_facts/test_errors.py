"""Tests for errors.py: the exit messages."""
import unittest

import testbase  # noqa: F401
from page_facts.errors import BadUrl, PageError, RenderError, Unreachable, exit_message


class Errors(unittest.TestCase):
    def test_unreachable_says_how_to_allow_the_host(self):
        msg = exit_message(Unreachable("straightscale.com", "the network proxy refused the connection: 403 Forbidden"))
        self.assertTrue(msg.startswith("UNREACHABLE: straightscale.com (the network proxy refused"))
        self.assertTrue(msg.endswith("allow straightscale.com in the cloud environment's network settings."))

    def test_other_messages(self):
        self.assertEqual(exit_message(BadUrl("not a web address: x")), "BAD_URL: not a web address: x")
        self.assertEqual(exit_message(RenderError("crashed")), "RENDER_FAILED: crashed")
        self.assertEqual(exit_message(PageError("PAGE_HTTP_403: ...")), "PAGE_HTTP_403: ...")


if __name__ == "__main__":
    unittest.main()
