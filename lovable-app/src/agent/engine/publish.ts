import type { Business } from '../config/schema';
import { MetaApiError, MetaNetworkError, type MetaApi } from '../meta/client';
import type { Deps } from './deps';

/**
 * The publisher: approved content items whose time has come go out on Instagram by themselves,
 * for businesses with `auto_publish` on. Instagram's Content Publishing API works in two steps
 * (create a media container, then publish it), and videos need minutes of processing in between,
 * so each item moves forward one step per scheduled run and keeps its progress in
 * content_items.publish.
 */

export interface PublishItem {
  id: number;
  kind: 'reel' | 'carousel' | 'image' | 'story';
  caption: string;
  first_comment: string | null;
  media: { url: string; type: 'image' | 'video' }[];
  cover_url: string | null;
}

/** Progress kept between runs. */
export interface PublishState {
  children?: string[];
  container?: string;
  started_at?: string;
  attempts?: number;
  next_at?: string;
}

export type Step =
  | { kind: 'wait'; state: PublishState }
  | { kind: 'published'; mediaId: string; permalink: string | null; state: PublishState }
  | { kind: 'failed'; error: string; state: PublishState };

/** Instagram usually needs a few minutes for a reel; give up after this. */
export const PROCESSING_LIMIT_MS = 45 * 60_000;
/** Temporary errors (network, rate limits) are retried this many times, 5, 10, 15... minutes apart. */
export const MAX_RETRIES = 5;

export const PERMISSION_HELP =
  'Instagram refused to publish: the connection lacks the instagram_content_publish permission. Add it to the ' +
  'Facebook Login configuration in the Meta app, press Connect again, then approve this post again.';

function containerParams(item: PublishItem): Record<string, unknown> | string {
  const m = item.media[0];
  if (!m) return 'This post has no media file.';
  switch (item.kind) {
    case 'image':
      if (m.type !== 'image') return 'An image post needs an image file.';
      return { image_url: m.url, caption: item.caption };
    case 'reel':
      if (m.type !== 'video') return 'A reel needs a video file.';
      return { media_type: 'REELS', video_url: m.url, caption: item.caption, share_to_feed: true, ...(item.cover_url ? { cover_url: item.cover_url } : {}) };
    case 'story':
      return m.type === 'video' ? { media_type: 'STORIES', video_url: m.url } : { media_type: 'STORIES', image_url: m.url };
    case 'carousel':
      return 'internal: carousels are built from children';
  }
}

const childParams = (m: PublishItem['media'][number]) =>
  m.type === 'video' ? { media_type: 'VIDEO', video_url: m.url, is_carousel_item: true } : { image_url: m.url, is_carousel_item: true };

type ContainerStatus = 'FINISHED' | 'IN_PROGRESS' | 'PUBLISHED' | 'ERROR' | 'EXPIRED' | string;

async function containerStatus(api: MetaApi, id: string): Promise<{ code: ContainerStatus; detail?: string }> {
  const r = await api.get<{ status_code?: string; status?: string }>(id, { fields: 'status_code,status' });
  return { code: r.status_code ?? 'IN_PROGRESS', detail: r.status };
}

function waitOrTimeout(state: PublishState, now: Date): Step {
  const started = state.started_at ? Date.parse(state.started_at) : now.getTime();
  if (now.getTime() - started > PROCESSING_LIMIT_MS) {
    return { kind: 'failed', error: `Instagram was still processing the media after ${PROCESSING_LIMIT_MS / 60_000} minutes.`, state };
  }
  return { kind: 'wait', state };
}

