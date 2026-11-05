"""Reads a sitemap XML text by counting its tags (no XML parser runs on the untrusted file): a <urlset>
gives a URL count, a <sitemapindex> gives the child sitemaps it lists (its <loc> values)."""
import html
import re

URLSET = re.compile(r"<(?:[\w-]+:)?urlset[\s>]", re.I)
INDEX = re.compile(r"<(?:[\w-]+:)?sitemapindex[\s>]", re.I)
URL_TAG = re.compile(r"<(?:[\w-]+:)?url[\s>]", re.I)
LOC = re.compile(r"<(?:[\w-]+:)?loc>\s*([^<\s]+)\s*<", re.I)


def parse(text: str) -> dict:
    if INDEX.search(text):
        return {"kind": "sitemapindex", "url_count": None,
                "children": [html.unescape(u) for u in LOC.findall(text)]}
    if URLSET.search(text):
        return {"kind": "urlset", "url_count": len(URL_TAG.findall(text)), "children": []}
    return {"kind": None, "url_count": None, "children": []}
