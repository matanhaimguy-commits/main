#!/usr/bin/env python3
"""The Atlas Cloud CLI behind the production gate. setup.sh installs it as /usr/local/bin/atlas.

Every command goes straight to the real CLI (/usr/local/lib/atlas-cli/atlas, or ATLAS_REAL_BIN) except the billable
ones: `atlas generate image|video|audio|3d MODEL ...` (alias `gen`) and `atlas chat`. For a generation it reads the
model, prompt, references and parameters from the command line and from `--input FILE` or `--input -` (stdin), runs
the same check as the PreToolUse hook (pipeline.check_call with tool "atlas_generate") and only then runs the real CLI
with the same argv, except that `--input FILE` becomes `--input -`: the CLI gets on stdin exactly the bytes the gate
read (no second read of the file). `atlas chat` goes to the same check, which blocks it.
Never gated: cost estimates (`generate cost|estimate`), `--explain`, `--help`, `generate get|wait|history|ops`,
models, upload, auth, account, doctor, skills, completion, version. `atlas update` is refused: setup.sh pins the
version whose grammar this file reads.

Fails closed: a call it can't read, an unknown command, or a gate that errors is blocked (exit 3) and the real CLI
does not run. README.md (same folder) has the details.

  atlas_gate.py <atlas args...>     what /usr/local/bin/atlas runs
Commands that skip the wrapper are denied by the PreToolUse hook on Bash, .claude/hooks/atlas_bash_guard.py.
"""
from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
TOOLS = REPO / "growth-engine" / "tools"
INSTALLED = "/usr/local/lib/atlas-cli/atlas"      # where setup.sh puts the real CLI
REAL = os.environ.get("ATLAS_REAL_BIN") or INSTALLED
TOOL = "atlas_generate"
BLOCKED_EXIT = 3
MAX_STDIN = 64 << 20

# the command tree of atlas-cli 0.1.38 (setup.sh pins it); anything else is blocked
TOP = {"account", "auth", "chat", "completion", "doctor", "generate", "gen", "help", "models", "skills", "update",
       "upload", "version", "__complete", "__completeNoDesc"}
KINDS = {"image", "video", "audio", "3d"}
SAFE_GENERATE = {"cost", "estimate", "get", "wait", "history", "ops", "help"}
ROOT_BOOLS = {"--json", "--no-color", "--quiet", "--verbose", "--help", "--version", "-q", "-v", "-h"}
LEAF_BOOLS = {"explain", "help", "no-download", "no-wait", "overwrite", "wait", "json", "no-color", "quiet", "verbose"}
SHORT = {"h": "help", "q": "quiet", "v": "verbose", "p": "prompt", "o": "output"}
CLI_ONLY = LEAF_BOOLS | {"output", "interval", "timeout"}
MEDIA_KEYS = {"image", "images", "end_image", "video", "videos", "audio", "audios"}
PAIRS = (("image", "images"), ("video", "videos"), ("audio", "audios"))   # the CLI folds the first into the second
ROLE = {"images": "image_references"}            # the role the gate and `pipeline.py prompt --media ID:role` use
TRUE, FALSE = {"1", "t", "T", "TRUE", "true", "True"}, {"0", "f", "F", "FALSE", "false", "False"}
NUM = re.compile(r"-\d+(\.\d+)?$")
REF = re.compile(r"\s*(?:[a-z][a-z0-9+.-]*://|//|@|prediction:|data:)", re.I)   # anything that may be a reference
URL_REF = re.compile(r"(?:https?://|prediction:|data:)", re.I)                     # the references the gate can check
CHAT_DEFAULT_MODEL = "deepseek-ai/deepseek-v3.2"
# the CLI reads these (found in 0.1.38's strings): endpoints, extra headers, release and telemetry hosts. A stored key
# must only ever go to api.atlascloud.ai, so the wrapper drops them before the real CLI runs.
ENV_DROP = ("ATLAS_API_BASE", "ATLAS_AUTH_BASE", "ATLAS_API_EXTRA_HEADER_NAME", "ATLAS_API_EXTRA_HEADER_VALUE",
            "ATLAS_AUTH_EXTRA_HEADER_NAME", "ATLAS_AUTH_EXTRA_HEADER_VALUE", "ATLAS_INTERNAL_ENV", "ATLAS_RELEASE_REPO",
            "ATLAS_VERSION_URL", "ATLAS_DOWNLOAD_DNS_URL", "ATLAS_POSTHOG_HOST", "ATLAS_POSTHOG_KEY")
