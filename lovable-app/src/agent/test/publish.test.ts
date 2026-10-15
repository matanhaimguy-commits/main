// @vitest-environment node
import { describe, expect, it } from 'vitest';
import { advance, PERMISSION_HELP, PROCESSING_LIMIT_MS, type PublishItem } from '../engine/publish';
import { MetaApiError, type MetaApi } from '../meta/client';

const IG = 'IG1';
const NOW = new Date('2026-10-21T17:30:00Z');

/** A scripted Graph API: container statuses per id, recorded calls. */
class Graph implements Partial<MetaApi> {
  calls: { method: string; path: string; body?: Record<string, unknown> }[] = [];
  status = new Map<string, string>();
  recent: { id: string; caption?: string; permalink?: string; timestamp?: string }[] = [];
  private n = 0;
  async post(path: string, body?: Record<string, unknown>) {
    this.calls.push({ method: 'post', path, body });
    if (path.endsWith('/media_publish')) {
      this.status.set(String(body?.creation_id), 'PUBLISHED');
      return { id: 'MEDIA1' } as any;
    }
    const id = `C${++this.n}`;
    this.status.set(id, body?.media_type === 'REELS' || body?.media_type === 'VIDEO' ? 'IN_PROGRESS' : 'FINISHED');
    return { id } as any;
  }
  async get(path: string, params?: Record<string, string>) {
    this.calls.push({ method: 'get', path, body: params });
    if (path === 'MEDIA1') return { permalink: 'https://www.instagram.com/reel/abc/' } as any;
    if (path === `${IG}/media`) return { data: this.recent } as any;
    return { status_code: this.status.get(path) ?? 'IN_PROGRESS' } as any;
  }
  posts = () => this.calls.filter((c) => c.method === 'post');
}
const api = (g: Graph) => g as unknown as MetaApi;

const reel: PublishItem = {
  id: 1,
  kind: 'reel',
  caption: 'Ajo nuk pyeti vetëm ty.',
  first_comment: null,
  media: [{ url: 'https://cdn/reel.mp4', type: 'video' }],
  cover_url: 'https://cdn/cover.jpg',
};

