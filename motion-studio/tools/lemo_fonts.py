#!/usr/bin/env python3
"""Fetch the fonts a Lemo-Opuscar demo expects (they are not in git) from the google/fonts repo.

    python3 tools/lemo_fonts.py ~/lemo/styles/<slug>/demo [more demo dirs ...]

Reads demo/fonts/*.css, and for every url(<file>) that is missing, guesses the Google Fonts family from the
file name (InterTight-var.woff2 -> ofl/intertight), reads that family's METADATA.pb from
raw.githubusercontent.com, and saves the best matching file (variable font first, italic when the name
says Italic) under the expected name. Browsers sniff the format, so a .ttf saved as .woff2 loads fine.
Prints what it could not find; get those by hand (the demo's CREDITS names every family).
"""
import pathlib, re, sys, urllib.request

RAW = "https://raw.githubusercontent.com/google/fonts/main"
SUFFIX = re.compile(r"[-_]?(var|vf|variable|regular|italic|bold|semibold|medium|light|black|extrabold|"
                    r"thin|\d{3}|latin|subset|sc)\b", re.I)


def fetch(url):
    try:
        with urllib.request.urlopen(url, timeout=20) as r:
            return r.read()
    except Exception:
        return None


def candidates(stem):
    base = stem
    while True:  # strip trailing style words: CormorantGaramond-SemiBoldItalic -> CormorantGaramond
        new = re.sub(r"[-_](Var|VF|Regular|Italic|Bold|SemiBold|SemiBoldItalic|Medium|Light|Black|ExtraBold|"
                      r"Thin|\d{3})$", "", base, flags=re.I)
        if new == base:
            break
        base = new
    key = re.sub(r"[^a-z0-9]", "", base.lower())
    out = [key]
    for drop in ("sc", "mono", "display", "text"):  # CormorantSC -> cormorantsc then cormorant
        if key.endswith(drop) and len(key) > len(drop) + 2:
            out.append(key[: -len(drop)])
    return out


def pick(meta, want_italic):
    files = re.findall(r'filename:\s*"([^"]+)"', meta)
    files = [f for f in files if ("Italic" in f) == want_italic] or files
    var = [f for f in files if "[" in f]
    return (var or files or [None])[0]


def main():
    missing = []
    for demo in map(pathlib.Path, sys.argv[1:]):
        for css in sorted((demo / "fonts").glob("*.css")):
            for name in re.findall(r"url\(['\"]?([^)'\"]+)", css.read_text()):
                if "/" in name or name.startswith("data:"):
                    continue
                target = css.parent / name
                if target.exists():
                    continue
                stem = pathlib.Path(name).stem
                got = False
                for lic in ("ofl", "apache", "ufl"):
                    for key in candidates(stem):
                        meta = fetch(f"{RAW}/{lic}/{key}/METADATA.pb")
                        if not meta:
                            continue
                        f = pick(meta.decode(), "italic" in stem.lower())
                        data = f and fetch(f"{RAW}/{lic}/{key}/{urllib.request.quote(f)}")
                        if data:
                            target.write_bytes(data)
                            print(f"got   {target}  <- {lic}/{key}/{f}")
                            got = True
                            break
                    if got:
                        break
                if not got:
                    missing.append(str(target))
    for m in missing:
        print(f"MISSING {m}  (see the demo's CREDITS for the family)")
    sys.exit(1 if missing else 0)


if __name__ == "__main__":
    main()
