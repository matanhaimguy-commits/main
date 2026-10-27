-- Studio: every content piece's production run, step by step, and the owner's checkpoints.
-- The studio pushes runs and questions (growth-engine/tools/hub.py studio-push / studio-ask, /api/studio/*);
-- the Studio page shows them and takes the owner's answers. Additive only.
-- Safe to re-run. Apply by hand (Lovable does not apply migrations that arrive through GitHub).

-- One row per piece: clients/<slug>/runs/<post_id>/ in the studio.
CREATE TABLE IF NOT EXISTS studio_runs (
  id                bigserial PRIMARY KEY,
  business          text NOT NULL REFERENCES businesses(slug) ON DELETE CASCADE,
  post_id           text NOT NULL,
  title             text,
  format            text,
  family            text,
  current_step      integer,
  status            text NOT NULL DEFAULT 'active' CHECK (status IN ('active', 'blocked', 'done', 'paused')),
  -- The studio's own "a person has to answer something" flag (its human queue); open decisions count too.
  waiting_on_owner  boolean NOT NULL DEFAULT false,
  summary           text,
  -- [{n, name, status: done|active|blocked|na|pending, note, at,
  --   gates: [{gate, label, status: PASS|FAIL|OVERRIDE|PENDING, score, max, by, at, note, asset}]}]
  steps             jsonb NOT NULL DEFAULT '[]'::jsonb,
  -- The run's ledger.json as last pushed.
  ledger            jsonb NOT NULL DEFAULT '{}'::jsonb,
  pushed_at         timestamptz NOT NULL DEFAULT now(),
  created_at        timestamptz NOT NULL DEFAULT now(),
  updated_at        timestamptz NOT NULL DEFAULT now(),
  UNIQUE (business, post_id)
);

CREATE INDEX IF NOT EXISTS studio_runs_recent ON studio_runs (updated_at DESC);

-- Files attached to a run and (optionally) one of its steps. Media live in the public "content" bucket
-- (uploaded through /api/content/upload); docs may come as inline markdown instead.
CREATE TABLE IF NOT EXISTS studio_files (
  id          bigserial PRIMARY KEY,
  run_id      bigint NOT NULL REFERENCES studio_runs(id) ON DELETE CASCADE,
  -- The studio's id for the file (by default its path), so a re-push updates instead of duplicating.
  key         text NOT NULL,
  step        integer,
  label       text NOT NULL,
  kind        text NOT NULL CHECK (kind IN ('doc', 'audio', 'image', 'video')),
  url         text,
  markdown    text,
  -- Of the uploaded bytes, so the studio can skip uploading an unchanged file again.
  sha256      text,
  position    integer NOT NULL DEFAULT 0,
  created_at  timestamptz NOT NULL DEFAULT now(),
  updated_at  timestamptz NOT NULL DEFAULT now(),
  UNIQUE (run_id, key),
  CHECK (url IS NOT NULL OR markdown IS NOT NULL)
);

CREATE INDEX IF NOT EXISTS studio_files_run ON studio_files (run_id, step, position);

-- The owner's checkpoints (G-HUMAN-SONG, GATE 4...): a question with options, answered on the Studio page,
-- then taken back into the studio (synced).
CREATE TABLE IF NOT EXISTS studio_decisions (
  id           bigserial PRIMARY KEY,
  run_id       bigint NOT NULL REFERENCES studio_runs(id) ON DELETE CASCADE,
  -- One question per key and run (by default the checkpoint code); asking the same key again while it is
  -- open updates the question.
  key          text NOT NULL,
  checkpoint   text NOT NULL,
  step         integer,
  question     text NOT NULL,
  -- Background for the question, markdown.
  context      text,
  -- [{label, description}]
  options      jsonb NOT NULL DEFAULT '[]'::jsonb,
  multi        boolean NOT NULL DEFAULT false,
  status       text NOT NULL DEFAULT 'open' CHECK (status IN ('open', 'answered', 'synced')),
  -- {choices: [label], note, by, at}
  answer       jsonb,
  answered_at  timestamptz,
  synced_at    timestamptz,
  created_at   timestamptz NOT NULL DEFAULT now(),
  updated_at   timestamptz NOT NULL DEFAULT now(),
  UNIQUE (run_id, key)
);

CREATE INDEX IF NOT EXISTS studio_decisions_status ON studio_decisions (status, run_id);

ALTER TABLE studio_runs ENABLE ROW LEVEL SECURITY;
ALTER TABLE studio_files ENABLE ROW LEVEL SECURITY;
ALTER TABLE studio_decisions ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON studio_runs FROM anon, authenticated;
REVOKE ALL ON studio_files FROM anon, authenticated;
REVOKE ALL ON studio_decisions FROM anon, authenticated;
