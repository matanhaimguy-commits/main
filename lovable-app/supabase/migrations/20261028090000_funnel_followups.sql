-- Funnel follow-ups: a funnel's last message (`after`) can wait a few minutes after the delivery
-- (funnel setting `after_delay_minutes`, 0 to 60). The wait is a queue the scheduled tick works
-- through; with the default of 0 nothing is queued and this table stays empty. Additive only.
-- Safe to re-run. Apply by hand (Lovable does not apply migrations that arrive through GitHub).

CREATE TABLE IF NOT EXISTS funnel_followups (
  id            bigserial PRIMARY KEY,
  -- The send ledger key the message goes out under (funnel:<funnel>:after:<trigger>). Unique, so a
  -- delivery queues its message once, and the ledger lets the message itself leave once.
  key           text NOT NULL UNIQUE,
  business      text NOT NULL,
  funnel_id     text NOT NULL,
  contact_id    bigint NOT NULL REFERENCES contacts(id) ON DELETE CASCADE,
  due_at        timestamptz NOT NULL,
  -- The delivery was a dry run (nothing reached the person) when this was queued.
  dry_run       boolean NOT NULL DEFAULT false,
  -- The person's newest message id when this was queued: anything newer is a reply in the meantime.
  watermark     bigint NOT NULL DEFAULT 0,
  status        text NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'sending', 'done', 'skipped')),
  -- How it ended: the send outcome (sent, dry_run, failed...) or the reason it was skipped.
  result        text,
  attempts      integer NOT NULL DEFAULT 0,
  locked_until  timestamptz,
  created_at    timestamptz NOT NULL DEFAULT now(),
  finished_at   timestamptz
);

CREATE INDEX IF NOT EXISTS funnel_followups_due ON funnel_followups (due_at) WHERE status IN ('pending', 'sending');
CREATE INDEX IF NOT EXISTS funnel_followups_contact ON funnel_followups (contact_id);

-- Like every table here: RLS on, no policies, nothing for the browser keys. Only the server reads
-- and writes, through agent_sql() with the service-role key.
ALTER TABLE funnel_followups ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON funnel_followups FROM anon, authenticated;
