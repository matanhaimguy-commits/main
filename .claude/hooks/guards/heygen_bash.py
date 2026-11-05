"""Bash commands that reach HeyGen outside the generation gate (Twin reel machine plan T1). The only HeyGen calls that
may generate are the two gated MCP tools (create_speech, create_video_from_avatar). This denies a command that:
- names a HeyGen host (anything on heygen.com or heygen.ai) beside a network tool (curl, wget, an HTTP library) or a
  code runner (`| sh`, `python3 -c`, `node -e`, eval), outside git; in any form atlas_text.forms reads (joined, with
  its own shell variables and `$(echo ...)` filled in, printf escapes and base64 decoded);
- expands, sets or prints a HeyGen credential (HEYGEN_API_KEY, HEYGEN_API_BASE, HEYGEN_API_URL, HEYGEN_ACCESS_TOKEN,
  HYPERFRAMES_API_KEY), dumps the environment into a HeyGen grep, or reads ~/.heygen/credentials;
- runs the `heygen` CLI, or the HeyGen-hosted hyperframes commands (`render --cloud`, `cloud`, `publish`, `auth`);
- runs a file (atlas_scripts.named_files) that names the API host or a credential, or whose relative imports reach one:
  the media-use audio engine (audio.mjs, heygen-tts.mjs, heygen-voice.mjs and lib/tts, bgm, sfx, heygen.mjs).
Text that only mentions HeyGen (a commit message, a grep of the docs, an echo) passes.
A guardrail for cooperating sessions, like the Atlas guard: the main session still reviews every diff.
"""
from __future__ import annotations

import os
import re
from pathlib import Path

from guards.atlas_scripts import named_files
from guards.atlas_text import forms

HERE = Path(__file__).resolve().parent
# what a file may not name (its code calls the API): the API and upload hosts and the credentials
FILE_DENY = ("api.heygen.com", "upload.heygen.com", "api-canary.heygen.com", "heygen_api_key", "heygen_api_base")
HOST = re.compile(r"[a-z0-9.-]*heygen\.(?:com|ai)\b")
CRED = r"(?:heygen_api_key|heygen_api_base|heygen_api_url|heygen_access_token|hyperframes_api_key)"
CRED_USE = re.compile(r"\$\{?" + CRED + r"\b|(?:^|[\s;&|(])" + CRED + r"=|\.heygen/credentials|/proc/\S*environ", re.I)
ENV_DUMP = re.compile(r"\b(?:env|printenv|set|export\s+-p|declare\s+-x|compgen\s+-v)\b[^\n]*\|\s*(?:grep|rg|awk|sed)\b"
                      r"[^\n]*heygen|\bprintenv\s+\S*heygen", re.I)
NET = re.compile(r"\b(?:curl|wget|httpie|xh|aria2c|urllib\d?|requests|httpx|aiohttp|http\.client|fetch|axios|got|"
                 r"undici|nc|ncat|telnet|openssl|socket)\b", re.I)
RUNNER = re.compile(r"\|\s*(?:sh|bash|zsh|dash|python[\d.]*|node|perl|ruby|deno|bun)\b|\beval\b|\bexec\s*\(|\bsource\b"
                    r"|\b(?:python[\d.]*|node|perl|ruby|deno|bun|php)\s+(?:-\w*[ce]\b|--eval\b|-\s|-$)", re.I)
SEGMENT = re.compile(r"&&|\|\||[;\n]")
START = r"(?:^|&&|\|\||[;|\n]|\$\(|`)\s*(?:\w+=\S*\s+)*"
NPX = r"(?:npx\s+(?:-y\s+|--yes\s+)*|bunx\s+|pnpm\s+(?:dlx|exec)\s+|yarn\s+dlx\s+)?"
CLI = re.compile(START + NPX + r"(?:\S*/)?(?:@heygen/[\w.-]+|heygen)(?:@[\w.-]+)?(?=\s|$|;|&|\|)", re.I)
HF = re.compile(START + NPX + r"(?:\S*/)?hyperframes(?:@[\w.-]+)?\s+(?:[^;&|\n]*\s)?"
                r"(?:cloud\b|publish\b|auth\b|render\b[^;&|\n]*--cloud\b)", re.I)
QUOTED = re.compile(r"'[^']*'|\"(?:[^\"\\]|\\.)*\"")
SHELL_C = re.compile(r"\b(?:sh|bash|zsh|dash)\s+-\w*c\b|\beval\b", re.I)
TRUSTED = (HERE / "heygen_bash.py", HERE / "test_heygen_bash.py", HERE.parent / "heygen_bash_guard.py")
IMPORT = re.compile(r"""(?:\bfrom\s*|\bimport\s*\(?\s*|\brequire\s*\(\s*)["'](\.{1,2}/[^"']+)["']""")
CODE = (".mjs", ".js", ".cjs", ".ts", ".mts")


def file_hits(text: str) -> list[str]:
    fs = forms(text, decode=len(text) < (1 << 20))
    return [p for p in FILE_DENY if any(p in f for f in fs)]


def without_git(cmd: str) -> str:
    return " ; ".join(s for s in SEGMENT.split(cmd) if not re.match(r"\s*git\b", s))


def commands(cmd: str) -> str:
    """The command with quoted text blanked (a commit message or an echo), unless it runs text as code."""
    return cmd if SHELL_C.search(cmd) else QUOTED.sub("''", cmd)


def host_call(cmd: str) -> str | None:
    rest = without_git(cmd)
    if not (NET.search(rest) or RUNNER.search(rest)):
        return None
    for f in forms(rest):
        if m := HOST.search(f):
            return m.group(0)
    return None


def _imports(path: Path) -> list[Path]:
    try:
        body = path.read_text(errors="replace")
    except OSError:
        return []
    out = []
    for rel in IMPORT.findall(body):
        p = (path.parent / rel).resolve()
        for cand in (p, *(p.with_suffix(s) for s in CODE if not p.suffix)):
            if cand.is_file():
                out.append(cand)
                break
    return out


def reaches(path: Path, limit: int = 200) -> list[str]:
    """What the file, or a file its relative imports reach, names (empty: nothing)."""
    seen, todo = set(), [path]
    while todo and len(seen) < limit:
        f = todo.pop()
        if f in seen:
            continue
        seen.add(f)
        try:
            body = f.read_bytes()[: 4 << 20].decode("utf-8", "replace")
        except OSError:
            continue
        if h := file_hits(body):
            return [f"{f.name}: {', '.join(h)}"] if f == path else [f"{f.name} (imported by {path.name}): {', '.join(h)}"]
        if f.suffix in CODE:
            todo += _imports(f)
    return []


def check(cmd: str, cwd: str) -> list[str]:
    """Why the command is denied; empty when it may run."""
    why = []
    if h := host_call(cmd):
        why.append(f"it names the HeyGen host {h} beside a network tool or a code runner")
    rest = without_git(cmd)
    if any(CRED_USE.search(f) for f in forms(rest)):
        why.append("it uses or reads a HeyGen credential")
    if ENV_DUMP.search(rest):
        why.append("it prints the environment's HeyGen variables")
    code = commands(cmd)
    if CLI.search(code):
        why.append("it runs the heygen CLI")
    if HF.search(code):
        why.append("it runs a HeyGen-hosted hyperframes command (render --cloud, cloud, publish or auth)")
    run, trusted = named_files(cmd, cwd)
    for f in run + trusted:
        if f in TRUSTED or not os.path.isfile(f):
            continue
        for r in reaches(Path(f)):
            why.append(f"it runs {f}, which reaches HeyGen directly ({r})")
    return why
