"""Shared by the page_facts tests: puts growth-engine/tools on sys.path, reads the fixtures, and stands in for
the network (a stub urllib opener and a stub page fetcher). No test touches the network."""
import email.message
import io
import sys
import urllib.error
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOOLS = HERE.parent
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))
from page_facts.fetch import Page  # noqa: E402
from page_facts.htmldoc import parse  # noqa: E402

SITE = "https://acme.example"


def fixture(name: str) -> str:
    return (HERE / "fixtures" / name).read_text(encoding="utf-8")


def doc(name: str):
    return parse(fixture(name))


class FakeResponse(io.BytesIO):
    def __init__(self, url: str, status: int, body: bytes, ctype: str):
        super().__init__(body)
        self.url, self.status, self.code = url, status, status
        self.headers = email.message.Message()
        self.headers["Content-Type"] = ctype

    def geturl(self):
        return self.url


class StubOpener:
    """Stands in for the urllib opener: `pages[url]` is (status, body, content type) or an exception to raise."""

    def __init__(self, pages: dict):
        self.pages, self.calls = pages, []

    def open(self, req, timeout=None):
        self.calls.append({"url": req.full_url, "user_agent": req.get_header("User-agent"), "timeout": timeout})
        got = self.pages.get(req.full_url, (404, "not found", "text/html"))
        if isinstance(got, Exception):
            raise got
        status, body, ctype = got
        resp = FakeResponse(req.full_url, status, body.encode("utf-8") if isinstance(body, str) else body, ctype)
        if status >= 400:
            raise urllib.error.HTTPError(req.full_url, status, "error", resp.headers, resp)
        return resp


def stub_fetch(pages: dict):
    """A fetch(url) for facts.collect: `pages[url]` is (status, text) or an exception; anything else is a 404."""
    def fetch(url):
        got = pages.get(url, (404, "not found"))
        if isinstance(got, Exception):
            raise got
        return Page(url=url, final_url=url, status=got[0], content_type="text/html; charset=utf-8", text=got[1],
                    truncated=False)
    return fetch
