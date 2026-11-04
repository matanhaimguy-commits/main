import { describe, expect, it } from 'vitest';
import { readFileSync } from 'node:fs';
import YAML from 'yaml';
import { parseBusiness } from '../src/config/load.js';
import { FunnelSchema } from '../src/config/schema.js';
import { auditBusiness } from '../src/logic/audit.js';
import { OrganicHandoffSchema, planOrganicImport } from '../src/integrations/organic.js';
import { renderResourcePage, resourceRoutes } from '../src/resources.js';

const bundle = JSON.parse(readFileSync(new URL('../imports/emperium-v24.json', import.meta.url), 'utf8'));
const business = parseBusiness(
  YAML.parse(readFileSync(new URL('../businesses/emperium.yaml', import.meta.url), 'utf8')),
  'emperium.yaml',
);
const origin = 'https://public.example.org/';

describe('Organic Engine to existing Social Agent landing pages', () => {
  it('reads all six approved assets, with no live activation', () => {
    expect(OrganicHandoffSchema.parse(bundle).flows).toHaveLength(6);
    const plan = planOrganicImport(bundle, business);
    expect(plan.additions).toHaveLength(0);
    expect(plan.pending).toHaveLength(6);
    expect(plan.pending.map((p) => p.keyword)).toEqual([
      'מודעות', 'מילים', 'הצעה', 'שפינדורה', 'רווח', 'כבוד',
    ]);
  });

  it('renders all six open, mobile-friendly RTL pages with their real content', async () => {
    const app = resourceRoutes();
    for (const flow of bundle.flows) {
      const res = await app.request('/emperium/' + flow.source_video_id);
      expect(res.status).toBe(200);
      const body = await res.text();
      expect(body).toContain('lang="he" dir="rtl"');
      expect(body).toContain('name="viewport"');
      expect(body).toContain('data-target="prompt-0"');
      expect(body).toContain('איך משתמשים בזה');
      expect(body).toContain('פתח ChatGPT');
      expect(body).toContain('navigator.clipboard.writeText');
    }
    expect(await (await app.request('/emperium/V24-00')).text()).toBe('Resource not found');
    expect((await app.request('/unknown/V24-01')).status).toBe(404);
  });

  it('shows the revenue calculator AND its follow-up prompt', () => {
    const revenue = renderResourcePage('emperium', 'V24-05')!;
    expect(revenue).toContain('prompt-0');
    expect(revenue).toContain('prompt-1');
    expect(revenue).toContain('כמה כסף');
    expect(revenue).toContain('פרסום');
  });

  it('includes the additional guide and the seven social responses', () => {
    const angles = renderResourcePage('emperium', 'V24-04')!;
    expect(angles).toContain('בחר');
    expect(angles).toContain('שמונה זוויות');
    const boundary = renderResourcePage('emperium', 'V24-06')!;
    expect(boundary).toContain('לצחוק על אחרים');
  });

  it('imports only bound published reels, and uses existing link-button delivery', () => {
    const post = '17812345678901234';
    const plan = planOrganicImport(bundle, business, { 'V24-01': post }, origin);
    expect(plan.additions).toHaveLength(1);
    expect(plan.pending).toHaveLength(5);
    const f = plan.additions[0]!;
    expect(f.id).toBe('oe-v24-01');
    expect(f.status).toBe('paused');
    expect(f.posts).toEqual([post]);
    expect(f.keywords).toEqual(['מודעות']);
    expect(f.opener.mode).toBe('tap');
    expect(f.deliver.link).toBe('https://public.example.org/resources/emperium/V24-01');
    expect(f.deliver.button).toBe('פתח את המדריך');
    expect(FunnelSchema.safeParse(f).success).toBe(true);
    expect(auditBusiness(plan.business, { hasToken: false }).filter((x) => x.level === 'error')).toEqual([]);
  });

  it('does not overwrite an existing funnel; repeated imports are idempotent', () => {
    const bindings = { 'V24-02': '17812345678901235' };
    const first = planOrganicImport(bundle, business, bindings, origin);
    const second = planOrganicImport(bundle, first.business, bindings, origin);
    expect(second.additions).toHaveLength(0);
    expect(second.unchanged).toEqual(['oe-v24-02']);
    const invalid = structuredClone(bundle);
    invalid.flows[1].trigger.keyword = 'אחר';
    expect(() => planOrganicImport(invalid, first.business, bindings, origin)).toThrow(/different settings/);
  });

  it('refuses missing real hosting, wrong post IDs and competing funnel keywords', () => {
    expect(() => planOrganicImport(bundle, business, { 'V24-01': '17812345678901234' }))
      .toThrow(/base-url/);
    expect(() => planOrganicImport(bundle, business, { 'V24-01': 'fake' }, origin))
      .toThrow(/Invalid real Meta post ID/);
    expect(() => planOrganicImport(bundle, business, { 'V24-01': '17812345678901234' }, 'http://host'))
      .toThrow(/HTTPS/);
    const competitor = {
      id: 'existing', status: 'active', trigger: 'comment', platforms: ['instagram'],
      posts: ['17812345678901234'], keywords: ['מודעות'], match: 'word',
      opener: { text: 'היי', button: 'שלח לי', mode: 'tap' },
      deliver: { text: 'קישור', link: 'https://example.org/offer', button: 'פתח' },
    };
    const withExisting = parseBusiness({ ...business, funnels: [competitor] }, 'existing');
    expect(() => planOrganicImport(bundle, withExisting, { 'V24-01': '17812345678901234' }, origin))
      .toThrow(/Keyword collision/);
  });
});
