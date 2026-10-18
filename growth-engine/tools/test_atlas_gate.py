"""Tests for the Atlas CLI wrapper (tools/atlas/atlas_gate.py), its gate path in pipeline.py and setup.sh's sha check.

    python3 -m unittest growth-engine/tools/test_atlas_gate.py

The wrapper runs as a subprocess from a temp copy of the repo (so each test sets its own Atlas allowlist), against a
temp ledger (PIPELINE_ROOT) and a stub in place of the real CLI that records its argv and stdin. Nothing reaches Atlas.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "atlas"))
import atlas_gate as G  # noqa: E402
import pipeline as P  # noqa: E402
import test_pipeline as TP  # noqa: E402

REPO = HERE.parents[1]
SLUG, POST, LIB = TP.SLUG, TP.POST, TP.LIB
STYLE_URL = "https://cdn.example.com/acme/style-v1.png"
COVER_PROMPT = "Instagram post, portrait 4:5. TEXT: '3 GABIME' ..."
IMG_MODEL = "google/nano-banana-2/edit"
ENV_SEEN = ("ATLAS_TELEMETRY", "ATLAS_AUTO_UPDATE", "DO_NOT_TRACK", "ATLAS_API_BASE", "ATLAS_AUTH_BASE",
            "ATLAS_API_EXTRA_HEADER_NAME", "ATLAS_API_EXTRA_HEADER_VALUE", "ATLAS_VERSION_URL", "ATLAS_POSTHOG_HOST")
STUB = """#!/usr/bin/env python3
import json, os, sys
data = sys.stdin.buffer.read()
with open(os.environ["STUB_OUT"], "w") as f:
    json.dump({"argv": sys.argv[1:], "stdin": data.decode("utf-8", "replace"),
               "env": {k: os.environ.get(k) for k in %r}}, f)
print("stub ran")
""" % (ENV_SEEN,)


def entry(model=IMG_MODEL, kind="image", **kw):
    """An owner's entry in standards.json models.atlas.allowed."""
    return {"id": model, "kind": kind, **kw}


IMG_ENTRY = entry(params_one_of={"aspect_ratio": ["4:5", "9:16"]})


