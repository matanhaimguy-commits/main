"""page_facts <url> [--render] [--json] [--out FILE]: wires the parts together, nothing else."""
import argparse
import json
import sys
from pathlib import Path

from .errors import BadUrl, PageError, RenderError, Unreachable, exit_message
from .facts import collect
from .fetch import fetch
from .render import render
from .summary import markdown
from .urls import normalize


def parse_args(argv):
    p = argparse.ArgumentParser(prog="page_facts", description="Checkable facts about a prospect's web page.")
    p.add_argument("url")
    p.add_argument("--render", action="store_true", help="also load the page in headless Chromium (Node + Playwright)")
    p.add_argument("--json", action="store_true", help="print the facts as one JSON object")
    p.add_argument("--out", help="write the output to this file instead of printing it")
    return p.parse_args(argv)


def main(argv=None, *, fetcher=fetch, renderer=render) -> None:
    a = parse_args(argv)
    try:
        facts = collect(normalize(a.url), fetch=fetcher, render=renderer if a.render else None)
    except (BadUrl, Unreachable, PageError, RenderError) as e:
        sys.exit(exit_message(e))
    text = json.dumps(facts, ensure_ascii=False, indent=1) if a.json else markdown(facts)
    if a.out:
        Path(a.out).write_text(text + "\n", encoding="utf-8")
        print(f"wrote {a.out}")
    else:
        print(text)
