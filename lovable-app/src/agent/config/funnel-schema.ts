import { z } from 'zod/v4';
import { AFTER_DELAY_MAX_MINUTES } from '../logic/after-delay';
import { buttonText, buttonTitle, id, PLATFORMS } from './fields';

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
  // Minutes to wait after the delivery before sending `after`. 0 (the default) sends it right away.
  // A delayed message is queued and sent by the scheduled tick, only if the person has not written
  // back and the 24h messaging window is still open.
  after_delay_minutes: z
    .number()
    .int('use whole minutes')
    .min(0, 'must be 0 or more')
    .max(AFTER_DELAY_MAX_MINUTES, `must be ${AFTER_DELAY_MAX_MINUTES} or less`)
    .default(0),
});

export type Funnel = z.infer<typeof FunnelSchema>;