class Wrapper(TP.Base):
    """End to end: the wrapper process, the gate and the stub."""

    @classmethod
    def setUpClass(cls):
        cls.repo_tmp = tempfile.TemporaryDirectory()
        r = Path(cls.repo_tmp.name)
        for rel in ("growth-engine/tools/pipeline.py", "growth-engine/tools/organic.py",
                    "growth-engine/tools/atlas/atlas_gate.py", "growth-engine/production/standards.json",
                    "growth-engine/production/schemas", "growth-engine/config"):
            src, dst = REPO / rel, r / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            (shutil.copytree if src.is_dir() else shutil.copy)(src, dst)
        cls.gate_py = r / "growth-engine/tools/atlas/atlas_gate.py"
        cls.standards = r / "growth-engine/production/standards.json"

    @classmethod
    def tearDownClass(cls):
        cls.repo_tmp.cleanup()

    def setUp(self):
        super().setUp()
        self.stub = self.root / "real-atlas"
        self.stub.write_text(STUB)
        self.stub.chmod(0o755)
        self.out = self.root / "stub.json"
        self.allow([])

    def allow(self, entries):
        std = json.loads((REPO / "growth-engine/production/standards.json").read_text())
        std["models"]["atlas"]["allowed"] = list(entries)
        self.standards.write_text(json.dumps(std))

    def atlas(self, *args, stdin=None, cwd=None, env=None):
        base = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "PIPELINE_ROOT": str(self.root),
                "ATLAS_REAL_BIN": str(self.stub), "STUB_OUT": str(self.out)}
        env = {**base, **(env or {})}
        env = {k: v for k, v in env.items() if v is not None}
        if self.out.exists():
            self.out.unlink()
        return subprocess.run([sys.executable, str(self.gate_py), *args], input=stdin if stdin is not None else b"",
                              capture_output=True, env=env, cwd=cwd or self.root)

    def ran(self):
        return json.loads(self.out.read_text()) if self.out.exists() else None

    def blocked(self, r, *needles):
        err = r.stderr.decode()
        self.assertEqual(r.returncode, 3, err)
        self.assertIsNone(self.ran(), "the real CLI must not run")
        for n in needles:
            self.assertIn(n, err)
        return err

    def passed(self, r, args, stdin=""):
        self.assertEqual(r.returncode, 0, r.stderr.decode())
        ran = self.ran()
        self.assertEqual({"argv": ran["argv"], "stdin": ran["stdin"]}, {"argv": list(args), "stdin": stdin})
        return ran

    def register(self, prompt, medias=None):
        """A new version of COVER with this prompt card, its prompt review PASS."""
        P.new_asset(SLUG, POST, "COVER", "cover", ["SL01"])
        a = P.set_prompt(SLUG, POST, "COVER", prompt,
                         medias if medias is not None else [{"value": STYLE_URL, "role": "image_references"}])
        P.record_report(SLUG, POST, self.report(gate="G-PROMPT-IMG", asset_id="COVER", version=a["version"],
                                                prompt_sha256=a["prompt_sha256"], checks=self.checks("prompt")))
        return a

    def reviewed_cover(self, aspect="4:5"):
        """A cover whose prompt, reference (the style ref, by URL) and budget passed: what Atlas may make."""
        self.lib_with_style()
        P.add_media(SLUG, LIB, "STYLE@v1", ids=[STYLE_URL])
        P.init_run(SLUG, POST, "carousel_mistakes")
        TP.write(P.spec_path(SLUG, POST, "SL01"), {**TP.SLIDE, "camera": {**TP.SLIDE["camera"], "aspect": aspect}})
        P.spec_check(SLUG, POST)
        P.record_report(SLUG, POST, self.report(gate="G-SPEC", shot_id="SL01",
                                                spec_sha256=P.sha_file(P.spec_path(SLUG, POST, "SL01")), checks=[]))
        P.new_asset(SLUG, POST, "COVER", "cover", ["SL01"])
        a = P.set_prompt(SLUG, POST, "COVER", COVER_PROMPT, [{"value": STYLE_URL, "role": "image_references"}])
        P.budget(SLUG, POST, planned=10, balance=500)
        P.record_report(SLUG, POST, self.report(gate="G-PROMPT-IMG", asset_id="COVER", version=1,
                                                prompt_sha256=a["prompt_sha256"], checks=self.checks("prompt")))
        return a

    COVER_ARGS = ("generate", "image", IMG_MODEL, "-p", COVER_PROMPT, "--images", STYLE_URL, "--aspect-ratio", "4:5")

    # ---- passthrough: free commands go straight to the real CLI, argv unchanged ----

    def test_free_commands_pass_through(self):
        for args in (["version"], ["auth", "status", "--json"], ["account", "balance"], ["--json", "models", "list",
                     "--type", "video"], ["models", "get", "bytedance/seedance-2.0-fast/text-to-video", "--json"],
                     ["generate", "get", "pred-1", "--wait"], ["gen", "history", "--limit", "5"],
                     ["generate", "ops", "resume", "op-1"], ["upload", "./ref.png", "--json"], ["generate", "--help"],
                     ["help", "generate", "video"], ["--help"], [], ["update", "--check"], ["chat", "--help"],
                     ["skills", "list", "--json"]):
            with self.subTest(args=args):
                self.passed(self.atlas(*args), args)

    def test_cost_estimates_are_never_gated(self):
        for args in (["generate", "cost", "video", "bytedance/seedance-2.0/text-to-video", "-p", "unregistered",
                      "--duration", "5", "--json"],
                     ["gen", "estimate", "image", IMG_MODEL, "-p", "x", "--images", "@local.png"],
                     ["--json", "generate", "cost", "audio", "some/tts", "-p", "x"]):
            with self.subTest(args=args):
                self.passed(self.atlas(*args), args)
        args = ["generate", "cost", "video", "m/x", "--input", "-"]
        self.passed(self.atlas(*args, stdin=b'{"prompt": "x"}'), args, stdin='{"prompt": "x"}')

    def test_help_and_explain_submit_nothing_and_pass(self):
        for args in (["generate", "video", "m/x", "--help"], ["generate", "video", "m/x", "-p", "x", "--explain"],
                     ["generate", "image", "m/x", "-p", "x", "--explain", "true"], ["generate", "image", "-h"]):
            with self.subTest(args=args):
                self.passed(self.atlas(*args), args)

    # ---- billable calls go through the gate ----

    def test_empty_allowlist_blocks_a_fully_reviewed_call(self):
        self.reviewed_cover()
        err = self.blocked(self.atlas(*self.COVER_ARGS), "GENERATION BLOCKED", "not on the owner's list",
                           "no Atlas model is named yet")
        self.assertNotIn("not registered", err)
        # an unnamed model is the first thing the gate says, before any prompt work
        err = self.blocked(self.atlas("generate", "video", "bytedance/seedance-2.0-fast/text-to-video", "-p", "x"),
                           "not on the owner's list")
        self.assertNotIn("not registered", err)

    def test_allowed_model_and_reviewed_call_runs_with_unchanged_argv(self):
        self.reviewed_cover()
        self.allow([IMG_ENTRY])
        args = ("--json", "-q", *self.COVER_ARGS, "--no-wait", "-o", "out/cover.png")
        self.passed(self.atlas(*args), args)
        calls = (P.run_dir(SLUG, POST) / "calls.jsonl").read_text().splitlines()
        e = json.loads(calls[-1])
        self.assertEqual((e["tool"], e["decision"], e["asset"]), ("atlas_generate", "ALLOW", "COVER@v1"))
        # the same version again is a retake: blocked
        self.blocked(self.atlas(*self.COVER_ARGS), "already generated")

    def test_banned_family_stays_blocked_even_with_g_exception(self):
        self.reviewed_cover()
        self.allow([IMG_ENTRY])
        seedream = "bytedance/seedream-v4.5/edit"
        P.record_gate(SLUG, POST, "G-EXCEPTION", "PASS", "Matan", asset="COVER@v1", note="one-off",
                      data={"model": seedream})
        args = list(self.COVER_ARGS)
        args[2] = seedream
        self.blocked(self.atlas(*args), f"Atlas model {seedream} is not on the owner's list")
        video = ["generate", "video", "bytedance/seedance-2.0/image-to-video", "-p", COVER_PROMPT, "--images",
                 STYLE_URL]
        self.blocked(self.atlas(*video), "seedance-2.0/image-to-video is not on the owner's list")

    def test_gate_checks_prompt_references_and_aspect_from_the_call(self):
        self.reviewed_cover()
        self.allow([IMG_ENTRY])
        args = list(self.COVER_ARGS)
        args[4] = "a different prompt"
        self.blocked(self.atlas(*args), "not registered")
        self.blocked(self.atlas("generate", "image", IMG_MODEL, "-p", COVER_PROMPT, "--aspect-ratio", "4:5"),
                     "references differ")
        self.blocked(self.atlas(*self.COVER_ARGS[:-1], "9:16"), "aspect_ratio 9:16 differs")
        self.blocked(self.atlas("generate", "video", IMG_MODEL, "-p", COVER_PROMPT, "--images", STYLE_URL),
                     "is named for image calls, not video")

    def test_unregistered_prompt_and_selftest_are_blocked(self):
        self.allow([IMG_ENTRY])
        self.blocked(self.atlas("generate", "image", IMG_MODEL, "-p", "a nice picture"), "not registered")
        self.blocked(self.atlas("generate", "image", "x/y", "-p", "GATE-SELFTEST"), "the production gate is live")

    def test_flags_before_the_subcommand(self):
        self.reviewed_cover()
        for pre in (["--json"], ["-q", "--no-color"], ["--verbose=true"]):
            with self.subTest(pre=pre):
                self.blocked(self.atlas(*pre, *self.COVER_ARGS), "not on the owner's list")
        self.blocked(self.atlas("generate", "--json", *self.COVER_ARGS[1:]), "not on the owner's list")
        for args in (["--output", "x", *self.COVER_ARGS], ["-p", "x", *self.COVER_ARGS], ["--", *self.COVER_ARGS],
                     ["-qv", *self.COVER_ARGS]):
            with self.subTest(args=args):
                self.blocked(self.atlas(*args), "put flags after the command")

    def test_input_file_and_stdin(self):
        self.reviewed_cover()
        self.allow([IMG_ENTRY])
        body = {"prompt": COVER_PROMPT, "images": [STYLE_URL], "aspect_ratio": "4:5"}
        raw_file = json.dumps(body)
        (self.root / "req.json").write_text(raw_file)
        # a file is read once: the real CLI gets `--input -` and, on stdin, the bytes the gate read
        args = ["generate", "image", IMG_MODEL, "--input", "req.json"]
        self.passed(self.atlas(*args), ["generate", "image", IMG_MODEL, "--input", "-"], stdin=raw_file)
        self.register(COVER_PROMPT)
        args = ["generate", "image", IMG_MODEL, "--input=req.json", "--json"]
        self.passed(self.atlas(*args), ["generate", "image", IMG_MODEL, "--input=-", "--json"], stdin=raw_file)
        # stdin: the gate reads it and the real CLI gets the same bytes
        self.register(COVER_PROMPT)
        raw = json.dumps(body, indent=1)
        args = ["generate", "image", IMG_MODEL, "--input", "-", "--json"]
        self.passed(self.atlas(*args, stdin=raw.encode()), args, stdin=raw)
        self.blocked(self.atlas(*args, stdin=json.dumps({**body, "prompt": "changed"}).encode()), "not registered")
        self.blocked(self.atlas(*args, stdin=b"not json"), "could not read", "--input -")
        self.blocked(self.atlas(*args, "-p", "x", stdin=raw.encode()), "prompt is given twice")
        self.blocked(self.atlas(*args, "--input", "req.json", stdin=raw.encode()), "--input is given twice")

    def test_fail_closed_when_the_gate_errors(self):
        self.reviewed_cover()
        self.allow([IMG_ENTRY])
        bad = self.root / "clients" / SLUG / "runs" / "AC-BROKEN" / "ledger.json"
        bad.parent.mkdir(parents=True)
        bad.write_text("{not json")
        self.blocked(self.atlas(*self.COVER_ARGS), "the gate check errored", "fails closed")
        bad.unlink()
        self.standards.write_text("{broken")
        self.blocked(self.atlas(*self.COVER_ARGS), "the gate check errored")

    def test_unreadable_billable_calls_are_blocked(self):
        self.allow([IMG_ENTRY])
        cases = {
            ("generate", "video", "m/x", "-p"): "has no value",
            ("generate", "video", "m/x", "-p", "--explain"): "starts with a dash",
            ("generate", "video", "m/x", "-x", "1"): "unknown flag -x",
            ("generate", "video", "m/x", "-px"): "unknown flag -px",
            ("generate", "video", "-p", "x"): "expected one MODEL",
            ("generate", "video", "m/x", "extra", "-p", "x"): "expected one MODEL",
            ("generate", "video", "m/x", "-p", "a", "-p", "b"): "prompt is given twice",
            ("generate", "video", "m/x", "-p", "a", "--param", "prompt=b"): "prompt is given twice",
            ("generate", "video", "m/x", "-p", "a", "--duration", "5", "--param", "duration=6"): "duration is given twice",
            ("generate", "video", "m/x", "-p", "a", "--image", "https://a/1.png", "--image", "https://a/2.png"):
                "image is given twice",
            ("generate", "video", "m/x", "-p", "a", "--images", "@ref.png"): "local file",
            ("generate", "video", "m/x", "-p", "a", "--image", "ref.png"): "not a URL",
            ("generate", "video", "m/x", "--input", "missing.json"): "missing.json",
            ("generate", "video", "m/x", "--explain=maybe"): "true or false",
            ("generate", "music", "m/x", "-p", "a"): "not a command the gate knows",
            ("frobnicate", "generate", "video"): "not a command of atlas-cli",
        }
        for args, needle in cases.items():
            with self.subTest(args=args):
                self.blocked(self.atlas(*args), needle)

    def test_chat_is_blocked_and_update_is_refused(self):
        self.blocked(self.atlas("chat", "-m", "deepseek-ai/deepseek-v3.2", "Return status=ok"), "atlas chat")
        self.blocked(self.atlas("chat", "--system", "--help", "hi"), "atlas chat")
        self.blocked(self.atlas("chat", "--input", "-", stdin=b'{"messages": []}'), "atlas chat")
        r = self.atlas("update")
        self.assertEqual(r.returncode, 3)
        self.assertIn("pinned to 0.1.38", r.stderr.decode())
        self.assertIsNone(self.ran())

    def test_owner_entry_params_and_text_fields(self):
        self.reviewed_cover()
        # a parameter the entry requires
        self.allow([entry(params={"resolution": "2k"}, params_one_of={"aspect_ratio": ["4:5"]})])
        self.blocked(self.atlas(*self.COVER_ARGS), "pass resolution: '2k'")
        self.blocked(self.atlas(*self.COVER_ARGS, "--resolution", "4k"), "pass resolution: '2k'")
        # a text field the entry does not list: blocked, whatever the prompt review said
        self.allow([IMG_ENTRY])
        self.blocked(self.atlas(*self.COVER_ARGS, "--negative-prompt", "blurry"), "negative_prompt carries text")
        self.blocked(self.atlas(*self.COVER_ARGS, "--param", "style=neon"), "style carries text")
        self.blocked(self.atlas(*self.COVER_ARGS, "--param", 'extra={"note": "make it pop"}'), "extra carries text")
        # listed as a text field, it is part of the reviewed prompt card
        self.allow([entry(params_one_of={"aspect_ratio": ["4:5"]}, text_fields=["negative_prompt"])])
        self.blocked(self.atlas(*self.COVER_ARGS, "--negative-prompt", "blurry"), "not registered")
        self.register(COVER_PROMPT + "\n\n[negative_prompt]\nblurry")
        self.blocked(self.atlas(*self.COVER_ARGS, "--negative-prompt", "blurry, text"), "not registered")
        args = (*self.COVER_ARGS, "--negative-prompt", "blurry", "--seed", "7")
        self.passed(self.atlas(*args), args)

    def test_unnamed_model_is_said_before_no_prompt(self):
        err = self.blocked(self.atlas("generate", "image", "x/y", "--aspect-ratio", "4:5"), "not on the owner's list")
        self.assertNotIn("no prompt", err)
        self.blocked(self.atlas("generate", "3d", "x/y", "-p", "a chair"), "no asset type in standards.json makes 3D")
        self.allow(["just-a-string"])
        self.blocked(self.atlas(*self.COVER_ARGS), "has an entry the gate can't read")

    def test_singular_and_plural_references_are_blocked(self):
        self.allow([IMG_ENTRY])
        for extra in (["--images", "https://b/B.png", "--image", "https://a/A.png"],
                      ["--image", "https://a/A.png", "--param", 'images=["https://b/B.png"]'],
                      ["--video", "https://a/A.mp4", "--param", 'videos=["https://b/B.mp4"]'],
                      ["--audio", "https://a/A.mp3", "--param", 'audios=["https://b/B.mp3"]']):
            with self.subTest(extra=extra):
                self.blocked(self.atlas("generate", "video", "m/x", "-p", "a", *extra), "give the references once")
        self.reviewed_cover()
        body = json.dumps({"image": "https://a/A.png"})
        self.blocked(self.atlas(*self.COVER_ARGS, "--input", "-", stdin=body.encode()), "give the references once")

    def test_odd_references_are_blocked(self):
        self.allow([IMG_ENTRY])
        for v in (" https://h/x.png", "//h/x.png", "ftp://h/x.png", "file:///etc/passwd", "FILE:///etc/passwd",
                  " @ref.png"):
            with self.subTest(v=v):
                self.blocked(self.atlas("generate", "video", "m/x", "-p", "a", "--param", f"last_image={v}"),
                             "the gate could not read")

    def test_pipeline_root_is_the_repo_unless_a_stub_runs(self):
        logs = Path(self.repo_tmp.name) / "growth-engine/production/logs/gate-unmatched.jsonl"
        mine = self.root / "growth-engine/production/logs/gate-unmatched.jsonl"
        for real in [None] + ([G.INSTALLED] if Path(G.INSTALLED).exists() else []):
            with self.subTest(real=real):
                before = logs.read_text().count("\n") if logs.exists() else 0
                self.blocked(self.atlas("generate", "image", "x/y", "-p", "GATE-SELFTEST", env={"ATLAS_REAL_BIN": real}),
                             "the production gate is live")
                self.assertEqual(logs.read_text().count("\n"), before + 1)
                self.assertFalse(mine.exists())

    def test_environment_is_forced(self):
        r = self.atlas("version", env={"ATLAS_TELEMETRY": "1", "ATLAS_AUTO_UPDATE": "1", "DO_NOT_TRACK": "0",
                                       "ATLAS_API_BASE": "https://other.example", "ATLAS_AUTH_BASE": "https://o",
                                       "ATLAS_API_EXTRA_HEADER_NAME": "X-Leak", "ATLAS_API_EXTRA_HEADER_VALUE": "1",
                                       "ATLAS_VERSION_URL": "https://o", "ATLAS_POSTHOG_HOST": "https://o"})
        env = self.passed(r, ["version"])["env"]
        self.assertEqual(env, {**{k: None for k in ENV_SEEN}, "ATLAS_TELEMETRY": "0", "ATLAS_AUTO_UPDATE": "0",
                               "DO_NOT_TRACK": "1"})

    def test_missing_real_cli_runs_nothing(self):
        self.stub.unlink()
        r = self.atlas("version")
        self.assertEqual(r.returncode, 127)
        self.assertIn("setup.sh", r.stderr.decode())


