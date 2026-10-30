"""Regenerates the brand's vault note (tools/brain_note.py) when the vault exists. Returns a one-line result."""
from pathlib import Path

import brain_note


def regenerate(slug: str, root: Path | None = None, vault: Path | None = None) -> str:
    if brain_note.notes_dir(vault, None) is None:
        return "vault note: skipped (no vault found; clone matanhaimguy-commits/brain to /home/user/brain)"
    argv = [slug] + (["--vault", str(vault)] if vault else []) + (["--root", str(root)] if root else [])
    code = brain_note.main(argv)
    return "vault note: regenerated" if code == 0 else f"vault note: brain_note.py failed (exit {code})"
