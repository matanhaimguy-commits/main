"""Tests for the twin hook rule (hook_rule.py, hook_grades.py, hook_anchors.py).
Run from growth-engine/tools: python3 -m unittest test_hook_rule"""
import unittest

import hook_anchors
import hook_grades
import hook_rule

IDS = hook_anchors.anchor_ids()
A1, A2 = IDS


def read(v, t, s, gates=()):
    return {"visual": v, "text": t, "spoken": s, "gates_failed": list(gates)}


def run(hook1, hook2, anchors1=("B+", "B+", "B+"), anchors2=("B+", "B+", "B+"), packet="packet-v2"):
    def g(hook, a):
        return {"hook": hook, "anchors": {A1: read(*a), A2: read(*a)}}
    return {"packet": packet, "graders": [g(hook1, anchors1), g(hook2, anchors2)]}


class Grades(unittest.TestCase):
    def test_order(self):
        order = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F"]
        ranks = [hook_grades.rank(g) for g in order]
        self.assertEqual(ranks, sorted(ranks, reverse=True))

    def test_not_a_grade(self):
        for g in ("n/a", "", None, "E", "AA"):
            self.assertIsNone(hook_grades.rank(g))
        self.assertEqual(hook_grades.rank(" a- "), hook_grades.rank("A-"))


class Anchors(unittest.TestCase):
    def test_two_anchors_from_the_skill(self):
        self.assertEqual(IDS, ["ANCHOR-B1", "ANCHOR-B6"])


class Rule(unittest.TestCase):
    def test_at_the_anchors_passes(self):
        r = hook_rule.judge(run(read("B+", "B+", "B+"), read("B+", "B+", "B+")))
        self.assertTrue(r["pass"], r["why"])

    def test_above_the_anchors_passes(self):
        self.assertTrue(hook_rule.judge(run(read("A", "A-", "A+"), read("B+", "A-", "B+")))["pass"])

    def test_below_an_anchor_on_any_one_channel_fails(self):
        for i, ch in enumerate(("visual", "text", "spoken")):
            low = ["B+", "B+", "B+"]
            low[i] = "B"
            r = hook_rule.judge(run(read(*low), read("A", "A", "A")))
            self.assertFalse(r["pass"], ch)
            self.assertTrue(any(ch in w and "grader 1" in w for w in r["why"]), r["why"])

    def test_second_grader_below_fails_too(self):
        r = hook_rule.judge(run(read("A", "A", "A"), read("A", "B", "A")))
        self.assertFalse(r["pass"])
        self.assertTrue(any("grader 2" in w for w in r["why"]))

    def test_must_match_the_stronger_anchor(self):
        anchors = {A1: read("B", "B", "B"), A2: read("A-", "A-", "A-")}
        g = {"hook": read("B+", "B+", "B+"), "anchors": anchors}
        self.assertFalse(hook_rule.judge({"packet": "packet-v2", "graders": [g, g]})["pass"])

    def test_each_grader_is_compared_with_its_own_anchors(self):
        # a harsh grader scores everything low, the hook included: still a pass
        self.assertTrue(hook_rule.judge(run(read("D", "D", "C"), read("A", "A", "A"),
                                            anchors1=("D", "D", "C")))["pass"])

    def test_a_failed_check_fails_even_with_top_grades(self):
        r = hook_rule.judge(run(read("A+", "A+", "A+", gates=[4]), read("A+", "A+", "A+")))
        self.assertFalse(r["pass"])
        self.assertTrue(any("check" in w for w in r["why"]))

    def test_no_frame_no_visual_pass(self):
        r = hook_rule.judge(run(read("n/a", "A", "A"), read("A", "A", "A")))
        self.assertFalse(r["pass"])
        self.assertTrue(any("no visual grade for the hook" in w for w in r["why"]))

    def test_anchor_without_a_grade_cannot_be_beaten(self):
        r = hook_rule.judge(run(read("A", "A", "A"), read("A", "A", "A"), anchors1=("n/a", "B", "B")))
        self.assertFalse(r["pass"])

    def test_needs_two_graders_and_packet_v2(self):
        one = run(read("A", "A", "A"), read("A", "A", "A"))
        one["graders"] = one["graders"][:1]
        self.assertFalse(hook_rule.judge(one)["pass"])
        self.assertFalse(hook_rule.judge(run(read("A", "A", "A"), read("A", "A", "A"), packet="v5"))["pass"])


if __name__ == "__main__":
    unittest.main()
