"""Tests for studio/answers.py: studio-answers."""
import unittest

from studio.answers import answers
from studio.testbase import Recorder


class Answers(unittest.TestCase):
    def test_lists_answered_questions_with_their_choices(self):
        hub = Recorder()
        hub.replies[("GET", "decisions")] = {"decisions": [{
            "id": 3, "business": "acme", "post_id": "AC-1", "checkpoint": "G-HUMAN-SONG", "key": "G-HUMAN-SONG", "step": 4,
            "question": "Ready?", "answer": {"choices": ["Yes"], "note": "slower chorus", "by": "owner", "at": "2026-10-27T11:00:00Z"}}]}
        self.assertEqual(answers(call=hub.call, slug="acme"), [{
            "id": 3, "business": "acme", "post_id": "AC-1", "checkpoint": "G-HUMAN-SONG", "key": "G-HUMAN-SONG", "step": 4,
            "question": "Ready?", "choices": ["Yes"], "note": "slower chorus", "by": "owner", "answered_at": "2026-10-27T11:00:00Z"}])
        self.assertEqual(hub.calls[0]["path"], "decisions?status=answered&business=acme")

    def test_without_a_slug_it_asks_for_every_business(self):
        hub = Recorder()
        hub.replies[("GET", "decisions")] = {"decisions": []}
        self.assertEqual(answers(call=hub.call), [])
        self.assertEqual(hub.calls[0]["path"], "decisions?status=answered")


if __name__ == "__main__":
    unittest.main()
