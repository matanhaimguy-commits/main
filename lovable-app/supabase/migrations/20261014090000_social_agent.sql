-- Social Agent: Instagram + Facebook comment-to-DM funnels and an AI sales agent.
-- Safe to run more than once. Applied through Lovable Cloud (query_database) or the SQL editor.
--
-- Every table has row level security on and no policies: the browser (anon/authenticated
-- keys) can read nothing. Only the app's server, with the service-role key, reads and writes,
-- through the agent_sql() function at the end of this file.

-- Raw webhook deliveries. The row is written before Meta gets its 200, so nothing
-- Meta sends is ever lost; the worker claims pending rows with a lease.
CREATE TABLE IF NOT EXISTS webhook_events (
  id            bigserial PRIMARY KEY,
  received_at   timestamptz NOT NULL DEFAULT now(),
  object        text,
  payload       jsonb NOT NULL,
  status        text NOT NULL DEFAULT 'pending',   -- pending | processing | done | error
  attempts      int NOT NULL DEFAULT 0,
  locked_until  timestamptz,
  processed_at  timestamptz,
  error         text
);
CREATE INDEX IF NOT EXISTS webhook_events_queue ON webhook_events (status, id);

-- One row per person per business per platform. Doubles as the conversation state.
CREATE TABLE IF NOT EXISTS contacts (
  id                 bigserial PRIMARY KEY,
  business           text NOT NULL,
  platform           text NOT NULL,                -- instagram | facebook
  external_id        text NOT NULL,                -- IGSID / PSID
  username           text,
  name               text,
  phone              text,
  email              text,
  stage              text NOT NULL DEFAULT 'new',  -- new | engaged | qualified | hot | booked | won | lost
  interest           text,
  budget             text,
  timeline           text,
  notes              text,
  source             text,                         -- how they arrived, e.g. funnel:guide-reel
  follows_business   boolean,
  opted_out          boolean NOT NULL DEFAULT false,
  ai_paused_until    timestamptz,
  ai_pause_reason    text,
  needs_reply        boolean NOT NULL DEFAULT false,
  reply_due_at       timestamptz,
  reply_lock_until   timestamptz,
  last_inbound_at    timestamptz,
  last_outbound_at   timestamptz,
  followup_for       timestamptz,                  -- last_inbound_at a follow-up was already sent for
  created_at         timestamptz NOT NULL DEFAULT now(),
  updated_at         timestamptz NOT NULL DEFAULT now(),
  UNIQUE (business, platform, external_id)
);
CREATE INDEX IF NOT EXISTS contacts_reply_queue ON contacts (needs_reply, reply_due_at) WHERE needs_reply;

-- Every new comment gets a row, matched or not. "Why did my funnel not fire" is a query.
CREATE TABLE IF NOT EXISTS comments (
  id            bigserial PRIMARY KEY,
  business      text NOT NULL,
  platform      text NOT NULL,
  comment_id    text NOT NULL,
  post_id       text,
  parent_id     text,
  author_id     text,
  author_name   text,
  text          text,
  commented_at  timestamptz,
  received_at   timestamptz NOT NULL DEFAULT now(),
  outcome       text NOT NULL,                     -- funnel | ai | skipped
  skip_reason   text,
  funnel_id     text,
  ai_intent     text,
  ai_decision   jsonb,
  contact_id    bigint REFERENCES contacts(id),
  UNIQUE (platform, comment_id)
);
CREATE INDEX IF NOT EXISTS comments_business_time ON comments (business, received_at DESC);

-- The send ledger. A row is claimed (status pending) BEFORE the API call, keyed by an
-- idempotency key, so the same send can never be attempted twice. Nothing retries a send.
-- delivered_at is only ever set from Facebook delivery receipts. Instagram has none, so
-- for Instagram it stays NULL: sent is a fact, delivered is unknown.
CREATE TABLE IF NOT EXISTS sends (
  id               bigserial PRIMARY KEY,
  business         text NOT NULL,
  platform         text NOT NULL,
  kind             text NOT NULL,                  -- private_reply | message | public_reply | hide_comment
  idempotency_key  text NOT NULL UNIQUE,
  funnel_id        text,
  step             text,                           -- opener | gate | deliver | after | ai | followup
  comment_id       text,
  contact_id       bigint REFERENCES contacts(id),
  recipient_id     text,
  request          jsonb,
  status           text NOT NULL DEFAULT 'pending', -- pending | sent | failed | unknown | dry_run | skipped
  message_id       text,
  error_code       int,
  error_subcode    int,
  error_message    text,
  created_at       timestamptz NOT NULL DEFAULT now(),
  sent_at          timestamptz,
  delivered_at     timestamptz,
  read_at          timestamptz
);
CREATE INDEX IF NOT EXISTS sends_business_time ON sends (business, created_at DESC);
CREATE INDEX IF NOT EXISTS sends_message_id ON sends (message_id) WHERE message_id IS NOT NULL;
CREATE INDEX IF NOT EXISTS sends_contact ON sends (contact_id, sent_at);

