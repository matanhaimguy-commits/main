#!/usr/bin/env python3
"""Talk to the Growth Engine hub (the Social Agent app) from a studio session.

Needs HUB_TOKEN (the studio token from the app's Settings) in the environment or in
growth-engine/.env, and network access to the hub and its storage host. The token is sent
as a header and never printed.

  hub.py ping
  hub.py clients                                   all businesses with brief, links, funnels
  hub.py client <slug>                             one business, full brief as JSON
  hub.py items [--business slug] [--status draft]
  hub.py upload <slug> <file> [<file> ...]         -> public URLs, one per line
  hub.py push <item.json>                          create/update one item (or {"items": [...]})
  hub.py funnel <slug> <funnel.json>               add/replace a keyword funnel
  hub.py results <slug> [--days 30]                what each post produced

Item JSON: {"business", "external_key", "kind": reel|carousel|image|story, "title",
"caption", "first_comment", "alt_text", "keyword", "funnel_id",
"media": [{"url", "type": image|video}], "cover_url", "scheduled_at" (ISO with offset),
"notes", "source": {...}}. Local file paths in media[].url (or "file": ...) are uploaded
first, so a whole post can be pushed in one command.

Studio (the app's Studio page: each piece's steps 0-15, gates, files and the owner's checkpoints):

  hub.py studio-push <slug> <post_id> [--title T] [--files manifest.json] [--business B] [--summary S]
                                                   read clients/<slug>/runs/<post_id>/ledger.json, build the
                                                   steps and gates as pipeline.py status sees them, upload
                                                   the manifest's files, create/update the run on the page
  hub.py studio-ask <slug> <post_id> <decision.json> [--business B]   put a checkpoint question to the owner
  hub.py studio-answers [--slug S]                 the owner's answers not yet taken in, as JSON
  hub.py studio-synced <decision_id>               mark an answer as taken into the studio

<slug> is a client folder or the app's business slug: a client folder whose brain.json names hub.business (as
clients/straightscale-en names "straightscale", the hub's only business) is sent as that business, so --business is
needed only to override it. Items' "business" is mapped the same way.
Manifest JSON (paths relative to the manifest): {"title", "summary",
"files": [{"step": 3, "label": "Speech script", "path": "docs/script.md"},
          {"step": 4, "label": "Song master v1", "path": "audio/song.v1.mp3"},
          {"label": "Look board", "url": "https://...", "kind": "image"}],
"steps": {"3": {"note": "...", "gates": [{"gate": "G-SCRIPT", "label": "Script Lab loop 1", "status": "FAIL",
          "score": 81, "by": "fresh cold reader", "at": "2026-10-27T10:00:00+00:00", "note": "..."}]}}}.
Docs (.md, .txt) go inline; audio, images and video are uploaded, and re-used while their bytes are
unchanged. "files" is the run's whole file list: a file left out is removed from the page. Manifest
gates show before the ledger's records of that step (use them for loop history the ledger doesn't hold).
Decision JSON: {"checkpoint": "G-HUMAN-SONG", "step": 4, "question": "...", "options": [{"label": "...",
"description": "..."}], "multi": false, "context": "markdown" or "context_file": "path.md",
"key": "G-HUMAN-SONG:SONG@v2" (optional; one question per key, the checkpoint by default)}.
After the owner answers on the Studio page: studio-answers, record each answer in the run (pipeline.py
approve/gate, --by the owner's name, as when they answer in chat), then studio-synced <id>.

Client OS (the app's per-brand dashboard; brands in growth-engine/tools/clients/registry.json):

  hub.py client-sync <slug> [--dry-run] [--json] [--month YYYY-MM]
                                                   build the brand's snapshot (brain, plan, one piece per Post
                                                   Card with its run, project and hook, spend) and POST it to
                                                   /api/clients/sync (contract: agent-start-spark docs/client-os.md);
                                                   --dry-run builds and checks it, prints the counts, sends nothing
"""
import json, mimetypes, os, re, sys, urllib.error, urllib.request
from pathlib import Path

from studio import answers as studio_answers, ask as studio_ask, push as studio_push, synced as studio_synced
from studio.business import business_for
from clients import sync as client_sync

ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = ROOT / ".env"
HUB_URL = os.environ.get("HUB_URL", "https://matan-social-agent.lovable.app").rstrip("/")
# The Studio page's commands (one module each in growth-engine/tools/studio/) and client-sync (tools/clients/).
STUDIO_COMMANDS = {"studio-push": studio_push, "studio-ask": studio_ask, "studio-answers": studio_answers,
                   "studio-synced": studio_synced, "client-sync": client_sync}


def token() -> str:
    t = os.environ.get("HUB_TOKEN")
    if not t and ENV_FILE.exists():
        for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
            m = re.match(r"\s*HUB_TOKEN\s*=\s*['\"]?([^'\"\s]+)", line)
            if m:
                t = m.group(1)
    if not t:
        sys.exit("NO_TOKEN: set HUB_TOKEN (Settings → Studio token in the app) as a cloud environment secret.")
    return t


