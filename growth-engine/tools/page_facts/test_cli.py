"""Tests for cli.py: markdown by default, --json, --out, --render, and the exit messages."""
import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path

from testbase import SITE, fixture, stub_fetch
from page_facts.cli import main
from page_facts.errors import Unreachable

FETCH = stub_fetch({SITE: (200, fixture("pixel_gtm_form.html"))})


def run(argv, **kw) -> str:
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        main(argv, **kw)
    return out.getvalue()


class Cli(unittest.TestCase):
    def test_markdown_by_default_and_json_on_request(self):
        self.assertTrue(run(["acme.example"], fetcher=FETCH).startswith("# Page facts: acme.example"))
        self.assertEqual(json.loads(run([SITE, "--json"], fetcher=FETCH))["forms"][0]["fields_to_fill"], 5)

    def test_out_writes_the_file(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "facts.md"
            self.assertEqual(run([SITE, "--out", str(path)], fetcher=FETCH).strip(), f"wrote {path}")
            self.assertIn("## Tracking", path.read_text(encoding="utf-8"))

    def test_render_only_when_asked(self):
        seen = []

        def renderer(url):
            seen.append(url)
            return {"html": "<p>x</p>", "requests": [], "final_url": url, "status": 200, "idle": True}
        run([SITE], fetcher=FETCH, renderer=renderer)
        self.assertEqual(seen, [])
        self.assertIn("from the rendered page", run([SITE, "--render"], fetcher=FETCH, renderer=renderer))
        self.assertEqual(seen, [SITE])

    def test_unreachable_exits_with_the_message(self):
        dead = stub_fetch({SITE: Unreachable("acme.example", "DNS lookup failed")})
        with self.assertRaises(SystemExit) as e:
            run([SITE], fetcher=dead)
        self.assertIn("UNREACHABLE: acme.example (DNS lookup failed)", str(e.exception))


if __name__ == "__main__":
    unittest.main()
