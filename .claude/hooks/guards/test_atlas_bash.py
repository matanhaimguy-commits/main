"""The Atlas Bash guard. Run: python3 -m unittest discover -s .claude/hooks/guards -p 'test_*.py'"""
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from guards.atlas_bash import check  # noqa: E402
from guards.atlas_scripts import TRUSTED  # noqa: E402
from guards.atlas_text import squash  # noqa: E402

HOOK = Path(__file__).resolve().parents[1] / "atlas_bash_guard.py"
REPO = Path(__file__).resolve().parents[3]


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
                    "npm install -g atlascloud-cli", "echo $ATLASCLOUD_API_KEY",
                    "ATLAS_REAL_BIN=/tmp/stub atlas generate image m -p x",
                    "node references/atlas-cloud-skills/skills/seedance-2-5-skill/scripts/generate.mjs cfg.json",
                    "node scripts/providers/atlas-rest.mjs", "cat ~/.config/atlas-cli/auth.json", "npx atlas-mcp"):
            with self.subTest(cmd=cmd):
                self.assertEqual(bash(cmd), "deny")

    def test_the_cheap_disguises_are_denied(self):
        for cmd in ("python3 -c \"h='api.atlas' + 'cloud.ai'; print(h)\"", "python3 -c \"h='api.atlas' 'cloud.ai'\"",
                    "curl https://api.atlas\"\"cloud.ai/x",
                    # a shell variable
                    "H=atlas; curl https://api.${H}cloud.ai/x", "a=atl; b=ascloud; curl https://api.$a$b.ai/v1",
                    "D=/usr/local/lib/atl; ${D}as-cli/atlas generate image m",
                    # $(echo ...) and backticks
                    "curl https://api.$(echo atlas)$(echo cloud).ai/x", "curl https://api.`echo atlas``echo cloud`.ai",
                    # base64 and printf escapes
                    "curl https://$(echo YXBpLmF0bGFzY2xvdWQuYWk= | base64 -d)/v1",
                    "echo Y3VybCBodHRwczovL2V4YW1wbGU= | base64 -d | sh",
                    "curl \"https://$(printf 'api.\\x61tlascloud.ai')/v1\"", "curl https://$'\\x61pi.atlascloud.ai'",
                    "printf '\\143\\165\\162\\154' | bash",
                    # a wildcard on the binary or the login
                    "/usr/local/lib/atlas*/atlas generate image m", "/usr/local/lib/*/atlas generate video m",
                    "/usr/*/lib/atl?s-cli/* generate image m", "cat ~/.config/atl*/auth.json",
                    # find -exec and xargs
                    "find /usr/local/lib -name atlas -type f -exec {} generate image m \\;",
                    "find / -perm -u+x -name 'atl*' | xargs -I{} {} generate image m",
                    # a % join inside python -c
                    "python3 -c \"import urllib.request as u; u.urlopen('https://api.atlas%s.ai' % 'cloud')\"",
                    "python3 -c \"import requests; requests.post('https://api.{}.ai'.format('atlas'+'cloud'))\""):
            with self.subTest(cmd=cmd):
                self.assertEqual(bash(cmd), "deny")

    def test_the_wrapper_and_its_free_commands_are_allowed(self):
        for cmd in ("atlas generate video m -p x --images https://cdn.example/a.jpg",
                    "/usr/local/bin/atlas generate cost image m -p x", "atlas models list --json",
                    "atlas account balance", "atlas generate get abc", "bash growth-engine/tools/atlas/setup.sh",
                    "bash references/fetch.sh", "python3 -m unittest growth-engine/tools/test_atlas_gate.py 2>&1 | tail -3",
                    "python3 -m unittest discover -s .claude/hooks/guards -p 'test_*.py'",
                    "python3 growth-engine/tools/pipeline.py check-call atlas_generate x.json",
                    "cat growth-engine/tools/atlas/README.md", "ls -la growth-engine/tools/atlas", "git status",
                    "git commit -m 'Atlas gate: see https://claude.ai/code'", "curl -s https://example.com"):
            with self.subTest(cmd=cmd):
                self.assertEqual(bash(cmd, str(REPO)), "allow")

    def test_unreadable_input_is_denied(self):
        for raw in ("", "not json", "[]", '{"tool_input": {}}', '{"tool_input": {"command": 3}}'):
            with self.subTest(raw=raw):
                self.assertEqual(decision(raw), "deny")

    def test_squash_joins_split_words(self):
        self.assertIn("api.atlascloud.ai", squash("'API.Atlas' + \"cloud.ai\""))


class Scripts(unittest.TestCase):
    def test_a_script_that_names_the_api_is_denied_however_it_runs(self):
        with tempfile.TemporaryDirectory() as t:
            Path(t, "x.py").write_text("import urllib.request\nurllib.request.urlopen('https://api.atlascloud.ai/v1')\n")
            Path(t, "mod.py").write_text("H = 'YXBpLmF0bGFzY2xvdWQuYWk='\n")
            Path(t, "ok.py").write_text("print('hello')\n")
            run = Path(t, "run.sh")
            run.write_text("#!/bin/sh\ncurl https://api.atlascloud.ai/x\n")
            os.chmod(run, 0o755)
            for cmd in ("python3 x.py", "python3 -u x.py", "python3 < x.py", f"cd /tmp && python3 {t}/x.py", "./run.sh",
                        "cat x.py | python3", "cat x.py | python3 -", "python3 -m mod", "sh -c \"$(cat run.sh)\"",
                        "cp x.py y.py && python3 y.py"):
                with self.subTest(cmd=cmd):
                    self.assertEqual(bash(cmd, t), "deny")
            self.assertEqual(bash("python3 ok.py", t), "allow")
            self.assertEqual(bash("cat x.py", t), "allow", "reading a file is not running it")

    def test_copying_a_trusted_file_is_denied(self):
        for cmd in ("cp growth-engine/tools/atlas/atlas_gate.py /tmp/g.py && python3 /tmp/g.py generate image m",
                    "cat growth-engine/tools/atlas/setup.sh > /tmp/s.sh", "ln -s references/fetch.sh /tmp/f.sh"):
            with self.subTest(cmd=cmd):
                self.assertEqual(bash(cmd, str(REPO)), "deny")

    def test_only_the_named_files_are_trusted(self):
        self.assertEqual({str(p.relative_to(REPO)) for p in TRUSTED if p.is_relative_to(REPO)}, {
            "growth-engine/tools/atlas/atlas_gate.py", "growth-engine/tools/atlas/setup.sh",
            "growth-engine/tools/test_atlas_gate.py", ".claude/hooks/guards/atlas_text.py",
            ".claude/hooks/guards/atlas_bash.py", ".claude/hooks/guards/test_atlas_bash.py", "references/fetch.sh"})
        self.assertIn(Path("/usr/local/bin/atlas"), TRUSTED)
        for p in TRUSTED:
            if p.is_relative_to(REPO):
                self.assertTrue(p.is_file(), p)

    def test_a_new_script_in_the_gate_folders_is_not_trusted(self):
        for d in (REPO / "growth-engine" / "tools", REPO / ".claude" / "hooks"):
            with tempfile.NamedTemporaryFile("w", suffix=".py", dir=d, delete=False) as f:
                f.write("import urllib.request\nurllib.request.urlopen('https://api.atlascloud.ai/v1')\n")
            try:
                with self.subTest(dir=d):
                    self.assertTrue(check(f"python3 {f.name}", str(REPO)))
            finally:
                os.unlink(f.name)


if __name__ == "__main__":
    unittest.main()
