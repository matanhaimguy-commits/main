"""The ways a check can stop, and the one-line message the CLI exits with for each (hub.py style)."""


class BadUrl(ValueError):
    """Not an http(s) address, or one that points inside this machine's network."""


class Unreachable(Exception):
    """The proxy refused the host, DNS failed, or the host did not answer."""

    def __init__(self, host: str, reason: str):
        super().__init__(f"{host}: {reason}")
        self.host, self.reason = host, reason


class PageError(Exception):
    """The site answered, but not with an HTML page (an HTTP error, a PDF, ...)."""


class RenderError(Exception):
    """The Node/Playwright helper failed for a reason other than the network."""


def exit_message(e: Exception) -> str:
    if isinstance(e, Unreachable):
        return (f"UNREACHABLE: {e.host} ({e.reason}). If the proxy refused it or DNS failed, "
                f"allow {e.host} in the cloud environment's network settings.")
    if isinstance(e, BadUrl):
        return f"BAD_URL: {e}"
    if isinstance(e, RenderError):
        return f"RENDER_FAILED: {e}"
    return str(e)
