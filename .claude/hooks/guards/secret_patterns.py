"""What a secret looks like: provider key formats, service-role JWTs and literal values given to *_TOKEN / *_KEY names.

Public keys (Supabase anon/publishable, Google browser keys) are not secrets and are not matched.
"""
import base64
import json
import re

# Inside a base64 blob (an embedded font or image) a run of letters is not a token.
NOT_B64 = r"(?<![A-Za-z0-9+/=])"

PROVIDERS = [
    ("Meta access token", re.compile(NOT_B64 + r"EAA[A-Za-z0-9]{60,}(?![A-Za-z0-9+/=])")),
    ("Instagram access token", re.compile(NOT_B64 + r"IG(?:QV|AA)[A-Za-z0-9_-]{60,}(?![A-Za-z0-9+/=])")),
    ("Anthropic key", re.compile(r"\bsk-ant-[A-Za-z0-9_-]{20,}")),
    ("OpenAI key", re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9]{20,}T3BlbkFJ[A-Za-z0-9]{20,}|\bsk-proj-[A-Za-z0-9_-]{40,}")),
    ("ElevenLabs key", re.compile(r"\bsk_[a-f0-9]{48}\b")),
    ("Apify token", re.compile(r"\bapify_api_[A-Za-z0-9]{20,}")),
    ("Supabase secret key", re.compile(r"\bsb_secret_[A-Za-z0-9_-]{20,}")),
    ("GitHub token", re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{36,}|github_pat_[A-Za-z0-9_]{50,})")),
    ("Stripe secret key", re.compile(r"\b(?:sk|rk)_live_[A-Za-z0-9]{20,}")),
    ("AWS access key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("Slack token", re.compile(r"\bxox[abprs]-[A-Za-z0-9-]{10,}")),
    ("private key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----")),
]

JWT = re.compile(r"\beyJ[A-Za-z0-9_-]{10,}\.(eyJ[A-Za-z0-9_-]{10,})\.[A-Za-z0-9_-]{10,}")

ASSIGNED = re.compile(
    r"(?i)\b[A-Z0-9_]*(?:TOKEN|SECRET|API_?KEY|PASSWORD|PASSWD|PRIVATE_KEY)[\"']?\s*[:=]\s*[\"']?([A-Za-z0-9_\-]{24,})")
# Keys made to ship in browser code: PostHog project, Stripe publishable, Supabase publishable.
PUBLIC_PREFIX = ("phc_", "pk_live_", "pk_test_", "sb_publishable_")
PLACEHOLDER = re.compile(r"(?i)example|placeholder|your|x{4,}|changeme|dummy|fake|sample|redacted|test")


def jwt_role(payload_b64: str) -> str | None:
    try:
        raw = base64.urlsafe_b64decode(payload_b64 + "=" * (-len(payload_b64) % 4))
        return json.loads(raw).get("role")
    except (ValueError, json.JSONDecodeError, AttributeError):
        return None


def looks_real(value: str) -> bool:
    """A literal that could be a key: letters and digits, varied, not a placeholder."""
    return (any(c.isdigit() for c in value) and any(c.isalpha() for c in value)
            and len(set(value)) >= 10 and not PLACEHOLDER.search(value) and not value.startswith(PUBLIC_PREFIX))
