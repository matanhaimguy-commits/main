"""Which trackers a page carries, by the exact signatures in signatures.py.

Searched: script bodies and the src/href/data-src addresses of the page's tags (never its visible text or
comments), and in rendered mode also the rendered page and its network requests. Each source is a "haystack"."""
from .signatures import COMPILED

URL_ATTRS = ("src", "href", "data-src")
EVIDENCE_CHARS = 120


def haystack(doc) -> str:
    """The code and addresses of a parsed page, one per line."""
    urls = [v for el in doc.elements for k, v in el["attrs"].items() if k in URL_ATTRS and v]
    return "\n".join(urls + [s["body"] for s in doc.scripts])


def scan(sig: dict, text: str) -> tuple[str | None, list[str]]:
    """The first matching evidence and every id, for one tracker in one haystack."""
    evidence, ids = None, []
    for kind in ("present", "ids"):
        for rx in sig[kind]:
            for m in rx.finditer(text):
                evidence = evidence or m.group(0)[:EVIDENCE_CHARS]
                if kind == "ids":
                    ids.append(m.group(1))
    if evidence:
        ids += [m.group(1) for rx in sig["ids_if_present"] for m in rx.finditer(text)]
    return evidence, list(dict.fromkeys(ids))


def detect(haystacks: dict[str, str]) -> list[dict]:
    """One entry per known tracker: found, ids, the first evidence, and which haystacks it was seen in."""
    out = []
    for sig in COMPILED:
        entry = {"name": sig["name"], "found": False, "ids": [], "evidence": None, "seen_in": []}
        for source, text in haystacks.items():
            evidence, ids = scan(sig, text)
            if evidence:
                entry["found"] = True
                entry["evidence"] = entry["evidence"] or evidence
                entry["seen_in"].append(source)
                entry["ids"] = list(dict.fromkeys(entry["ids"] + ids))
        out.append(entry)
    return out
