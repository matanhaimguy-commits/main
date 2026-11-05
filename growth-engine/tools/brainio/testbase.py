"""Shared by the brainio, braindraft and brand tests: a temporary repo root holding clients/acme/ from the starter template."""
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

TEMPLATE = TOOLS.parent.parent / "clients" / "_template"


class BrainCase(unittest.TestCase):
    slug = "acme"

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.dir = self.root / "clients" / self.slug
        shutil.copytree(TEMPLATE, self.dir)

    def tearDown(self):
        self.tmp.cleanup()

    def brain(self) -> dict:
        return json.loads((self.dir / "brain.json").read_text(encoding="utf-8"))

    def write_brain(self, b: dict) -> None:
        (self.dir / "brain.json").write_text(json.dumps(b, indent=2) + "\n", encoding="utf-8")
