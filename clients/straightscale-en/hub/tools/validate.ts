// Validates profile.en.json with the hub's own zod schema and placeholder audit.
// Run from the repo root: bun clients/straightscale-en/hub/tools/validate.ts
import { readFileSync } from 'node:fs';
import { BusinessSchema } from '../../../../lovable-app/src/agent/config/schema';
import { hasPlaceholders } from '../../../../lovable-app/src/agent/logic/audit';

const path = new URL('../profile.en.json', import.meta.url);
const profile = JSON.parse(readFileSync(path, 'utf8'));

const result = BusinessSchema.shape.profile.safeParse(profile);
if (!result.success) {
  console.error('FAIL: profile does not match the schema');
  console.error(JSON.stringify(result.error.issues, null, 2));
  process.exit(1);
}
const unknown = Object.keys(profile).filter((k) => !(k in BusinessSchema.shape.profile.shape));
if (unknown.length) {
  console.error(`FAIL: keys the schema would drop: ${unknown.join(', ')}`);
  process.exit(1);
}
const business = BusinessSchema.parse({ slug: 'straightscale-en-draft', name: 'StraightScale', profile });
const todos = hasPlaceholders(business);
console.log(`PASS: profile matches BusinessSchema.profile (${Object.keys(profile).length} fields, ${business.profile.faq.length} FAQ)`);
console.log(`Placeholders the audit would block live sending on (${todos.length}):`);
for (const t of todos) console.log(`  - ${t}`);
