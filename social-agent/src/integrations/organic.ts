import { z } from 'zod';
import { BusinessSchema, FunnelSchema, type Business, type Funnel } from '../config/schema.js';
import { normalize } from '../logic/text.js';

const FlowSchema = z.object({
  flow_key: z.string().min(1),
  source_video_id: z.string().min(1),
  topic: z.string().min(1),
  platform: z.literal('instagram'),
  post_id: z.string().nullable(),
  trigger: z.object({
    event: z.literal('comment'), match: z.literal('keyword'),
    keyword: z.string().min(1), case_sensitive: z.literal(false),
  }),
  delivery: z.object({
    opening_message: z.string().min(1),
    asset_type: z.string().min(1), asset_content: z.string().min(1),
  }),
  execution_owner: z.literal('Social Agent'),
  enabled: z.literal(false),
});

export const OrganicHandoffSchema = z.object({
  schema_version: z.literal('organic-engine/social-agent-handoff/v1'),
  client: z.string().min(1),
  execution_owner: z.literal('Social Agent'),
  activation_status: z.literal('PREPARED_NOT_DEPLOYED'),
  flows: z.array(FlowSchema).min(1),
});
export type OrganicHandoff = z.infer<typeof OrganicHandoffSchema>;

function funnelId(video: string): string {
  const id = 'oe-' + video.toLowerCase().replace(/[^a-z0-9_-]+/g, '-');
  if (!/^[a-z0-9][a-z0-9_-]*$/.test(id)) throw new Error('Invalid video ID');
  return id;
}

function resourceUrl(base: string, client: string, video: string): string {
  let parsed: URL;
  try { parsed = new URL(base); } catch { throw new Error('Real public HTTPS base URL required'); }
  if (parsed.protocol !== 'https:' || parsed.username || parsed.password ||
      parsed.search || parsed.hash || parsed.pathname !== '/') {
    throw new Error('Supply the deployed root HTTPS URL, for example https://your-domain.com/');
  }
  return parsed.origin + '/resources/' + encodeURIComponent(client) + '/' + encodeURIComponent(video);
}

export interface OrganicImportPlan {
  additions: Funnel[];
  pending: { videoId: string; keyword: string }[];
  unchanged: string[];
  business: Business;
}

/**
 * The existing Social Agent sends a normal link button. The public landing page
 * itself shows the full approved prompt and how to use it.
 * No new messaging engine, no Meta API calls, and no automatic activation.
 */
export function planOrganicImport(raw: unknown, business: Business,
  postBindings: Record<string, string> = {}, baseUrl?: string): OrganicImportPlan {
  const handoff = OrganicHandoffSchema.parse(raw);
  if (handoff.client !== business.slug) throw new Error(
    'Organic client ' + handoff.client + ' differs from business ' + business.slug);
  const seenVideos = new Set<string>();
  const seenFlows = new Set<string>();
  const pending: OrganicImportPlan['pending'] = [];
  const additions: Funnel[] = [];
  const unchanged: string[] = [];

  for (const flow of handoff.flows) {
    if (seenVideos.has(flow.source_video_id) || seenFlows.has(flow.flow_key)) {
      throw new Error('Duplicate Organic flow: ' + flow.source_video_id);
    }
    seenVideos.add(flow.source_video_id);
    seenFlows.add(flow.flow_key);
    const post = postBindings[flow.source_video_id] ?? flow.post_id;
    if (!post) {
      pending.push({ videoId: flow.source_video_id, keyword: flow.trigger.keyword });
      continue;
    }
    if (!/^[0-9]{6,}(?:_[0-9]{6,})?$/.test(post)) {
      throw new Error('Invalid real Meta post ID for ' + flow.source_video_id);
    }
    if (!baseUrl) throw new Error('A published resource URL is needed. Pass --base-url with the deployed Social Agent HTTPS origin.');
    const link = resourceUrl(baseUrl, handoff.client, flow.source_video_id);
    const id = funnelId(flow.source_video_id);
    const existing = business.funnels.find((f) => f.id === id);
    if (existing) {
      if (!existing.posts.includes(post) ||
          !existing.keywords.some((k) => normalize(k) === normalize(flow.trigger.keyword)) ||
          existing.deliver.link !== link) {
        throw new Error('Existing funnel ' + id + ' has different settings; review it before replacing.');
      }
      unchanged.push(id);
      continue;
    }
    for (const other of [...business.funnels, ...additions]) {
      if (other.trigger !== 'comment' || !other.platforms.includes('instagram')) continue;
      if (!other.all_posts && !other.posts.includes(post)) continue;
      if (other.keywords.some((k) => normalize(k) === normalize(flow.trigger.keyword))) {
        throw new Error('Keyword collision with existing funnel ' + other.id + ' on post ' + post);
      }
    }
    const opener = flow.delivery.opening_message.replace(/^[״"']|[״"']$/g, '').trim();
    additions.push(FunnelSchema.parse({
      id, status: 'paused', trigger: 'comment', platforms: ['instagram'],
      posts: [post], keywords: [flow.trigger.keyword], match: 'word',
      public_replies: ['שלחתי לך הודעה בפרטי 🙌'],
      opener: {
        text: (opener + '\nלחץ על הכפתור לקבל את הכלי 👇').slice(0, 620),
        button: 'שלח לי', mode: 'tap',
      },
      deliver: { text: 'הכלי והמדריך שלך מחכים כאן 👇', link, button: 'פתח את המדריך' },
      after: 'אם יש לך שאלה על מה שקיבלת, אפשר לכתוב לי כאן.',
    }));
  }

  for (const videoId of Object.keys(postBindings)) {
    if (!seenVideos.has(videoId)) throw new Error('Unknown video ID in post bindings: ' + videoId);
  }
  const updated = BusinessSchema.parse({ ...business, funnels: [...business.funnels, ...additions] });
  return { additions, pending, unchanged, business: updated };
}
