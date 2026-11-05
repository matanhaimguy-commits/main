"""Page basics as written in the HTML: title, meta description, every H1, canonical, lang, viewport and the
og: tags. A missing one is None (or an empty list), never a guess."""


def meta(doc, key: str, value: str) -> str | None:
    for el in doc.find("meta"):
        if el["attrs"].get(key, "").lower() == value:
            return el["attrs"].get("content", "").strip()
    return None


def canonical(doc) -> str | None:
    for el in doc.find("link"):
        if "canonical" in el["attrs"].get("rel", "").lower().split():
            return el["attrs"].get("href", "").strip()
    return None


def open_graph(doc) -> dict:
    og = {}
    for el in doc.find("meta"):
        prop = el["attrs"].get("property", "").lower()
        if prop.startswith("og:") and prop not in og:
            og[prop] = el["attrs"].get("content", "").strip()
    return og


def read(doc) -> dict:
    titles = doc.find("title")
    html = doc.find("html")
    return {"title": titles[0]["text"] if titles else None,
            "meta_description": meta(doc, "name", "description"),
            "h1": [el["text"] for el in doc.find("h1")],
            "canonical": canonical(doc),
            "lang": (html[0]["attrs"].get("lang") or None) if html else None,
            "viewport": meta(doc, "name", "viewport"),
            "og": open_graph(doc)}
