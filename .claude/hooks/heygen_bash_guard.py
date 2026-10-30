#!/usr/bin/env python3
"""PreToolUse hook on Bash: HeyGen generates only through the two gated MCP tools (create_speech and
create_video_from_avatar, D-T4). A command that calls HeyGen's API or upload host, its key, the heygen CLI, or a script
that reaches them (the media-use audio engine) is denied; the rules live in guards/heygen_bash.py. It fails closed.
"""
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from guards.deny import deny  # noqa: E402
from guards.heygen_bash import check  # noqa: E402


def main() -> int:
    try:
        data = json.loads(sys.stdin.read())
        cmd = data["tool_input"]["command"]
        if not isinstance(cmd, str):
            raise TypeError("command is not text")
        reasons = check(cmd, data.get("cwd") or os.getcwd())
    except Exception as e:  # fail closed
        reasons = [f"the HeyGen Bash guard could not check this call ({type(e).__name__}); it fails closed"]
    if reasons:
        print(deny("HEYGEN OUTSIDE THE GATE (growth-engine/production/standards.json models.heygen).\n- "
                   + "\n- ".join(reasons)
                   + "\nThe twin speaks and moves only through the gated HeyGen MCP tools create_speech and "
                     "create_video_from_avatar; voice, music and sound effects come from the gated Atlas command. "
                     "Read these scripts with the Read tool only."))
    return 0


if __name__ == "__main__":
    sys.exit(main())
