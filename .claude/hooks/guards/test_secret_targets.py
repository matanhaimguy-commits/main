"""What the secret guard scans. Run: python3 -m unittest discover -s .claude/hooks/guards -p 'test_*.py'"""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from guards.secret_targets import commit_dir, targets  # noqa: E402


def git(d, *a):
    subprocess.run(["git", *a], cwd=d, check=True, capture_output=True)


class TargetsTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.d = self.tmp.name
        git(self.d, "init", "-q")
        Path(self.d, ".gitignore").write_text(".env\n")

    def tearDown(self):
        self.tmp.cleanup()

    def test_write_edit_and_multiedit_texts(self):
        f = str(Path(self.d, "a.py"))
        self.assertEqual(targets("Write", {"file_path": f, "content": "x"}, self.d), [(f, "x")])
        self.assertEqual(targets("Edit", {"file_path": f, "new_string": "y"}, self.d), [(f, "y")])
        self.assertEqual([t for _, t in targets("MultiEdit", {"file_path": f, "edits": [{"new_string": "z"}]}, self.d)], ["z"])

    def test_ignored_env_file_is_where_secrets_belong(self):
        self.assertEqual(targets("Write", {"file_path": str(Path(self.d, ".env")), "content": "HUB_TOKEN=x"}, self.d), [])
        tracked = str(Path(self.d, ".env.example"))
        self.assertEqual(len(targets("Write", {"file_path": tracked, "content": "x"}, self.d)), 1)

    def test_commit_scans_the_staged_lines(self):
        Path(self.d, "k.txt").write_text("staged line\n")
        git(self.d, "add", "k.txt")
        found = dict(targets("Bash", {"command": f"git -C {self.d} commit -m x"}, "/"))
        self.assertIn("staged line", found["the files this commit adds"])

    def test_commit_dir(self):
        self.assertEqual(commit_dir("cd /home/user/brain && git commit -m x", "/w"), "/home/user/brain")
        self.assertEqual(commit_dir("git -C '/a b' commit", "/w"), "/a b")
        self.assertEqual(commit_dir("git commit -m x", "/w"), "/w")


if __name__ == "__main__":
    unittest.main()
