"""Summary section: robots.txt and the sitemap, present or not, with the sitemap's URL count."""
from .wording import plural


def absent(entry: dict) -> str:
    if entry.get("note"):
        return f"not usable ({entry['note']})"
    return f"missing (HTTP {entry['status']})"


def robots_line(r: dict) -> str:
    if not r["present"]:
        return f"- robots.txt: {absent(r)}"
    blocks = "; it blocks every crawler (Disallow: / for User-agent: *)" if r["blocks_all"] else ""
    return f"- robots.txt: present, declares {plural(len(r['sitemaps']), 'sitemap')}{blocks}"


def sitemap_line(s: dict) -> str:
    if not s["present"]:
        return f"- Sitemap {s['url']}: {absent(s)}"
    if s["kind"] == "sitemapindex":
        return (f"- Sitemap {s['url']}: an index of {plural(s['children'], 'sitemap')}; "
                f"{plural(s['url_count'], 'URL')} in the {s['children_read']} read")
    return f"- Sitemap {s['url']}: present, {plural(s['url_count'], 'URL')}"


def section(facts: dict) -> list[str]:
    return ["## robots.txt and sitemap", robots_line(facts["robots_txt"]), sitemap_line(facts["sitemap"])]
