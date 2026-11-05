#!/usr/bin/env python3
"""PreToolUse hook on Bash: Atlas Cloud runs only through the gated `atlas` command. A command that calls the real
binary, the API host, the key, the stored login, the Atlas skills' scripts or another install is denied; the rules live
in guards/atlas_bash.py. It fails closed: input it can't read, or a check that errors, is denied.
"""
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from guards.atlas_bash import check  # noqa: E402
from guards.deny import deny  # noqa: E402


def main() -> int:
    try:
        data = json.loads(sys.stdin.read())
        cmd = data["tool_input"]["command"]
        if not isinstance(cmd, str):
            raise TypeError("command is not text")
        reasons = check(cmd, data.get("cwd") or os.getcwd())
    except Exception as e:  # fail closed
        reasons = [f"the Atlas Bash guard could not check this call ({type(e).__name__}); it fails closed"]
    if reasons:
        print(deny("ATLAS OUTSIDE THE GATE (growth-engine/tools/atlas/README.md).\n- " + "\n- ".join(reasons)
                   + "\nUse the `atlas` wrapper; never the real binary, the API, the key, the stored login or the Atlas "
                     "skills' scripts (read those with the Read tool only)."))
    return 0


if __name__ == "__main__":
    sys.exit(main())
