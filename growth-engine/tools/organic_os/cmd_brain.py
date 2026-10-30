"""organic.py brain-check <slug> [--write]"""
from __future__ import annotations

from .brain import brain_check, brain_report
from .files import client_dir, load_brain, load_demand
from .issues import has_errors
from .show import print_issues


def run(a) -> int:
    brain = load_brain(a.slug)
    issues, gaps = brain_check(brain, load_demand(a.slug, brain))
    print_issues("brain", issues)
    print(f"{len(gaps)} gaps to fill")
    for g in gaps:
        print(f"  - {g['field']}: {g['missing']}")
    if a.write:
        (client_dir(a.slug) / "brain-gaps.md").write_text(brain_report(a.slug, brain, issues, gaps))
        print(f"wrote clients/{a.slug}/brain-gaps.md")
    return 1 if has_errors(issues) else 0
