"""Tests for brain_note.py. Run: python3 -m unittest growth-engine/tools/test_brain_note.py"""
import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import brain_note as bn  # noqa: E402

FAKE_TOKEN = "EAAfakeTOKEN1234567890abcdefXYZ"
FAKE_KEY = "fake-api-key-value-do-not-print"
FAKE_PASSWORD = "hunter2-fake-password"
FAKE_PHONE = "+355 69 123 4567"

BRAIN = {
    "client": "acme",
    "updated": "2026-10-15",
    "access_token": FAKE_TOKEN,
    "business_model": {"sells": "audits", "capacity": "unknown", "api_key": FAKE_KEY},
    "offer": {"main_offer": "free audit", "keyword": "AUDIT"},
    "integrations": {"metaPageToken": FAKE_TOKEN, "hub": {"password": FAKE_PASSWORD, "url": "https://hub.example"}},
    "contact": {"owner_note": f"call the owner on {FAKE_PHONE} after six"},
    "avatars": [{"id": "AV-01", "name": "Busy owner", "words": ["the phone is quiet"], "client_secret": "s3cr3t-fake"}],
    "lead_magnets": [{"keyword": "AUDIT", "resource": "30-minute audit", "live": True, "funnel_id": None}],
    "visual": {"colors": {"main_red": "#BE0F18"}, "fonts": ["Montserrat"], "real_footage": False},
    "voice": {"samples": [], "language": "sq"},
}
SECRET_VALUES = (FAKE_TOKEN, FAKE_KEY, FAKE_PASSWORD, "s3cr3t-fake", FAKE_PHONE)


def run(*args):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = bn.main([str(a) for a in args])
    return code, out.getvalue(), err.getvalue()