describe('publisher', () => {
  it('creates a reel container, waits while Instagram processes it, then publishes once', async () => {
    const g = new Graph();
    const s1 = await advance(api(g), IG, reel, {}, NOW);
    expect(s1.kind).toBe('wait');
    expect(g.posts()[0]).toMatchObject({
      path: `${IG}/media`,
      body: { media_type: 'REELS', video_url: 'https://cdn/reel.mp4', cover_url: 'https://cdn/cover.jpg', share_to_feed: true, caption: reel.caption },
    });
    // Next run: still processing, nothing new created.
    const s2 = await advance(api(g), IG, reel, s1.state, new Date(NOW.getTime() + 60_000));
    expect(s2.kind).toBe('wait');
    expect(g.posts()).toHaveLength(1);
    // Processing done: published, with its link.
    g.status.set(s1.state.container!, 'FINISHED');
    const s3 = await advance(api(g), IG, reel, s2.state, new Date(NOW.getTime() + 120_000));
    expect(s3).toMatchObject({ kind: 'published', mediaId: 'MEDIA1', permalink: 'https://www.instagram.com/reel/abc/' });
    expect(g.posts().map((c) => c.path)).toEqual([`${IG}/media`, `${IG}/media_publish`]);
  });

  it('never publishes twice: a container already published is looked up among the latest posts', async () => {
    const g = new Graph();
    g.status.set('C9', 'PUBLISHED');
    g.recent = [{ id: 'MEDIA7', caption: reel.caption, permalink: 'https://www.instagram.com/reel/x/', timestamp: NOW.toISOString() }];
    const s = await advance(api(g), IG, reel, { container: 'C9', started_at: NOW.toISOString() }, NOW);
    expect(s).toMatchObject({ kind: 'published', mediaId: 'MEDIA7' });
    expect(g.posts()).toHaveLength(0);
  });

  it('publishes an image in one pass and a carousel from its children', async () => {
    const g = new Graph();
    const image = await advance(api(g), IG, { ...reel, kind: 'image', media: [{ url: 'https://cdn/a.jpg', type: 'image' }] }, {}, NOW);
    expect(image.kind).toBe('published');
    expect(g.posts()[0]!.body).toEqual({ image_url: 'https://cdn/a.jpg', caption: reel.caption });

    const c = new Graph();
    const carousel: PublishItem = { ...reel, kind: 'carousel', media: [1, 2, 3].map((i) => ({ url: `https://cdn/${i}.jpg`, type: 'image' as const })) };
    const done = await advance(api(c), IG, carousel, {}, NOW);
    expect(done.kind).toBe('published');
    const bodies = c.posts().map((p) => p.body);
    expect(bodies.slice(0, 3)).toEqual([1, 2, 3].map((i) => ({ image_url: `https://cdn/${i}.jpg`, is_carousel_item: true })));
    expect(bodies[3]).toEqual({ media_type: 'CAROUSEL', children: 'C1,C2,C3', caption: reel.caption });
  });

  it('fails clearly on wrong media, processing errors and endless processing', async () => {
    const g = new Graph();
    expect(await advance(api(g), IG, { ...reel, media: [{ url: 'https://cdn/a.jpg', type: 'image' }] }, {}, NOW)).toMatchObject({
      kind: 'failed',
      error: 'A reel needs a video file.',
    });
    g.status.set('C5', 'ERROR');
    expect((await advance(api(g), IG, reel, { container: 'C5' }, NOW)).kind).toBe('failed');
    g.status.set('C6', 'IN_PROGRESS');
    const late = new Date(NOW.getTime() + PROCESSING_LIMIT_MS + 1);
    expect((await advance(api(g), IG, reel, { container: 'C6', started_at: NOW.toISOString() }, late)).kind).toBe('failed');
  });

  it('lets Meta errors through to the caller, which turns a missing permission into clear advice', async () => {
    const g = new Graph();
    g.post = async () => {
      throw new MetaApiError('(#10) Application does not have permission for this action', 403, 10);
    };
    await expect(advance(api(g), IG, reel, {}, NOW)).rejects.toBeInstanceOf(MetaApiError);
    expect(PERMISSION_HELP).toContain('instagram_content_publish');
  });
});

// ---- the scheduled run against Postgres --------------------------------------------------------

import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import postgres from 'postgres';
import { afterAll, beforeAll, beforeEach } from 'vitest';
import type { Sql } from '../db/sql';
import { runPublisher } from '../engine/publish';
import { IG_ID, makeBusiness } from './fixtures';
import { dbAvailable, freshDb, makeHarness, TEST_DB, truncate, type Harness } from './harness';

const hasDb = await dbAvailable();
const migration = (name: string) => readFileSync(fileURLToPath(new URL(`../../../supabase/migrations/${name}`, import.meta.url)), 'utf8');