class Parse(TP.Base):
    """What the wrapper hands the gate for a command line (TP.Base: the gate log goes to a temp folder)."""

    def test_tool_input(self):
        c = G.decide(["generate", "video", "kling/x/i2v", "-p", "a cat", "--images", "https://a/1.png", "--images",
                      "prediction:abc:0", "--end-image", "https://a/2.png", "--duration", "5", "--aspect-ratio", "9:16",
                      "--param", "generate_audio=false", "--param", 'camera={"move": "dolly"}', "--seed", "-1",
                      "--no-wait", "--timeout", "5m", "-o", "x.mp4"])
        self.assertEqual(c.tool_input(), {
            "kind": "video", "model": "kling/x/i2v", "prompt": "a cat",
            "medias": [{"value": "https://a/1.png", "role": "image_references"},
                       {"value": "prediction:abc:0", "role": "image_references"},
                       {"value": "https://a/2.png", "role": "end_image"}],
            "params": {"duration": 5, "aspect_ratio": "9:16", "generate_audio": False, "camera": {"move": "dolly"},
                       "seed": -1}})

    def test_reference_case_and_other_fields(self):
        c = G.decide(["generate", "video", "m", "-p", "x", "--param", "last_image=HTTPS://h/x.png",
                      "--param", "reference_images=[\"prediction:abc:1\"]"])
        self.assertEqual(c.tool_input()["medias"], [{"value": "HTTPS://h/x.png", "role": "last_image"},
                                                    {"value": "prediction:abc:1", "role": "reference_images"}])

    def test_routes(self):
        self.assertIsNone(G.decide(["generate", "cost", "video", "m", "-p", "x"]))
        self.assertIsNotNone(G.decide(["generate", "video", "m", "-p", "x", "--explain=false", "--explain"]))
        self.assertIsNotNone(G.decide(["generate", "video", "m", "-p", "x", "--explain=false"]))
        self.assertEqual(G.decide(["gen", "3d", "m", "-p", "x"]).kind, "3d")
        self.assertEqual(G.decide(["chat", "hi"]).tool_input()["kind"], "chat")
        with self.assertRaises(G.Refused):
            G.decide(["update", "--check=false"])

    def test_pipeline_rejects_malformed_atlas_input(self):
        for ti in ({"kind": "video"}, {"kind": "gif", "model": "m"}, {"kind": "image", "model": "m", "medias": ["x"]},
                   {"kind": "image", "model": "m", "medias": [{"value": 1, "role": "image"}]}):
            with self.subTest(ti=ti):
                ok, why = P.check_call("atlas_generate", ti)
                self.assertFalse(ok)
                self.assertIn("atlas_generate input must be", why[0])
        ok, why = P.check_call("atlas_generate", {"kind": "chat", "model": "m"})
        self.assertFalse(ok)
        self.assertIn("atlas chat", why[0])

    def test_the_mcp_hook_still_ignores_unknown_tools(self):
        self.assertEqual(P.STANDARDS["gated_tools"]["atlas_generate"], {"service": "atlas", "kind": "from_call"})
        self.assertTrue(P.check_call("mcp__Higgs__balance", {})[0])


