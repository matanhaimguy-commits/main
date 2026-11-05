"""The files a Bash command may run, for the Atlas Bash guard, and the few files trusted to name Atlas.

When the command starts an interpreter anywhere (`python3 x.py`, `cat x.py | python3`, `python3 - < x.py`, `sh -c
"$(cat x)"`, `cp a.py b.py && python3 b.py`), every existing file it names is read, plus the module of `python -m`
and the test files of `unittest discover -s DIR`. An executable file named anywhere is read too.
"""
from __future__ import annotations

import os
import re
import shlex
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
# the only files that may name Atlas's binary, host or scripts: the gate, its installer and wrapper, their tests,
# this guard, and the reference fetcher (it clones the Atlas skills for reading). Kept in step by test_atlas_bash.py.
TRUSTED = tuple(REPO / p for p in (
    "growth-engine/tools/atlas/atlas_gate.py", "growth-engine/tools/atlas/setup.sh",
    "growth-engine/tools/test_atlas_gate.py", ".claude/hooks/guards/atlas_text.py",
    ".claude/hooks/guards/atlas_bash.py", ".claude/hooks/guards/test_atlas_bash.py", "references/fetch.sh",
)) + (Path("/usr/local/bin/atlas"),)
INTERPRETER = re.compile(r"(python[\d.]*|node|nodejs|bash|sh|zsh|dash|ksh|ruby|perl|php|deno|bun|tsx|ts-node|source|\.)")
PIECE = re.compile(r"[^\s'\"`$()<>|;&]+")
COPY = re.compile(r"(^|[\s;&|(])(cp|mv|install|ln|rsync|dd|tee|ditto)\b|(?<![\d&>])>>?(?!&)")


def words(cmd: str) -> list[str]:
    try:
        lex = shlex.shlex(cmd, posix=True, punctuation_chars=True)
        lex.whitespace_split = True
        return list(lex)
    except ValueError:
        return cmd.split()


def resolve(word: str, cwd: str) -> Path | None:
    p = Path(os.path.expanduser(word))
    p = p if p.is_absolute() else Path(cwd) / p
    try:
        real = p.resolve()
        return real if real.is_file() else None
    except OSError:
        return None


def runs_code(ws: list[str]) -> bool:
    return any(INTERPRETER.fullmatch(os.path.basename(w)) for w in ws)


def _module(name: str, cwd: str) -> list[Path]:
    base = Path(cwd, *name.split("."))
    return [p for p in (base.with_suffix(".py"), base / "__main__.py") if p.is_file()]


def _discover(ws: list[str], cwd: str) -> list[Path]:
    if "discover" not in ws:
        return []
    start = ws[ws.index("-s") + 1] if "-s" in ws[:-1] else "."
    pat = ws[ws.index("-p") + 1] if "-p" in ws[:-1] else "test*.py"
    return sorted(Path(cwd, start).glob(pat))


def named_files(cmd: str, cwd: str) -> tuple[list[Path], list[Path]]:
    """(files to read, trusted files the command names)."""
    ws, found = words(cmd), []
    code = runs_code(ws)
    for i, w in enumerate(ws):
        if code and w == "-m" and i + 1 < len(ws):
            found += _module(ws[i + 1], cwd)
    for w in dict.fromkeys(ws + PIECE.findall(cmd)):          # pieces: the words inside "$(cat x)" and `cat x`
        real = resolve(w, cwd)
        if real and (code or os.access(real, os.X_OK)):
            found.append(real)
    if code:
        found += _discover(ws, cwd)
    found = list(dict.fromkeys(p.resolve() for p in found))
    return [p for p in found if p not in TRUSTED], [p for p in found if p in TRUSTED]


def copies_trusted(cmd: str, cwd: str) -> list[Path]:
    """Trusted files a command copies, links or redirects (a copy is not on the list, but would run its code)."""
    if not COPY.search(cmd):
        return []
    named = [resolve(w, cwd) for w in words(cmd)]
    return [p for p in dict.fromkeys(named) if p in TRUSTED]