ENV_FORCE = {"ATLAS_TELEMETRY": "0", "ATLAS_AUTO_UPDATE": "0", "DO_NOT_TRACK": "1"}


class Blocked(Exception):
    """The gate can't read the call: blocked, the real CLI does not run."""


class Refused(Exception):
    """A command this wrapper does not run (not a generation): `atlas update`."""


def blocked_message(reasons: list[str]) -> str:
    """The same text the PreToolUse hook (.claude/hooks/generation_gate.py) shows."""
    return ("GENERATION BLOCKED by the production gate (growth-engine/production/VISUAL-QA.md section 9).\n- "
            + "\n- ".join(reasons)
            + "\nRun `python3 growth-engine/tools/pipeline.py status <slug> <post_id>` for the open steps.")


# ---- which command is this -------------------------------------------------------------------------

def command_path(args: list[str]) -> tuple[list[int], bool]:
    """Positions of the words naming the command (`generate`, `image`), read the way the CLI's router (cobra) reads
    them. The second value is False when a flag before them makes the route unclear."""
    pos = []
    for i, t in enumerate(args):
        if len(pos) == 2 or (len(pos) == 1 and args[pos[0]] not in ("generate", "gen")):
            break
        if t == "--":
            return pos, False
        if t.startswith("-"):
            if t in ROOT_BOOLS or "=" in t:
                continue
            return pos, False            # the router may read the next word as this flag's value
        pos.append(i)
    return pos, True


def parse_leaf(args: list[str], bools=LEAF_BOOLS, short=SHORT, spans: list | None = None
               ) -> tuple[list[tuple[str, object]], list[str]]:
    """Flags (in order) and positional words of a leaf command, as the CLI's own parser reads them (checked against
    0.1.38 with `generate cost ... --explain`): `--flag value`, `--flag=value`, `-p value`, `-p=value`; a boolean
    takes an optional true/false word after it. `spans` gets, per flag, (index of the word holding its value, True
    when that word is `--flag=value`)."""
    flags, words, i = [], [], 0
    spans = [] if spans is None else spans
    while i < len(args):
        t = args[i]
        i += 1
        if t == "--":
            words += args[i:]
            break
        if t.startswith("--"):
            name, eq, val = t[2:].partition("=")
        elif t.startswith("-") and t != "-" and not NUM.match(t):
            name, eq, val = t[1:].partition("=")
            if name not in short:
                raise Blocked(f"unknown flag {t} (write flags one at a time, e.g. -q -p TEXT)")
            name = short[name]
        else:
            words.append(t)
            continue
        if not name:
            raise Blocked(f"can't read the flag {t}")
        if name in bools:
            if eq and val not in TRUE | FALSE:
                raise Blocked(f"{t}: the value must be true or false")
            if not eq:
                val = "true"
                if i < len(args) and args[i] in TRUE | FALSE:
                    val = args[i]
                    i += 1
            flags.append((name, val in TRUE))
            spans.append((i - 1, bool(eq)))
            continue
        if not eq:
            if i >= len(args):
                raise Blocked(f"--{name} has no value")
            val = args[i]
            i += 1
            if val.startswith("-") and val != "-" and not NUM.match(val):
                raise Blocked(f"the value of --{name} starts with a dash ({val}): write --{name}=VALUE")
        flags.append((name, val))
        spans.append((i - 1, bool(eq)))
    return flags, words


def is_on(flags, name: str) -> bool:
    vals = [v for n, v in flags if n == name]
    return bool(vals) and all(vals)


# ---- what the call makes --------------------------------------------------------------------------

def coerce(v: str):
    if re.fullmatch(r"-?\d+", v):
        return int(v)
    if re.fullmatch(r"-?\d+\.\d+", v):
        return float(v)
    return {"true": True, "false": False}.get(v, v)


def strings(v):
    if isinstance(v, str):
        yield v
    elif isinstance(v, list):
        for x in v:
            yield from strings(x)
    elif isinstance(v, dict):
        for x in v.values():
            yield from strings(x)