class AtlasRules(TP.Base):
    """The owner's entries (standards.json models.atlas.allowed) as the gate applies them, in process."""

    def setUp(self):
        super().setUp()
        self._allowed = P.STANDARDS["models"]["atlas"]["allowed"]

    def tearDown(self):
        P.STANDARDS["models"]["atlas"]["allowed"] = self._allowed
        super().tearDown()

    def name(self, *entries):
        P.STANDARDS["models"]["atlas"]["allowed"] = list(entries)

    def test_entries_the_gate_cannot_read_block_everything(self):
        for bad in ("m/x", {"id": "m/x"}, {"id": "m/x", "kind": "3d"}, {"id": "m/x", "kind": "video"},
                    {"id": "m/x", "kind": "image", "params_one_of": {"aspect_ratio": "4:5"}},
                    {"id": "m/x", "kind": "image", "text_fields": "lyrics"},
                    {"id": "m/x", "kind": "image", "min_s": "5"}, {"id": "m/x", "kind": "image", "typo": 1}):
            with self.subTest(bad=bad):
                self.name(entry("good/one"), bad)
                e, why = P._atlas_entry("good/one", "image")
                self.assertIsNone(e)
                self.assertIn("an entry the gate can't read", why[0])
        self.name(entry("v/x", "video", min_s=5, max_s=10))
        self.assertEqual(P._atlas_entry("v/x", "video")[1], [])
        self.assertIn("named for video calls, not image", P._atlas_entry("v/x", "image")[1][0])
        self.assertIn("makes 3D", P._atlas_entry("v/x", "3d")[1][0])

    def test_duration_use_and_text_fields(self):
        e = entry("v/x", "video", use=["video_clip"], min_s=5, max_s=10, params={"resolution": "1080p"},
                  params_if_given={"camera_fixed": [False]}, text_fields=["negative_prompt"])
        a, led = {"type": "video_clip", "shots": []}, {"slug": SLUG, "post_id": POST}

        def why(params, atype="video_clip", medias=()):
            req = {"kind": "video", "model": "v/x", "params": {"resolution": "1080p", "duration": 5, **params},
                   "medias": [{"value": m, "role": "image"} for m in medias], "atlas": e}
            return " | ".join(P._atlas_checks(req, {**a, "type": atype}, led))

        self.assertEqual(why({}), "")
        self.assertIn("duration 12 outside 5 to 10", why({"duration": 12}))
        self.assertIn("duration None outside", why({"duration": None}))
        self.assertIn("duration True outside", why({"duration": True}))
        self.assertIn("pass resolution: '1080p'", why({"resolution": "720p"}))
        self.assertIn("camera_fixed must be one of [False]", why({"camera_fixed": True}))
        self.assertIn("named for video_clip, not a cover", why({}, atype="cover"))
        self.assertIn("negative_prompt is a text field", why({"negative_prompt": ["x"]}))
        self.assertIn("lyrics carries text", why({"lyrics": "la la"}))
        self.assertEqual(why({"last_frame": "https://a/end.png", "seed": 3}, medias=["https://a/end.png"]), "")
        self.assertEqual(P._atlas_text({"prompt": "a cat", "params": {"negative_prompt": "dogs", "x": "y"}}, e),
                         "a cat\n\n[negative_prompt]\ndogs")

    def test_audio_references_are_checked(self):
        post = "AC-2026-10-W3-03"
        P.init_run(SLUG, post, "reel_quote_broll")
        P.new_asset(SLUG, post, "VO", "voice")
        P.set_prompt(SLUG, post, "VO", "Ti humb klientë çdo ditë.", [])
        P.budget(SLUG, post, planned=30, balance=500)
        P.record_gate(SLUG, post, "G-SCRIPT", "PASS", "script-lab gate", score=88)
        self.name(entry("x/tts", "audio"))
        clone = {"kind": "audio", "model": "x/tts", "prompt": "Ti humb klientë çdo ditë.",
                 "medias": [{"value": "https://somewhere/voice.mp3", "role": "audio"}], "params": {}}
        ok, why = P.check_call("atlas_generate", clone)
        self.assertFalse(ok)
        self.assertIn("references differ", " ".join(why))
        self.assertIn("is not a registered asset with a passed review", " ".join(why))
        ok, why = P.check_call("atlas_generate", {**clone, "medias": []})
        self.assertTrue(ok, why)


