"""Every HeyGen connector tool outside gated_tools (standards.json heygen_connector): reads pass, everything else is
denied. A HeyGen tool is named mcp__HeyGen__<tool> (any case) or mcp__<connector id>__<tool> with an id from the list.
The two twin tools are in gated_tools, so the generation gate decides them; this module leaves them alone."""
from __future__ import annotations

import re


def bare_name(tool: str, standards: dict) -> str | None:
    """The tool's own name when it is a HeyGen connector tool, else None."""
    cfg = standards.get("heygen_connector") or {}
    m = re.match(r"^mcp__(.+?)__(.+)$", tool or "")
    if not m:
        return None
    server = m.group(1)
    names = {n.lower() for n in cfg.get("server_names", [])}
    return m.group(2) if server.lower() in names or server in cfg.get("connector_ids", []) else None


def read_only(name: str, standards: dict) -> bool:
    ro = (standards.get("heygen_connector") or {}).get("read_only") or {}
    return name.startswith(tuple(ro.get("prefixes", []))) or any(re.fullmatch(p, name) for p in ro.get("patterns", []))


def deny_reason(tool: str, standards: dict) -> str | None:
    """Why this HeyGen tool is refused (None: it is not HeyGen, it is a read, or the generation gate owns it)."""
    name = bare_name(tool, standards)
    if name is None or read_only(name, standards):
        return None
    gated = standards.get("gated_tools") or {}
    if any(k.lower() == f"mcp__heygen__{name}".lower() for k in gated):
        return None
    return (f"HeyGen {name} is not a read and not one of the twin's two gated tools (create_speech, "
            "create_video_from_avatar): HeyGen writes, deletes, uploads, templates and account changes are off "
            "(standards.json heygen_connector)")
