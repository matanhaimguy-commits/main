"""hub.py intake-pull <slug> [--fixture file.json] [--dry-run]

Reads the client's newest submitted intake from the hub app (GET /api/clients/intakes?brand=<slug>) and writes it under
clients/<slug>/intake/. Two shapes are read:
  slim (Quick onboarding): intake/slim.json, and the uploaded documents downloaded right away into
    clients/<slug>/foundation/ (gitignored; signed links last 10 minutes);
  old (38 questions): intake/answers.json and files.json.
Prints O1's gate: what is still missing. --fixture reads a saved response instead of the hub (no network, and the
documents are not downloaded); --dry-run writes nothing. Without --fixture the studio token is needed."""
import sys

from clients.paths import REPO, client_dir
from studio.cli import opt, positionals

from . import docs, fetch, questions, required, slim as slim_mod, write as writer

USAGE = "intake-pull <slug> [--fixture file.json] [--dry-run]"


def pull(slug: str, *, call=None, fixture: str | None = None, dry_run: bool = False,
         root=None, question_file=None, get=None) -> tuple[dict, list[dict], list]:
    got = fetch.latest(fetch.from_fixture(fixture) if fixture else fetch.from_hub(call, slug))
    if got["shape"] == "legacy":
        bad = required.missing(got["answers"], questions.load(question_file))
        return got, bad, ([] if dry_run else writer.write(slug, got, bad, root))
    s = got["slim"]
    fetched = [] if (dry_run or fixture) else docs.download(s["docs"], client_dir(root or REPO, slug) / "foundation", get or docs.fetch_bytes)
    got["fetched"] = fetched
    bad = slim_mod.gate(s, fetched)
    return got, bad, ([] if dry_run else writer.write_slim(slug, s, fetched, bad, root))


def cli(rest: list[str], *, call, upload=None, hub_url: str = "") -> None:
    (slug,) = positionals(rest, ["slug"], USAGE)
    dry = "--dry-run" in rest
    got, bad, paths = pull(slug, call=call, fixture=opt(rest, "--fixture"), dry_run=dry)
    note = " (dry run, nothing written)" if dry else ""
    if got["shape"] == "slim":
        s = got["slim"]
        saved = [f for f in got["fetched"] if f["saved_as"]]
        print(f"{slug}: quick intake submitted {got['submitted_at']}: {len(s['docs'])} document(s), {len(saved)} saved to "
              f"clients/{slug}/foundation/, {len(s['competitors'])} competitor(s){note}")
    else:
        print(f"{slug}: intake submitted {got['submitted_at']}: {len(got['answers'])} answer(s), "
              f"{len(got.get('files') or [])} file(s)" + note)
    for p in paths:
        print(f"wrote {p}")
    if bad:
        print(f"O1 gate: NOT READY, {len(bad)} item(s) missing")
        for m in bad:
            print(f"  {m['id']}: {m['label']} ({m['why']})")
        sys.exit(1)
    print("O1 gate: ready" + (" (all required fields complete)" if got["shape"] == "legacy" else " (draft the brain next: tools/draft.py)"))
