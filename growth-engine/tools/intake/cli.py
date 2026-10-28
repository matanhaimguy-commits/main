"""hub.py intake-pull <slug> [--fixture file.json] [--dry-run]

Reads the client's newest submitted intake from the hub app (the /intake/$token form; GET /api/clients/intakes?brand=<slug>) and writes clients/<slug>/intake/
answers.json and files.json. Prints O1's gate: the required answers still missing. --fixture reads a saved intake
instead of the hub (no network); --dry-run writes nothing. Without --fixture the studio token is needed."""
import sys

from studio.cli import opt, positionals

from . import fetch, questions, required, write as writer

USAGE = "intake-pull <slug> [--fixture file.json] [--dry-run]"


def pull(slug: str, *, call=None, fixture: str | None = None, dry_run: bool = False,
         root=None, question_file=None) -> tuple[dict, list[dict], list]:
    got = fetch.latest(fetch.from_fixture(fixture) if fixture else fetch.from_hub(call, slug))
    bad = required.missing(got["answers"], questions.load(question_file))
    return got, bad, ([] if dry_run else writer.write(slug, got, bad, root))


def cli(rest: list[str], *, call, upload=None, hub_url: str = "") -> None:
    (slug,) = positionals(rest, ["slug"], USAGE)
    got, bad, paths = pull(slug, call=call, fixture=opt(rest, "--fixture"), dry_run="--dry-run" in rest)
    n = len(got["answers"])
    print(f"{slug}: intake submitted {got['submitted_at']}: {n} answer(s), {len(got.get('files') or [])} file(s)"
          + (" (dry run, nothing written)" if "--dry-run" in rest else ""))
    for p in paths:
        print(f"wrote {p}")
    if bad:
        print(f"O1 gate: NOT READY, {len(bad)} required answer(s) missing")
        for m in bad:
            print(f"  {m['id']}: {m['label']} ({m['why']})")
        sys.exit(1)
    print("O1 gate: ready (all required fields complete)")
