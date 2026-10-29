"""The end of the draft: sources and schema pass, then O2 research is queued (research/o2-queue.json)."""
import datetime as dt
import json
from pathlib import Path

from brainio import validate
from clients.paths import REPO, client_dir

from . import sources


def check(slug: str, brain: dict, root: Path | None = None, today: str | None = None) -> tuple[list[str], Path | None]:
    """Returns (problems, queue file). The queue file is written only when there are no problems."""
    errs = validate.errors(brain) + [f"{p['path']}: {p['problem']}" for p in sources.problems(brain)]
    if errs:
        return errs, None
    res = client_dir(root or REPO, slug) / "research"
    res.mkdir(parents=True, exist_ok=True)
    q = res / "o2-queue.json"
    q.write_text(json.dumps({"status": "queued", "reason": "brain drafted: every field has a source or says what is missing",
                             "queued_at": today or dt.date.today().isoformat(),
                             "next": "research-scout runs Foundation steps 01 to 03 (ONBOARDING O2); seeds in research/seeds.json"},
                            indent=1) + "\n", encoding="utf-8")
    return [], q
