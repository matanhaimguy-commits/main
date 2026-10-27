"""Secret scan. Run: python3 -m unittest discover -s .claude/hooks/guards -p 'test_*.py'

Sample secrets are built at run time so this file holds none itself.
"""
import base64
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from guards.secret_scan import scan  # noqa: E402


def jwt(role: str) -> str:
    part = lambda d: base64.urlsafe_b64encode(json.dumps(d).encode()).decode().rstrip("=")
    return f"{part({'alg': 'HS256', 'typ': 'JWT'})}.{part({'iss': 'supabase', 'role': role})}.{'s1gnatureAbc' * 3}"


class ScanTest(unittest.TestCase):
    def kinds(self, text):
        return [f["kind"] for f in scan(text)]

    def test_provider_keys(self):
        self.assertEqual(self.kinds("key = '" + "sk-" + "ant-" + "a1B2" * 10 + "'"), ["Anthropic key"])
        self.assertEqual(self.kinds("EA" + "A" + "Bz9" * 40), ["Meta access token"])
        self.assertEqual(self.kinds("apify" + "_api_" + "Q7w" * 10), ["Apify token"])
        self.assertEqual(self.kinds("sk" + "_" + "0a1b2c3d" * 6), ["ElevenLabs key"])

    def test_service_role_jwt_is_a_secret_and_anon_is_not(self):
        self.assertEqual(self.kinds(jwt("service_role")), ["Supabase service-role key"])
        self.assertEqual(self.kinds(jwt("anon")), [])

    def test_literal_values_for_token_names(self):
        self.assertEqual(self.kinds("HUB_TOKEN=" + "h7Kq2Lm9Zp4Rt8Wx3Vb6Nc1D"), ["a literal value for a token, key or password"])
        self.assertEqual(self.kinds('"higgsfield_api_key": "' + "Ab12Cd34Ef56Gh78Ij90Kl12" + '"'), ["a literal value for a token, key or password"])

    def test_references_and_placeholders_pass(self):
        for text in ["HUB_TOKEN = os.environ.get('HUB_TOKEN')", "token: process.env.HUB_TOKEN",
                     "API_KEY=your_api_key_goes_here_123456", "HUB_TOKEN=${HUB_TOKEN}", "Read the studio token in Settings."]:
            self.assertEqual(self.kinds(text), [], text)

    def test_base64_blobs_and_public_keys_pass(self):
        blob = "src: url(data:font/woff2;base64,d09GMgABAAAA+" + "EA" + "Aw" + "Qk9" * 40 + "/AAAB)"
        self.assertEqual(self.kinds(blob), [])
        self.assertEqual(self.kinds("POSTHOG_KEY = '" + "phc" + "_" + "a1B2c3D4e5F6g7H8i9J0kLmN" + "'"), [])

    def test_findings_never_hold_the_secret(self):
        secret = "sk-" + "ant-" + "Zz9Yy8Xx7Ww6Vv5Uu4Tt3"
        self.assertNotIn(secret, json.dumps(scan(secret)))


if __name__ == "__main__":
    unittest.main()
