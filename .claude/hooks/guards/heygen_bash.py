"""Bash commands that reach HeyGen outside the generation gate (Twin reel machine plan T1). The only HeyGen calls that
may generate are the two gated MCP tools (create_speech, create_video_from_avatar). This denies a command that:
- names HeyGen's API or upload host, or its key or gateway variables, in any form atlas_text.forms reads (as written,
  joined, with its own shell variables and `$(echo ...)` filled in, printf escapes and base64 decoded);
- runs the `heygen` CLI (the media-use resolver's music and sound library, hyperframes cloud renders);
- runs a file (atlas_scripts.named_files) that names them, or whose relative imports reach one: the media-use audio
  engine (audio.mjs, heygen-tts.mjs, heygen-voice.mjs and lib/tts, bgm, sfx, heygen.mjs) calls the API directly.
A guardrail for cooperating sessions, like the Atlas guard: the main session still reviews every diff.
"""
from __future__ import annotations

import os
import re
from pathlib import Path

from guards.atlas_scripts import named_files
from guards.atlas_text import forms

HERE = Path(__file__).resolve().parent
DENY = ("api.heygen.com", "upload.heygen.com", "api-canary.heygen.com", "heygen_api_key", "heygen_api_base")
# the files that may name the host: this guard, its hook and its tests
TRUSTED = (HERE / "heygen_bash.py", HERE / "test_heygen_bash.py", HERE.parent / "heygen_bash_guard.py")
CLI = re.compile(r"(?:^|[;&|(\n]|&&|\|\|)\s*(?:\w+=\S*\s+)*(?:npx\s+(?:-y\s+|--yes\s+)*|bunx\s+|pnpm\s+dlx\s+)?"
                 r"(?:\S*/)?(?:@heygen/[\w.-]+|heygen)(?:@[\w.-]+)?(?=\s|$|;|&|\|)", re.I)
IMPORT = re.compile(r"""(?:\bfrom\s*|\bimport\s*\(?\s*|\brequire\s*\(\s*)["'](\.{1,2}/[^"']+)["']""")
CODE = (".mjs", ".js", ".cjs", ".ts", ".mts")


def hits(text: str) -> list[str]:
    fs = forms(text, decode=len(text) < (1 << 20))
    return [p for p in DENY if any(p in f for f in fs)]


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
        if h := hits(body):
            return [f"{f.name}: {', '.join(h)}"] if f == path else [f"{f.name} (imported by {path.name}): {', '.join(h)}"]
        if f.suffix in CODE:
            todo += _imports(f)
    return []


def check(cmd: str, cwd: str) -> list[str]:
    """Why the command is denied; empty when it may run."""
    why = []
    if h := hits(cmd):
        why.append(f"the command mentions {', '.join(h)}")
    if CLI.search(cmd):
        why.append("it runs the heygen CLI")
    run, trusted = named_files(cmd, cwd)
    for f in run + trusted:
        if f in TRUSTED or not os.path.isfile(f):
            continue
        for r in reaches(Path(f)):
            why.append(f"it runs {f}, which reaches HeyGen directly ({r})")
    return why
