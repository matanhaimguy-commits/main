"""The starter folder clients/_template: brain-check fails only on its unknowns, never on the schema."""
import json
import unittest

from clients.paths import REPO
from clients.testbase import TOOLS  # noqa: F401  (puts tools/ on sys.path)
from organic_os.brain import brain_check
from organic_os.issues import ERROR

TEMPLATE = REPO / "clients" / "_template"


class Template(unittest.TestCase):
    def setUp(self):
        self.brain = json.loads((TEMPLATE / "brain.json").read_text(encoding="utf-8"))
        self.issues, self.gaps = brain_check(self.brain, [])

    def test_has_the_starter_files(self):
        for name in ("brain.json", "content-map.json", "README.md", "cards/.gitkeep", "intake/.gitkeep"):
            self.assertTrue((TEMPLATE / name).exists(), name)

    def test_brain_passes_the_schema(self):
        self.assertEqual([i for i in self.issues if i["code"] == "schema"], [])

    def test_brain_fails_only_on_the_expected_unknowns(self):
        errors = [i for i in self.issues if i["level"] == ERROR]
        self.assertEqual({i["code"] for i in errors}, {"blocking"})
        fields = sorted(i["msg"].split(" ")[0] for i in errors)
        self.assertEqual(fields, ["constraints.cannot_say", "mechanism.ump", "mechanism.ums", "offer.main_offer",
                                  "offer.next_step", "voice.language"])
        self.assertTrue(all("Nothing is produced until it is filled" in i["msg"] for i in errors))

    def test_every_text_value_is_marked_unknown(self):
        main = self.brain["offer"]["main_offer"]
        self.assertTrue(main.startswith("unknown:"))

    def test_content_map_is_json_with_the_stage_mix(self):
        cmap = json.loads((TEMPLATE / "content-map.json").read_text(encoding="utf-8"))
        self.assertAlmostEqual(sum(cmap["mix"].values()), 1.0)


if __name__ == "__main__":
    unittest.main()
