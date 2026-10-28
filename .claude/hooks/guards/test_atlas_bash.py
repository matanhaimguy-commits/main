"""The Atlas Bash guard. Run: python3 -m unittest discover -s .claude/hooks/guards -p 'test_*.py'"""
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from guards.atlas_bash import check, squash  # noqa: E402

HOOK = Path(__file__).resolve().parents[1] / "atlas_bash_guard.py"


def decision(raw: str) -> str:
    r = subprocess.run([sys.executable, str(HOOK)], input=raw, capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    return json.loads(r.stdout)["hookSpecificOutput"]["permissionDecision"] if r.stdout else "allow"


def bash(cmd: str, cwd: str = "/") -> str:
    return decision(json.dumps({"tool_name": "Bash", "tool_input": {"command": cmd}, "cwd": cwd}))


class Commands(unittest.TestCase):
    def test_direct_routes_are_denied(self):
        for cmd in ("/usr/local/lib/atlas-cli/atlas generate video m -p x",
                    "cp /usr/local/lib/atlas-cli/atlas /tmp/a && /tmp/a generate image m",
                    "curl -H 'Authorization: Bearer x' https://api.atlascloud.ai/api/v1/model/generateVideo",
                    "python3 -c \"import urllib.request as u; u.urlopen('https://api.atlascloud.ai/api/v1/x')\"",
                    "python3 -c \"h='api.atlas' + 'cloud.ai'; print(h)\"",
                    "python3 -c \"h='api.atlas' 'cloud.ai'\"", "curl https://api.atlas\"\"cloud.ai/x",
                    "H=atlas; curl https://api.${H}cloud.ai/x",
                    "npm install -g atlascloud-cli", "echo $ATLASCLOUD_API_KEY",
                    "ATLAS_REAL_BIN=/tmp/stub atlas generate image m -p x",
                    "node references/atlas-cloud-skills/skills/seedance-2-5-skill/scripts/generate.mjs cfg.json",
                    "node scripts/providers/atlas-rest.mjs", "cat ~/.config/atlas-cli/auth.json", "npx atlas-mcp"):
            with self.subTest(cmd=cmd):
                self.assertEqual(bash(cmd), "deny")

    def test_the_wrapper_and_its_free_commands_are_allowed(self):
        for cmd in ("atlas generate video m -p x", "/usr/local/bin/atlas generate cost image m -p x",
                    "atlas models list --json", "atlas account balance", "atlas generate get abc",
                    "bash growth-engine/tools/atlas/setup.sh", "ls -la", "git status"):
            with self.subTest(cmd=cmd):
                self.assertEqual(bash(cmd, str(Path(__file__).resolve().parents[3])), "allow")

    def test_unreadable_input_is_denied(self):
        for raw in ("", "not json", "[]", '{"tool_input": {}}', '{"tool_input": {"command": 3}}'):
            with self.subTest(raw=raw):
                self.assertEqual(decision(raw), "deny")

    def test_squash_joins_split_words(self):
        self.assertIn("api.atlascloud.ai", squash("'API.Atlas' + \"cloud.ai\""))


class Scripts(unittest.TestCase):
    def test_a_script_that_names_the_api_is_denied(self):
        with tempfile.TemporaryDirectory() as t:
            Path(t, "x.py").write_text("import urllib.request\nurllib.request.urlopen('https://api.atlascloud.ai/v1')\n")
            Path(t, "ok.py").write_text("print('hello')\n")
            run = Path(t, "run.sh")
            run.write_text("#!/bin/sh\ncurl https://api.atlascloud.ai/x\n")
            os.chmod(run, 0o755)
            for cmd in ("python3 x.py", "python3 -u x.py", "python3 < x.py", f"cd /tmp && python3 {t}/x.py", "./run.sh"):
                with self.subTest(cmd=cmd):
                    self.assertEqual(bash(cmd, t), "deny")
            self.assertEqual(bash("python3 ok.py", t), "allow")
            self.assertEqual(bash("cat x.py", t), "allow", "reading a file is not running it")

    def test_the_gates_own_code_is_trusted(self):
        repo = Path(__file__).resolve().parents[3]
        self.assertEqual(check("python3 growth-engine/tools/atlas/atlas_gate.py --help", str(repo)), [])


if __name__ == "__main__":
    unittest.main()
