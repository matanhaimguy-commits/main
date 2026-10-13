import { readdirSync, readFileSync, existsSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import YAML from 'yaml';
import { BusinessSchema, type Business, type Platform } from './schema.js';

// src/config and dist/config both sit two levels below the project root.
export const PROJECT_ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
export const DEFAULT_BUSINESSES_DIR = path.join(PROJECT_ROOT, 'businesses');

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

/** Loads every businesses/*.yaml (files starting with "_" are templates and are skipped). */
export function loadBusinesses(dir: string = DEFAULT_BUSINESSES_DIR): Business[] {
  if (!existsSync(dir)) return [];
  const files = readdirSync(dir)
    .filter((f) => /\.ya?ml$/.test(f) && !f.startsWith('_'))
    .sort();
  const problems: string[] = [];
  const businesses: Business[] = [];
  for (const file of files) {
    try {
      const raw = YAML.parse(readFileSync(path.join(dir, file), 'utf8'));
      businesses.push(parseBusiness(raw, file));
    } catch (err) {
      if (err instanceof ConfigError) problems.push(...err.problems);
      else problems.push(`${file}: ${(err as Error).message}`);
    }
  }
  if (problems.length) throw new ConfigError(problems);
  return businesses;
}

export interface Registry {
  readonly businesses: readonly Business[];
  bySlug(slug: string): Business | undefined;
  /** Finds the business that owns a Page ID (facebook) or Instagram account ID (instagram). */
  byAccount(platform: Platform, accountId: string): Business | undefined;
}

export function buildRegistry(businesses: Business[]): Registry {
  const problems: string[] = [];
  const slugs = new Map<string, Business>();
  const accounts = new Map<string, Business>();
  for (const b of businesses) {
    if (slugs.has(b.slug)) problems.push(`duplicate business slug "${b.slug}"`);
    slugs.set(b.slug, b);
    const keys = [`facebook:${b.meta.page_id}`];
    if (b.meta.instagram_id) keys.push(`instagram:${b.meta.instagram_id}`);
    for (const key of keys) {
      const owner = accounts.get(key);
      if (owner) problems.push(`${key} is claimed by both "${owner.slug}" and "${b.slug}"`);
      accounts.set(key, b);
    }
  }
  if (problems.length) throw new ConfigError(problems);
  return {
    businesses,
    bySlug: (slug) => slugs.get(slug),
    byAccount: (platform, accountId) => accounts.get(`${platform}:${accountId}`),
  };
}

export function loadRegistry(dir?: string): Registry {
  return buildRegistry(loadBusinesses(dir));
}
