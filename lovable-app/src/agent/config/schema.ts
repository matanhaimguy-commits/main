import { z } from 'zod/v4';

export const PLATFORMS = ['instagram', 'facebook'] as const;
export type Platform = (typeof PLATFORMS)[number];

const id = z.string().regex(/^[a-z0-9][a-z0-9_-]*$/, 'use lowercase letters, digits, - and _');

// Meta caps button titles at 20 characters and button-template text at 640.
const buttonTitle = z.string().min(1).max(20);
const buttonText = z.string().min(1).max(640);

export const LinkSchema = z.object({
  id,
  title: buttonTitle,
  url: z.url(),
  // Tells the AI when this link is the right one to send.
  when: z.string().optional(),
});

export const FunnelSchema = z.object({
  id,
  status: z.enum(['active', 'paused']).default('active'),
  // comment: someone comments a keyword on a pinned post (private reply).
  // story_reply: someone replies to a story with a keyword (Instagram).
  // dm_keyword: someone sends the keyword as a DM.
  trigger: z.enum(['comment', 'story_reply', 'dm_keyword']).default('comment'),
  platforms: z.array(z.enum(PLATFORMS)).min(1).default(['instagram', 'facebook']),
  // Post / media IDs this funnel is pinned to. Required for comment funnels.
  posts: z.array(z.coerce.string()).default([]),
  // Account-wide comment funnel. The audit refuses it unless acknowledged,
  // because a comment on a two-year-old post would be pulled into this funnel.
  all_posts: z.boolean().default(false),
  all_posts_acknowledged: z.boolean().default(false),
  keywords: z.array(z.string().min(1)).min(1),
  match: z.enum(['exact', 'word', 'contains']).default('word'),
  // Optional public reply under the comment; one is picked per comment.
  public_replies: z.array(z.string().min(1)).default([]),
  // First DM. With mode "tap" the button is a postback that delivers the link
  // in a second message; the tap also opens the 24h window so the AI can talk.
  // With mode "link" the button opens the delivery link directly.
  opener: z.object({
    text: buttonText,
    button: buttonTitle,
    mode: z.enum(['tap', 'link']).default('tap'),
  }),
  // Instagram only: ask them to follow before delivering. Costs one extra tap.
  follow_gate: z
    .object({
      enabled: z.boolean().default(true),
      text: buttonText,
      button: buttonTitle,
    })
    .optional(),
  deliver: z.object({
    text: buttonText,
    link: z.string().min(1), // a link id from `links`, or a full URL
    button: buttonTitle,
  }),
  // Last message: open a conversation, not just hand over a link.
  after: z.string().min(1).max(1000).optional(),
});

export const BusinessSchema = z.object({
  slug: id,
  name: z.string().min(1),
  enabled: z.boolean().default(true),
  // Real messages go out only when this is true AND the LIVE_SENDING env var is true.
  live: z.boolean().default(false),
  // While non-empty, only these Instagram usernames / user IDs get automated
  // messages. Use it to test with a second account before opening to the public.
  testers: z.array(z.coerce.string()).default([]),
  // Approved Content items with a time go out on Instagram by themselves at that time.
  // Needs instagram_content_publish on the Page connection. Off by default.
  auto_publish: z.boolean().default(false),
  timezone: z.string().default('UTC'),
  // Usually filled in by the "Connect Facebook & Instagram" button on the Connect page.
  // Set these only to pin IDs or to use a token from an env var instead.
  meta: z
    .object({
      page_id: z.coerce.string().min(1).optional(),
      instagram_id: z.coerce.string().min(1).optional(),
      // Name of an env var that holds this Page's access token. Never the token itself.
      page_token_env: z.string().regex(/^[A-Z][A-Z0-9_]*$/).optional(),
    })
    .prefault({}),
  profile: z.object({
    about: z.string().min(1),
    offers: z.string().min(1),
    audience: z.string().optional(),
    goal: z.string().min(1),
    qualifying_questions: z.array(z.string()).default([]),
    faq: z.array(z.object({ q: z.string(), a: z.string() })).default([]),
    policies: z.string().optional(),
    voice: z.string().optional(),
    never: z.array(z.string()).default([]),
    extra: z.string().optional(),
  }),
  links: z.array(LinkSchema).default([]),
  ai: z
    .object({
      enabled: z.boolean().default(true),
      dm_replies: z.boolean().default(true),
      // Public answers under posts to questions no funnel owns.
      comment_replies: z.boolean().default(false),
      // Private reply DMs to buying-intent comments no funnel owns.
      comment_dms: z.boolean().default(false),
      hide_spam: z.boolean().default(false),
      model: z.string().optional(),
      effort: z.enum(['low', 'medium', 'high', 'xhigh', 'max']).default('medium'),
      // Wait this long after the last inbound message, so a burst of short
      // messages gets one answer.
      reply_delay_seconds: z.number().int().min(0).max(120).default(8),
      max_replies_per_contact_per_day: z.number().int().min(1).default(40),
      max_public_replies_per_day: z.number().int().min(0).default(100),
      pause_hours_after_human: z.number().min(0).default(12),
      followup: z
        .object({
          enabled: z.boolean().default(true),
          after_hours: z.number().min(1).max(22).default(4),
        })
        .prefault({}),
    })
    .prefault({}),
  comments: z
    .object({
      // Replies inside comment threads are ignored by default.
      include_replies: z.boolean().default(false),
    })
    .prefault({}),
  track_clicks: z.boolean().default(false),
  // The public lead form at /l/<slug>: works for everyone, whatever Meta lets the app receive.
  lead_form: z
    .object({
      enabled: z.boolean().default(true),
      language: z.enum(['en', 'sq', 'he']).default('en'),
      title: z.string().max(80).optional(),
      intro: z.string().max(400).optional(),
      // Shown after sending (a link id from `links`, or a full URL), e.g. a booking page.
      after_link: z.string().max(300).optional(),
    })
    .prefault({}),
  funnels: z.array(FunnelSchema).default([]),
});

export type Business = z.infer<typeof BusinessSchema>;
export type Funnel = z.infer<typeof FunnelSchema>;
export type Link = z.infer<typeof LinkSchema>;
