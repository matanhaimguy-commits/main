-- Facebook Pages connected through the "Connect Facebook & Instagram" button.
-- Page tokens are encrypted (AES-256-GCM, key derived from META_APP_SECRET).
CREATE TABLE meta_connections (
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
CREATE TABLE app_state (
  key         text PRIMARY KEY,
  value       jsonb NOT NULL,
  updated_at  timestamptz NOT NULL DEFAULT now()
);