def call(method: str, path: str, body=None, timeout=120, api="content", missing_ok=False):
    req = urllib.request.Request(
        f"{HUB_URL}/api/{api}/{path}",
        method=method,
        data=json.dumps(body, ensure_ascii=False).encode() if body is not None else None,
        headers={"Authorization": f"Bearer {token()}", "Content-Type": "application/json", "User-Agent": "growth-engine-studio"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read() or b"{}")
    except urllib.error.HTTPError as e:
        if missing_ok and e.code == 404:
            return None
        sys.exit(f"HUB_HTTP_{e.code}: {e.read()[:600].decode(errors='replace')}")
    except urllib.error.URLError as e:
        sys.exit(f"HUB_UNREACHABLE: {e.reason}. Allow {HUB_URL.split('//')[1]} in the cloud environment's network settings.")


def upload(slug: str, file: Path) -> str:
    """One-time signed URL from the hub, then PUT the bytes straight to storage."""
    signed = call("POST", "upload", {"business": slug, "filename": file.name})
    ctype = mimetypes.guess_type(file.name)[0] or "application/octet-stream"
    req = urllib.request.Request(signed["uploadUrl"], method="PUT", data=file.read_bytes(),
                                 headers={"Content-Type": ctype, "x-upsert": "true"})
    try:
        with urllib.request.urlopen(req, timeout=600) as r:
            r.read()
    except urllib.error.HTTPError as e:
        sys.exit(f"STORAGE_HTTP_{e.code}: {e.read()[:400].decode(errors='replace')}")
    except urllib.error.URLError as e:
        host = signed["uploadUrl"].split("/")[2]
        sys.exit(f"STORAGE_UNREACHABLE: {e.reason}. Allow {host} in the cloud environment's network settings.")
    return signed["publicUrl"]


def media_type(path: str) -> str:
    return "video" if path.lower().endswith((".mp4", ".mov", ".webm")) else "image"


def resolve_media(item: dict, base: Path) -> dict:
    """Uploads local files named in media[] / cover_url and swaps in their public URLs."""
    slug = item["business"]
    out = []
    for m in item.get("media", []):
        src = m.get("file") or m.get("url", "")
        if src and not src.startswith(("http://", "https://")):
            p = (base / src).resolve()
            if not p.exists():
                sys.exit(f"NO_FILE: {p}")
            m = {"url": upload(slug, p), "type": m.get("type") or media_type(src)}
        else:
            m = {k: v for k, v in m.items() if k != "file"}
        out.append(m)
    item["media"] = out
    cover = item.get("cover_url")
    if cover and not cover.startswith(("http://", "https://")):
        item["cover_url"] = upload(slug, (base / cover).resolve())
    return item


def main(argv=None):
    a = sys.argv[1:] if argv is None else list(argv)
    if not a or a[0] in ("-h", "--help"):
        print(__doc__)
        return
    cmd, rest = a[0], a[1:]

    def opt(name, default=None):
        if name in rest:
            i = rest.index(name)
            return rest[i + 1]
        return default

    if cmd == "ping":
        n = len(call("GET", "clients")["clients"])
        print(f"hub OK at {HUB_URL}: {n} business(es)")
    elif cmd == "clients":
        for c in call("GET", "clients")["clients"]:
            ig = f"@{c['instagram']['username']}" if c.get("instagram") else "no Instagram"
            fun = ", ".join(f"{f['id']}({'/'.join(f['keywords'])})" for f in c["funnels"]) or "no funnels"
            print(f"{c['slug']:<20} {c['name']:<24} {ig:<22} live={c['live']}  funnels: {fun}")
    elif cmd == "client":
        slug = business_for(rest[0])
        c = next((c for c in call("GET", "clients")["clients"] if c["slug"] == slug), None)
        if not c:
            sys.exit(f"NO_CLIENT: {slug}")
        print(json.dumps(c, ensure_ascii=False, indent=1))
    elif cmd == "items":
        q = "&".join(f"{k}={v}" for k, v in (("business", opt("--business") and business_for(opt("--business"))), ("status", opt("--status"))) if v)
        for it in call("GET", "items" + (f"?{q}" if q else ""))["items"]:
            when = it.get("scheduled_at") or ""
            print(f"#{it['id']:<5} {it['business']:<16} {it['status']:<10} {it['kind']:<9} {when[:16]:<17} {it.get('external_key') or ''}  {(it.get('title') or it['caption'][:50])!r}")
    elif cmd == "upload":
        slug = business_for(rest[0])
        for f in rest[1:]:
            print(upload(slug, Path(f)))
    elif cmd == "push":
        path = Path(rest[0])
        body = json.loads(path.read_text(encoding="utf-8"))
        items = body["items"] if "items" in body else [body]
        for i in items:
            if i.get("business"):
                i["business"] = business_for(i["business"])
        items = [resolve_media(i, path.parent) for i in items]
        res = call("POST", "items", {"items": items})
        for it in res["items"]:
            print(f"#{it['id']} {it['status']} {it['kind']} {it.get('external_key') or ''}")
    elif cmd == "funnel":
        slug, path = business_for(rest[0]), Path(rest[1])
        res = call("POST", "funnels", {"business": slug, "funnel": json.loads(path.read_text(encoding="utf-8"))})
        print(json.dumps(res, ensure_ascii=False, indent=1))
    elif cmd == "results":
        slug = business_for(rest[0])
        res = call("GET", f"results?business={slug}&days={opt('--days', '30')}")
        print(json.dumps(res["results"], ensure_ascii=False, indent=1))
    elif cmd in STUDIO_COMMANDS:
        STUDIO_COMMANDS[cmd].cli(rest, call=call, upload=upload, hub_url=HUB_URL)
    else:
        sys.exit(f"unknown command {cmd}; run hub.py --help")


if __name__ == "__main__":
    main()
