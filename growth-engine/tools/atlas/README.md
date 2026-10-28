# Atlas Cloud CLI behind the production gate

Atlas Cloud (`atlas`, pinned to 0.1.38) can make images, video, audio and 3D. Every billable call goes through the
production gate (`growth-engine/tools/pipeline.py check_call`, VISUAL-QA section 9), so nothing is made on Atlas
without a registered, reviewed prompt, reviewed references and a budget, and only on a model the owner has named with
its parameters. The named models are in `standards.json` `models.atlas.allowed` (STANDARDS.md 1); every other
model is blocked.

| File | What it is |
|---|---|
| `setup.sh` | Installs the pinned CLI (sha256 checked before install) and the `atlas` wrapper, signs in, prints a status. Idempotent. |
| `atlas_gate.py` | The wrapper: reads each command, gates the billable ones, then runs the real CLI. |
| `../atlas_rules.py` | The owner's entries applied to one call (`pipeline.py` loads the ledger and calls it). Tests: `../test_atlas_rules.py`. |
| `../test_atlas_gate.py` | Tests: `python3 -m unittest growth-engine/tools/test_atlas_gate.py` |

## Owner setup

In the cloud environment's settings:
1. **Network** (verified 18 Oct 2026): `*.atlascloud.ai` is reachable. The install downloads the release from
   github.com; if that is blocked, run `setup.sh` with a local tarball or binary (below).
2. **Network secret** (verified 18 Oct 2026): a Bearer secret for host `api.atlascloud.ai` holding the Atlas API key.
   The proxy adds `Authorization: Bearer <key>` to every request to that host, so the key never enters the session. It
   attaches only after Claude Code starts (the Setup script's own requests don't get it).
3. **Setup script** (not set up yet): `bash /home/user/main/growth-engine/tools/atlas/setup.sh || true`. Until it is,
   run `setup.sh` by hand in a session where `atlas` is missing.

`setup.sh` then:
- installs the real CLI at `/usr/local/lib/atlas-cli/atlas` (not on PATH) for linux amd64 or arm64, skipping the
  download when the pinned binary is already there. Offline: `bash setup.sh <tarball, binary, or a folder with one>`;
- writes the wrapper `/usr/local/bin/atlas`, which runs `atlas_gate.py` (and so `standards.json`) from
  `/home/user/main`, and from the checkout `setup.sh` ran from only when `/home/user/main` is missing;
- signs in if no login is stored (a login with a refresh token counts as stored): with `ATLASCLOUD_API_KEY` when it is
  set (never printed), else with the placeholder `atlas auth login --token network-secret` (no network call; the proxy
  swaps in the real key). To switch to a real key later: `atlas auth logout`, then run `setup.sh` with
  `ATLASCLOUD_API_KEY` set;
- proves the gate is live (a `GATE-SELFTEST` generation must be blocked) and prints version, wrapper, login, whether
  `api.atlascloud.ai` answers, and the balance ("not checked yet" while it runs as the Setup script);
- exits 1 when the gate is not live, the login failed, or another `atlas` comes first on PATH (the official installer's
  `~/.local/bin/atlas` or `npm i -g atlascloud-cli` would shadow the wrapper and skip the gate).

Every call runs with `ATLAS_TELEMETRY=0`, `ATLAS_AUTO_UPDATE=0` and `DO_NOT_TRACK=1` (forced, whatever the caller's
environment says). The wrapper also drops the CLI's endpoint, extra-header, release and telemetry-host overrides
(`ATLAS_API_BASE`, `ATLAS_AUTH_BASE`, `ATLAS_*_EXTRA_HEADER_*`, `ATLAS_INTERNAL_ENV`, `ATLAS_RELEASE_REPO`,
`ATLAS_VERSION_URL`, `ATLAS_DOWNLOAD_DNS_URL`, `ATLAS_POSTHOG_*`), so a stored key only ever goes to
`api.atlascloud.ai`, and `PIPELINE_ROOT` (the gate checks the repo's own ledgers; only the tests' stub may move it).

## How the gate works

| Command | What the wrapper does |
|---|---|
| `atlas generate image\|video\|audio MODEL ...` (also `gen`) | Gated. Builds `{kind, model, prompt, medias, params}` and runs `pipeline.check_call("atlas_generate", ...)`. Allowed: runs the real CLI with the same arguments, except that `--input FILE` becomes `--input -` with the bytes the gate read on stdin. Denied: prints `GENERATION BLOCKED ...` and exits 3. |
| `atlas generate 3d MODEL ...` | Gated and always blocked: no asset type makes 3D, and the owner's list takes no 3d entry. |
| `atlas chat` | Gated, and the gate always blocks it (billable LLM text is not a production step). |
| `atlas generate cost\|estimate ...`, `--explain`, `--help` | Never gated: they submit nothing. |
| `generate get\|wait\|history\|ops`, `models`, `upload`, `auth`, `account`, `doctor`, `skills`, `version`, `completion` | Passed straight through. |
| `atlas update` | Refused (`--check` passes): the version is pinned in `setup.sh`, because the wrapper reads 0.1.38's grammar. |

