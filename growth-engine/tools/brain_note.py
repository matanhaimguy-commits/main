#!/usr/bin/env python3
"""Keep a client's vault note in step with its machine brain.

  python3 growth-engine/tools/brain_note.py <slug> [--title StraightScale] [--check] [--root PATH]

Reads clients/<slug>/brain.json and rewrites only the text between

  <!-- generated:start -->
  <!-- generated:end -->

in brain/Clients/<Title>/<Title>.md (the "Profile (generated)" section). Everything outside the
markers, including a "Notes from the owner" section, is left exactly as it is. If the note does not
exist it is created with frontmatter, the markers and an empty "Notes from the owner" section. If the
note exists without markers, the section is added before "## Notes from the owner" (or at the end).

Never written to the note: any key whose name suggests a secret (token, key, password, secret,
credential; "keyword" is fine), and any value that looks like a token or a phone number.

--title   the vault folder and note name; default: an existing brain/Clients/ folder matching the slug,
          else the slug in title case.
--check   write nothing; exit 1 when the note is missing or out of date (for the daily run).
--root    repo root (default: this repo). Used by the tests.

Exit codes: 0 written or already up to date, 1 out of date (--check), 2 error (no brain.json, bad
JSON, broken markers, bad slug or title).
"""
from __future__ import annotations

import argparse
import datetime as dt
import difflib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
START = "<!-- generated:start -->"
END = "<!-- generated:end -->"
HEADING = "## Profile (generated)"
OWNER_HEADING = "## Notes from the owner"

# ---- secrets ----------------------------------------------------------------------------------

_SECRET_SUBSTRINGS = ("token", "secret", "password", "passwd", "passphrase", "credential")
_SECRET_PARTS = {"key", "keys", "pwd", "auth"}
_SECRET_KEY_SUFFIX = re.compile(r"(api|access|private|secret|signing|auth|app|client|service|license)keys?$")
_TOKEN_RUN = re.compile(r"[A-Za-z0-9_\-]{32,}")
_KNOWN_TOKEN = re.compile(r"(?<![A-Za-z0-9])(sk-|sk_|pk_live_|rk_live_|ghp_|gho_|github_pat_|xox[abpr]-|EAA|AIza)[A-Za-z0-9_\-]{16,}")
_PHONE = re.compile(r"\+\d[\d\s().\-]{6,}\d")


def _key_parts(name: str) -> list[str]:
    spaced = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", str(name))
    return [p for p in re.split(r"[^A-Za-z0-9]+", spaced.lower()) if p]


def is_secret_key(name: str) -> bool:
    """True when a key's name suggests it holds a secret. "keyword" is not one."""
    low = str(name).lower()
    if any(s in low for s in _SECRET_SUBSTRINGS):
        return True
    for part in _key_parts(name):
        if part in _SECRET_PARTS or _SECRET_KEY_SUFFIX.search(part):
            return True
    return False


def _token_like(run: str) -> bool:
    return bool(re.search(r"[a-z]", run) and re.search(r"[A-Z]", run) and re.search(r"\d", run))


def looks_secret_value(value: str) -> bool:
    """True when a string holds something token-like: a known token prefix, or a run of 32+ letters,
    digits, _ and - that mixes upper case, lower case and digits (paths and sentences do not)."""
    s = str(value)
    return bool(_KNOWN_TOKEN.search(s) or any(_token_like(m.group()) for m in _TOKEN_RUN.finditer(s)))


def redact(value: str) -> str:
    s = _KNOWN_TOKEN.sub("(left out: looks like a secret)", str(value))
    s = _TOKEN_RUN.sub(lambda m: "(left out: looks like a secret)" if _token_like(m.group()) else m.group(), s)
    return _PHONE.sub("(phone number left out)", s)


# ---- rendering --------------------------------------------------------------------------------

_ACRONYMS = {"id": "ID", "ids": "IDs", "ai": "AI", "ump": "UMP", "ums": "UMS", "url": "URL", "urls": "URLs",
             "dm": "DM", "dms": "DMs", "cta": "CTA", "ctas": "CTAs", "ig": "IG", "fb": "FB", "seo": "SEO",
             "crm": "CRM", "kpi": "KPI", "faq": "FAQ"}
_ITEM_ID_KEYS = ("id", "keyword", "slug", "handle", "code")
_ITEM_SUMMARY_KEYS = ("name", "title", "statement", "position", "question", "text", "resource", "phrase", "label")


def label(key: str) -> str:
    words = [_ACRONYMS.get(w, w) for w in _key_parts(key)]
    if not words:
        return str(key)
    first = words[0]
    words[0] = first if first in _ACRONYMS.values() else first[:1].upper() + first[1:]
    return " ".join(words)


