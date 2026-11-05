-- Growth Engine: the content calendar the studio fills and the hub publishes from.
-- Safe to re-run. Apply by hand (Lovable does not apply migrations that arrive through GitHub).

CREATE TABLE IF NOT EXISTS content_items (
  id            bigserial PRIMARY KEY,
  business      text NOT NULL REFERENCES businesses(slug) ON DELETE CASCADE,
  -- The studio's own id for the item, so a re-run updates instead of duplicating.
  external_key  text,
  kind          text NOT NULL CHECK (kind IN ('reel', 'carousel', 'image', 'story')),
  status        text NOT NULL DEFAULT 'draft'
                CHECK (status IN ('draft', 'approved', 'scheduled', 'publishing', 'published', 'rejected', 'failed')),
  title         text,
  caption       text NOT NULL DEFAULT '',
  first_comment text,
  alt_text      text,
  -- The comment keyword this post asks for, and the funnel that answers it.
  keyword       text,
  funnel_id     text,
  -- [{url, path, type: "image" | "video", width, height}] in posting order.
  media         jsonb NOT NULL DEFAULT '[]'::jsonb,
  cover_url     text,
  scheduled_at  timestamptz,
  published_at  timestamptz,
  ig_media_id   text,
  permalink     text,
  error         text,
  -- What the studio wants a person to check (native-language read, facts...).
  notes         text,
  -- Where the idea came from: research run, plan, template.
  source        jsonb NOT NULL DEFAULT '{}'::jsonb,
  metrics       jsonb NOT NULL DEFAULT '{}'::jsonb,
  created_at    timestamptz NOT NULL DEFAULT now(),
  updated_at    timestamptz NOT NULL DEFAULT now(),
  UNIQUE (business, external_key)
);

CREATE INDEX IF NOT EXISTS content_items_due ON content_items (status, scheduled_at);
CREATE INDEX IF NOT EXISTS content_items_business ON content_items (business, created_at DESC);

ALTER TABLE content_items ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON content_items FROM anon, authenticated;

-- Public bucket: Instagram fetches the media from these URLs when a post is published.
INSERT INTO storage.buckets (id, name, public)
VALUES ('content', 'content', true)
ON CONFLICT (id) DO UPDATE SET public = true;
