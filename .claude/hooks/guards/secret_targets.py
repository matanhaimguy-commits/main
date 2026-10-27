"""What text a tool call would put on disk or into git: Write/Edit content, a Bash command, a commit's added lines.

An ignored env file (.env, .env.local, .dev.vars) is where secrets belong, so writing one is not scanned.
"""
import re
import subprocess
from pathlib import Path

ENV_NAMES = re.compile(r"^(\.env(\..+)?|\.dev\.vars)$")
GIT_COMMIT = re.compile(r"\bgit\b[^;&|]*\bcommit\b")


def _git(args: list[str], cwd: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True, timeout=20)


def ignored_env_file(path: str) -> bool:
    p = Path(path)
    if not ENV_NAMES.match(p.name):
        return False
    r = _git(["check-ignore", "-q", str(p)], str(p.parent if p.parent.exists() else Path.cwd()))
    return r.returncode in (0, 128)  # ignored, or not inside a git work tree at all


def commit_dir(command: str, cwd: str) -> str:
    m = re.search(r"\bgit\s+-C\s+(\"[^\"]+\"|'[^']+'|\S+)", command) or re.match(r"\s*cd\s+(\"[^\"]+\"|'[^']+'|\S+)\s*&&", command)
    return m.group(1).strip("\"'") if m else cwd


def added_lines(command: str, cwd: str) -> str:
    """The lines a `git commit` in this command would add: staged, plus unstaged tracked changes with -a/--all."""
    d = commit_dir(command, cwd)
    diffs = [_git(["diff", "--cached", "-U0", "--no-color"], d).stdout]
    if re.search(r"\bcommit\b[^;&|]*(\s-[a-zA-Z]*a[a-zA-Z]*\b|\s--all\b)", command):
        diffs.append(_git(["diff", "-U0", "--no-color"], d).stdout)
    return "\n".join(l[1:] for diff in diffs for l in diff.splitlines() if l.startswith("+") and not l.startswith("+++"))


def targets(tool: str, data: dict, cwd: str) -> list[tuple[str, str]]:
    """(where, text) pairs to scan for this call."""
    if tool in ("Write", "Edit", "MultiEdit", "NotebookEdit"):
        path = data.get("file_path") or data.get("notebook_path") or "?"
        if ignored_env_file(path):
            return []
        texts = [data.get("content"), data.get("new_string"), data.get("new_source")]
        texts += [e.get("new_string") for e in data.get("edits") or []]
        return [(path, t) for t in texts if t]
    if tool == "Bash":
        cmd = data.get("command") or ""
        out = [("the Bash command", cmd)]
        if GIT_COMMIT.search(cmd):
            out.append(("the files this commit adds", added_lines(cmd, cwd)))
        return out
    return []
