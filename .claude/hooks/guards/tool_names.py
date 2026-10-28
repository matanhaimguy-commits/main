"""Gated tool names as cloud sessions see them.

A cloud session can name a connector by an id (mcp__<id>__generate_image) instead of its name (mcp__Higgs__generate_image).
canonical() maps such a call to the gated tool with the same ending, so the gates apply whatever the server is called.
A server with a plain name (Figma, HeyGen) keeps its own name: only id-named servers are mapped.
"""
import re

NAMED_SERVER = re.compile(r"[A-Za-z][A-Za-z_]*")


def canonical(tool: str, gated: dict) -> str:
    if tool in gated:
        return tool
    m = re.match(r"^mcp__(.+?)__(.+)$", tool)
    if not m or NAMED_SERVER.fullmatch(m.group(1)):
        return tool
    hits = [k for k in gated if k.endswith("__" + m.group(2))]
    return hits[0] if len(hits) == 1 else tool
