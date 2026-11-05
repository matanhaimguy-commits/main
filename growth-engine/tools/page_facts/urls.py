"""URL checks for untrusted input: http(s) only, no loopback or private IP literals, and same-site tests."""
import ipaddress
from urllib.parse import urlsplit

from .errors import BadUrl

LOCAL_SUFFIXES = (".localhost", ".local", ".internal")


def normalize(url: str) -> str:
    """What the owner typed ("acme.com") as a full address."""
    url = url.strip()
    return url if "://" in url else f"https://{url}"


def host_of(url: str) -> str:
    return (urlsplit(url).hostname or "").lower()


def origin(url: str) -> str:
    p = urlsplit(url)
    return f"{p.scheme}://{p.netloc}"


def check_url(url: str) -> str:
    """Raises BadUrl unless `url` is a public http(s) address; returns it unchanged."""
    p = urlsplit(url)
    host = (p.hostname or "").lower()
    if p.scheme not in ("http", "https") or not host:
        raise BadUrl(f"not a web address: {url[:200]}")
    if host == "localhost" or host.endswith(LOCAL_SUFFIXES):
        raise BadUrl(f"a local address: {host}")
    try:
        ip = ipaddress.ip_address(host)
    except ValueError:
        return url
    if not ip.is_global:
        raise BadUrl(f"a private or local IP address: {host}")
    return url


def same_site(a: str, b: str) -> bool:
    """Same host, ignoring a leading www."""
    return host_of(a).removeprefix("www.") == host_of(b).removeprefix("www.")
