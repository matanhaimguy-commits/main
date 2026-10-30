"""Find secrets in a text. Findings name the kind and a masked preview, never the secret itself."""
from .secret_patterns import ASSIGNED, JWT, PROVIDERS, jwt_role, looks_real


def mask(s: str) -> str:
    return f"{s[:4]}…({len(s)} chars)"


def scan(text: str) -> list[dict]:
    found = []
    for kind, rx in PROVIDERS:
        found += [{"kind": kind, "preview": mask(m.group(0))} for m in rx.finditer(text)]
    for m in JWT.finditer(text):
        if jwt_role(m.group(1)) == "service_role":
            found.append({"kind": "Supabase service-role key", "preview": mask(m.group(0))})
    for m in ASSIGNED.finditer(text):
        v = m.group(1)
        if looks_real(v) and not any(f["preview"] == mask(v) for f in found):
            found.append({"kind": "a literal value for a token, key or password", "preview": mask(v)})
    return found
