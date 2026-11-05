"""The default output: a short plain-English markdown summary for the leak scorecard. Facts only: no
scores, no grades, no estimates. The caveats (JS-built shell, truncation) come first."""
from . import say_forms, say_page, say_routes, say_site, say_tracking
from .urls import host_of
from .wording import page_read

SECTIONS = (say_tracking, say_forms, say_routes, say_page, say_site)


def header(f: dict) -> list[str]:
    when = f["checked_at"].replace("T", " ").replace("Z", " UTC")
    return [f"# Page facts: {host_of(f['final_url'])}",
            f"Checked {f['final_url']} on {when}, from {page_read(f)}. Every line can be checked by opening the page."]


def caveats(f: dict) -> list[str]:
    out, js = [], f["js_built"]
    if js["flagged"]:
        seen = ", ".join(js["mount_points"] + js["bundle_scripts"])
        shell = f"the static HTML is a JavaScript-built shell ({js['body_text_chars']} characters of text; {seen})"
        out.append(f"> **Incomplete:** {shell}. Trackers, forms and links that JavaScript adds are not in it, so a "
                   f"\"not found\" below may be wrong. Run again with --render." if f["mode"] == "static" else
                   f"> Note: {shell}; the facts below come from the rendered page and its network requests.")
    if f["truncated"]:
        out.append("> Note: the page is over the size cap; only its first 3 MB were read.")
    if f.get("rendered") and not f["rendered"]["network_idle"]:
        out.append("> Note: the page never went quiet on the network within 45 s; later requests were not seen.")
    return out


def markdown(f: dict) -> str:
    blocks = [header(f), caveats(f)] + [s.section(f) for s in SECTIONS]
    return "\n\n".join("\n".join(b) for b in blocks if b)
