-- Publisher: progress of an Instagram post between scheduled runs (container ids, retries).
-- Safe to re-run. Apply by hand (Lovable does not apply migrations that arrive through GitHub).

ALTER TABLE content_items ADD COLUMN IF NOT EXISTS publish jsonb NOT NULL DEFAULT '{}'::jsonb;
