"""Small phrases shared by the summary sections."""


def where_read(facts: dict) -> str:
    """Where a "not found" was looked for."""
    if facts["mode"] == "rendered":
        return "the page's HTML, the rendered page or its network requests"
    return "the page's HTML"


def page_read(facts: dict) -> str:
    """Which version of the page the forms, links and basics come from."""
    return "the rendered page" if facts["mode"] == "rendered" else "the page's HTML"


def plural(n: int, word: str) -> str:
    return f"{n} {word}{'' if n == 1 else 's'}"


def quote(text: str | None, limit: int = 200) -> str:
    if not text:
        return "missing"
    text = text if len(text) <= limit else text[: limit - 1] + "…"
    return f'"{text}"'
