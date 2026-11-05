#!/usr/bin/env python3
"""PreToolUse hook on every HeyGen connector tool: reads pass, the two twin tools are left to the generation gate, and
every other HeyGen tool is denied (guards/heygen_tools.py, standards.json heygen_connector). It fails closed."""
import json
import sys
from pathlib import Path

HOOKS = Path(__file__).resolve().parent
sys.path.insert(0, str(HOOKS))
from guards.deny import deny  # noqa: E402
from guards.heygen_tools import deny_reason  # noqa: E402


def main() -> int:
    try:
        data = json.loads(sys.stdin.read() or "{}")
        standards = json.loads((HOOKS.parents[1] / "growth-engine" / "production" / "standards.json").read_text())
        why = deny_reason(data.get("tool_name", ""), standards)
    except Exception as e:  # fail closed
        why = f"the HeyGen tools gate could not check this call ({type(e).__name__}); it fails closed"
    if why:
        print(deny(f"HEYGEN TOOL OFF: {why}"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
