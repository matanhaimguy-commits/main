"""Tests for render.py, with the Node helper stubbed (no browser runs)."""
import json
import subprocess
import unittest

from testbase import SITE
from page_facts.errors import RenderError, Unreachable
from page_facts.render import HELPER, render


def helper(returncode=0, stdout="", stderr=""):
    calls = []

    def run(cmd, **kw):
        calls.append((cmd, kw))
        return subprocess.CompletedProcess(cmd, returncode, stdout, stderr)
    return run, calls


class Render(unittest.TestCase):
    def test_reads_the_helpers_json(self):
        out = json.dumps({"status": 200, "final_url": SITE + "/", "idle": False, "html": "<h1>Hi</h1>",
                          "requests": [SITE + "/", "https://connect.facebook.net/en_US/fbevents.js"]})
        run, calls = helper(stdout=out)
        got = render(SITE, run=run)
        self.assertEqual(got, {"html": "<h1>Hi</h1>", "requests": [SITE + "/", "https://connect.facebook.net/en_US/fbevents.js"],
                               "final_url": SITE + "/", "status": 200, "idle": False})
        cmd, kw = calls[0]
        self.assertEqual(cmd, ["node", str(HELPER), SITE])
        self.assertNotIn("shell", kw)

    def test_a_proxy_refusal_is_unreachable(self):
        run, _ = helper(1, stderr=f"page.goto: net::ERR_TUNNEL_CONNECTION_FAILED at {SITE}/")
        with self.assertRaises(Unreachable) as e:
            render(SITE, run=run)
        self.assertEqual((e.exception.host, e.exception.reason), ("acme.example", "Chromium: ERR_TUNNEL_CONNECTION_FAILED"))

    def test_other_failures_are_render_errors(self):
        def no_node(*a, **k):
            raise FileNotFoundError("node")

        def too_slow(*a, **k):
            raise subprocess.TimeoutExpired("node", 90)
        for run in (helper(1, stderr="browserType.launch: crashed")[0], helper(0, stdout="oops")[0], no_node, too_slow):
            with self.assertRaises(RenderError):
                render(SITE, run=run)


if __name__ == "__main__":
    unittest.main()