The wrapper reads the call the way the CLI does. `-p`/`--prompt` (or `prompt` in `--param` or `--input`) is the
prompt, whatever the model calls its text field (the CLI maps it, e.g. to `text` for
`elevenlabs/v3/text-to-speech`). `--images` are references with role `image_references`; `--image`, `--end-image`,
`--video`, `--audio` keep their names as roles, and so does any other field holding a URL or `prediction:ID:INDEX`.
Other `--name value` and `--param key=value` fields are parameters, and `--input FILE` or `--input -` is read too.

The gate then checks, for an Atlas call, exactly this:
1. the model has an entry in the owner's list (below) for this kind of call; this comes first, before any prompt work;
2. the prompt, plus the entry's `text_fields` the call sets (below), is registered on an asset (`pipeline.py prompt`)
   whose type makes this kind of call;
3. the call follows the entry: `use`, `params`, `params_one_of`, `params_if_given`, the duration within `min_s` to
   `max_s`, and no parameter carrying text the entry does not list;
4. image and video calls match the Shot Spec's aspect, by whichever shape key the model takes (`call_aspect.py`):
   `--aspect-ratio` or `--ratio` (`9:16`), or `--size` (`1152x2048`) compared by its ratio. gpt-image-2 takes only
   `--size` and has no 4:5 size, so its entries' `size_for_aspect` names the size for each aspect (a 4:5 slide at
   1024x1536, cropped to 4:5 at export). H3 image-to-video takes only `ratio: adaptive`: `aspect_from: image`;
5. G-BUDGET is fresh (24 h), video calls need step 9 closed, a song needs G-HUMAN-SONG before any picture, a version
   runs once, and attempts are counted;
6. the Shot Specs are current with G-SPEC, the prompt has its G-PROMPT-IMG or G-PROMPT-VID PASS, and the references
   are the reviewed ones in the same order and roles, each with its own review PASS (the storyboard rule for talking or
   multi-shot clips included);
7. audio generation calls also need the released script (G-SCRIPT). Audio asset types have no prompt-review gate (as for
   ElevenLabs: the words are the released script), but their references are checked as in 6, so a voice clone from an
   unreviewed `--audio URL` is blocked.

An **analysis** entry (`"analysis": true`, today `xai/stt-v1`) makes nothing, so steps 2 and 4 to 7 don't apply: the
call has no prompt, its one reference (`--audio URL`) is registered on one of our assets of a type the entry `reads`,
and step 3's parameter rules hold (`language: en`). It needs no G-BUDGET (about $0.10 an hour of audio); the record
goes to that asset's run. An entry with `"duration_from": "audio"` (OmniHuman 2.0) has no duration setting: the gate
refuses `duration`, takes the length from the one `--audio` reference's G-AUDIO PASS (`pipeline.py gate ... G-AUDIO
--data '{"seconds": 9.4}'`) and checks it against `min_s` to `max_s`; `"aspect_from": "image"` skips step 4 (the frame
follows the image), and `"prop_subjects_only": true` passes only clips whose Shot Specs show nothing but `PR-` props.

G-EXCEPTION does not open Atlas, and none of the Higgsfield model rules (`models.image`, `models.video`) apply: the
owner's entry is the whole model rule.

Where the record goes: once the gate finds the asset, the ALLOW or DENY line goes to that run's `calls.jsonl`. A denial
before that (unnamed model, 3d, unregistered prompt, `atlas chat`, the self-test) goes to
`growth-engine/production/logs/gate-unmatched.jsonl`. A call the wrapper can't read never reaches the gate: it is
only printed.

It fails closed: an unknown command, a flag it can't read, a field given twice, `--input` given twice, `--image` with
`--images` (or `video`/`videos`, `audio`/`audios`: the CLI folds the single one in first, whatever the order: give the
references once, as `--images`, in order), a flag before the command, a local `@file` reference (upload it with
`atlas upload FILE` and register the URL on its asset), a reference that is not `http(s)://`, `prediction:` or
`data:` (for example `ftp://`, `//host/x` or a leading space), or any error in the check blocks the call and the real
CLI does not run.

Never call the Atlas REST API, the real binary, or the scripts of the Atlas skills in `references/atlas-cloud-skills`
(their `atlas-rest` provider calls the API directly, and the network secret pays for it): that skips the gate. Those
skills are prompt-craft reference only; read them with the Read tool.

## How the owner names a model

