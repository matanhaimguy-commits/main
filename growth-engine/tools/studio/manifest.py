"""The manifest's files as the hub takes them: docs inline, media uploaded once and re-used while unchanged."""
import hashlib
import sys
from pathlib import Path

DOC_EXT = (".md", ".markdown", ".txt")
KIND_EXT = {"doc": DOC_EXT + (".pdf",), "audio": (".mp3", ".wav", ".m4a", ".aac", ".ogg", ".flac"),
            "image": (".png", ".jpg", ".jpeg", ".webp", ".gif"), "video": (".mp4", ".mov", ".webm", ".m4v")}
MAX_DOC_CHARS = 300_000


def kind_of(name: str) -> str | None:
    n = name.lower().split("?")[0]
    return next((k for k, exts in KIND_EXT.items() if n.endswith(exts)), None)


def check_entry(i: int, f: dict) -> str:
    """The file's kind, or stop with what is wrong with the entry."""
    label, path, url = f.get("label"), f.get("path"), f.get("url")
    if not label:
        sys.exit(f"BAD_MANIFEST: file {i + 1} needs a \"label\"")
    if bool(path) == bool(url):
        sys.exit(f"BAD_MANIFEST: {label!r} needs a \"path\" or a \"url\" (one of them)")
    kind = f.get("kind") or kind_of(path or url)
    if kind not in KIND_EXT:
        sys.exit(f"BAD_MANIFEST: can't tell what {label!r} is; add \"kind\": doc|audio|image|video")
    return kind


def local_file(e: dict, p: Path, business: str, existing: dict, upload) -> bool:
    """Fills e from a local file: a text doc inline, anything else uploaded unless the hub has the same bytes.
    Returns whether it uploaded."""
    if not p.is_file():
        sys.exit(f"NO_FILE: {p}")
    if e["kind"] == "doc" and p.suffix.lower() in DOC_EXT:
        text = p.read_text(encoding="utf-8")
        if len(text) > MAX_DOC_CHARS:
            sys.exit(f"TOO_BIG: {p} has {len(text)} characters; the hub takes {MAX_DOC_CHARS} per doc")
        e["markdown"] = text
        return False
    sha = hashlib.sha256(p.read_bytes()).hexdigest()
    old = existing.get(e["key"]) or {}
    e["sha256"] = sha
    if old.get("sha256") == sha and old.get("url"):
        e["url"] = old["url"]
        return False
    e["url"] = upload(business, p)
    return True


def resolve_files(manifest: dict, base: Path, business: str, existing: dict, upload) -> tuple[list[dict], int]:
    """The manifest's "files" for the hub, and how many were uploaded. `existing` maps the hub's file keys to
    {sha256, url}; `upload(business, path)` returns a public URL."""
    out, uploaded = [], 0
    for i, f in enumerate(manifest.get("files") or []):
        kind = check_entry(i, f)
        e = {"key": str(f.get("key") or f.get("path") or f.get("url")), "label": f["label"], "kind": kind}
        if f.get("step") is not None:
            e["step"] = int(f["step"])
        if f.get("url"):
            e["url"] = f["url"]
        else:
            uploaded += local_file(e, (base / f["path"]).resolve(), business, existing, upload)
        out.append(e)
    return out, uploaded