class Base(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.write_brain(BRAIN)
        self.note = self.root / "brain" / "Clients" / "Acme" / "Acme.md"

    def tearDown(self):
        self._tmp.cleanup()

    def write_brain(self, data):
        p = self.root / "clients" / "acme" / "brain.json"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")

    def gen(self, *extra):
        return run("acme", "--title", "Acme", "--root", self.root, *extra)


class TestSecrets(unittest.TestCase):
    def test_secret_key_names(self):
        for k in ("access_token", "api_key", "apiKey", "metaPageToken", "password", "client_secret",
                  "HUB_TOKEN", "privatekey", "credentials", "keys"):
            self.assertTrue(bn.is_secret_key(k), k)
        for k in ("keyword", "keywords", "monkey", "turkey", "business_model", "lead_magnets", "funnel_id"):
            self.assertFalse(bn.is_secret_key(k), k)

    def test_render_leaves_out_secrets_but_keeps_keyword(self):
        text, skipped = bn.render_profile(BRAIN, "clients/acme/brain.json")
        for v in SECRET_VALUES:
            self.assertNotIn(v, text)
        for word in ("Access token", "API key", "Password", "Client secret", "Meta page token"):
            self.assertNotIn(word, text)
        self.assertIn("**Keyword:** AUDIT", text)
        self.assertIn("**AUDIT**: 30-minute audit", text)
        joined = "\n".join(skipped)
        self.assertIn("access_token", joined)
        self.assertIn("integrations.hub.password", joined)
        for v in SECRET_VALUES:
            self.assertNotIn(v, joined)  # the report names paths, never values

    def test_token_like_value_under_innocent_key(self):
        text, skipped = bn.render_profile({"notes": f"use {FAKE_TOKEN} for the page"}, "x")
        self.assertNotIn(FAKE_TOKEN, text)
        self.assertTrue(skipped)

    def test_paths_and_sentences_are_not_tokens(self):
        for v in ("motion-studio/projects/straightscale-03/assets/brand/logo-full.png",
                  "2026-10-W3-director-friday", "Patchwork Marketing: paying several suppliers", "#BE0F18"):
            self.assertFalse(bn.looks_secret_value(v), v)


class TestRender(unittest.TestCase):
    def test_generic_layout(self):
        text, _ = bn.render_profile(BRAIN, "clients/acme/brain.json")
        self.assertIn("- **Client:** acme", text)
        self.assertIn("### Business model", text)       # nested dict -> headed section
        self.assertIn("#### Colors", text)               # dict inside a dict -> deeper heading
        self.assertIn("- **Main red:** #BE0F18", text)
        self.assertIn("- **AV-01**: Busy owner", text)   # list of objects -> titled bullets
        self.assertIn("    - the phone is quiet", text) # list inside an item -> nested bullets
        self.assertIn("- **Samples:** none", text)
        self.assertIn("- **Real footage:** no", text)
        self.assertIn("- **Funnel ID:** not set", text)
        self.assertTrue(text.rstrip().endswith("Source: clients/acme/brain.json"))

    def test_marker_text_in_a_value_cannot_break_the_note(self):
        text, _ = bn.render_profile({"note": f"x {bn.END} y {bn.START}"}, "x")
        self.assertNotIn(bn.END, text)
        self.assertNotIn(bn.START, text)

    def test_deterministic(self):
        self.assertEqual(bn.render_profile(BRAIN, "s"), bn.render_profile(BRAIN, "s"))


class TestNote(Base):
    def test_creates_missing_note(self):
        code, out, _ = self.gen()
        self.assertEqual(code, 0)
        self.assertIn("created", out)
        note = self.note.read_text(encoding="utf-8")
        self.assertTrue(note.startswith("---\ntype: client\n"))
        self.assertIn("tags: [client, acme]", note)
        self.assertIn("# Acme", note)
        self.assertIn("## Profile (generated)", note)
        self.assertEqual(note.count(bn.START), 1)
        self.assertEqual(note.count(bn.END), 1)
        self.assertIn("## Notes from the owner", note)
        self.assertLess(note.index(bn.END), note.index("## Notes from the owner"))
        for v in SECRET_VALUES:
            self.assertNotIn(v, note)
            self.assertNotIn(v, out)

    def test_preserves_everything_outside_markers(self):
        before = ("---\ntype: client\nupdated: 2026-01-01\ntags: [client, acme]\n---\n\n# Acme\n\nHand-written intro.\n\n"
                  "## Profile (generated)\n\n")
        after = ("\n\n## Notes from the owner\n\n- Prefers calls on Tuesdays.\n- Do not mention the old logo.\n\n"
                 "## Other section\n\nKeep me.\n")
        self.note.parent.mkdir(parents=True)
        self.note.write_text(before + bn.START + "\nstale profile text\n" + bn.END + after, encoding="utf-8")
        code, out, _ = self.gen()
        self.assertEqual(code, 0)
        self.assertIn("updated", out)
        note = self.note.read_text(encoding="utf-8")
        self.assertTrue(note.startswith(before + bn.START))
        self.assertTrue(note.endswith(bn.END + after))
        self.assertNotIn("stale profile text", note)
        self.assertIn("### Business model", note)

    def test_adds_section_before_owner_notes_when_markers_missing(self):
        self.note.parent.mkdir(parents=True)
        original = "# Acme\n\nIntro.\n\n## Notes from the owner\n\nMy note.\n"
        self.note.write_text(original, encoding="utf-8")
        code, out, _ = self.gen()
        self.assertEqual(code, 0)
        note = self.note.read_text(encoding="utf-8")
        self.assertTrue(note.startswith("# Acme\n\nIntro.\n\n## Profile (generated)"))
        self.assertTrue(note.endswith("## Notes from the owner\n\nMy note.\n"))
        self.assertLess(note.index(bn.END), note.index("## Notes from the owner"))

    def test_appends_when_no_markers_and_no_owner_section(self):
        self.note.parent.mkdir(parents=True)
        self.note.write_text("# Acme\n\nIntro.\n", encoding="utf-8")
        self.assertEqual(self.gen()[0], 0)
        note = self.note.read_text(encoding="utf-8")
        self.assertTrue(note.startswith("# Acme\n\nIntro.\n\n## Profile (generated)"))

    def test_second_run_changes_nothing(self):
        self.gen()
        first = self.note.read_text(encoding="utf-8")
        code, out, _ = self.gen()
        self.assertEqual(code, 0)
        self.assertIn("up to date", out)
        self.assertEqual(self.note.read_text(encoding="utf-8"), first)

    def test_broken_markers_write_nothing(self):
        self.note.parent.mkdir(parents=True)
        for broken in (f"# Acme\n{bn.START}\nno end\n", f"# Acme\n{bn.END}\nx\n{bn.START}\n",
                       f"{bn.START}\n{bn.END}\n{bn.START}\n{bn.END}\n"):
            self.note.write_text(broken, encoding="utf-8")
            code, _, err = self.gen()
            self.assertEqual(code, 2, broken)
            self.assertIn("nothing written", err)
            self.assertEqual(self.note.read_text(encoding="utf-8"), broken)

    def test_missing_or_bad_brain(self):
        self.assertEqual(run("nobody", "--root", self.root)[0], 2)
        (self.root / "clients" / "acme" / "brain.json").write_text("{not json", encoding="utf-8")
        self.assertEqual(self.gen()[0], 2)
        self.assertFalse(self.note.exists())

    def test_bad_slug_and_title(self):
        self.assertEqual(run("../etc", "--root", self.root)[0], 2)
        self.assertEqual(run("acme", "--title", "../x", "--root", self.root)[0], 2)

    def test_default_title_uses_existing_folder(self):
        (self.root / "brain" / "Clients" / "ACME Corp").mkdir(parents=True)
        self.write_brain(BRAIN)
        p = self.root / "clients" / "acme-corp" / "brain.json"
        p.parent.mkdir(parents=True)
        p.write_text(json.dumps(BRAIN), encoding="utf-8")
        self.assertEqual(bn.default_title(self.root, "acme-corp"), "ACME Corp")
        self.assertEqual(bn.default_title(self.root, "new-client"), "New Client")
        self.assertEqual(run("acme-corp", "--root", self.root)[0], 0)
        self.assertTrue((self.root / "brain" / "Clients" / "ACME Corp" / "ACME Corp.md").exists())


class TestCheck(Base):
    def test_check_missing_note_fails_and_creates_nothing(self):
        code, out, _ = self.gen("--check")
        self.assertEqual(code, 1)
        self.assertIn("would create", out)
        self.assertFalse(self.note.exists())

    def test_check_up_to_date_then_drift(self):
        self.gen()
        self.assertEqual(self.gen("--check")[0], 0)
        changed = dict(BRAIN, offer={"main_offer": "free audit, 45 minutes", "keyword": "AUDIT"})
        self.write_brain(changed)
        before = self.note.read_text(encoding="utf-8")
        code, out, _ = self.gen("--check")
        self.assertEqual(code, 1)
        self.assertIn("out of date", out)
        self.assertIn("+- **Main offer:** free audit, 45 minutes", out)
        self.assertIn("-- **Main offer:** free audit", out)
        self.assertEqual(self.note.read_text(encoding="utf-8"), before)  # --check never writes
        self.assertEqual(self.gen()[0], 0)
        self.assertEqual(self.gen("--check")[0], 0)

    def test_check_ignores_owner_edits_outside_markers(self):
        self.gen()
        note = self.note.read_text(encoding="utf-8")
        self.note.write_text(note + "- A new owner note.\n", encoding="utf-8")
        self.assertEqual(self.gen("--check")[0], 0)

    def test_check_catches_hand_edits_inside_markers(self):
        self.gen()
        note = self.note.read_text(encoding="utf-8").replace("- **Client:** acme", "- **Client:** edited by hand")
        self.note.write_text(note, encoding="utf-8")
        self.assertEqual(self.gen("--check")[0], 1)


if __name__ == "__main__":
    unittest.main()
