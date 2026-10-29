"""Downloads the intake's documents into clients/<slug>/foundation/ (gitignored: private client documents).

Signed URLs expire in 10 minutes, so this runs right after the intake is read. The hub token is never sent to the
storage host (the signed URL carries its own permission). A document that fails is listed with its error, the rest
are still saved."""
import json
import re
import urllib.error
import urllib.request
from pathlib import Path

MAX_BYTES = 100 * 1024 * 1024


def safe_name(name: str, taken: set[str]) -> str:
    """A file name with no path parts, and unique among the names already used."""
    base = re.sub(r"[^\w.\- ]+", "_", Path(str(name)).name).strip(" .") or "document"
    out, n = base, 1
    while out.lower() in taken:
        n += 1
        stem, dot, ext = base.rpartition(".")
        out = f"{stem}-{n}.{ext}" if dot and stem else f"{base}-{n}"
    taken.add(out.lower())
    return out


def fetch_bytes(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "growth-engine-studio"})
    with urllib.request.urlopen(req, timeout=120) as r:
        data = r.read(MAX_BYTES + 1)
    if len(data) > MAX_BYTES:
        raise ValueError("larger than 100 MB")
    return data


def download(docs: list[dict], dest: Path, get=fetch_bytes) -> list[dict]:
    """Saves each doc under dest; returns [{name, saved_as, mime, size, bytes, error}] and writes dest/manifest.json
    (no signed URLs in it)."""
    dest.mkdir(parents=True, exist_ok=True)
    taken, out = set(), []
    for d in docs:
        rec = {"name": d["name"], "saved_as": None, "mime": d.get("mime"), "size": d.get("size"), "bytes": None, "error": None}
        try:
            data = get(d["signed_url"])
            rec["saved_as"] = safe_name(d["name"], taken)
            (dest / rec["saved_as"]).write_bytes(data)
            rec["bytes"] = len(data)
            if isinstance(d.get("size"), int) and d["size"] != len(data):
                rec["error"] = f"size {len(data)} bytes, the intake said {d['size']}"
        except (urllib.error.URLError, OSError, ValueError) as e:
            rec["error"] = f"could not download ({getattr(e, 'reason', e)}); the link may have expired, pull again"
        out.append(rec)
    (dest / "manifest.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return out
