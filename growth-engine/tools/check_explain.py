"""pipeline.py check-call --explain: the generation hook's whole answer for a call, from the shell. It maps a connector
id name (mcp__<id>__create_speech) to the gated tool as the hook does, refuses a switched-off service, then runs the
gate with log=False so a dry check never counts as a call. Takes the pipeline module as P.
Tests: growth-engine/tools/test_heygen_gate.py (Explain)."""
from __future__ import annotations

import sys


def _guards(P):
    hooks = str(P.GE.parent / ".claude" / "hooks")
    if hooks not in sys.path:
        sys.path.insert(0, hooks)
    from guards.services import off_reason
    from guards.tool_names import canonical
    return canonical, off_reason


def explain(P, tool_name: str, tool_input: dict) -> tuple[bool, str]:
    canonical, off_reason = _guards(P)
    gated = P.STANDARDS["gated_tools"]
    tool = canonical(tool_name, gated)
    spec = gated.get(tool)
    lines = [f"tool: {tool_name}" + (f" (gated as {tool})" if tool != tool_name else "")]
    if not spec:
        return True, "\n".join(lines + ["rule: not a gated tool", "ALLOW"])
    lines.append(f"rule: service {spec['service']}, kind {spec['kind']}")
    off = off_reason(tool, P.STANDARDS)
    if off:
        return False, "\n".join(lines + ["DENY", f"  SERVICE OFF: {off}"])
    ok, why = P.check_call(tool, tool_input or {}, log=False)
    return ok, "\n".join(lines + ["ALLOW" if ok else "DENY"] + [f"  {w}" for w in why])
