"""Each <form> on the page: where it sends, how many fields a visitor fills, and whether it asks for an
email or a phone number. Hidden, submit, button, reset and image inputs are not fields a visitor fills."""
import re

FIELD_TAGS = ("input", "select", "textarea")
NOT_FILLED = {"hidden", "submit", "button", "reset", "image"}
EMAIL = re.compile(r"e-?mail", re.I)
PHONE = re.compile(r"phone|mobile|whatsapp|\btel\b|\bcell", re.I)
HINT_ATTRS = ("name", "id", "placeholder", "autocomplete", "aria-label")


def field_type(el: dict) -> str:
    if el["tag"] != "input":
        return el["tag"]
    return (el["attrs"].get("type") or "text").strip().lower()


def asks(fields: list[dict], kind: str, pattern: re.Pattern) -> bool:
    return any(f["type"] == kind or any(pattern.search(f["hints"].get(a, "")) for a in HINT_ATTRS) for f in fields)


def read(doc) -> list[dict]:
    forms = [{"action": el["attrs"].get("action", ""), "method": (el["attrs"].get("method") or "get").upper(),
              "where": el["where"], "fields": []} for el in doc.find("form")]
    for el in doc.find(*FIELD_TAGS):
        kind = field_type(el)
        if el["form"] is None or kind in NOT_FILLED:
            continue
        forms[el["form"]]["fields"].append({"name": el["attrs"].get("name") or el["attrs"].get("id", ""), "type": kind,
                                            "required": "required" in el["attrs"], "hints": el["attrs"]})
    for f in forms:
        f["fields_to_fill"] = len(f["fields"])
        f["asks_email"] = asks(f["fields"], "email", EMAIL)
        f["asks_phone"] = asks(f["fields"], "tel", PHONE)
        for fld in f["fields"]:
            del fld["hints"]
    return forms
