"""Fetches one URL as untrusted text, with an honest User-Agent, a timeout and a size cap.

Any HTTP status comes back as a Page (callers decide what a 404 means). A host the proxy refuses, that DNS
does not know, or that does not answer raises Unreachable. `opener` is injectable for tests."""
import http.client
import urllib.error
import urllib.request
from dataclasses import dataclass

from .charset import decode
from .errors import BadUrl, Unreachable
from .opener import build_opener
from .urls import check_url, host_of

USER_AGENT = "page-facts/1.0 (StraightScale leak-scorecard checker; reads public pages only)"
TIMEOUT = 20
CAP = 3_000_000
NET_ERRORS = (TimeoutError, OSError, http.client.HTTPException)


@dataclass
class Page:
    url: str
    final_url: str
    status: int
    content_type: str
    text: str
    truncated: bool


def describe(reason) -> str:
    text = str(reason)
    if "Tunnel connection failed" in text:
        return f"the network proxy refused the connection: {text.split(':', 1)[-1].strip()}"
    if any(s in text for s in ("Name or service not known", "nodename nor servname", "getaddrinfo failed")):
        return "DNS lookup failed"
    return text[:200]


def open_url(url: str, opener, timeout: int):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/html,application/xml,text/plain,*/*;q=0.5"})
    try:
        return (opener or build_opener()).open(req, timeout=timeout)
    except urllib.error.HTTPError as e:
        return e
    except BadUrl:
        raise
    except urllib.error.URLError as e:
        raise Unreachable(host_of(url), describe(e.reason)) from None
    except NET_ERRORS as e:
        raise Unreachable(host_of(url), f"no usable answer within {timeout}s ({type(e).__name__})") from None


def fetch(url: str, *, opener=None, timeout: int = TIMEOUT, cap: int = CAP) -> Page:
    resp = open_url(check_url(url), opener, timeout)
    try:
        raw = resp.read(cap + 1)
    except NET_ERRORS as e:
        raise Unreachable(host_of(url), f"the answer was cut off ({type(e).__name__})") from None
    finally:
        resp.close()
    headers = resp.headers
    return Page(url=url, final_url=resp.geturl() or url, status=getattr(resp, "status", None) or resp.code,
                content_type=headers.get("Content-Type", ""), text=decode(raw[:cap], headers.get_content_charset()),
                truncated=len(raw) > cap)