class BashHook(unittest.TestCase):
    def hook(self, cmd=None, raw=None):
        r = subprocess.run([sys.executable, str(HERE / "atlas" / "atlas_gate.py"), "--bash-hook"],
                           input=raw if raw is not None else json.dumps({"tool_name": "Bash",
                                                                         "tool_input": {"command": cmd}}),
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0)
        return json.loads(r.stdout)["hookSpecificOutput"]["permissionDecision"] if r.stdout else "allow"

    def test_direct_routes_are_denied(self):
        for cmd in ("/usr/local/lib/atlas-cli/atlas generate video m -p x",
                    "curl -H 'Authorization: Bearer x' https://api.atlascloud.ai/api/v1/model/generateVideo",
                    "npm install -g atlascloud-cli", "echo $ATLASCLOUD_API_KEY",
                    "node references/atlas-cloud-skills/skills/seedance-2-5-skill/scripts/generate.mjs cfg.json",
                    "node scripts/providers/atlas-rest.mjs", "cat ~/.config/atlas-cli/auth.json"):
            with self.subTest(cmd=cmd):
                self.assertEqual(self.hook(cmd), "deny")
        self.assertEqual(self.hook("atlas generate video m -p x"), "allow")
        self.assertEqual(self.hook("bash growth-engine/tools/atlas/setup.sh"), "allow")

    def test_unreadable_input_is_denied(self):
        for raw in ("", "not json", "[]", '{"tool_input": {}}', '{"tool_input": {"command": 3}}'):
            with self.subTest(raw=raw):
                self.assertEqual(self.hook(raw=raw), "deny")


