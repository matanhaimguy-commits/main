"""Tests for studio/synced.py: studio-synced."""
import contextlib
import io
import unittest

from studio.synced import cli, mark_synced
from studio.testbase import Recorder


class Synced(unittest.TestCase):
    def test_marks_one_answer_and_says_when_it_already_was(self):
        hub = Recorder()
        hub.replies[("POST", "synced")] = {"synced": [3], "already": [], "problems": []}
        self.assertTrue(mark_synced(3, call=hub.call))
        self.assertEqual(hub.calls[0]["body"], {"ids": [3]})
        hub.replies[("POST", "synced")] = {"synced": [], "already": [3], "problems": []}
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            cli(["3"], call=hub.call)
        self.assertEqual(out.getvalue().strip(), "decision #3 was already synced")

    def test_needs_a_decision_number(self):
        with self.assertRaises(SystemExit):
            cli(["abc"], call=Recorder().call)
        with self.assertRaises(SystemExit):
            cli([], call=Recorder().call)


if __name__ == "__main__":
    unittest.main()
