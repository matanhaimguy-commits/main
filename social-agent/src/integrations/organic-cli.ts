#!/usr/bin/env node
/**
 * Import approved Organic Engine CTAs into the EXISTING Social Agent.
 * Read-only preview by default. --apply writes PAUSED post-pinned funnels only.
 *
 * npm run organic:import -- --file imports/emperium-v24.json --business emperium
 * npm run organic:import -- --file imports/emperium-v24.json --business emperium \
 *   --post V24-01=17812345678901234 --apply
 */
import { readFileSync, writeFileSync, existsSync } from 'node:fs';
import path from 'node:path';
import YAML from 'yaml';
import { PROJECT_ROOT, parseBusiness } from '../config/load.js';
import { planOrganicImport } from './organic.js';

function argument(name: string, args: string[]): string | undefined {
  const at = args.indexOf(name);
  if (at === -1) return undefined;
  const value = args[at + 1];
  if (!value || value.startsWith('--')) throw new Error('Missing value after ' + name);
  return value;
}

function main(args: string[]) {
  const source = argument('--file', args);
  const slug = argument('--business', args);
  if (!source || !slug) {
    throw new Error('Usage: npm run organic:import -- --file FILE --business SLUG [--post VIDEO_ID=META_POST_ID ...] [--base-url https://your-deployed-domain] [--apply]');
  }
  const apply = args.includes('--apply');
  const baseUrl = argument('--base-url', args);
  const postBindings: Record<string, string> = {};
  for (let i = 0; i < args.length; i++) {
    if (args[i] !== '--post') continue;
    const assignment = args[++i];
    const separator = assignment?.indexOf('=');
    if (!assignment || separator === undefined || separator < 1 || separator === assignment.length - 1) throw new Error('Post binding format: --post V24-01=17812345678901234');
    const videoId = assignment.slice(0, separator);
    const postId = assignment.slice(separator + 1);
    if (postBindings[videoId]) throw new Error('Duplicate post binding for ' + videoId);
    postBindings[videoId] = postId;
  }

  const inputFile = path.resolve(PROJECT_ROOT, source);
  const businessFile = path.resolve(PROJECT_ROOT, 'businesses', slug + '.yaml');
  if (!existsSync(inputFile)) throw new Error('Handoff missing: ' + inputFile);
  if (!existsSync(businessFile)) throw new Error('Business config missing: ' + businessFile);
  const handoff = JSON.parse(readFileSync(inputFile, 'utf8'));
  const document = YAML.parseDocument(readFileSync(businessFile, 'utf8'));
  if (document.errors.length) throw new Error('Business YAML invalid: ' + document.errors.join(', '));
  const business = parseBusiness(document.toJS(), businessFile);
  const plan = planOrganicImport(handoff, business, postBindings, baseUrl);

  console.log('Organic Engine -> Social Agent, business: ' + slug);
  console.log('Ready to import (PAUSED, landing page links): ' + plan.additions.length);
  for (const funnel of plan.additions) {
    console.log('  ' + funnel.id + ' | post ' + funnel.posts.join(', ') +
      ' | keyword: ' + funnel.keywords.join(', ') +
      ' | page: ' + funnel.deliver.link);
  }
  console.log('Already imported (unchanged): ' + plan.unchanged.length);
  console.log('Awaiting published post IDs: ' + plan.pending.length);
  for (const p of plan.pending) console.log('  ' + p.videoId + ' | keyword ' + p.keyword);

  if (!apply) {
    console.log('PREVIEW ONLY. No Meta calls and no changes. Use --apply after supplying real post IDs.');
    return;
  }
  if (plan.additions.length === 0) {
    console.log('Nothing to add. Business config unchanged.');
    return;
  }
  // YAML Document keeps the existing business's fields and comments.
  // Existing funnels are preserved. Only the newly pinned, paused funnels are appended.
  document.setIn(['funnels'], plan.business.funnels);
  const rendered = String(document);
  const reparsed = YAML.parse(rendered);
  parseBusiness(reparsed, 'updated ' + slug);
  writeFileSync(businessFile, rendered, 'utf8');
  console.log('Saved ' + plan.additions.length + ' PAUSED funnels to ' + businessFile);
  console.log('Run npm run audit and npm run cli -- preview ' + slug + ' <funnel-id>.');
  console.log('The URL must load publicly on a phone. Activate only after testing the posted Reel and real DM.');
}

try {
  main(process.argv.slice(2));
} catch (error) {
  console.error('Organic import refused: ' + (error as Error).message);
  process.exitCode = 1;
}
