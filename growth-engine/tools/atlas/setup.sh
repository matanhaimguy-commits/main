#!/usr/bin/env bash
# Installs the Atlas Cloud CLI (pinned 0.1.38) behind the production gate. Idempotent: run it as the cloud
# environment's Setup script (before Claude Code starts) and again by hand at any time.
#
#   bash growth-engine/tools/atlas/setup.sh [LOCAL]
#
# LOCAL (optional, for offline installs): the release tarball cli_0.1.38_linux_<arch>.tar.gz, the `atlas` binary from
# it, or a folder holding either. Every source is checked against the pinned sha256 before anything is installed.
#
# Result: the real CLI at /usr/local/lib/atlas-cli/atlas (not on PATH) and the gated wrapper at /usr/local/bin/atlas,
# which runs growth-engine/tools/atlas/atlas_gate.py from /home/user/main (README.md in this folder). Sign-in: if the CLI
# holds no login, it logs in with ATLASCLOUD_API_KEY when that is set, else with the placeholder "network-secret" (the
# session's proxy puts the real key on every request to api.atlascloud.ai). The key is never printed.
# Exit 1 when the gate is not live, the login failed, or another `atlas` comes first on PATH (it would skip the gate).
set -euo pipefail

VERSION=0.1.38
PREFIX="${ATLAS_PREFIX:-/usr/local}"         # tests install into a temp folder
REAL_DIR="$PREFIX/lib/atlas-cli"
REAL="$REAL_DIR/atlas"
WRAPPER="$PREFIX/bin/atlas"
export ATLAS_TELEMETRY=0 ATLAS_AUTO_UPDATE=0 DO_NOT_TRACK=1

REPO="$(cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")/../../.." && pwd)"
GATE="$REPO/growth-engine/tools/atlas/atlas_gate.py"

say() { printf '%s\n' "$*"; }
die() { printf 'atlas setup: %s\n' "$*" >&2; exit 1; }

[ "$(uname -s)" = Linux ] || die "Linux only (this is $(uname -s))"
case "$(uname -m)" in
  x86_64|amd64)
    ARCH=amd64
    TAR_SHA=b7fcf0b13abfe1ef47062b92d7cc9c3010a4b9f5092953499106b1c364ec01d1
    BIN_SHA=5eaa4df913d9f021dac341a3754e05a6ea8221f6490da5e0a568261e7630c1db ;;
  aarch64|arm64)
    ARCH=arm64
    TAR_SHA=e7a68435644abc127ec8e0e617ed6170568614be9ece0073b5234b5c9238767c
    BIN_SHA=b3e6c66d96e1d26db9dbe4d1bc8478f7051ffa763fa2ff88dfb816748e19f148 ;;
  *) die "unsupported CPU $(uname -m) (amd64 and arm64 only)" ;;
esac
TARBALL="cli_${VERSION}_linux_${ARCH}.tar.gz"
URL="https://github.com/AtlasCloudAI/cli/releases/download/v${VERSION}/${TARBALL}"
[ -f "$GATE" ] || die "the gate is missing: $GATE"

SUDO=""
if [ "$(id -u)" -ne 0 ]; then
  command -v sudo >/dev/null 2>&1 || die "run as root (it writes /usr/local)"
  SUDO="sudo -n"
fi

sha() { sha256sum "$1" | cut -d' ' -f1; }
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

# A pinned binary from a tarball (checked before it is opened) or a bare binary; prints its path, or nothing.
from_tarball() {
  [ "$(sha "$1")" = "$TAR_SHA" ] || { say "  skip $1: sha256 is not the pinned $TARBALL" >&2; return 0; }
  mkdir -p "$TMP/x"
  tar -xzf "$1" -C "$TMP/x" atlas
  from_binary "$TMP/x/atlas"
}
from_binary() {
  [ "$(sha "$1")" = "$BIN_SHA" ] || { say "  skip $1: sha256 is not the pinned atlas $VERSION ($ARCH)" >&2; return 0; }
  printf '%s\n' "$1"
}
from_local() {
  local p="$1" f out
  if [ -d "$p" ]; then
    for f in "$p/atlas" "$p/$TARBALL" "$p/cli.tar.gz"; do
      [ -f "$f" ] || continue
      case "$f" in *.tar.gz) out="$(from_tarball "$f")" ;; *) out="$(from_binary "$f")" ;; esac
      if [ -n "$out" ]; then printf '%s\n' "$out"; return 0; fi
    done
  elif [ -f "$p" ]; then
    if gzip -t "$p" 2>/dev/null; then from_tarball "$p"; else from_binary "$p"; fi
  else
    die "no such file or folder: $p"
  fi
}

# 1. the real CLI
if [ -x "$REAL" ] && [ "$(sha "$REAL")" = "$BIN_SHA" ]; then
  how="already installed"