-- Conversation transcript (what the AI reads). mid is unique, which also dedupes
-- Meta's echo of messages we sent ourselves.
CREATE TABLE IF NOT EXISTS messages (
  id          bigserial PRIMARY KEY,
  contact_id  bigint NOT NULL REFERENCES contacts(id),
  direction   text NOT NULL,                       -- in | out
  source      text NOT NULL,                       -- user | comment | funnel | ai | human | system
  mid         text UNIQUE,
  text        text,
  payload     jsonb,
  send_id     bigint REFERENCES sends(id),
  created_at  timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS messages_contact_time ON messages (contact_id, created_at);

-- Tracked links (/r/:token). Instagram gives no delivery receipts, so reads,
-- button taps and clicks are how an Instagram funnel proves it is landing.
CREATE TABLE IF NOT EXISTS links (
  token             text PRIMARY KEY,
  business          text NOT NULL,
  contact_id        bigint REFERENCES contacts(id),
  send_id           bigint REFERENCES sends(id),
  funnel_id         text,
  url               text NOT NULL,
  clicks            int NOT NULL DEFAULT 0,
  first_clicked_at  timestamptz,
  created_at        timestamptz NOT NULL DEFAULT now()
);

-- Postback button taps, per funnel. A tap proves the opener landed.
CREATE TABLE IF NOT EXISTS taps (
  id          bigserial PRIMARY KEY,
  business    text NOT NULL,
  contact_id  bigint REFERENCES contacts(id),
  funnel_id   text,
  payload     text,
  created_at  timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS ai_runs (
  id                  bigserial PRIMARY KEY,
  business            text NOT NULL,
  contact_id          bigint REFERENCES contacts(id),
  kind                text NOT NULL,               -- reply | followup | comment
  model               text,
  input_tokens        int,
  output_tokens       int,
  cache_read_tokens   int,
  stop_reason         text,
  error               text,
  created_at          timestamptz NOT NULL DEFAULT now()
);

-- Alert de-duplication so one broken funnel does not page you every minute.
CREATE TABLE IF NOT EXISTS alerts (
  key           text PRIMARY KEY,
  last_sent_at  timestamptz NOT NULL,
  count         int NOT NULL DEFAULT 1
);

-- Per-business switches set by the system itself, e.g. after Meta flags sends as spam (error 368).
CREATE TABLE IF NOT EXISTS business_state (
  business               text PRIMARY KEY,
  sending_paused_until   timestamptz,
  paused_reason          text,
  updated_at             timestamptz NOT NULL DEFAULT now()
);

-- Facebook Pages connected through the "Connect Facebook & Instagram" button.
-- Page tokens are encrypted (AES-256-GCM, key derived from the Meta app secret).
CREATE TABLE IF NOT EXISTS meta_connections (
  page_id             text PRIMARY KEY,
  page_name           text NOT NULL,
  instagram_id        text,
  instagram_username  text,
  business            text UNIQUE,          -- the business slug this Page serves, once chosen
  token_enc           text NOT NULL,
  subscribed_at       timestamptz,
  connected_at        timestamptz NOT NULL DEFAULT now(),
  updated_at          timestamptz NOT NULL DEFAULT now()
);

-- Small key/value facts for the setup page (last webhook verification, last event...).
CREATE TABLE IF NOT EXISTS app_state (
  key         text PRIMARY KEY,
  value       jsonb NOT NULL,
  updated_at  timestamptz NOT NULL DEFAULT now()
);

-- One row per business the agent serves. `config` is the business as written in the
-- dashboard (profile, links, funnels, AI settings); the app validates it on every save.
CREATE TABLE IF NOT EXISTS businesses (
  slug        text PRIMARY KEY,
  config      jsonb NOT NULL,
  created_at  timestamptz NOT NULL DEFAULT now(),
  updated_at  timestamptz NOT NULL DEFAULT now()
);

-- ---- lock everything down -------------------------------------------------------------

DO $$
DECLARE t text;
BEGIN
  FOREACH t IN ARRAY ARRAY['webhook_events','contacts','comments','sends','messages','links','taps','ai_runs',
                           'alerts','business_state','meta_connections','app_state','businesses'] LOOP
    EXECUTE format('ALTER TABLE public.%I ENABLE ROW LEVEL SECURITY', t);
    EXECUTE format('REVOKE ALL ON public.%I FROM anon, authenticated', t);
  END LOOP;
END $$;

-- ---- the server's SQL entry point -------------------------------------------------------

-- The app runs on Cloudflare Workers, which cannot hold a Postgres connection, so it sends
-- each statement here over Supabase's REST API with the service-role key. Values arrive
-- already quoted as literals (see src/agent/db/sql.ts). Only service_role may call it.
CREATE OR REPLACE FUNCTION public.agent_sql(q text, want_rows boolean DEFAULT true)
RETURNS jsonb
LANGUAGE plpgsql
SET search_path = public
SET standard_conforming_strings = on
AS $$
DECLARE
  result jsonb;
  n bigint;
BEGIN
  IF want_rows THEN
    EXECUTE format(
      'WITH agent_sql_rows AS (%s) SELECT coalesce(jsonb_agg(to_jsonb(agent_sql_rows)), ''[]''::jsonb) FROM agent_sql_rows', q)
      INTO result;
    RETURN result;
  END IF;
  EXECUTE q;
  GET DIAGNOSTICS n = ROW_COUNT;
  RETURN jsonb_build_object('count', n);
END $$;

REVOKE ALL ON FUNCTION public.agent_sql(text, boolean) FROM PUBLIC;
REVOKE ALL ON FUNCTION public.agent_sql(text, boolean) FROM anon, authenticated;
GRANT EXECUTE ON FUNCTION public.agent_sql(text, boolean) TO service_role;

-- ---- background work --------------------------------------------------------------------

-- Every minute, call the app's /api/tick so queued events, due AI replies, follow-ups and
-- health checks run even when no webhook arrives. The app writes its own address and a
-- random secret to app_state('tick_target') the first time an admin opens the dashboard
-- on the published site; until then this does nothing.
CREATE EXTENSION IF NOT EXISTS pg_net;
CREATE EXTENSION IF NOT EXISTS pg_cron;

CREATE OR REPLACE FUNCTION public.agent_tick()
RETURNS void
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = public
AS $$
DECLARE
  target jsonb;
BEGIN
  SELECT value INTO target FROM app_state WHERE key = 'tick_target';
  IF target IS NULL OR coalesce(target->>'url', '') = '' THEN
    RETURN;
  END IF;
  PERFORM net.http_post(
    url := target->>'url',
    body := '{}'::jsonb,
    headers := jsonb_build_object('Content-Type', 'application/json', 'X-Agent-Tick', target->>'secret'),
    timeout_milliseconds := 30000
  );
END $$;

REVOKE ALL ON FUNCTION public.agent_tick() FROM PUBLIC;
REVOKE ALL ON FUNCTION public.agent_tick() FROM anon, authenticated;

-- Housekeeping once a day: old processed webhook deliveries and the scheduler's own logs.
CREATE OR REPLACE FUNCTION public.agent_cleanup()
RETURNS void
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = public
AS $$
BEGIN
  DELETE FROM webhook_events WHERE status = 'done' AND received_at < now() - interval '30 days';
  DELETE FROM cron.job_run_details WHERE end_time < now() - interval '3 days';
END $$;

REVOKE ALL ON FUNCTION public.agent_cleanup() FROM PUBLIC;
REVOKE ALL ON FUNCTION public.agent_cleanup() FROM anon, authenticated;

SELECT cron.unschedule(jobname) FROM cron.job WHERE jobname IN ('social-agent-tick', 'social-agent-cleanup');
SELECT cron.schedule('social-agent-tick', '* * * * *', 'SELECT public.agent_tick()');
SELECT cron.schedule('social-agent-cleanup', '17 3 * * *', 'SELECT public.agent_cleanup()');
