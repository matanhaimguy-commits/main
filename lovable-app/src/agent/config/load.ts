import YAML from 'yaml';
import { BusinessSchema, type Business, type Platform } from './schema';

export class ConfigError extends Error {
  constructor(public readonly problems: string[]) {
    super(`Invalid business config:\n  - ${problems.join('\n  - ')}`);
  }
}

export function parseBusiness(raw: unknown, source: string): Business {
  const result = BusinessSchema.safeParse(raw);
  if (!result.success) {
    throw new ConfigError(
      result.error.issues.map((i) => `${source}: ${i.path.join('.') || '(root)'}: ${i.message}`),
    );
  }
  return result.data;
}

/** Reads YAML text as a plain object, with a readable error. */
export function yamlToRaw(text: string, source = 'business'): unknown {
  try {
    return YAML.parse(text);
  } catch (err) {
    throw new ConfigError([`${source}: not valid YAML: ${(err as Error).message}`]);
  }
}

/** Parses a business written as YAML (the dashboard's editor and imported files). */
export function parseBusinessYaml(text: string, source = 'business'): Business {
  return parseBusiness(yamlToRaw(text, source), source);
}

export function businessToYaml(raw: unknown): string {
  return YAML.stringify(raw, { lineWidth: 0 });
}

/** The parts of a connected Page (from the Connect page) the registry needs. */
export interface ConnectedPage {
  page_id: string;
  instagram_id: string | null;
  business: string | null;
}

export interface Registry {
  readonly businesses: readonly Business[];
  bySlug(slug: string): Business | undefined;
  /** Finds the business that owns a Page ID (facebook) or Instagram account ID (instagram). */
  byAccount(platform: Platform, accountId: string): Business | undefined;
  /** Re-applies connected Pages, e.g. right after someone connects one. */
  refresh(pages: ConnectedPage[]): void;
}

/**
 * IDs written in a business file win. Otherwise the business gets the Page that was
 * assigned to it on the Connect page (and that Page's linked Instagram account).
 */
export function withConnectedPage(b: Business, pages: ConnectedPage[], claimedByFiles: Set<string>): Business {
  const filePage = b.meta.page_id;
  const page = filePage
    ? pages.find((p) => p.page_id === filePage)
    : pages.find((p) => p.business === b.slug && !claimedByFiles.has(p.page_id));
  if (!page) return b;
  return {
    ...b,
    meta: { ...b.meta, page_id: page.page_id, instagram_id: b.meta.instagram_id ?? page.instagram_id ?? undefined },
  };
}

export function buildRegistry(base: Business[], pages: ConnectedPage[] = []): Registry {
  let businesses: Business[] = [];
  let slugs = new Map<string, Business>();
  let accounts = new Map<string, Business>();

  const apply = (connected: ConnectedPage[]) => {
    const claimedByFiles = new Set(base.map((b) => b.meta.page_id).filter((id): id is string => !!id));
    const effective = base.map((b) => withConnectedPage(b, connected, claimedByFiles));
    const problems: string[] = [];
    const nextSlugs = new Map<string, Business>();
    const nextAccounts = new Map<string, Business>();
    for (const b of effective) {
      if (nextSlugs.has(b.slug)) problems.push(`duplicate business slug "${b.slug}"`);
      nextSlugs.set(b.slug, b);
      const keys: string[] = [];
      if (b.meta.page_id) keys.push(`facebook:${b.meta.page_id}`);
      if (b.meta.instagram_id) keys.push(`instagram:${b.meta.instagram_id}`);
      for (const key of keys) {
        const owner = nextAccounts.get(key);
        if (owner) problems.push(`${key} is claimed by both "${owner.slug}" and "${b.slug}"`);
        nextAccounts.set(key, b);
      }
    }
    if (problems.length) throw new ConfigError(problems);
    businesses = effective;
    slugs = nextSlugs;
    accounts = nextAccounts;
  };
  apply(pages);

  return {
    get businesses() {
      return businesses;
    },
    bySlug: (slug) => slugs.get(slug),
    byAccount: (platform, accountId) => accounts.get(`${platform}:${accountId}`),
    refresh: apply,
  };
}
