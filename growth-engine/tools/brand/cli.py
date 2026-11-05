"""hub.py brand-pull <slug> [--fixture file.json] [--dry-run]

Reads the Brand card (GET /api/clients/brand-overrides?brand=<slug>, read-only) and writes each field Matan set into
clients/<slug>/brain.json, with the source "Matan (Brand card, <date>)" in field_sources. The result must pass the brain
schema, or nothing is written. Then the vault note is regenerated when the vault exists. brain.json stays the source of
truth. --fixture reads a saved response (no network); --dry-run shows the changes and writes nothing."""
import datetime as dt
import json
import sys
from pathlib import Path

from brainio import store, validate
from studio.cli import opt, positionals

from . import apply as applier, fetch, vault

USAGE = "brand-pull <slug> [--fixture file.json] [--dry-run]"


def load_fixture(path: str) -> dict:
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        sys.exit(f"BAD_FIXTURE: {path}: {e}")


def pull(slug: str, *, call=None, fixture: str | None = None, dry_run: bool = False, root=None, today: str | None = None,
         vault_dir=None) -> dict:
    """Returns {changes, updated_at, vault}. Exits with the problems and writes nothing if any field is bad."""
    resp = load_fixture(fixture) if fixture else fetch.from_hub(call, slug)
    if not isinstance(resp.get("overrides"), dict):
        sys.exit("BAD_BRAND_OVERRIDES: no overrides object")
    brain = store.load(slug, root)
    new, changes, problems = applier.apply(brain, resp["overrides"], today or dt.date.today().isoformat())
    problems += validate.errors(new) if not problems else []
    if problems:
        sys.exit("BRAND_PULL_FAILED, nothing written:\n  " + "\n  ".join(problems))
    note, written = "dry run, nothing written", new != brain
    if new != brain and not dry_run:
        store.save(slug, new, root)
        note = vault.regenerate(slug, root, vault_dir)
    return {"changes": changes, "updated_at": resp.get("updated_at"), "vault": note, "written": written}


def cli(rest: list[str], *, call, upload=None, hub_url: str = "") -> None:
    (slug,) = positionals(rest, ["slug"], USAGE)
    r = pull(slug, call=call, fixture=opt(rest, "--fixture"), dry_run="--dry-run" in rest)
    print(f"{slug}: Brand card updated {r['updated_at']}: {len(r['changes'])} field(s) changed")
    for c in r["changes"]:
        print(f"  {c['field']} -> {c['path']}")
    print(r["vault"] if r["written"] else "nothing to write; brain.json already matches the Brand card")