class Renderer:
    def __init__(self) -> None:
        self.skipped: list[str] = []  # paths of keys or values left out, never their values

    def text(self, value, path: str) -> str:
        if value is None:
            return "not set"
        if isinstance(value, bool):
            return "yes" if value else "no"
        if isinstance(value, (int, float)):
            return str(value)
        s = " ".join(str(value).split())  # one line, no stray newlines
        if looks_secret_value(s):
            self.skipped.append(f"{path} (token-like text removed)")
        if _PHONE.search(s):
            self.skipped.append(f"{path} (phone number removed)")
        s = redact(s)
        return s.replace("<!--", "&lt;!--").replace("-->", "--&gt;")

    def keep(self, key, path: str) -> bool:
        if is_secret_key(key):
            self.skipped.append(f"{path} (key name suggests a secret)")
            return False
        return True

    # A "simple" value renders as a bullet; dicts and lists of dicts get their own section.
    @staticmethod
    def simple(value) -> bool:
        if isinstance(value, dict):
            return False
        if isinstance(value, list):
            return not any(isinstance(v, (dict, list)) for v in value)
        return True

    def bullets_for_list(self, items: list, path: str, indent: int) -> list[str]:
        pad = "  " * indent
        out = []
        for i, v in enumerate(items):
            p = f"{path}[{i}]"
            if isinstance(v, dict):
                out.extend(self.item(v, p, indent))
            elif isinstance(v, list):
                out.append(f"{pad}- item {i + 1}")
                out.extend(self.bullets_for_list(v, p, indent + 1))
            else:
                out.append(f"{pad}- {self.text(v, p)}")
        return out

    def field(self, key: str, value, path: str, indent: int) -> list[str]:
        pad = "  " * indent
        if isinstance(value, list):
            if not value:
                return [f"{pad}- **{label(key)}:** none"]
            return [f"{pad}- **{label(key)}:**"] + self.bullets_for_list(value, path, indent + 1)
        if isinstance(value, dict):
            kept = {k: v for k, v in value.items() if self.keep(k, f"{path}.{k}")}
            if not kept:
                return [f"{pad}- **{label(key)}:** none"]
            out = [f"{pad}- **{label(key)}:**"]
            for k, v in kept.items():
                out.extend(self.field(k, v, f"{path}.{k}", indent + 1))
            return out
        return [f"{pad}- **{label(key)}:** {self.text(value, path)}"]

    def item(self, obj: dict, path: str, indent: int) -> list[str]:
        """One element of a list of objects: a bullet titled by its id and summary, fields nested."""
        pad = "  " * indent
        kept = {k: v for k, v in obj.items() if self.keep(k, f"{path}.{k}")}
        id_key = next((k for k in _ITEM_ID_KEYS
                       if k in kept and isinstance(kept[k], (str, int, float)) and not isinstance(kept[k], bool)), None)
        sum_key = next((k for k in _ITEM_SUMMARY_KEYS
                        if k in kept and k != id_key and isinstance(kept[k], (str, int, float))
                        and not isinstance(kept[k], bool)), None)
        title_bits = []
        if id_key:
            title_bits.append(f"**{self.text(kept[id_key], f'{path}.{id_key}')}**")
        if sum_key:
            title_bits.append(self.text(kept[sum_key], f"{path}.{sum_key}"))
        rest = {k: v for k, v in kept.items() if k not in (id_key, sum_key)}
        if not title_bits:
            title_bits.append("item")
        out = [f"{pad}- " + ": ".join(title_bits)]
        for k, v in rest.items():
            out.extend(self.field(k, v, f"{path}.{k}", indent + 1))
        return out

    def section(self, key: str, value, path: str, level: int) -> list[str]:
        head = f"{'#' * level} {label(key)}" if level <= 6 else f"**{label(key)}**"
        out = [head, ""]
        if isinstance(value, dict):
            out.extend(self.dict_body(value, path, level))
        elif isinstance(value, list):
            out.extend(self.bullets_for_list(value, path, 0) if value else ["none"])
            out.append("")
        return out

    def dict_body(self, obj: dict, path: str, level: int) -> list[str]:
        kept = [(k, v) for k, v in obj.items() if self.keep(k, f"{path}.{k}" if path else k)]
        flat = [(k, v) for k, v in kept if self.simple(v)]
        nested = [(k, v) for k, v in kept if not self.simple(v)]
        out = []
        for k, v in flat:
            out.extend(self.field(k, v, f"{path}.{k}" if path else k, 0))
        if flat:
            out.append("")
        for k, v in nested:
            out.extend(self.section(k, v, f"{path}.{k}" if path else k, level + 1))
        if not kept:
            out.extend(["none", ""])
        return out


def render_profile(brain: dict, source: str) -> tuple[str, list[str]]:
    """The text that goes between the markers, and the list of things left out."""
    r = Renderer()
    lines = [
        f"Generated from `{source}` by `growth-engine/tools/brain_note.py`. Do not edit between the markers:",
        "change brain.json and run the tool again. Keys that look like secrets are never written here.",
        "",
    ]
    lines.extend(r.dict_body(brain, "", 2))
    lines.append(f"Source: {source}")
    body = "\n".join(lines)
    body = re.sub(r"\n{3,}", "\n\n", body).strip("\n")
    return body, r.skipped


# ---- the note ---------------------------------------------------------------------------------

class MarkerError(Exception):
    pass


