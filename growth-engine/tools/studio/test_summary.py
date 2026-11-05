"""Tests for studio/summary.py: the run's one-line summary."""
import unittest

from studio.summary import pending_queue, summarize


def step(n, status, name=None, note=None):
    s = {"n": n, "name": name or f"Step {n}", "status": status}
    if note:
        s["note"] = note
    return s


class Summary(unittest.TestCase):
    def test_says_where_the_piece_is_and_what_waits_on_the_owner(self):
        led = {"family": "song", "queue": [{"checkpoint": "G-HUMAN-SONG", "status": "PENDING"},
                                           {"checkpoint": "G-HUMAN-SONG", "status": "PENDING"},
                                           {"checkpoint": "G-HUMAN-SPINE", "status": "FYI"}]}
        self.assertEqual(summarize([step(0, "done"), step(4, "active", "Audio")], led),
                         "Step 4 Audio. Waiting on you: G-HUMAN-SONG.")
        self.assertEqual(len(pending_queue(led)), 2)

    def test_done_blocked_and_runs_without_steps(self):
        led = {"family": "library", "queue": []}
        self.assertEqual(summarize([step(0, "done"), step(1, "na")], led), "All steps done.")
        self.assertEqual(summarize([step(1, "blocked", "Idea", "no genre yet")], led), "Step 1 Idea: blocked. no genre yet")
        self.assertEqual(summarize([], led), "A library run: no production steps.")

    def test_stays_under_300_characters(self):
        led = {"family": "song", "queue": [{"checkpoint": f"G-{i:03d}" + "X" * 20, "status": "PENDING"} for i in range(30)]}
        self.assertEqual(len(summarize([step(0, "active")], led)), 300)


if __name__ == "__main__":
    unittest.main()
