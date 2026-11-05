"""draft.py seed|checklist|check <slug>   (Quick onboarding, step 2)

  seed <slug>       put the slim intake's few facts into brain.json (each with its source) and write research/seeds.json
  checklist <slug>  the 38 questions as the drafter's internal checklist, with what the brain holds for each
  check <slug>      every drafted field has a source or 'unknown: <what>', the schema passes; then O2 research is queued
                    (research/o2-queue.json). Exit 1 and nothing queued when a field has neither."""
import json
import sys

from brainio import store
from clients.paths import REPO, client_dir

from . import checklist, finish, seed as seeder

USAGE = "usage: draft.py seed|checklist|check <slug>"


def run(cmd: str, slug: str, root=None) -> int:
    brain = store.load(slug, root)
    if cmd == "checklist":
        print(checklist.render(checklist.build(brain)))
        return 0
    if cmd == "seed":
        d = client_dir(root or REPO, slug)
        p = d / "intake" / "slim.json"
        if not p.exists():
            sys.exit(f"NO_INTAKE: {p} is missing; run hub.py intake-pull {slug} first")
        slim = json.loads(p.read_text(encoding="utf-8"))
        new, seeds = seeder.seed(brain, slim, slug)
        store.save(slug, new, root)
        (d / "research").mkdir(exist_ok=True)
        (d / "research" / "seeds.json").write_text(json.dumps(seeds, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(f"{slug}: seeded {len(new['field_sources'])} field(s) with sources; wrote research/seeds.json")
        return 0
    if cmd == "check":
        errs, q = finish.check(slug, brain, root)
        for e in errs:
            print(f"  {e}")
        print(f"draft check: {'FAIL, ' + str(len(errs)) + ' problem(s); O2 not queued' if errs else 'PASS, O2 research queued (' + q.as_posix() + ')'}")
        return 1 if errs else 0
    sys.exit(USAGE)


def main(argv: list[str]) -> int:
    if len(argv) != 2 or argv[0] not in ("seed", "checklist", "check"):
        sys.exit(USAGE)
    return run(argv[0], argv[1])