describe.skipIf(!hasDb)('publisher (Postgres)', () => {
  let sql: Sql;
  let pg: postgres.Sql;
  let h: Harness;
  let status: string;
  let failPost: Error | undefined;

  async function setup(autoPublish: boolean) {
    const b = makeBusiness({ auto_publish: autoPublish });
    await pg`INSERT INTO businesses (slug, config) VALUES (${b.slug}, ${pg.json({ slug: b.slug } as any)}) ON CONFLICT DO NOTHING`;
    h = await makeHarness(sql, [b]);
    status = 'IN_PROGRESS';
    failPost = undefined;
    h.meta.post = async (path: string, body?: Record<string, unknown>) => {
      h.meta.calls.push({ method: 'post', args: [path, body] });
      if (failPost) throw failPost;
      if (path.endsWith('/media_publish')) return { id: 'M1' } as any;
      if (path.endsWith('/comments')) return { id: 'K1' } as any;
      return { id: 'C1' } as any;
    };
    h.meta.get = async (path: string, params?: Record<string, string>) => {
      h.meta.calls.push({ method: 'get', args: [path, params] });
      if (path === 'M1') return { permalink: 'https://www.instagram.com/reel/m1/' } as any;
      return { status_code: status } as any;
    };
  }
  async function addItem(o: { key: string; status: string; minutesFromNow: number }) {
    await pg`
      INSERT INTO content_items (business, external_key, kind, status, title, caption, first_comment, media, scheduled_at)
      VALUES ('acme', ${o.key}, 'reel', ${o.status}, 'Reel', 'Hello', 'Comment GUIDE 👇',
              ${pg.json([{ url: 'https://cdn/r.mp4', type: 'video' }] as any)}, now() + ${`${o.minutesFromNow} minutes`}::interval)`;
  }
  const item = async (key: string) => (await pg`SELECT * FROM content_items WHERE external_key = ${key}`)[0]!;
  // Ends the 50-second lease, as if the next minute's run had come.
  const nextMinute = () => pg`UPDATE content_items SET updated_at = now() - interval '2 minutes'`;

  beforeAll(async () => {
    sql = await freshDb();
    pg = postgres(TEST_DB, { max: 2, onnotice: () => {} });
    const content = migration('20261015090000_content.sql');
    await pg.unsafe(content.slice(0, content.indexOf('-- Public bucket')));
    await pg.unsafe(migration('20261016090000_publisher.sql'));
  });
  afterAll(async () => {
    await sql?.end({ timeout: 2 });
    await pg?.end({ timeout: 2 });
  });
  beforeEach(async () => {
    await pg`TRUNCATE content_items RESTART IDENTITY`;
    await truncate(sql);
  });

  it('posts a due reel by itself, one step per run, and leaves the rest alone', async () => {
    await setup(true);
    await addItem({ key: 'due', status: 'scheduled', minutesFromNow: -1 });
    await addItem({ key: 'later', status: 'scheduled', minutesFromNow: 60 });
    await addItem({ key: 'draft', status: 'draft', minutesFromNow: -1 });

    expect(await runPublisher(h.deps)).toBe(1);
    expect(await item('due')).toMatchObject({ status: 'publishing', publish: { container: 'C1' } });
    // Same minute: the lease keeps a second run off it.
    expect(await runPublisher(h.deps)).toBe(0);

    await nextMinute();
    expect(await runPublisher(h.deps)).toBe(1);
    expect((await item('due')).status).toBe('publishing');

    status = 'FINISHED';
    await nextMinute();
    await runPublisher(h.deps);
    expect(await item('due')).toMatchObject({ status: 'published', ig_media_id: 'M1', permalink: 'https://www.instagram.com/reel/m1/', error: null });
    expect(h.meta.calls.filter((c) => c.method === 'post').map((c) => c.args[0])).toEqual([`${IG_ID}/media`, `${IG_ID}/media_publish`, 'M1/comments']);
    expect(h.alerts.at(-1)).toContain('posted "Reel" on Instagram');
    expect((await item('later')).status).toBe('scheduled');
    expect((await item('draft')).status).toBe('draft');
  });

  it('does nothing while Auto-publish is off', async () => {
    await setup(false);
    await addItem({ key: 'due', status: 'scheduled', minutesFromNow: -1 });
    expect(await runPublisher(h.deps)).toBe(0);
    expect((await item('due')).status).toBe('scheduled');
  });

  it('marks the post failed with clear advice when the permission is missing', async () => {
    await setup(true);
    await addItem({ key: 'due', status: 'scheduled', minutesFromNow: -1 });
    failPost = new MetaApiError('(#10) Application does not have permission for this action', 403, 10);
    await runPublisher(h.deps);
    expect(await item('due')).toMatchObject({ status: 'failed', error: PERMISSION_HELP });
    expect(h.alerts.at(-1)).toContain('could not post');
  });
});
