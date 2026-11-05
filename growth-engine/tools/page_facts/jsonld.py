"""The @type values in the page's JSON-LD blocks (<script type="application/ld+json">), nested ones and
@graph items included. A block that is not valid JSON is counted, never guessed at."""
import json


def walk(node, types: list[str]) -> None:
    if isinstance(node, list):
        for item in node:
            walk(item, types)
    elif isinstance(node, dict):
        t = node.get("@type")
        if isinstance(t, str):
            types.append(t)
        elif isinstance(t, list):
            types.extend(x for x in t if isinstance(x, str))
        for value in node.values():
            walk(value, types)


def types(doc) -> dict:
    found, blocks, invalid = [], 0, 0
    for s in doc.scripts:
        if s["attrs"].get("type", "").split(";")[0].strip().lower() != "application/ld+json":
            continue
        blocks += 1
        try:
            walk(json.loads(s["body"]), found)
        except (ValueError, RecursionError):
            invalid += 1
    return {"types": list(dict.fromkeys(found)), "blocks": blocks, "invalid_blocks": invalid}
