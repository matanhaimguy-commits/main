"""Tests for studio/ledger_steps.py: a run's ledger as the Studio page's steps."""
import unittest

from studio.ledger_steps import build_steps, page_status, step_note
from studio.testbase import POST, SLUG, P, StudioCase


class PageStatus(unittest.TestCase):
    def test_the_first_open_step_is_the_current_one(self):
        self.assertEqual(page_status("done", False), "done")
        self.assertEqual(page_status("na", False), "na")
        self.assertEqual(page_status("todo", False), "active")
        self.assertEqual(page_status("todo", True), "pending")
        self.assertEqual(page_status("blocked", False), "blocked")

    def test_a_family_skip_says_why(self):
        self.assertEqual(step_note({"status": "na", "note": "family"}, "still"), "Not part of a still piece.")
        self.assertEqual(step_note({"status": "blocked", "note": " waiting "}, "song"), "waiting")


class BuildSteps(StudioCase):
    def test_steps_follow_the_ledger_and_the_pipelines_gates(self):
        led = self.song_run()
        steps = build_steps(P, led)
        self.assertEqual([s["n"] for s in steps], list(range(16)))
        self.assertEqual([s["status"] for s in steps[:3]], ["done", "active", "pending"])
        self.assertEqual(steps[0]["name"], "Foundation and brief")
        self.assertEqual(steps[0]["gates"], [{"gate": "G-BRIEF", "label": "Brief", "status": "PASS", "by": "claude",
                                              "at": led["run_gates"]["G-BRIEF"][0]["at"], "note": "brief from brain.json"}])
        self.assertEqual([(g["gate"], g["status"]) for g in steps[1]["gates"]], [("G-IDEA", "FAIL")])
        # The song family adds the owner's listen at step 4.
        self.assertEqual([(g["gate"], g["status"]) for g in steps[4]["gates"]],
                         [("G-AUDIO-MASTER", "PENDING"), ("G-HUMAN-SONG", "PENDING")])

    def test_manifest_history_and_notes_come_first(self):
        led = self.song_run()
        extra = {"3": {"note": "Speech released at 86", "gates": [
            {"gate": "G-SCRIPT", "label": "Script Lab loop 1", "status": "FAIL", "score": 81}]}}
        steps = build_steps(P, led, extra)
        self.assertEqual(steps[3]["note"], "Speech released at 86")
        self.assertEqual(steps[3]["gates"][0], {"gate": "G-SCRIPT", "label": "Script Lab loop 1", "status": "FAIL", "score": 81})
        self.assertEqual(steps[3]["gates"][1]["status"], "PENDING")

    def test_skipped_steps_and_a_blocked_current_step(self):
        P.init_run(SLUG, POST, "carousel_mistakes")
        P.record_gate(SLUG, POST, "G-BRIEF", "PASS", "claude", note="ok")
        P.close_step(SLUG, POST, 0, "done")
        P.close_step(SLUG, POST, 1, "blocked", "waiting for the series look")
        steps = build_steps(P, P.load_ledger(SLUG, POST))
        self.assertEqual([s["n"] for s in steps if s["status"] == "na"], [4, 5, 8, 12])
        self.assertEqual((steps[1]["status"], steps[1]["note"]), ("blocked", "waiting for the series look"))
        self.assertEqual(steps[2]["status"], "pending")
        self.assertIn("at", steps[1])

    def test_library_runs_have_no_steps(self):
        P.init_run(SLUG, "AC-LIB-STYLE", "carousel_mistakes")
        self.assertEqual(build_steps(P, P.load_ledger(SLUG, "AC-LIB-STYLE")), [])


if __name__ == "__main__":
    unittest.main()
