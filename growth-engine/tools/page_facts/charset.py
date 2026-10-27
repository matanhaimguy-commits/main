"""Bytes to text: the charset from the Content-Type header, else from a <meta charset>, else UTF-8."""
import re

META_CHARSET = re.compile(rb"""<meta[^>]+charset=["']?([\w-]+)""", re.I)


def decode(raw: bytes, header_charset: str | None = None) -> str:
    m = META_CHARSET.search(raw[:4096])
    meta = m.group(1).decode("ascii", "ignore") if m else None
    for name in (header_charset, meta):
        if name:
            try:
                return raw.decode(name, errors="replace")
            except LookupError:
                continue
    return raw.decode("utf-8", errors="replace")