Add an entry to `growth-engine/production/standards.json` `models.atlas.allowed`, with a dated line in `STANDARDS.md`'s
changelog. Only the owner does this. Read the model's fields first with `atlas models get MODEL --json`. Example (the
shape only; this model is not named):

```json
{ "id": "google/nano-banana-2/edit", "kind": "image", "use": ["slide", "cover"],
  "params_one_of": { "aspect_ratio": ["4:5"], "resolution": ["2k"] },
  "text_fields": [] }
```

| Key | Meaning |
|---|---|
| `id`, `kind` | The exact model id (`atlas models list --json`) and `image`, `video` or `audio`. |
| `use` | Optional: the asset types it may make (`cover`, `slide`, `video_clip`, `voice`, ...). |
| `params` / `params_one_of` / `params_if_given` | A value the call must pass / one of these values it must pass / values allowed when it passes the key. |
| `min_s`, `max_s` | Duration bounds in seconds; required for video. |
| `text_fields` | Extra text fields the call may set (`negative_prompt`, `lyrics`, `style`, `title`, `negative_tags`, ...). They are reviewed with the prompt: register the prompt card as the prompt, then for each of these fields the call sets, in this order, a line `[field]` and its text. If a text field has a default in `atlas models get` (some music models have default lyrics), pass it explicitly. |
| `duration_from` | `"audio"`: the model has no duration; the clip is as long as its audio reference, measured on that audio's G-AUDIO PASS (`data.seconds`), within `min_s` to `max_s`. |
| `aspect_from` | `"image"`: the frame follows the image reference, so the call passes no aspect ratio. |
| `size_for_aspect` | For a model shaped by `size`: each Shot Spec aspect and the sizes that make it (`{"4:5": ["1024x1536"]}`). Without it a size passes when its ratio equals the spec's. |
| `prop_subjects_only` | `true`: only for clips whose every Shot Spec subject is a `PR-` prop (a talking object). |
| `analysis`, `reads` | `true` and the asset types it reads: an analysis call (no prompt, no budget, one registered file). |

Any parameter that carries text and is not listed in the entry blocks the call (a reference given as an object,
`{"url": a registered reference, "type": "image"}` as in H3's `refers`, is structure, not text), so list `aspect_ratio`, `resolution`,
`quality`, a voice id and the like with their allowed values. A family banned in STANDARDS.md 1 (Seedance, Veo, Sora
and the rest) stays banned on Atlas unless the owner names that exact model.

## The Bash guard (installed 28 Oct 2026)

The wrapper guards the `atlas` command; `.claude/hooks/atlas_bash_guard.py` (a PreToolUse hook on Bash in
`.claude/settings.json`, `onFailure: block`) guards the other routes. It is a guardrail for cooperating sessions, not a
sandbox: the real controls are that only the wrapper is documented and that the main session reviews every diff.
Rules: `.claude/hooks/guards/atlas_bash.py` (what is denied), `atlas_text.py` (the forms of a text it reads) and
`atlas_scripts.py` (the files a command runs, and the trusted list); tests: `test_atlas_bash.py`. It denies:
- the real binary or its login (`atlas-cli`), the API host or key (`atlascloud`, `cloud.ai`), `ATLAS_REAL_BIN`, the
  Atlas skills' scripts (`atlas-cloud-skills`, `atlas-rest`) and `atlas-mcp`, read as written, with quote and `+` joins
  taken out, with the command's own shell variables and `$(echo …)` filled in, and printf escapes and base64 decoded;
- `atlas` beside a network call or a code runner, outside the wrapper's own commands, git and the repo's Atlas files;
- decoded text run as code (`base64 -d | sh`), a wildcard that matches the binary or the login, `find -exec` or
  `xargs` near the install;
- a file the command runs that names them: when an interpreter runs anywhere in the command, every file it names
  (`cat x.py | python3`, `python3 < x.py`, `python -m mod`, `unittest discover -s DIR`, `cp a.py b.py && python3 b.py`),
  plus any executable file named;
- copying, linking or redirecting a trusted file.

Trusted (may name Atlas): `atlas_gate.py`, `setup.sh`, `test_atlas_gate.py`, the guard's own `atlas_text.py`,
`atlas_bash.py` and `test_atlas_bash.py`, `references/fetch.sh` (it clones the Atlas skills for reading) and the
wrapper `/usr/local/bin/atlas`; the test keeps that list exact. Input it can't read is denied. `atlas ...` and
`/usr/local/bin/atlas ...` pass: the wrapper gates the billable commands itself.

Not closed by text matching: a program that builds the host at run time from pieces carrying no `atlas` (character
codes, a file it reads, a variable exported by an earlier command), and code a program loads on its own. It also
blocks harmless commands that mention those strings (search with the Grep tool instead).