/** A post already published by an earlier run that never saw Meta's answer: find it instead of posting twice. */
async function findPublished(api: MetaApi, igId: string, item: PublishItem, state: PublishState): Promise<{ id: string; permalink: string | null } | null> {
  const since = state.started_at ? Date.parse(state.started_at) - 60_000 : 0;
  const res = await api.get<{ data: { id: string; caption?: string; permalink?: string; timestamp?: string }[] }>(`${igId}/media`, {
    fields: 'id,caption,permalink,timestamp',
    limit: '10',
  });
  const want = item.caption.trim();
  const hit = res.data.find((m) => (m.caption ?? '').trim() === want && (!m.timestamp || Date.parse(m.timestamp) >= since));
  return hit ? { id: hit.id, permalink: hit.permalink ?? null } : null;
}

/** Moves one item forward as far as it can go right now. Meta errors are thrown to the caller. */
export async function advance(api: MetaApi, igId: string, item: PublishItem, prev: PublishState, now: Date): Promise<Step> {
  const state: PublishState = { ...prev, started_at: prev.started_at ?? now.toISOString() };

  if (!state.container) {
    if (item.kind === 'carousel') {
      if (item.media.length < 2 || item.media.length > 10) return { kind: 'failed', error: 'A carousel needs 2 to 10 media files.', state };
      if (!state.children) {
        const children: string[] = [];
        for (const m of item.media) children.push((await api.post<{ id: string }>(`${igId}/media`, childParams(m))).id);
        state.children = children;
      }
      for (const child of state.children) {
        const s = await containerStatus(api, child);
        if (s.code === 'ERROR' || s.code === 'EXPIRED') {
          return { kind: 'failed', error: `Instagram could not process a carousel file: ${s.detail ?? s.code}.`, state };
        }
        if (s.code !== 'FINISHED') return waitOrTimeout(state, now);
      }
      state.container = (
        await api.post<{ id: string }>(`${igId}/media`, { media_type: 'CAROUSEL', children: state.children.join(','), caption: item.caption })
      ).id;
    } else {
      const params = containerParams(item);
      if (typeof params === 'string') return { kind: 'failed', error: params, state };
      state.container = (await api.post<{ id: string }>(`${igId}/media`, params)).id;
    }
  }

  const s = await containerStatus(api, state.container);
  if (s.code === 'ERROR' || s.code === 'EXPIRED') {
    return { kind: 'failed', error: `Instagram could not process the media: ${s.detail ?? s.code}.`, state };
  }
  if (s.code === 'PUBLISHED') {
    const found = await findPublished(api, igId, item, state);
    if (found) return { kind: 'published', mediaId: found.id, permalink: found.permalink, state };
    return { kind: 'failed', error: 'Instagram says this post was published, but it is not among the latest posts. Check Instagram before posting it again.', state };
  }
  if (s.code !== 'FINISHED') return waitOrTimeout(state, now);

  const { id: mediaId } = await api.post<{ id: string }>(`${igId}/media_publish`, { creation_id: state.container });
  let permalink: string | null = null;
  try {
    permalink = (await api.get<{ permalink?: string }>(mediaId, { fields: 'permalink' })).permalink ?? null;
  } catch {
    // The post is live; the link is a nice-to-have.
  }
  return { kind: 'published', mediaId, permalink, state };
}

/** Meta errors that are worth another try a few minutes later. */
function isTemporary(err: unknown): boolean {
  if (err instanceof MetaNetworkError) return true;
  if (!(err instanceof MetaApiError)) return false;
  // 9007: "media not ready"; 1/2: unknown/temporary; 5xx: Meta's side.
  return err.category === 'rate_limit' || err.code === 9007 || err.code === 1 || err.code === 2 || err.status >= 500;
}

function describe(err: unknown): string {
  if (err instanceof MetaApiError && err.category === 'permission') return PERMISSION_HELP;
  if (err instanceof MetaApiError && err.category === 'token') return 'The Page connection stopped working. Press Connect again, then approve this post again.';
  return `Instagram refused the post: ${(err as Error).message}`;
}

interface DueRow extends PublishItem {
  business: string;
  title: string | null;
  publish: PublishState | null;
}

