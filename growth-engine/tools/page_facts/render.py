"""--render: runs render.js (Node + Playwright's Chromium) and reads its JSON: the rendered HTML and every
request URL the page made, which catches a pixel loaded through GTM. `run` is injectable for tests."""
import json
import subprocess
from pathlib import Path

from .errors import RenderError, Unreachable
from .fetch import CAP
from .urls import check_url, host_of

HELPER = Path(__file__).with_name("render.js")
TIMEOUT = 90
MAX_REQUESTS = 3000
NETWORK_CODES = ("ERR_TUNNEL_CONNECTION_FAILED", "ERR_NAME_NOT_RESOLVED", "ERR_PROXY_CONNECTION_FAILED",
                 "ERR_CONNECTION_REFUSED", "ERR_CONNECTION_TIMED_OUT", "ERR_ADDRESS_UNREACHABLE")


def render(url: str, *, run=subprocess.run, timeout: int = TIMEOUT) -> dict:
    """{"html", "requests", "final_url", "status", "idle"}; raises Unreachable or RenderError."""
    check_url(url)
    try:
        p = run(["node", str(HELPER), url], capture_output=True, text=True, timeout=timeout)
    except FileNotFoundError:
        raise RenderError("node is not installed; run without --render") from None
    except subprocess.TimeoutExpired:
        raise RenderError(f"the page did not finish loading in {timeout}s") from None
    if p.returncode != 0:
        err = (p.stderr or "").strip()
        code = next((c for c in NETWORK_CODES if c in err), None)
        if code:
            raise Unreachable(host_of(url), f"Chromium: {code}")
        raise RenderError(err[-400:] or f"render.js exited with {p.returncode}")
    try:
        data = json.loads(p.stdout)
    except ValueError:
        raise RenderError("render.js printed something that is not JSON") from None
    return {"html": str(data.get("html") or "")[:CAP], "requests": [str(u) for u in data.get("requests", [])][:MAX_REQUESTS],
            "final_url": data.get("final_url") or url, "status": data.get("status"), "idle": bool(data.get("idle", True))}
