"""Exact tracker signatures. Never loose words: "facebook" or "analytics" in a page proves nothing.

Each entry: `present` patterns prove the tracker's code is on the page; `ids` patterns prove it and capture an
id; `ids_if_present` capture ids only once the tracker is proven (a bare quoted id proves nothing alone).
The ids patterns also match the network requests a rendered page makes (e.g. a pixel loaded through GTM)."""
import re

ID_GTM, ID_GA4, ID_AW = r"(GTM-[A-Z0-9]{4,12})", r"(G-[A-Z0-9]{4,15})", r"(AW-\d{6,12})"
QUOTE = r"""["']"""

SIGNATURES = [
    {"name": "Meta Pixel",
     "present": [r"connect\.facebook\.net/[\w-]+/fbevents\.js", r"\bfbq\(\s*" + QUOTE + "init" + QUOTE],
     "ids": [r"\bfbq\(\s*" + QUOTE + "init" + QUOTE + r"\s*,\s*" + QUOTE + r"?(\d{5,20})",
             r"facebook\.com/tr/?\?(?:[^\"'\s<>]*&(?:amp;)?)?id=(\d{5,20})", r"connect\.facebook\.net/signals/config/(\d{5,20})"]},
    {"name": "Google Tag Manager",
     "present": [r"googletagmanager\.com/gtm\.js"],
     "ids": [r"googletagmanager\.com/(?:gtm\.js|ns\.html)\?id=" + ID_GTM],
     "ids_if_present": [QUOTE + ID_GTM + QUOTE]},
    {"name": "GA4",
     "present": [],
     "ids": [r"googletagmanager\.com/gtag/js\?id=" + ID_GA4,
             r"\bgtag\(\s*" + QUOTE + "config" + QUOTE + r"\s*,\s*" + QUOTE + ID_GA4,
             r"(?:google-analytics|analytics\.google)\.com/g/collect\?[^\s\"'<>]*?\btid=" + ID_GA4]},
    {"name": "Google Ads",
     "present": [r"googleadservices\.com/pagead/conversion", r"googleads\.g\.doubleclick\.net/pagead/viewthroughconversion"],
     "ids": [r"googletagmanager\.com/gtag/js\?id=" + ID_AW,
             r"\bgtag\(\s*" + QUOTE + "(?:config|event)" + QUOTE + r"\s*,\s*" + QUOTE + ID_AW,
             r"\bsend_to" + QUOTE + r"?\s*:\s*" + QUOTE + ID_AW]},
    {"name": "TikTok Pixel",
     "present": [r"analytics\.tiktok\.com/[\w./-]*events\.js"],
     "ids": [r"\bttq\.load\(\s*" + QUOTE + r"([A-Z0-9]{10,30})" + QUOTE,
             r"analytics\.tiktok\.com/[\w./-]*events\.js\?[^\s\"'<>]*?\bsdkid=([A-Z0-9]{10,30})"]},
    {"name": "Microsoft Clarity",
     "present": [r"clarity\.ms/tag/"],
     "ids": [r"clarity\.ms/tag/([a-z0-9]{6,20})\b"],
     "ids_if_present": [QUOTE + "clarity" + QUOTE + r"\s*,\s*" + QUOTE + "script" + QUOTE + r"\s*,\s*" + QUOTE + r"([a-z0-9]{6,20})" + QUOTE]},
    {"name": "Hotjar",
     "present": [r"static\.hotjar\.com/c/hotjar-"],
     "ids": [r"static\.hotjar\.com/c/hotjar-(\d{5,10})\.js"],
     "ids_if_present": [r"\bhjid\s*:\s*(\d{5,10})"]},
]

COMPILED = [{"name": s["name"], **{k: [re.compile(p) for p in s.get(k, [])] for k in ("present", "ids", "ids_if_present")}}
            for s in SIGNATURES]
