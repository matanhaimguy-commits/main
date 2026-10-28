"""Bash commands that reach Atlas Cloud without the gated `atlas` wrapper (growth-engine/tools/atlas/README.md).

A guardrail for cooperating sessions, not a sandbox: the real controls are that only the gated wrapper is documented
and that the main session reviews every diff. It denies a command that:
- names the real binary or its login (`atlas-cli`), the API host or key (`atlascloud`, `cloud.ai`), the test-stub
  switch `ATLAS_REAL_BIN`, the Atlas skills' scripts or `atlas-mcp`, in any form atlas_text.py reads (as written,
  joined, with its own shell variables and `$(echo …)` filled in, printf escapes and base64 decoded);
- names `atlas` beside a network call or a code runner, outside the wrapper's own command and git;
- runs decoded text as code (`base64 -d | sh`, `exec(b64decode(...))`);
- uses a wildcard that matches the real binary or the login, or `find -exec` / `xargs` near them;
- runs or copies a file (atlas_scripts.py) that names them, except the few trusted files.
Not closed by text matching: a program that builds the host at run time from pieces that carry no `atlas` (character
codes, a file it reads, an environment variable set in an earlier command), and code a trusted-looking program loads.
"""
from __future__ import annotations

import fnmatch
import os
import re

from guards.atlas_scripts import copies_trusted, named_files, words
from guards.atlas_text import forms, hits, squash

PROTECTED = ("/usr/local/lib/atlas-cli/atlas", "/usr/local/lib/atlas-cli", os.path.expanduser("~/.config/atlas-cli"),
             os.path.expanduser("~/.config/atlas-cli/auth.json"))
NET = re.compile(r"\b(curl|wget|https?|urllib\d?|requests|httpx|aiohttp|socket|fetch|axios|nc|ncat|telnet|openssl)\b")
RUNNER = re.compile(r"\|\s*(sh|bash|zsh|dash|python[\d.]*|node|perl|ruby)\b|\beval\b|\bexec\s*\(|\bsource\b")
DECODE = re.compile(r"base64\s+(-\w*d\w*|--decode)|b64decode|fromhex|xxd\s+-r|codecs\.decode|\\x[0-9a-f]{2}|\\[0-7]{3}")
FIND = re.compile(r"\bfind\b.*\s-(exec|execdir|ok|okdir)\b|\bxargs\b")
WRAPPER = re.compile(r"^\s*(/usr/local/bin/)?atlas(\s|$)")
SEGMENT = re.compile(r"&&|\|\||[;|\n]")
OWN_PATHS = re.compile(r"\S*growth-engine/tools/atlas\b\S*|\S*test_atlas_\w+(\.py)?|\S*atlas_(rules|calls|gate)(\.py)?\b|"
                       r"atlas_generate")


def residual(cmd: str) -> str:
    """The command without the wrapper's own commands, git, and the repo's Atlas files named by path."""
    keep = [s for s in SEGMENT.split(cmd) if not WRAPPER.match(s) and not re.match(r"\s*git\b", s)]
    return OWN_PATHS.sub(" ", " ".join(keep))


def wildcard_hits(cmd: str, cwd: str) -> list[str]:
    out = []
    for w in words(cmd):
        if not re.search(r"[*?\[]", w):
            continue
        pat = w if os.path.isabs(os.path.expanduser(w)) else os.path.join(cwd, w)
        pat = os.path.expanduser(pat)
        out += [p for p in PROTECTED if fnmatch.fnmatch(p, pat) or fnmatch.fnmatch(p, pat.rstrip("/") + "/*")]
    return out


def check(cmd: str, cwd: str) -> list[str]:
    """Why the command is denied; empty when it may run."""
    why = []
    if h := hits(cmd):
        why.append(f"the command mentions {', '.join(h)}")
    rest = residual(cmd)
    if any("atlas" in f for f in forms(rest)) and (NET.search(rest.lower()) or RUNNER.search(rest)):
        why.append("it names atlas beside a network call or a code runner (only the `atlas` wrapper may)")
    if DECODE.search(cmd.lower()) and RUNNER.search(cmd):
        why.append("it runs decoded text as code")
    if w := wildcard_hits(cmd, cwd):
        why.append(f"a wildcard matches {', '.join(dict.fromkeys(w))}")
    if FIND.search(cmd) and ("atlas" in squash(cmd) or re.search(r"\s(/|/usr|/usr/local|/usr/local/lib)/?(\s|$)", cmd)):
        why.append("find -exec or xargs near the Atlas install")
    for f in copies_trusted(cmd, cwd):
        why.append(f"it copies or redirects {f}, which may name Atlas only where it is")
    run, _ = named_files(cmd, cwd)
    for f in run:
        try:
            with open(f, "rb") as fh:
                body = fh.read(4 << 20).decode("utf-8", "replace")
        except OSError as e:
            why.append(f"can't read {f} to check it ({e.strerror})")
            continue
        if h := hits(body, decode=len(body) < (1 << 20)):
            why.append(f"{f} mentions {', '.join(h)}")
    return why
