"""The twin format in the router and the config (organic_os/twin_route.py). Run: python3 -m unittest discover -s
growth-engine/tools/organic_os -t growth-engine/tools"""
import unittest

import organic_os as o
from organic_os import twin_route
from organic_os.card_people import twin_issues
from organic_os.testbase import BRAIN, MAP, card

HOST = {"engine": "heygen", "looks": [{"id": "L1"}], "voices": [{"id": "V1"}]}
TWIN_BRAIN = {**BRAIN, "host": HOST}
F = o.CONFIG["formats"]


def fmts(opts):
    return [x["format"] for x in opts]


class TwinFormatTest(unittest.TestCase):
    def test_config_entry(self):
        f = F["reel_twin_stage"]
        self.assertEqual((f["format_family"], f["twin_only"]), ("presenter", True))
        self.assertEqual(set(f["l19"]), set(o.l19.PROPERTIES))
        self.assertIn("unmeasured", f["heygen_credits_status"])
        self.assertLessEqual(f["heygen_credits"][0], f["heygen_credits"][1])
        self.assertEqual(f["atlas_units"]["voice_s"], [0, 0])   # the voice is HeyGen's, not Atlas's

    def test_twin_is_a_presenter_identity_for_the_two_presenter_formats(self):
        for fid in ("reel_whiteboard", "reel_strategist_prop"):
            self.assertEqual(F[fid]["presenter_identities"], ["staged_strategist", "twin"])
        self.assertEqual([k for k, v in F.items() if v.get("twin_only")], ["reel_twin_stage"])

    def test_never_routed_without_twin_host_and_a_host_block(self):
        c = card(job="trust", belief="B4", load_bearing_beat="mechanism")
        self.assertNotIn("reel_twin_stage", fmts(o.route(c, TWIN_BRAIN, MAP)))
        self.assertNotIn("reel_twin_stage", fmts(o.route({**c, "twin_host": True}, BRAIN, MAP)))
        self.assertIn("reel_twin_stage", fmts(o.route({**c, "twin_host": True}, TWIN_BRAIN, MAP)))

    def test_reroute_only_where_the_twin_ranks_first(self):
        run = lambda c: o.route(c, TWIN_BRAIN, MAP)
        c = card(job="trust", belief="B4", load_bearing_beat="mechanism")
        top = fmts(run({**c, "twin_host": True}))[0]
        hit = twin_route.reroute(c, TWIN_BRAIN, run)
        self.assertEqual(hit is not None, top == "reel_twin_stage")
        # a beat the twin cannot lead (motion-only list) never re-routes; and no host block, or already a twin card
        self.assertIsNone(twin_route.reroute(c, BRAIN, lambda x: o.route(x, BRAIN, MAP)))
        self.assertIsNone(twin_route.reroute({**c, "twin_host": True}, TWIN_BRAIN, run))
        self.assertIsNone(twin_route.reroute(c, TWIN_BRAIN, lambda x: [{"format": "reel_whiteboard", "score": 9}]))
        self.assertEqual(twin_route.reroute(c, TWIN_BRAIN, lambda x: [{"format": "reel_twin_stage", "score": 9}])["format"],
                         "reel_twin_stage")

    def test_card_needs_twin_host(self):
        self.assertEqual([i["code"] for i in twin_issues({"format": "reel_twin_stage"}, TWIN_BRAIN)], ["twin_host"])
        self.assertEqual(twin_issues({"format": "reel_twin_stage", "twin_host": True}, TWIN_BRAIN), [])
        self.assertEqual(twin_issues({"format": "reel_whiteboard"}, TWIN_BRAIN), [])


if __name__ == "__main__":
    unittest.main()
