"""Printing check results for the command line."""
from __future__ import annotations

from .issues import ERROR


def print_issues(label: str, issues: list[dict]) -> None:
    if not issues:
        print(f"OK  {label}")
        return
    for i in issues:
        print(f"{'FAIL' if i['level'] == ERROR else 'warn'} {label}: [{i['code']}] {i['msg']}")
