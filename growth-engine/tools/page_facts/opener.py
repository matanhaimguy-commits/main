"""The urllib opener for live fetches: proxy from HTTPS_PROXY, TLS verified against the proxy's CA bundle
(never disabled), http(s) only, and redirects only to public addresses."""
import os
import ssl
import urllib.request

from .urls import check_url

CA_BUNDLE = "/root/.ccr/ca-bundle.crt"


class SafeRedirects(urllib.request.HTTPRedirectHandler):
    """Follows a redirect only when the new address passes check_url (raises BadUrl otherwise)."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        check_url(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def tls_context() -> ssl.SSLContext:
    cafile = os.environ.get("SSL_CERT_FILE") or (CA_BUNDLE if os.path.exists(CA_BUNDLE) else None)
    return ssl.create_default_context(cafile=cafile)


def build_opener() -> urllib.request.OpenerDirector:
    """No file:, ftp: or data: handlers, so an address taken from a page can never read local files."""
    opener = urllib.request.OpenerDirector()
    for h in (urllib.request.ProxyHandler(), urllib.request.HTTPHandler(),
              urllib.request.HTTPSHandler(context=tls_context()), SafeRedirects(),
              urllib.request.HTTPDefaultErrorHandler(), urllib.request.HTTPErrorProcessor()):
        opener.add_handler(h)
    return opener
