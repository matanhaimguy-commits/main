"""Is the static HTML a client-rendered shell (Lovable, Vite, Wix and the like)? Then trackers, forms and
links added by JavaScript are missing from it, and the static facts are incomplete.

Flagged when the page has almost no visible text AND a mount point (<div id="root"> and kin) or a bundle
script. The evidence is returned with the verdict so the owner can check it in the page source."""
import re

THIN_TEXT = 300
MOUNT_IDS = {"root", "app", "__next", "__nuxt", "svelte", "q-app", "react-root"}
BUNDLE = re.compile(r"/assets/[^/]+\.js|/static/js/|/_next/static/|/_nuxt/|/build/[^/]+\.js|bundle|chunk|"
                    r"\b(?:main|app|index)[.-][\w-]{6,}\.js|parastorage\.com|wixstatic\.com", re.I)
SHOWN = 5


def check(doc) -> dict:
    mounts = [f"#{el['attrs']['id']}" for el in doc.elements if el["attrs"].get("id") in MOUNT_IDS]
    mounts += ["<app-root>"] if doc.find("app-root") else []
    bundles = [s["attrs"]["src"] for s in doc.scripts if s["attrs"].get("src")
               and (s["attrs"].get("type") == "module" or BUNDLE.search(s["attrs"]["src"]))]
    chars = len(doc.text)
    return {"flagged": chars < THIN_TEXT and bool(mounts or bundles), "body_text_chars": chars,
            "mount_points": mounts[:SHOWN], "bundle_scripts": bundles[:SHOWN]}
