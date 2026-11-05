"""The forms of a text the Atlas Bash guard matches: as written, with quote and `+` joins taken out, with the command's
own shell variables and `$(echo …)` filled in, with printf escapes decoded, and every base64-looking word decoded."""
from __future__ import annotations

import base64
import binascii
import re

DENY = ("atlas-cli", "atlascloud", "cloud.ai", "atlas_real_bin", "atlas-cloud-skills", "atlas-rest", "atlas-mcp")
B64 = re.compile(r"[A-Za-z0-9+/_-]{12,}={0,2}")


def squash(text: str) -> str:
    """Lower case, with the quote and `+` joins a command can split a word with taken out."""
    t = re.sub(r"""(['"`])\s*\+?\s*(['"`])""", "", text.lower())
    t = re.sub(r"\s*\+\s*", "", t)
    return re.sub(r"""['"`\\{}]""", "", t)


def fill_vars(text: str) -> str:
    """`a=atlas; curl api.${a}cloud.ai` reads as `curl api.atlascloud.ai` (twice, for a variable built from others)."""
    for _ in range(2):
        vals = {m[0]: m[1].strip("'\"") for m in re.findall(r"""\b([A-Za-z_]\w*)=("[^"]*"|'[^']*'|[^\s;&|]*)""", text)}
        for name in sorted(vals, key=len, reverse=True):
            text = re.sub(r"\$\{?" + re.escape(name) + r"\}?", lambda _m, v=vals[name]: v, text)
    return text


def fill_echo(text: str) -> str:
    """`$(echo atlas)`, `$(printf %s atlas)` and the backtick forms read as their words."""
    inner = r"(?:echo|printf)\s+(?:-\w+\s+|%s\s+)*(.*?)"
    text = re.sub(r"\$\(\s*" + inner + r"\s*\)", lambda m: m[1], text)
    return re.sub(r"`\s*" + inner + r"\s*`", lambda m: m[1], text)


def unescape(text: str) -> str:
    """printf and $'…' escapes: \\x61, \\141, \\u0061."""
    text = re.sub(r"\\x([0-9a-fA-F]{2})", lambda m: chr(int(m[1], 16)), text)
    text = re.sub(r"\\u([0-9a-fA-F]{4})", lambda m: chr(int(m[1], 16)), text)
    return re.sub(r"\\([0-7]{3})", lambda m: chr(int(m[1], 8)), text)


def decoded_words(text: str) -> list[str]:
    out = []
    for w in B64.findall(text):
        for dec in (base64.b64decode, base64.urlsafe_b64decode):
            try:
                s = dec(w + "=" * (-len(w) % 4)).decode("utf-8")
            except (binascii.Error, ValueError):
                continue
            if s.isprintable():
                out.append(s)
    return out


def forms(text: str, decode: bool = True) -> list[str]:
    filled = unescape(fill_echo(fill_vars(text)))
    found = [text.lower(), squash(text), squash(filled)]
    return found + ([squash(d) for d in decoded_words(text)] if decode else [])


def hits(text: str, decode: bool = True) -> list[str]:
    fs = forms(text, decode)
    return [p for p in DENY if any(p in f for f in fs)]
