"""Bash commands that reach Atlas Cloud without the gated `atlas` wrapper (growth-engine/tools/atlas/README.md).

Denied: the real binary and its stored login (`atlas-cli`), the API host and the key (`atlascloud`, `cloud.ai`), the
test-stub switch (`ATLAS_REAL_BIN`), the Atlas skills' scripts and other installs. The match also runs on the command
with quotes and `+` joins taken out ("api.atlas" + "cloud.ai"), and on the script files the command runs (after an
interpreter or `<`, or an executable file), except the gate's own code. The wrapper `/usr/local/bin/atlas` and plain
`atlas` are allowed: the wrapper gates the billable commands itself. A text match: a script that builds the host from
pieces at run time still gets through.
"""
from __future__ import annotations

import os
import re
import shlex
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
DENY = ("atlas-cli", "atlascloud", "cloud.ai", "atlas_real_bin", "atlas-cloud-skills", "atlas-rest", "atlas-mcp")
TRUSTED_DIRS = (REPO / "growth-engine" / "tools", REPO / ".claude" / "hooks")
TRUSTED_FILES = (Path("/usr/local/bin/atlas"),)     # the wrapper setup.sh writes; it names the real binary
INTERPRETER = re.compile(r"(python[\d.]*|node|nodejs|bash|sh|zsh|dash|ksh|ruby|perl|php|deno|bun|tsx|ts-node|source|\.)")
MAX_READ = 4 << 20


def squash(text: str) -> str:
    """Lower case, with the quote and `+` joins a command can split a word with taken out."""
    t = re.sub(r"""(['"`])\s*\+?\s*(['"`])""", "", text.lower())
    t = re.sub(r"\s*\+\s*", "", t)
    return re.sub(r"""['"`\\]""", "", t)


def hits(text: str) -> list[str]:
    low, flat = text.lower(), squash(text)
    return [p for p in DENY if p in low or p in flat]


def words(cmd: str) -> list[str]:
    try:
        lex = shlex.shlex(cmd, posix=True, punctuation_chars=True)
        lex.whitespace_split = True
        return list(lex)
    except ValueError:
        return cmd.split()


def trusted(path: Path) -> bool:
    return path in TRUSTED_FILES or any(path.is_relative_to(d) for d in TRUSTED_DIRS)


def scripts(cmd: str, cwd: str) -> list[Path]:
    """Files the command runs: the word after an interpreter (flags skipped) or `<`, and any executable file named."""
    ws, found = words(cmd), []
    for i, w in enumerate(ws):
        cands = [w]
        if INTERPRETER.fullmatch(os.path.basename(w)) or w == "<":
            cands += [x for x in ws[i + 1:i + 4] if not x.startswith("-")][:1]
        for c in cands:
            p = Path(os.path.expanduser(c))
            p = p if p.is_absolute() else Path(cwd) / p
            try:
                real = p.resolve()
                if real.is_file() and (c != w or os.access(real, os.X_OK)) and not trusted(real):
                    found.append(real)
            except OSError:
                continue
    return found


def check(cmd: str, cwd: str) -> list[str]:
    """Why the command is denied; empty when it may run."""
    why = [f"the command mentions {', '.join(h)}"] if (h := hits(cmd)) else []
    for f in scripts(cmd, cwd):
        try:
            with open(f, "rb") as fh:
                body = fh.read(MAX_READ).decode("utf-8", "replace")
        except OSError as e:
            why.append(f"can't read {f} to check it ({e.strerror})")
            continue
        if h := hits(body):
            why.append(f"{f} mentions {', '.join(h)}")
    return why
