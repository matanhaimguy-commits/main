/**
 * A new business as created from the dashboard. Fields marked TODO must be filled in:
 * the audit blocks real sending while any TODO is left.
 */
export function starterBusiness(slug: string, name: string): Record<string, unknown> {
  return {
    slug,
    name,
    enabled: true,
    live: false,
    testers: [],
    timezone: 'Asia/Jerusalem',
    profile: {
      about: 'TODO: who the business is and what it does, in two or three sentences.',
      offers: 'TODO: each service or product, what is included, and the price (or "price on a call").',
      audience: 'TODO: who the ideal customer is.',
      goal: 'TODO: the one next step every conversation should lead to, e.g. book a free call',
      qualifying_questions: ['TODO: e.g. What does your business sell, and where?'],
      faq: [],
      voice: 'Friendly and to the point, like the owner answering their own DMs. Hebrew is informal. At most one emoji per message.',
      never: ['Promise results, discounts or deadlines that are not written here.'],
    },
    links: [],
    ai: { enabled: true, dm_replies: true, comment_replies: false, comment_dms: false },
    funnels: [],
  };
}

/** A starting point for a new comment-to-DM funnel in the editor. */
export function starterFunnel(id: string): Record<string, unknown> {
  return {
    id,
    status: 'active',
    trigger: 'comment',
    platforms: ['instagram', 'facebook'],
    posts: [],
    keywords: ['guide'],
    match: 'word',
    public_replies: ['Sent you a DM 🙌'],
    opener: { text: "Here it is 👇 Tap and it's yours.", button: 'Send it to me', mode: 'tap' },
    deliver: { text: 'Enjoy 🎁', link: '', button: 'Open it' },
    after: 'Questions? Just reply here 🙂',
  };
}
