# The shared brain moved

The shared memory (project notes, client notes, decisions, content logs, daily logs) now lives in the owner's
Obsidian vault: the private repo `matanhaimguy-commits/brain`, folder `Agency OS/` (start with
`Agency OS/00 Agency OS.md`). In cloud sessions it is cloned at `/home/user/brain`; see the first bullet of
`CLAUDE.md`. Client facts still change only in `clients/<slug>/brain.json` in this repo, and
`growth-engine/tools/brain_note.py <slug>` writes the client note into the vault.
