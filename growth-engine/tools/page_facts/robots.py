"""Reads a robots.txt text: the Sitemap: lines it declares, and whether it blocks every crawler
("Disallow: /" in a group for User-agent: *)."""


def looks_like_html(text: str) -> bool:
    """Many JS-built sites answer every path, robots.txt included, with their index.html."""
    head = text.lstrip()[:200].lower()
    return head.startswith(("<!doctype", "<html", "<head", "<body"))


def parse(text: str) -> dict:
    sitemaps, agents, blocks_all, in_rules = [], [], False, False
    for line in text.splitlines():
        key, _, value = line.split("#", 1)[0].partition(":")
        key, value = key.strip().lower(), value.strip()
        if key == "sitemap" and value:
            sitemaps.append(value)
        elif key == "user-agent":
            agents = [value] if in_rules else agents + [value]
            in_rules = False
        elif key in ("disallow", "allow"):
            in_rules = True
            blocks_all = blocks_all or (key == "disallow" and value == "/" and "*" in agents)
    return {"sitemaps": sitemaps, "blocks_all": blocks_all}