class Setup(unittest.TestCase):
    """setup.sh checks every source against the pinned sha256 before it installs anything."""

    @unittest.skipUnless(Path(G.INSTALLED).exists(), "needs the pinned atlas binary installed by setup.sh")
    def test_install_from_a_checkout_copy_prefers_the_main_repo(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            co = t / "checkout" / "growth-engine" / "tools" / "atlas"
            co.mkdir(parents=True)
            for f in ("setup.sh", "atlas_gate.py"):
                shutil.copy(HERE / "atlas" / f, co / f)
            (t / "home").mkdir()
            dead = "http://127.0.0.1:9"
            env = {k: v for k, v in os.environ.items() if k not in ("ATLASCLOUD_API_KEY", "NO_PROXY", "no_proxy")}
            env.update(ATLAS_PREFIX=str(t / "prefix"), HOME=str(t / "home"), XDG_CONFIG_HOME=str(t / "home" / ".config"),
                       ATLAS_CONFIG_DIR=str(t / "home" / ".config" / "atlas-cli"), PIPELINE_ROOT=str(t / "ledger"),
                       HTTPS_PROXY=dead, https_proxy=dead, HTTP_PROXY=dead, http_proxy=dead, ALL_PROXY=dead)
            r = subprocess.run(["bash", str(co / "setup.sh"), G.INSTALLED], capture_output=True, text=True, env=env,
                               timeout=120)
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            self.assertIn("gate:     live", r.stdout)
            self.assertIn("test install (PATH not checked)", r.stdout)
            wrapper = (t / "prefix" / "bin" / "atlas").read_text()
            self.assertIn(f"for repo in /home/user/main {t / 'checkout'}; do", wrapper)
            self.assertEqual(P.sha_file(t / "prefix" / "lib" / "atlas-cli" / "atlas"), P.sha_file(Path(G.INSTALLED)))

    def run_setup(self, *args):
        with tempfile.TemporaryDirectory() as t:
            env = {**os.environ, "ATLAS_PREFIX": str(Path(t) / "prefix")}
            r = subprocess.run(["bash", str(HERE / "atlas" / "setup.sh"), *args], capture_output=True, text=True,
                               env=env)
            installed = sorted(str(p.relative_to(t)) for p in Path(t).rglob("*") if p.is_file())
        return r, installed

    def test_wrong_binary_or_tarball_installs_nothing(self):
        with tempfile.TemporaryDirectory() as t:
            fake = Path(t) / "atlas"
            fake.write_text("#!/bin/sh\necho fake\n")
            r, installed = self.run_setup(str(fake))
            self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
            self.assertIn("holds no pinned atlas", r.stderr)
            self.assertEqual(installed, [])
            tar = Path(t) / "cli.tar.gz"
            subprocess.run(["tar", "-czf", str(tar), "-C", t, "atlas"], check=True)
            fake.unlink()
            r, installed = self.run_setup(t)
            self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
            self.assertIn("not the pinned", r.stderr)
            self.assertEqual(installed, [])


if __name__ == "__main__":
    unittest.main()