def block(generated: str) -> str:
    return f"{HEADING}\n\n{START}\n{generated}\n{END}\n"


def new_note(title: str, slug: str, generated: str, today: str) -> str:
    return (
        "---\n"
        "type: client\n"
        f"updated: {today}\n"
        f"tags: [client, {slug}]\n"
        "---\n\n"
        f"# {title}\n\n"
        f"Client note for `{slug}`. The profile below is generated from `clients/{slug}/brain.json`; "
        f"write your own notes outside the markers. Open questions: [[{title} decisions]]. "
        f"Posts: [[{title} content log]]. Rules for every client: [[Standing rules]]. Back to [[00 Index]].\n\n"
        + block(generated)
        + f"\n{OWNER_HEADING}\n\n"
    )


def splice(note: str | None, generated: str, *, title: str, slug: str, today: str) -> str:
    """Return the note with only the generated region replaced (or added)."""
    if note is None:
        return new_note(title, slug, generated, today)
    n_start, n_end = note.count(START), note.count(END)
    if n_start == 0 and n_end == 0:
        owner = re.search(rf"^{re.escape(OWNER_HEADING)}\s*$", note, flags=re.M)
        if owner:
            i = owner.start()
            return note[:i] + block(generated) + "\n" + note[i:]
        sep = "" if note.endswith("\n\n") else ("\n" if note.endswith("\n") else "\n\n")
        return note + sep + block(generated)
    if n_start != 1 or n_end != 1:
        raise MarkerError(f"expected one start and one end marker, found {n_start} and {n_end}")
    a, b = note.index(START), note.index(END)
    if b < a:
        raise MarkerError("the end marker comes before the start marker")
    return note[: a + len(START)] + "\n" + generated + "\n" + note[b:]


def region(note: str | None) -> str:
    if not note or START not in note or END not in note:
        return ""
    return note[note.index(START) + len(START): note.index(END)].strip("\n")


def default_title(root: Path, slug: str) -> str:
    want = re.sub(r"[^a-z0-9]", "", slug.lower())
    clients = root / "brain" / "Clients"
    if clients.is_dir():
        for d in sorted(clients.iterdir()):
            if d.is_dir() and re.sub(r"[^a-z0-9]", "", d.name.lower()) == want:
                return d.name
    return " ".join(w[:1].upper() + w[1:] for w in re.split(r"[-_]+", slug) if w)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Regenerate the 'Profile (generated)' section of a client's vault note.")
    ap.add_argument("slug")
    ap.add_argument("--title")
    ap.add_argument("--check", action="store_true", help="write nothing; exit 1 when the note is out of date")
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)

    if not re.fullmatch(r"[a-z0-9][a-z0-9_-]*", args.slug):
        print(f"error: bad slug {args.slug!r} (lowercase letters, digits, - and _ only)", file=sys.stderr)
        return 2
    root = args.root.resolve()
    title = args.title or default_title(root, args.slug)
    if not title.strip() or "/" in title or "\\" in title or title.strip(".") == "":
        print(f"error: bad title {title!r}", file=sys.stderr)
        return 2

    src_rel = f"clients/{args.slug}/brain.json"
    src = root / src_rel
    try:
        brain = json.loads(src.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"error: {src_rel} not found", file=sys.stderr)
        return 2
    except json.JSONDecodeError as e:
        print(f"error: {src_rel} is not valid JSON: {e}", file=sys.stderr)
        return 2
    if not isinstance(brain, dict):
        print(f"error: {src_rel} must hold a JSON object", file=sys.stderr)
        return 2

    note_rel = f"brain/Clients/{title}/{title}.md"
    note_path = root / note_rel
    old = note_path.read_text(encoding="utf-8") if note_path.exists() else None
    generated, skipped = render_profile(brain, src_rel)
    try:
        new = splice(old, generated, title=title, slug=args.slug, today=dt.date.today().isoformat())
    except MarkerError as e:
        print(f"error: {note_rel}: {e}; nothing written", file=sys.stderr)
        return 2

    for s in skipped:
        print(f"left out: {s}")

    if new == old:
        print(f"{note_rel}: up to date")
        return 0

    if old is None:
        what = "would create" if args.check else "created"
        print(f"{note_rel}: {what} (note was missing)")
    elif START not in old:
        what = "would add" if args.check else "added"
        print(f"{note_rel}: {what} the '{HEADING[3:]}' section (no markers before)")
    else:
        diff = difflib.unified_diff(region(old).splitlines(), generated.splitlines(),
                                    "profile (in note)", "profile (from brain.json)", n=0, lineterm="")
        changed = [l for l in diff]
        adds = sum(1 for l in changed if l.startswith("+") and not l.startswith("+++"))
        dels = sum(1 for l in changed if l.startswith("-") and not l.startswith("---"))
        what = "out of date" if args.check else "updated"
        print(f"{note_rel}: {what} (+{adds} -{dels} lines in the generated section)")
        for l in changed:
            print(l)

    if args.check:
        return 1
    note_path.parent.mkdir(parents=True, exist_ok=True)
    note_path.write_text(new, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
