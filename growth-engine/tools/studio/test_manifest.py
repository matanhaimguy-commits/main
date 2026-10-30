"""Tests for studio/manifest.py: the files a push shows on the page."""
import hashlib
import tempfile
import unittest
from pathlib import Path

from studio.manifest import kind_of, resolve_files
from studio.testbase import Recorder


class Manifest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.base = Path(self.tmp.name)
        (self.base / "docs").mkdir()
        (self.base / "docs" / "script.md").write_text("# Script\n\nLumpy months?\n", encoding="utf-8")
        (self.base / "song.mp3").write_bytes(b"ID3 song bytes")
        (self.base / "board.png").write_bytes(b"\x89PNG board")
        self.hub = Recorder()

    def tearDown(self):
        self.tmp.cleanup()

    def test_kinds_come_from_the_extension(self):
        self.assertEqual([kind_of(n) for n in ("a.MD", "b.wav", "c.webp", "d.mov?x=1", "e.pdf", "f.bin")],
                         ["doc", "audio", "image", "video", "doc", None])

    def test_docs_go_inline_and_unchanged_media_is_not_uploaded_again(self):
        song_sha = hashlib.sha256(b"ID3 song bytes").hexdigest()
        existing = {"song.mp3": {"sha256": song_sha, "url": "https://storage.example/acme/song-old.mp3"}}
        files, uploaded = resolve_files({"files": [
            {"step": 3, "label": "Speech script", "path": "docs/script.md"},
            {"step": 4, "label": "Song master v1", "path": "song.mp3"},
            {"step": 8, "label": "Hook board", "path": "board.png", "key": "HOOK-BOARD"},
            {"label": "Reference", "url": "https://example.com/ref.jpg"},
        ]}, self.base, "acme", existing, self.hub.upload)
        self.assertEqual(files[0], {"key": "docs/script.md", "label": "Speech script", "kind": "doc", "step": 3,
                                    "markdown": "# Script\n\nLumpy months?\n"})
        self.assertEqual(files[1]["url"], "https://storage.example/acme/song-old.mp3")
        self.assertEqual(files[2], {"key": "HOOK-BOARD", "label": "Hook board", "kind": "image", "step": 8,
                                    "sha256": hashlib.sha256(b"\x89PNG board").hexdigest(),
                                    "url": "https://storage.example/acme/board.png"})
        self.assertEqual(files[3], {"key": "https://example.com/ref.jpg", "label": "Reference", "kind": "image",
                                    "url": "https://example.com/ref.jpg"})
        self.assertEqual((uploaded, self.hub.uploads), (1, [("acme", "board.png")]))

    def test_bad_entries_stop_with_a_reason(self):
        for files, why in (([{"path": "a.md"}], "needs a \"label\""),
                           ([{"label": "A"}], "needs a \"path\" or a \"url\""),
                           ([{"label": "A", "path": "a.md", "url": "https://x/a.md"}], "needs a \"path\" or a \"url\""),
                           ([{"label": "A", "path": "a.bin"}], "can't tell what"),
                           ([{"label": "A", "path": "missing.md"}], "NO_FILE")):
            with self.assertRaises(SystemExit) as e:
                resolve_files({"files": files}, self.base, "acme", {}, self.hub.upload)
            self.assertIn(why, str(e.exception))


if __name__ == "__main__":
    unittest.main()