else
  src=""
  if [ $# -ge 1 ] && [ -n "$1" ]; then
    src="$(from_local "$1")"
    [ -n "$src" ] || die "$1 holds no pinned atlas $VERSION ($ARCH)"
    how="installed from $1"
  elif [ -f "$WRAPPER" ] && [ ! -L "$WRAPPER" ] && [ "$(sha "$WRAPPER")" = "$BIN_SHA" ]; then
    src="$TMP/atlas"; cp "$WRAPPER" "$src"        # an ungated copy at /usr/local/bin: it becomes the real CLI
    how="moved from $WRAPPER"
  else
    curl -fsSL --retry 3 --max-time 300 -o "$TMP/$TARBALL" "$URL" || die "download failed: $URL"
    src="$(from_tarball "$TMP/$TARBALL")"
    [ -n "$src" ] || die "the downloaded $TARBALL does not match the pinned sha256; nothing installed"
    how="downloaded $TARBALL (sha256 checked)"
  fi
  $SUDO install -d -m 0755 "$REAL_DIR"
  $SUDO install -m 0755 "$src" "$REAL.new.$$"
  if [ "$(sha "$REAL.new.$$")" != "$BIN_SHA" ]; then
    $SUDO rm -f "$REAL.new.$$"
    die "the copy for $REAL does not match the pinned sha256; nothing installed"
  fi
  $SUDO mv -f "$REAL.new.$$" "$REAL"
fi

# 2. the gated wrapper (the gate and standards.json of /home/user/main; the checkout this ran from only if that is gone,
#    so a worktree or scratch copy never sets the allowlist for the global `atlas`)
repos="/home/user/main"
[ "$REPO" = /home/user/main ] || repos="$repos $(printf '%q' "$REPO")"
cat > "$TMP/wrapper" <<EOF
#!/usr/bin/env bash
# Atlas CLI behind the production gate. Written by growth-engine/tools/atlas/setup.sh; don't edit, re-run it.
# The real CLI ($REAL) is never called directly: this runs the gate first (atlas_gate.py).
export ATLAS_REAL_BIN="\${ATLAS_REAL_BIN:-$REAL}"
for repo in $repos; do
  gate="\$repo/growth-engine/tools/atlas/atlas_gate.py"
  if [ -f "\$gate" ]; then exec python3 "\$gate" "\$@"; fi
done
echo "atlas: the production gate (growth-engine/tools/atlas/atlas_gate.py) is missing; nothing was run." >&2
exit 3
EOF
$SUDO install -d -m 0755 "$(dirname "$WRAPPER")"
$SUDO install -m 0755 "$TMP/wrapper" "$WRAPPER.new.$$"
$SUDO mv -f "$WRAPPER.new.$$" "$WRAPPER"

# 3. sign-in
auth_json="$("$WRAPPER" auth status --json 2>/dev/null || true)"
if printf '%s' "$auth_json" | grep -q '"status": *"logged_in"'; then
  login="logged in (already)"
elif printf '%s' "$auth_json" | grep -q '"refresh_token_present": *true'; then
  login="logged in (already; the access token refreshes on the next call)"     # never overwrite a refreshable login
elif [ -n "${ATLASCLOUD_API_KEY:-}" ]; then
  if "$WRAPPER" auth login --token "$ATLASCLOUD_API_KEY" >/dev/null 2>&1; then
    login="logged in now with ATLASCLOUD_API_KEY"
  else
    login="NOT logged in: atlas auth login with ATLASCLOUD_API_KEY failed (output hidden)"
  fi
else
  if "$WRAPPER" auth login --token network-secret >/dev/null 2>&1; then
    login="logged in now with the placeholder (the network secret for api.atlascloud.ai adds the real key)"
  else
    login="NOT logged in: atlas auth login --token network-secret failed"
  fi
fi

# 4. status
version="$("$WRAPPER" version --json 2>/dev/null | sed -n 's/.*"version": *"\([^"]*\)".*/\1/p' | head -n1)"
selftest="$(ATLAS_REAL_BIN=/nonexistent/atlas-selftest "$WRAPPER" generate image gate/selftest -p GATE-SELFTEST 2>&1)" \
  && rc=0 || rc=$?
if [ "$rc" -eq 3 ] && printf '%s' "$selftest" | grep -q "the production gate is live"; then
  gate_state="live (a GATE-SELFTEST generation was blocked)"
else
  gate_state="NOT WORKING (exit $rc): $(printf '%s' "$selftest" | tail -n 2 | tr '\n' ' ')"
fi
code="$(curl -sS -o /dev/null -w '%{http_code}' --max-time 15 https://api.atlascloud.ai/ 2>/dev/null || true)"
case "$code" in ""|000) net="no answer from api.atlascloud.ai (network not allowed yet?)" ;;
                 *) net="api.atlascloud.ai answers (HTTP $code)" ;; esac
bal_json="$("$WRAPPER" account balance --json 2>/dev/null || true)"
if printf '%s' "$bal_json" | grep -q '"outcome": *"succeeded"'; then
  avail="$(printf '%s' "$bal_json" | python3 -c 'import json,sys; a=json.load(sys.stdin)["data"]["available"]; print(a["value"], a["currency"])' 2>/dev/null || echo "?")"
  balance="ok ($avail available)"
else
  balance="not checked yet (the network secret attaches after Claude Code starts; run: atlas account balance)"
fi
first="$(command -v atlas || true)"
path_note="first on PATH"
if [ -n "${ATLAS_PREFIX:-}" ]; then
  path_note="test install (PATH not checked)"
elif [ "$first" != "$WRAPPER" ]; then
  path_note="NOT first on PATH: \`atlas\` is ${first:-missing}, which skips the gate. Remove it (the official installer puts it in ~/.local/bin, npm in its global bin) or fix PATH"
fi

say "Atlas CLI setup"
say "  version:  ${version:-unknown} (pinned $VERSION, $ARCH; $how)"
say "  real CLI: $REAL (sha256 ok, not on PATH)"
say "  wrapper:  $WRAPPER ($path_note) -> $GATE"
say "  gate:     $gate_state"
say "  login:    $login"
say "  network:  $net"
say "  balance:  $balance"
case "$gate_state" in live*) ;; *) exit 1 ;; esac
case "$login" in NOT*) exit 1 ;; esac
case "$path_note" in NOT*) exit 1 ;; esac
exit 0
