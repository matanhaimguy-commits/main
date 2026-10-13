import { parseBusiness } from '../src/config/load.js';
import type { Business } from '../src/config/schema.js';

export const PAGE_ID = '111111111111111';
export const IG_ID = '17841400000000001';
export const APP_SECRET = 'test-app-secret';
export const VERIFY_TOKEN = 'test-verify-token';

export function makeBusiness(overrides: Record<string, unknown> = {}): Business {
  return parseBusiness(
    {
      slug: 'acme',
      name: 'Acme Studio',
      live: true,
      meta: { page_id: PAGE_ID, instagram_id: IG_ID, page_token_env: 'PAGE_TOKEN_ACME' },
      profile: {
        about: 'Acme Studio runs paid social campaigns for e-commerce brands in Israel and Europe.',
        offers: 'Ads management from 4,000 ILS per month. Free 20-minute strategy call.',
        goal: 'Book a free strategy call',
      },
      links: [
        { id: 'guide_pdf', title: 'Open the guide', url: 'https://acme.studio/guide.pdf' },
        { id: 'book_call', title: 'Book a call', url: 'https://cal.com/acme/strategy', when: 'qualified lead' },
      ],
      funnels: [
        {
          id: 'guide-reel',
          posts: [`${PAGE_ID}_POST_A`, 'MEDIA_A'],
          keywords: ['guide', 'מדריך'],
          public_replies: ['Sent you a DM 🙌'],
          opener: { text: 'Here is the guide you asked for 👇', button: 'Send it to me' },
          deliver: { text: 'Enjoy the guide!', link: 'guide_pdf', button: 'Open the guide' },
          after: 'Stuck or have a question? Just reply here.',
        },
      ],
      ...overrides,
    },
    'test',
  );
}
