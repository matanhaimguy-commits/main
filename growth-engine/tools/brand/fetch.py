"""GET clients/brand-overrides?brand=<slug> -> {brand, overrides: {field: value}, updated_at}. Read-only."""
import sys
import urllib.parse


def from_hub(call, slug: str) -> dict:
    resp = call("GET", "brand-overrides?" + urllib.parse.urlencode({"brand": slug}), api="clients")
    if not isinstance(resp, dict) or not isinstance(resp.get("overrides"), dict):
        sys.exit("BAD_BRAND_OVERRIDES: the hub's answer has no overrides object")
    if resp.get("brand") not in (None, slug):
        sys.exit(f"BAD_BRAND_OVERRIDES: asked for {slug}, the hub answered for {resp['brand']}")
    return resp