/** One pass: claim due items, move each forward one step, record the outcome. Returns how many it touched. */
export async function runPublisher(deps: Deps, limit = 3): Promise<number> {
  const on = deps.registry.businesses.filter((b) => b.enabled && b.auto_publish && b.meta.instagram_id);
  if (!on.length) return 0;
  // A short lease (updated_at) keeps two overlapping runs off the same item.
  const rows = await deps.sql<DueRow[]>`
    UPDATE content_items SET status = 'publishing', updated_at = now()
    WHERE id IN (
      SELECT id FROM content_items
      WHERE business IN ${deps.sql(on.map((b) => b.slug))}
        AND (
          (status = 'scheduled' AND scheduled_at <= now())
          OR (status = 'publishing' AND updated_at < now() - interval '50 seconds'
              AND coalesce((publish->>'next_at')::timestamptz, '-infinity'::timestamptz) <= now())
        )
      ORDER BY scheduled_at NULLS LAST, id
      LIMIT ${limit}
      FOR UPDATE SKIP LOCKED)
    RETURNING id, business, kind, title, caption, first_comment, media, cover_url, publish`;

  for (const row of rows) {
    const b = on.find((x) => x.slug === row.business) as Business;
    const prev: PublishState = row.publish ?? {};
    const api = deps.metaFor(b);
    if (!api) {
      await finish(deps, b, row, { kind: 'failed', error: 'No working Page connection for this business. Press Connect again.', state: prev });
      continue;
    }
    let step: Step;
    try {
      step = await advance(api, b.meta.instagram_id as string, row, prev, deps.now());
    } catch (err) {
      const attempts = (prev.attempts ?? 0) + 1;
      if (isTemporary(err) && attempts <= MAX_RETRIES) {
        const next = new Date(deps.now().getTime() + attempts * 5 * 60_000).toISOString();
        deps.log.warn('publish will retry', { item: row.id, attempts, err });
        await deps.sql`
          UPDATE content_items SET publish = ${deps.sql.json({ ...prev, attempts, next_at: next } as any)},
            error = ${`Trying again (${attempts}/${MAX_RETRIES}): ${(err as Error).message}`}, updated_at = now()
          WHERE id = ${row.id}`;
        continue;
      }
      deps.log.error('publish failed', { item: row.id, err });
      step = { kind: 'failed', error: describe(err), state: prev };
    }
    await finish(deps, b, row, step, api);
  }
  return rows.length;
}

async function finish(deps: Deps, b: Business, row: DueRow, step: Step, api?: MetaApi) {
  const label = row.title ? `"${row.title}"` : `post #${row.id}`;
  if (step.kind === 'wait') {
    await deps.sql`UPDATE content_items SET publish = ${deps.sql.json(step.state as any)}, error = NULL, updated_at = now() WHERE id = ${row.id}`;
    return;
  }
  if (step.kind === 'failed') {
    await deps.sql`
      UPDATE content_items SET status = 'failed', error = ${step.error}, publish = ${deps.sql.json(step.state as any)}, updated_at = now()
      WHERE id = ${row.id}`;
    await deps.alert({ key: `publish-failed:${row.id}`, text: `⚠️ ${b.name}: could not post ${label} on Instagram. ${step.error}` });
    return;
  }
  await deps.sql`
    UPDATE content_items SET status = 'published', published_at = now(), ig_media_id = ${step.mediaId},
      permalink = coalesce(${step.permalink}, permalink), error = NULL, publish = ${deps.sql.json(step.state as any)}, updated_at = now()
    WHERE id = ${row.id}`;
  if (row.first_comment && api) {
    try {
      await api.post(`${step.mediaId}/comments`, { message: row.first_comment });
    } catch (err) {
      deps.log.warn('first comment failed', { item: row.id, err });
    }
  }
  await deps.alert({ key: `published:${row.id}`, text: `📣 ${b.name}: posted ${label} on Instagram.${step.permalink ? ` ${step.permalink}` : ''}` });
}
