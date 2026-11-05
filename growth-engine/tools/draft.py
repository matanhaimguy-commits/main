#!/usr/bin/env python3
"""Quick onboarding, step 2: seed, checklist and check for a client's drafted brain. See braindraft/cli.py."""
import sys

from braindraft.cli import main

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
