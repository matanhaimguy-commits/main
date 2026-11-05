"""Summary section: the contact and booking routes found, and the kinds of route that are not there."""
from .wording import page_read

KINDS = {"booking": "booking link", "form": "Typeform/Tally form", "messaging": "WhatsApp/Messenger/Instagram DM link",
         "direct": "phone or email link"}


def line(r: dict) -> str:
    text = f', "{r["text"]}"' if r.get("text") else ""
    return f"- {r['service']} ({r['where']}, {r['via']}{text}): {r['url']}"


def section(facts: dict) -> list[str]:
    routes = sorted(facts["routes"], key=lambda r: list(KINDS).index(r["kind"]))
    lines = ["## Contact and booking routes"] + [line(r) for r in routes]
    missing = [label for kind, label in KINDS.items() if not any(r["kind"] == kind for r in routes)]
    if missing:
        lines.append(f"- Not in {page_read(facts)}: " + "; ".join(missing) + ".")
    return lines
