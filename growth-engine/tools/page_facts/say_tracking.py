"""Summary section: one line per tracker, found (with its ids and the code that proves it) or not found."""
from .wording import where_read

ID_WORDS = {"Google Tag Manager": "container", "GA4": "measurement ID", "Microsoft Clarity": "project",
            "Hotjar": "site ID"}
SOURCES = {"html": "the page's HTML", "rendered": "the rendered page", "requests": "the network requests"}


def line(t: dict, facts: dict) -> str:
    if not t["found"]:
        return f"- {t['name']}: not found in {where_read(facts)}"
    word = ID_WORDS.get(t["name"], "id")
    ids = f"{word}{'s' if len(t['ids']) > 1 else ''} {', '.join(t['ids'])}" if t["ids"] else f"no {word} in the code"
    seen = " and ".join(SOURCES.get(s, s) for s in t["seen_in"])
    evidence = (t["evidence"] or "").replace("`", "'")
    return f"- {t['name']}: found ({ids}) in {seen}; the code: `{evidence}`"


def section(facts: dict) -> list[str]:
    return ["## Tracking"] + [line(t, facts) for t in facts["trackers"]]
