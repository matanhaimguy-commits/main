#!/usr/bin/env python3
"""Organic Growth OS command line. The checks live in organic_os/ (one module per job); run with -h for the commands."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from organic_os.cli import main  # noqa: E402

if __name__ == "__main__":
    sys.exit(main())
