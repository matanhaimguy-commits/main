-- Raw webhook deliveries. The row is written before Meta gets its 200, so nothing
-- Meta sends is ever lost; the worker claims pending rows with a lease.
CREATE TABLE webhook_events (
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
CREATE INDEX webhook_events_queue ON webhook_events (status, id);

-- One row per person per business per platform. Doubles as the conversation state.
CREATE TABLE contacts (
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
CREATE INDEX contacts_reply_queue ON contacts (needs_reply, reply_due_at) WHERE needs_reply;

-- Every new comment gets a row, matched or not. "Why did my funnel not fire" is a query.
CREATE TABLE comments (
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
CREATE INDEX comments_business_time ON comments (business, received_at DESC);

-- The send ledger. A row is claimed (status pending) BEFORE the API call, keyed by an
-- idempotency key, so the same send can never be attempted twice. Nothing retries a send.
-- delivered_at is only ever set from Facebook delivery receipts. Instagram has none, so
-- for Instagram it stays NULL: sent is a fact, delivered is unknown.
CREATE TABLE sends (
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
CREATE INDEX sends_business_time ON sends (business, created_at DESC);
CREATE INDEX sends_message_id ON sends (message_id) WHERE message_id IS NOT NULL;
CREATE INDEX sends_contact ON sends (contact_id, sent_at);

-- Conversation transcript (what the AI reads). mid is unique, which also dedupes
-- Meta's echo of messages we sent ourselves.
CREATE TABLE messages (
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
CREATE INDEX messages_contact_time ON messages (contact_id, created_at);

-- Tracked links (/r/:token). Instagram gives no delivery receipts, so reads,
-- button taps and clicks are how an Instagram funnel proves it is landing.
CREATE TABLE links (
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
CREATE TABLE taps (
  id          bigserial PRIMARY KEY,
  business    text NOT NULL,
  contact_id  bigint REFERENCES contacts(id),
  funnel_id   text,
  payload     text,
  created_at  timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE ai_runs (
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
CREATE TABLE alerts (
  key           text PRIMARY KEY,
  last_sent_at  timestamptz NOT NULL,
  count         int NOT NULL DEFAULT 1
);

-- Per-business switches set by the system itself, e.g. after Meta flags sends as spam (error 368).
CREATE TABLE business_state (
  business               text PRIMARY KEY,
  sending_paused_until   timestamptz,
  paused_reason          text,
  updated_at             timestamptz NOT NULL DEFAULT now()
);
