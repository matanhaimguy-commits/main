"""robots.txt and the sitemap, fetched from the page's own site (never another host).

The sitemap read is the first one robots.txt declares on the same site, else /sitemap.xml. For a sitemap
index, up to MAX_CHILDREN child sitemaps on the same site are read and their URLs added up."""
from . import robots, sitemap
from .errors import BadUrl, Unreachable
from .urls import origin, same_site

MAX_CHILDREN = 10


def get(fetch, url: str) -> tuple[int | None, str]:
    """(status, text), or (None, why) when the file could not be fetched."""
    try:
        page = fetch(url)
    except (Unreachable, BadUrl) as e:
        return None, str(e)
    return page.status, page.text


def robots_entry(fetch, page_url: str) -> dict:
    url = origin(page_url) + "/robots.txt"
    status, text = get(fetch, url)
    entry = {"url": url, "status": status, "present": False, "sitemaps": [], "blocks_all": False}
    if status == 200 and robots.looks_like_html(text):
        entry["note"] = "answers with an HTML page, not a robots.txt file"
    elif status == 200:
        entry.update(present=True, **robots.parse(text))
    elif status is None:
        entry["note"] = text
    return entry


def read_sitemap(fetch, url: str) -> tuple[int | None, dict | None, str | None]:
    """(status, parsed, note) for one sitemap address."""
    status, text = get(fetch, url)
    if status != 200:
        return status, None, text if status is None else None
    if text[:1] == "\x1f":
        return status, None, "gzipped; not read"
    parsed = sitemap.parse(text)
    return status, (parsed if parsed["kind"] else None), (None if parsed["kind"] else "answers, but not with a sitemap")


def sitemap_entry(fetch, page_url: str, declared: list[str]) -> dict:
    own = [u for u in declared if same_site(u, page_url)]
    url = own[0] if own else origin(page_url) + "/sitemap.xml"
    status, parsed, note = read_sitemap(fetch, url)
    entry = {"url": url, "status": status, "present": bool(parsed), "kind": None, "url_count": None}
    if note:
        entry["note"] = note
    if not parsed:
        return entry
    entry.update(kind=parsed["kind"], url_count=parsed["url_count"])
    if parsed["kind"] == "sitemapindex":
        children = [c for c in parsed["children"] if same_site(c, page_url)][:MAX_CHILDREN]
        counts = [p["url_count"] for _, p, _ in (read_sitemap(fetch, c) for c in children) if p and p["url_count"] is not None]
        entry.update(children=len(parsed["children"]), children_read=len(counts), url_count=sum(counts))
    return entry


def read(page_url: str, fetch) -> dict:
    robots_txt = robots_entry(fetch, page_url)
    return {"robots_txt": robots_txt, "sitemap": sitemap_entry(fetch, page_url, robots_txt["sitemaps"])}
