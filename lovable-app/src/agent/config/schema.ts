import { z } from 'zod/v4';
import { buttonTitle, id } from './fields';
import { FunnelSchema, type Funnel } from './funnel-schema';

// The pieces live in their own files; everything is still imported from here.
export { PLATFORMS, type Platform } from './fields';
export { FunnelSchema, type Funnel };

export const LinkSchema = z.object({
  id,
  title: buttonTitle,
  url: z.url(),
  // Tells the AI when this link is the right one to send.
  when: z.string().optional(),
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
export type Link = z.infer<typeof LinkSchema>;
