"""Build the HyperFrames project for one film: index.html, the templates, vendored scripts, fonts and media.

Any variable value that names an existing image or video file (relative to the EDL) is copied into assets/media/ and
rewritten to that path, so templates only ever load local files.
"""
import copy
import json
import shutil
from pathlib import Path

from . import layers
from .edl import resolve

KIT = Path(__file__).resolve().parents[1]
STUDIO = KIT.parent
MEDIA_EXT = {".png", ".jpg", ".jpeg", ".webp", ".svg", ".mp4", ".webm", ".mov"}


def localise(edl, build):
    """A copy of the EDL whose media variables point into build/assets/media/."""
    edl = copy.deepcopy(edl)
    media = build / "assets" / "media"
    media.mkdir(parents=True, exist_ok=True)

    def fix(vars_):
        for k, val in list(vars_.items()):
            if isinstance(val, str) and Path(val).suffix.lower() in MEDIA_EXT:
                src = resolve(edl, val)
                if src.is_file():
                    shutil.copy2(src, media / src.name)
                    vars_[k] = f"assets/media/{src.name}"

    fix(edl.setdefault("set", {}))
    for b in edl["beats"]:
        for key in ("hero", "scene", "grade"):
            if b.get(key):
                fix(b[key].setdefault("vars", {}))
    return edl


def fonts(edl, build):
    out = []
    (build / "assets" / "fonts").mkdir(parents=True, exist_ok=True)
    for f in edl["brand"].get("fonts", []):
        src = resolve(edl, f["src"])
        shutil.copy2(src, build / "assets" / "fonts" / src.name)
        out.append(dict(f, src=f"assets/fonts/{src.name}"))
    return out


def vendor(build):
    v = build / "assets" / "vendor"
    v.mkdir(parents=True, exist_ok=True)
    gsap = STUDIO / "vendor" / "gsap.min.js"
    if not gsap.is_file():
        raise FileNotFoundError(f"{gsap} missing: run bash motion-studio/setup.sh")
    shutil.copy2(gsap, v / "gsap.min.js")
    shutil.copy2(KIT / "third_party" / "motion-blur.js", v / "motion-blur.js")


def build(edl, face, out_dir):
    out = Path(out_dir)
    if out.exists():
        shutil.rmtree(out)
    (out / "compositions").mkdir(parents=True)
    for t in sorted((KIT / "templates").glob("*.html")):
        shutil.copy2(t, out / "compositions" / t.name)
    vendor(out)
    local = localise(edl, out)
    twin = resolve(edl, edl["twin"]["src"])
    shutil.copy2(twin, out / "assets" / "media" / twin.name)
    html = layers.index_html(local, face, f"assets/media/{twin.name}", fonts(edl, out))
    (out / "index.html").write_text(html)
    (out / "hyperframes.json").write_text(json.dumps({"name": "twin-kit-film"}, indent=2) + "\n")
    return out
