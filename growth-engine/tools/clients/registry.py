"""The brands in registry.json: slug, name, hub business, language, status, stage, timezone, cadence, cap, vault folder."""
import json
from pathlib import Path

REGISTRY = Path(__file__).resolve().parent / "registry.json"
REQUIRED = ("slug", "name", "hub_business", "language", "status", "account_stage", "timezone", "cadence",
            "monthly_usd_cap", "vault_folder")
STATUSES = ("onboarding", "research", "active", "paused")  # the hub's brands.status (C1 docs/client-os.md)


class RegistryError(Exception):
    """registry.json is wrong or has no such brand."""


def brands(path: Path | None = None) -> list[dict]:
    data = json.loads(Path(path or REGISTRY).read_text(encoding="utf-8"))
    out = data.get("brands") or []
    for b in out:
        missing = [k for k in REQUIRED if k not in b]
        if missing:
            raise RegistryError(f"{b.get('slug', '?')}: missing {', '.join(missing)}")
        if b["status"] not in STATUSES:
            raise RegistryError(f"{b['slug']}: status {b['status']!r} is not one of {', '.join(STATUSES)}")
    slugs = [b["slug"] for b in out]
    if len(set(slugs)) != len(slugs):
        raise RegistryError("a slug is listed twice")
    return out


def brand(slug: str, path: Path | None = None) -> dict:
    found = next((b for b in brands(path) if b["slug"] == slug), None)
    if found is None:
        raise RegistryError(f"{slug} is not in {Path(path or REGISTRY).name}; add it there first")
    return found
