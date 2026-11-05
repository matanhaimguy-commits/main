#!/usr/bin/env bash
# Installs the generation gate (VISUAL-QA.md section 9.2) for a session whose project root is NOT this repo
# (cloud sessions rooted one level up, e.g. /home/user with the repo at /home/user/main).
# A session rooted at the repo already loads .claude/settings.json from the repo.
# After installing, prove it: call mcp__Higgs__generate_image with prompt "GATE-SELFTEST" (any model); the gate
# must block it with "self-test: the production gate is live". If it doesn't, open /hooks once or restart the session.
set -euo pipefail
REPO="$(cd "$(dirname "$0")/../.." && pwd)"
TARGET="${1:-$(dirname "$REPO")}/.claude/settings.json"
mkdir -p "$(dirname "$TARGET")"
python3 - "$REPO" "$TARGET" <<'PY'
import json, sys
from pathlib import Path
repo, target = Path(sys.argv[1]), Path(sys.argv[2])
src = json.loads((repo / ".claude" / "settings.json").read_text())
hook = src["hooks"]["PreToolUse"][0]
hook = json.loads(json.dumps(hook))
hook["hooks"][0]["command"] = f"python3 {repo}/.claude/hooks/generation_gate.py"
cur = json.loads(target.read_text()) if target.exists() else {}
pre = cur.setdefault("hooks", {}).setdefault("PreToolUse", [])
pre[:] = [h for h in pre if "generation_gate.py" not in json.dumps(h)] + [hook]
target.write_text(json.dumps(cur, indent=2) + "\n")
print(f"gate hook installed in {target}")
PY
