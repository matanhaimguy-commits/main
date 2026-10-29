"""Which intake shape the hub returned: the slim one (docs-first) or the old 38-question one."""


def row_of(resp) -> dict | None:
    """The intake row inside a response. Old shape: {"intakes": [row, ...]}, newest first. Slim shape: the row itself."""
    if not isinstance(resp, dict):
        return None
    if "intakes" in resp:
        rows = resp.get("intakes") or []
        return rows[0] if rows else None
    return resp if resp.get("business_name") or "docs" in resp or "answers" in resp else None


def kind(row: dict) -> str:
    return "legacy" if isinstance(row.get("answers"), dict) else "slim"
