#!/usr/bin/env bash
# Launch the real headless Chrome, but route it through this machine's HTTPS
# proxy. Remotion hard-codes "--no-proxy-server", which fails in sandboxes where
# all outbound traffic must use the proxy. TLS verification stays fully on.
real="${REAL_CHROME:?REAL_CHROME not set}"
args=()
for a in "$@"; do
  case "$a" in
    --no-proxy-server|--proxy-server=*|--proxy-bypass-list=*) ;;
    *) args+=("$a") ;;
  esac
done
proxy="${HTTPS_PROXY:-${https_proxy:-}}"
if [ -n "$proxy" ]; then
  args+=("--proxy-server=$proxy" "--proxy-bypass-list=localhost;127.0.0.1;::1")
fi
exec "$real" "${args[@]}"
