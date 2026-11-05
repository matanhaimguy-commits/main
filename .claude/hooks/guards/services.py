"""Services the owner has switched off (standards.json disabled_services): the gate refuses them whatever the call."""


def off_reason(tool: str, standards: dict) -> str | None:
    spec = standards.get("gated_tools", {}).get(tool) or {}
    return (standards.get("disabled_services") or {}).get(spec.get("service"))
