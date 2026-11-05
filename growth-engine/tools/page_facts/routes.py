"""Contact and booking routes, from links, iframes and embed widgets (data-url), matched by exact host
(a host or its subdomain, never a substring), plus tel: and mailto: links. Each with its URL and where it
appears (header, footer or body, best effort)."""
from urllib.parse import urlsplit

SERVICES = [
    ("booking", "Calendly", ("calendly.com",)),
    ("booking", "Cal.com", ("cal.com",)),
    ("booking", "Acuity", ("acuityscheduling.com", "as.me")),
    ("booking", "HubSpot meetings", ("meetings.hubspot.com", "meetings-eu1.hubspot.com")),
    ("booking", "Setmore", ("setmore.com",)),
    ("booking", "SimplyBook", ("simplybook.me", "simplybook.it")),
    ("booking", "Booksy", ("booksy.com",)),
    ("booking", "Fresha", ("fresha.com",)),
    ("form", "Typeform", ("typeform.com",)),
    ("form", "Tally", ("tally.so",)),
    ("messaging", "WhatsApp", ("wa.me", "api.whatsapp.com")),
    ("messaging", "Messenger", ("m.me",)),
    ("messaging", "Instagram DM", ("ig.me",)),
]
DIRECT = {"tel": "Phone", "mailto": "Email"}
SOURCES = (("a", "href", "link"), ("area", "href", "link"), ("iframe", "src", "iframe"))


def classify(url: str) -> tuple[str, str] | None:
    """(kind, service) for a route address, or None."""
    p = urlsplit(url.strip())
    if p.scheme.lower() in DIRECT:
        return "direct", DIRECT[p.scheme.lower()]
    host = (p.hostname or "").lower()
    for kind, service, hosts in SERVICES:
        if any(host == h or host.endswith("." + h) for h in hosts):
            return kind, service
    return None


def candidates(doc):
    for tag, attr, via in SOURCES:
        for el in doc.find(tag):
            yield el, el["attrs"].get(attr, ""), via
    for el in doc.elements:
        if el["attrs"].get("data-url"):
            yield el, el["attrs"]["data-url"], "embed"


def find(doc) -> list[dict]:
    out, seen = [], set()
    for el, url, via in candidates(doc):
        hit = classify(url) if url else None
        if not hit or (url, el["where"], via) in seen:
            continue
        seen.add((url, el["where"], via))
        route = {"kind": hit[0], "service": hit[1], "url": url.strip(), "where": el["where"], "via": via}
        if el.get("text"):
            route["text"] = el["text"][:80]
        out.append(route)
    return out
