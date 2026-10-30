"""The HeyGen Bash guard. Run: python3 -m unittest discover -s .claude/hooks/guards -p 'test_*.py'"""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from guards.heygen_bash import TRUSTED, check  # noqa: E402

HOOK = Path(__file__).resolve().parents[1] / "heygen_bash_guard.py"
REPO = Path(__file__).resolve().parents[3]
AUDIO = REPO / ".claude/skills/media-use/audio/scripts"


def bash(cmd: str, cwd: str = "/") -> str:
    r = subprocess.run([sys.executable, str(HOOK)], capture_output=True, text=True,
                       input=json.dumps({"tool_name": "Bash", "tool_input": {"command": cmd}, "cwd": cwd}))
    assert r.returncode == 0, r.stderr
    return json.loads(r.stdout)["hookSpecificOutput"]["permissionDecision"] if r.stdout else "allow"


class Commands(unittest.TestCase):
    def test_direct_routes_are_denied(self):
        for cmd in ("curl -H 'x-api-key: k' https://api.heygen.com/v3/voices/speech -d '{}'",
                    "curl -X PUT --data-binary @a.mp3 https://upload.heygen.com/v1/asset",
                    "python3 -c \"import urllib.request as u; u.urlopen('https://api.heygen.com/v2/video/generate')\"",
                    "echo $HEYGEN_API_KEY", "HEYGEN_API_BASE=https://x.example node run.mjs",
                    "h=api.hey; curl https://${h}gen.com/v3/x", "curl \"https://api.\"'heygen'\".com/v3/x\"",
                    "echo YXBpLmhleWdlbi5jb20= | base64 -d | xargs curl", "heygen auth login",
                    "npx -y @heygen/cli resolve bgm", "cd /tmp && heygen video create", "x=$(heygen video list)",
                    # any heygen.com or heygen.ai host with a network tool or a code runner
                    "curl -sS https://files2.heygen.ai/x.mp4 -o a.mp4", "wget https://resource.heygen.ai/v.mp4",
                    "python3 -c \"import requests; requests.get('https://app.heygen.com/x')\"",
                    "node -e \"fetch('https://api2.heygen.com/v1')\"", "echo 'curl api.heygen.com' | sh",
                    # credentials
                    "env | grep -i heygen", "printenv HEYGEN_API_KEY", "printenv | grep HEYGEN",
                    "cat ~/.heygen/credentials", "HEYGEN_API_URL=https://x.example npx hyperframes cloud render",
                    "echo $HYPERFRAMES_API_KEY", "cat /proc/self/environ",
                    # HeyGen-hosted hyperframes
                    "npx hyperframes render --cloud", "npx hyperframes render ./proj --quality high --cloud",
                    "hyperframes cloud render", "npx hyperframes publish", "npx -y hyperframes auth login",
                    "cd proj && npx hyperframes@0.4.1 cloud status"):
            with self.subTest(cmd=cmd):
                self.assertEqual(bash(cmd), "deny")

    def test_the_media_use_scripts_that_call_heygen_are_denied(self):
        for script in ("heygen-tts.mjs", "heygen-voice.mjs", "audio.mjs", "lib/tts.mjs", "lib/bgm.mjs",
                       "lib/heygen.mjs"):
            with self.subTest(script=script):
                self.assertEqual(bash(f"node {AUDIO / script} --text hi"), "deny")
        self.assertEqual(bash("node audio/scripts/audio.mjs build", cwd=str(REPO / ".claude/skills/media-use")), "deny")

    def test_a_script_that_imports_the_heygen_lib_is_denied(self):
        with tempfile.TemporaryDirectory() as d:
            (Path(d) / "lib").mkdir()
            (Path(d) / "lib" / "net.mjs").write_text('export const B = "https://api.heygen.com/v3";\n')
            (Path(d) / "mid.mjs").write_text('import { B } from "./lib/net.mjs";\nexport { B };\n')
            (Path(d) / "run.mjs").write_text('import { B } from "./mid.mjs";\nconsole.log(B);\n')
            why = check("node run.mjs", d)
            self.assertTrue(any("net.mjs" in w for w in why), why)

    def test_reading_and_ordinary_work_is_allowed(self):
        for cmd in ("ls .claude/skills/media-use/audio/scripts", "git status", "grep -n speech README.md",
                    "python3 growth-engine/tools/pipeline.py status acme AC-2026-10-W3-01",
                    "node .claude/skills/media-use/scripts/transcribe.mjs a.wav", "echo the heygen twin",
                    "ls ~/.heygen-notes",
                    # text that only mentions HeyGen
                    "git commit -m 'Deny api.heygen.com; heygen video create is off (curl too)'",
                    "git log --grep='heygen video'", "grep -rn api.heygen.com .claude/skills | head",
                    "grep -rn HEYGEN_API_KEY .claude/skills/media-use", "echo \"(heygen video)\"",
                    "echo '; heygen video create'", "npx hyperframes render ./proj -o out.mp4",
                    "npx hyperframes lint", "python3 x.py --note 'see https://docs.heygen.com'"):
            with self.subTest(cmd=cmd):
                self.assertEqual(bash(cmd, cwd=str(REPO)), "allow")

    def test_its_own_files_are_trusted(self):
        for f in TRUSTED:
            self.assertTrue(f.is_file(), f)
        self.assertEqual(bash("python3 -m unittest discover -s .claude/hooks/guards -t .claude/hooks", cwd=str(REPO)),
                         "allow")

    def test_unreadable_input_fails_closed(self):
        r = subprocess.run([sys.executable, str(HOOK)], input="not json", capture_output=True, text=True)
        self.assertEqual(json.loads(r.stdout)["hookSpecificOutput"]["permissionDecision"], "deny")


class Settings(unittest.TestCase):
    def test_the_guard_runs_on_bash_and_blocks_on_failure(self):
        hooks = json.loads((REPO / ".claude/settings.json").read_text())["hooks"]["PreToolUse"]
        e = next(e for e in hooks if any("heygen_bash_guard.py" in h["command"] for h in e["hooks"]))
        self.assertEqual(e["matcher"], "Bash")
        h = next(h for h in e["hooks"] if "heygen_bash_guard.py" in h["command"])
        self.assertEqual(h["onFailure"], "block")


if __name__ == "__main__":
    unittest.main()
