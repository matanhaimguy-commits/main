"""Seeds a brain from the slim intake: only the few facts the client typed, each with its source, never over a value
that is already filled. Also returns research/seeds.json (website, Instagram, competitors, consents) for O2."""
import copy
import re

from brainio import paths
from brainio.unknown import is_placeholder

CLIENT = "client intake"
# What clients/_template holds before anyone has filled it in: counts as empty.
STARTER_VALUES = {"client": ("_template",), "visual.face": ("faceless",)}


def handle(instagram: str) -> str:
    m = re.search(r"instagram\.com/([\w.]+)", instagram)
    h = m.group(1) if m else instagram.lstrip("@").strip("/ ")
    return f"@{h}" if h else ""


def seed(brain: dict, slim: dict, slug: str) -> tuple[dict, dict]:
    new, sources = copy.deepcopy(brain), {}

    def put(path: str, value, source: str):
        cur = paths.get(new, path)
        if value and (is_placeholder(cur) or cur in STARTER_VALUES.get(path, ())):
            paths.set_(new, path, value)
            sources[path] = source

    put("client", slim["business_name"], f"{CLIENT}: business name")
    ig = handle(slim["instagram"])
    line = " ".join(x for x in (f"{ig} (Instagram)" if ig else "", slim["website"]) if x)
    put("account", line, f"{CLIENT}: Instagram and website links")
    put("offer.main_offer", slim["offer_line"], f"{CLIENT}: offer line")
    if slim["consents"].get("ai_people") is False:
        put("visual.face", "faceless", f"{CLIENT}: consent, no AI-made people or faces")
    if new.get("hub", {}).get("business") in (None, "", "_template"):
        new.setdefault("hub", {})["business"] = slim["brand"] or slug
    new.setdefault("field_sources", {}).update(sources)
    seeds = {"slug": slug, "website": slim["website"], "instagram": slim["instagram"], "competitors": slim["competitors"],
             "consents": slim["consents"], "docs_dir": f"clients/{slug}/foundation"}
    return new, seeds
