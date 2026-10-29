"""The slim intake: {brand, business_name, website, instagram, offer_line, competitors: [str],
consents: {ai_people: bool, proof: bool}, docs: [{name, mime, size, signed_url}], submitted_at}."""
import sys


def _text(v) -> str:
    return v.strip() if isinstance(v, str) else ""


def normalize(row: dict) -> dict:
    """The row cleaned to the slim fields. Stops on a wrong type; a missing field stays empty (the gate reports it)."""
    comps, docs, cons = (row.get(k) if row.get(k) is not None else d for k, d in (("competitors", []), ("docs", []), ("consents", {})))
    if not isinstance(comps, list) or not isinstance(docs, list) or not isinstance(cons, dict):
        sys.exit("BAD_INTAKE: competitors and docs must be lists and consents an object")
    for d in docs:
        if not isinstance(d, dict) or not d.get("name") or not d.get("signed_url"):
            sys.exit("BAD_INTAKE: every doc needs a name and a signed_url")
    return {
        "brand": _text(row.get("brand")),
        "business_name": _text(row.get("business_name")),
        "website": _text(row.get("website")),
        "instagram": _text(row.get("instagram")),
        "offer_line": _text(row.get("offer_line")),
        "competitors": [_text(c) for c in comps if _text(c)],
        "consents": {"ai_people": cons.get("ai_people"), "proof": cons.get("proof")},
        "docs": [{"name": d["name"], "mime": d.get("mime"), "size": d.get("size"), "signed_url": d["signed_url"]} for d in docs],
        "submitted_at": row.get("submitted_at") or row.get("created_at"),
    }


def gate(slim: dict, fetched: list[dict]) -> list[dict]:
    """O1's gate for the slim shape: [{id, label, why}] for what is still missing. Empty means ready."""
    out = []
    if not slim["business_name"]:
        out.append({"id": "business_name", "label": "Business name", "why": "empty"})
    if not (slim["website"] or slim["instagram"] or slim["docs"]):
        out.append({"id": "sources", "label": "Something to read", "why": "needs at least one of: website, instagram, a document"})
    for k, v in slim["consents"].items():
        if not isinstance(v, bool):
            out.append({"id": f"consents.{k}", "label": f"Consent: {k}", "why": "needs a yes or a no"})
    out += [{"id": f"doc:{f['name']}", "label": f["name"], "why": f["error"]} for f in fetched if f.get("error")]
    return out