class Call:
    """One billable call: what the gate gets (tool_input) and the stdin bytes to replay to the real CLI."""

    def __init__(self, kind: str, model: str):
        self.kind, self.model = kind, model
        self.prompt, self.medias, self.params = None, [], {}
        self.src: dict[str, str] = {}
        self.stdin: bytes | None = None
        self.argv: list[str] = []          # what the real CLI runs (set by decide)

    def field(self, key: str, value, source: str):
        """One schema field (from a flag, --param or the --input JSON): the prompt, a reference or a parameter.
        The CLI refuses a field given twice (duplicate_parameter, conflicting_parameter_sources); so does the gate."""
        key = key.replace("-", "_")
        if key == "model":
            if value != self.model:
                raise Blocked(f"{source} names model {value!r} but the command names {self.model!r}")
            return
        prev = self.src.get(key)
        if prev is not None and not (key == "images" and prev == source == "--images"):
            raise Blocked(f"{key} is given twice ({prev} and {source}): give each field once")
        self.src[key] = source
        if key == "prompt":
            if not isinstance(value, str):
                raise Blocked(f"the prompt in {source} is not text")
            self.prompt = value
            return
        refs = [s for s in strings(value) if key in MEDIA_KEYS or REF.match(s)]
        for s in refs:
            if s.startswith("@"):
                raise Blocked(f"{key} {s} is a local file, which can change after review: upload it "
                              "(`atlas upload FILE`), register the URL on its asset and pass the URL")
            if not URL_REF.match(s):
                raise Blocked(f"{key} {s!r} is not a URL or prediction:ID:INDEX (the gate checks references by URL)")
            self.medias.append({"value": s, "role": ROLE.get(key, key)})
        if refs and key in MEDIA_KEYS:
            return
        self.params[key] = value

    def load_input(self, path: str):
        """Reads the JSON request once (stdin, or the file); the real CLI later gets these same bytes on stdin."""
        if self.stdin is not None:
            raise Blocked("--input is given twice: put the whole request in one JSON object")
        where = f"--input {path}"
        try:
            if path == "-":
                data = sys.stdin.buffer.read(MAX_STDIN + 1)
            else:
                with open(path, "rb") as f:
                    data = f.read(MAX_STDIN + 1)
        except OSError as e:
            raise Blocked(f"{where}: {e}")
        if len(data) > MAX_STDIN:
            raise Blocked(f"{where} is larger than {MAX_STDIN >> 20} MB")
        self.stdin = data
        try:
            obj = json.loads(data.decode("utf-8"))
        except (UnicodeDecodeError, ValueError) as e:
            raise Blocked(f"{where}: {e}")
        if not isinstance(obj, dict):
            raise Blocked(f"{where} is not a JSON object")
        for k, v in obj.items():
            self.field(k, v, "--input")

    def tool_input(self) -> dict:
        return {"kind": self.kind, "model": self.model, "prompt": self.prompt or "", "medias": self.medias,
                "params": self.params}


def _chat(args: list[str]) -> Call | None:
    """`atlas chat` is billable: gated (and blocked by the gate) unless it only prints help."""
    try:
        flags, _ = parse_leaf(args, short={**SHORT, "m": "model"})
    except Blocked:
        flags = []
    if is_on(flags, "help"):
        return None
    models = [v for n, v in flags if n == "model"]
    return Call("chat", str(models[-1]) if models else CHAT_DEFAULT_MODEL)


def _update(args: list[str]) -> None:
    try:
        flags, _ = parse_leaf(args, bools=LEAF_BOOLS | {"check"})
    except Blocked:
        flags = []
    if is_on(flags, "help") or is_on(flags, "check"):
        return None
    raise Refused("atlas update is not run here: the Atlas CLI is pinned to 0.1.38 by growth-engine/tools/atlas/setup.sh "
                  "(the gate reads that version's command grammar). Change the pin there.")


