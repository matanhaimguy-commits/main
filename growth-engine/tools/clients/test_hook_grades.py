"""Tests for clients/hook_grades.py."""
import unittest

from clients import hook_grades


class HookGrades(unittest.TestCase):
    def test_a_graded_hook_gives_one_object(self):
        self.assertEqual(hook_grades.of({"text": "first", "grade": "A"}), [{"hook": "first", "grade": "A", "by": "hook-lab"}])
        self.assertEqual(hook_grades.of({"spoken": "one", "grade": "A+"})[0]["hook"], "one")

    def test_no_grade_no_hook_or_no_text_is_an_empty_list_never_none(self):
        for h in (None, {}, {"text": "first"}, {"grade": "A"}):
            self.assertEqual(hook_grades.of(h), [])


if __name__ == "__main__":
    unittest.main()
