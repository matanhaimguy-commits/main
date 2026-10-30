"""Puts the facts together into the one JSON object documented in __init__.py.

Static mode reads the page's HTML. Rendered mode (render= the render function) also reads the page after
JavaScript ran and the request URLs it made; the js_built check always describes the static HTML."""
from datetime import datetime, timezone

from . import basics, forms, js_built, jsonld, routes, site_files, trackers
from .errors import PageError
from .htmldoc import parse

HTML_TYPES = ("text/html", "application/xhtml+xml")


def check_page(page) -> None:
    if page.status >= 400:
        raise PageError(f"PAGE_HTTP_{page.status}: {page.final_url} answered {page.status}, so there is no page to "
                        f"read (bot protection or a missing page). Check the address in a browser.")
    if not page.content_type.lower().startswith(HTML_TYPES) and "<html" not in page.text[:2000].lower():
        raise PageError(f"NOT_HTML: {page.final_url} is {page.content_type or 'not an HTML page'}.")


def collect(url: str, *, fetch, render=None, clock=None) -> dict:
    page = fetch(url)
    check_page(page)
    static = parse(page.text)
    haystacks, shown, rendered = {"html": trackers.haystack(static)}, static, None
    if render:
        rendered = render(page.final_url)
        shown = parse(rendered["html"])
        haystacks.update(rendered=trackers.haystack(shown), requests="\n".join(rendered["requests"]))
    facts = {"url": url, "final_url": page.final_url, "status": page.status,
             "mode": "rendered" if render else "static",
             "checked_at": (clock or (lambda: datetime.now(timezone.utc)))().strftime("%Y-%m-%dT%H:%M:%SZ"),
             "truncated": page.truncated, "js_built": js_built.check(static), "trackers": trackers.detect(haystacks),
             "forms": forms.read(shown), "routes": routes.find(shown), "basics": basics.read(shown),
             "jsonld": jsonld.types(shown), **site_files.read(page.final_url, fetch)}
    if rendered:
        facts["rendered"] = {"requests_seen": len(rendered["requests"]), "network_idle": rendered["idle"]}
    return facts