def decide(argv: list[str]) -> Call | None:
    """None: run the real CLI as is. A Call: gate it first. Raises Blocked when the call can't be read."""
    pos, clear = command_path(argv)
    if not clear:
        raise Blocked("put flags after the command (atlas generate <kind> MODEL [flags]) so the gate can read the call")
    words = [argv[i] for i in pos]
    if not words:
        return None                                      # atlas, atlas --help, atlas --version
    if words[0] not in TOP:
        raise Blocked(f"`atlas {words[0]}` is not a command of atlas-cli 0.1.38")
    rest_at = [i for i in range(len(argv)) if i not in pos]
    rest = [argv[i] for i in rest_at]
    if words[0] == "chat":
        return _chat(rest)
    if words[0] == "update":
        return _update(rest)
    if words[0] not in ("generate", "gen") or len(words) == 1 or words[1] in SAFE_GENERATE:
        return None
    kind = words[1]
    if kind not in KINDS:
        raise Blocked(f"`atlas {words[0]} {kind}` is not a command the gate knows (image, video, audio, 3d, cost, "
                      "get, wait, history, ops)")
    spans: list[tuple[int, bool]] = []
    flags, models = parse_leaf(rest, spans=spans)
    if is_on(flags, "help") or is_on(flags, "explain"):
        return None                                      # prints help or the compiled input; submits nothing
    if len(models) != 1:
        raise Blocked(f"expected one MODEL, got {models or 'none'}")
    call = Call(kind, models[0])
    call.argv = list(argv)
    for (name, val), (at, eq) in zip(flags, spans):
        if name in CLI_ONLY:
            continue
        if name == "input":
            call.load_input(val)
            if val != "-":                               # the CLI reads what the gate read, not the file again
                call.argv[rest_at[at]] = argv[rest_at[at]].split("=", 1)[0] + "=-" if eq else "-"
        elif name == "param":
            key, sep, raw = val.partition("=")
            if not sep or not key:
                raise Blocked(f"--param {val}: expected key=value")
            try:
                value = json.loads(raw)
            except ValueError:
                value = raw
            call.field(key, value, "--param")
        elif name == "prompt" or name.replace("-", "_") in MEDIA_KEYS:
            call.field(name, val, f"--{name}")
        else:
            call.field(name, coerce(val), f"--{name}")
    for one, many in PAIRS:
        if one in call.src and many in call.src:
            raise Blocked(f"{one} ({call.src[one]}) and {many} ({call.src[many]}) are both given, and the CLI puts {one} "
                          f"first whatever the order: give the references once, as --{many}, in order")
    return call


# ---- run ------------------------------------------------------------------------------------------

def gate(tool_input: dict) -> tuple[bool, list[str]]:
    if str(TOOLS) not in sys.path:
        sys.path.insert(0, str(TOOLS))
    import pipeline
    return pipeline.check_call(TOOL, tool_input)


def replay_stdin(data: bytes) -> None:
    """Give the real CLI the same stdin bytes the gate read (an unlinked in-memory file on fd 0)."""
    try:
        fd = os.memfd_create("atlas-input")
    except (AttributeError, OSError):
        import tempfile
        with tempfile.TemporaryFile() as f:
            fd = os.dup(f.fileno())
    view = memoryview(data)
    while view:
        view = view[os.write(fd, view):]
    os.lseek(fd, 0, os.SEEK_SET)
    os.dup2(fd, 0)
    os.close(fd)


def run_real(argv: list[str]) -> int:
    if not os.access(REAL, os.X_OK):
        print(f"atlas: the real Atlas CLI is not installed at {REAL}: run bash growth-engine/tools/atlas/setup.sh",
              file=sys.stderr)
        return 127
    os.execv(REAL, ["atlas", *argv])
    return 127  # not reached


def is_test_stub() -> bool:
    """True when ATLAS_REAL_BIN names something other than the installed CLI (the tests' stub)."""
    alt = os.environ.get("ATLAS_REAL_BIN")
    if not alt:
        return False
    try:
        return not os.path.samefile(alt, INSTALLED)
    except OSError:
        return True


def harden_env() -> None:
    """No telemetry, no auto-update, no other endpoint; and the gate's ledger is the repo's own (PIPELINE_ROOT is
    honoured only with a test stub, so a caller can't point the gate at a ledger outside the repo)."""
    os.environ.update(ENV_FORCE)
    for k in ENV_DROP:
        os.environ.pop(k, None)
    if not is_test_stub():
        os.environ.pop("PIPELINE_ROOT", None)


def main(argv: list[str]) -> int:
    harden_env()
    try:
        call = decide(argv)
        if call is not None:
            ok, why = gate(call.tool_input())
            if not ok:
                print(blocked_message(why), file=sys.stderr)
                return BLOCKED_EXIT
            if call.stdin is not None:
                replay_stdin(call.stdin)
    except Refused as e:
        print(f"atlas: {e}", file=sys.stderr)
        return BLOCKED_EXIT
    except Blocked as e:
        print(blocked_message([f"the gate could not read this atlas call: {e}"]), file=sys.stderr)
        return BLOCKED_EXIT
    except Exception as e:  # fail closed
        print(blocked_message([f"the gate check errored ({type(e).__name__}: {e}); fix growth-engine/tools/pipeline.py "
                               "or the ledger it names. The gate fails closed."]), file=sys.stderr)
        return BLOCKED_EXIT
    return run_real((call.argv if call is not None else None) or argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
