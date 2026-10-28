"""Shared by the intake tests: a temporary repo root and the sample fixture (a made-up bakery)."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

FIXTURE = Path(__file__).resolve().parent / "fixtures" / "sample-intake.json"


def sample() -> dict:
    return json.loads(FIXTURE.read_text(encoding="utf-8"))


class IntakeCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()
