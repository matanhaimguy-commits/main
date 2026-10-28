"""Switched-off services. Run: python3 -m unittest discover -s .claude/hooks/guards -p 'test_*.py'"""
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from guards.services import off_reason  # noqa: E402

STANDARDS = json.loads((Path(__file__).resolve().parents[3] / "growth-engine" / "production" / "standards.json").read_text())


class ServicesTest(unittest.TestCase):
    def test_higgsfield_is_off(self):
        self.assertIn("Atlas", off_reason("mcp__Higgs__generate_image", STANDARDS))
        self.assertIn("Atlas", off_reason("mcp__Higgs__generate_video_batch", STANDARDS))

    def test_other_services_stay_on(self):
        self.assertIsNone(off_reason("mcp__ElevenLabs__creative_generate_speech", STANDARDS))
        self.assertIsNone(off_reason("atlas_generate", STANDARDS))
        self.assertIsNone(off_reason("Bash", STANDARDS))


if __name__ == "__main__":
    unittest.main()
