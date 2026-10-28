"""Missing client files give one clear error line and exit 1 (card-check, week-check, route, score), and carousels
stop at 10 slides (the hub takes at most 10 files). Run: python3 -m unittest discover -s growth-engine/tools/organic_os
-t growth-engine/tools"""
import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path

import yaml

import organic_os as o
from organic_os import cli, files
from organic_os.testbase import BRAIN, DEMAND, MAP, card


class MissingFiles(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self._root, files.ROOT = files.ROOT, self.root
        d = self.root / "clients" / "acme"
        d.mkdir(parents=True)
        (d / "brain.json").write_text(json.dumps(BRAIN))
        self.card = d / "card.yaml"
        self.card.write_text(yaml.safe_dump(card()))

    def tearDown(self):
        files.ROOT = self._root
        self.tmp.cleanup()

    def run_cli(self, *args):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = cli.main([str(a) for a in args])
        return code, out.getvalue(), err.getvalue()

    def test_no_content_map(self):
        for cmd in (("card-check", "acme", self.card), ("week-check", "acme", self.card), ("route", "acme", self.card)):
            with self.subTest(cmd=cmd[0]):
                code, out, err = self.run_cli(*cmd)
                self.assertEqual(code, 1)
                self.assertEqual(err.count("\n"), 1, err)
                self.assertIn("clients/acme/content-map.json is missing: build the month's Content Map", err)

    def test_no_posts_csv(self):
        code, _, err = self.run_cli("score", "acme")
        self.assertEqual((code, err.count("\n")), (1, 1))
        self.assertIn("clients/acme/analytics/posts.csv is missing: pull the post results first", err)

    def test_no_card_or_brain(self):
        (self.root / "clients" / "acme" / "content-map.json").write_text(json.dumps(MAP))
        code, _, err = self.run_cli("card-check", "acme", self.root / "nope.yaml")
        self.assertEqual(code, 1)
        self.assertIn("nope.yaml is missing: no such card or folder", err)
        code, _, err = self.run_cli("card-check", "nobody", self.card)
        self.assertIn("clients/nobody/brain.json is missing", err)


class CarouselSlides(unittest.TestCase):
    def slides(self, n):
        c = card(job="trust", belief="B3", format="carousel_self_check", credit_budget=10, slides=n)
        return [i["msg"] for i in o.card_check(c, BRAIN, MAP, DEMAND) if i["code"] == "slides"]

    def test_seven_to_ten(self):
        self.assertEqual(self.slides(7) + self.slides(10), [])
        for n in (6, 11, 12):
            self.assertIn("7 to 10 slides (the hub takes at most 10 files", self.slides(n)[0])


if __name__ == "__main__":
    unittest.main()
