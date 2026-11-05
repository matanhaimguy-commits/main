#!/usr/bin/env python3
"""PreToolUse hook: blocks a tool call that would write a secret into a file, a command or a git commit.

The checks live in guards/ (secret_patterns, secret_scan, secret_targets). Secrets belong in the cloud environment's
secrets or in an ignored .env file. If the check itself breaks, it warns and lets the call through.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from guards.deny import deny, warn  # noqa: E402
from guards.secret_scan import scan  # noqa: E402
from guards.secret_targets import targets  # noqa: E402


def main() -> int:
    try:
        data = json.loads(sys.stdin.read() or "{}")
        hits = []
        for where, text in targets(data.get("tool_name", ""), data.get("tool_input") or {}, data.get("cwd") or "."):
            hits += [f"{f['kind']} ({f['preview']}) in {where}" for f in scan(text)]
    except Exception as e:  # never block all work on a guard bug
        print(warn(f"secret guard could not run ({type(e).__name__}: {e}); check .claude/hooks/guards/"))
        return 0
    if hits:
        print(deny("SECRET BLOCKED: this would put a secret where it can leak (the main repo is public).\n- "
                   + "\n- ".join(hits)
                   + "\nRead it from the environment instead (cloud environment secrets, or an ignored .env file), "
                     "and never paste it into a file, a command or a note."))
    return 0


if __name__ == "__main__":
    sys.exit(main())
