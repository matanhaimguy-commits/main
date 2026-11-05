"""python3 growth-engine/tools/page_facts <url> [--render] [--json] [--out FILE]
(or, from growth-engine/tools: python3 -m page_facts <url> ...)"""
import sys
from pathlib import Path

if not __package__:
    sys.path[0] = str(Path(__file__).resolve().parent.parent)
from page_facts.cli import main  # noqa: E402

main()
