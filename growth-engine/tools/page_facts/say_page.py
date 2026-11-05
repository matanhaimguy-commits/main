"""Summary section: the page basics and the JSON-LD types, each as written or "missing"."""
from .wording import plural, quote


def jsonld_line(j: dict) -> str:
    if not j["blocks"]:
        return "- JSON-LD: none"
    bad = f", {j['invalid_blocks']} not valid JSON" if j["invalid_blocks"] else ""
    types = ", ".join(j["types"]) or "no @type"
    return f"- JSON-LD types: {types} ({plural(j['blocks'], 'block')}{bad})"


def section(facts: dict) -> list[str]:
    b = facts["basics"]
    h1 = f"- H1 ({len(b['h1'])}): " + "; ".join(quote(t, 120) if t else "(empty)" for t in b["h1"]) if b["h1"] else "- H1: none"
    return ["## Page basics",
            f"- Title: {quote(b['title'])}",
            f"- Meta description: {quote(b['meta_description'])}",
            h1,
            f"- Canonical: {b['canonical'] or 'missing'}",
            f"- Language (html lang): {b['lang'] or 'missing'}",
            f"- Viewport: {quote(b['viewport'])}",
            "- Open Graph: " + (", ".join(b["og"]) if b["og"] else "none"),
            jsonld_line(facts["jsonld"])]
