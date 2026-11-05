import type { Business } from '../config/schema';
import type { Deps } from './deps';

/**
 * Leads from the public form at /l/<slug>. The form works for everyone: it does not depend on what Meta lets the
 * app receive, so it is where a comment reply or an Instagram instant reply sends people until (and after) the app
 * has Advanced Access. A lead is a contact on the "web" channel, keyed by phone number, so sending twice updates
 * the same person. The AI never messages these contacts (there is no Meta thread); a person calls them.
 */
export interface LeadInput {
  name: string;
  phone: string;
  instagram?: string;
  need?: string;
  /** "How did you hear about us?": software misses DMs and word of mouth, so we ask (Organic OS 9.2). */
  heard?: string;
  source?: string;
}

export class LeadError extends Error {}

const MAX_PER_HOUR = 30;
export const normalizePhone = (p: string) => p.replace(/[^\d+]/g, '').replace(/(?!^)\+/g, '');

export async function submitLead(deps: Pick<Deps, 'sql' | 'alert'>, b: Business, input: LeadInput): Promise<{ contactId: number; repeat: boolean }> {
  const phone = normalizePhone(input.phone);
  const digits = phone.replace(/\D/g, '');
  if (digits.length < 6 || digits.length > 16) throw new LeadError('phone');
  const name = input.name.trim().slice(0, 80);
  if (!name) throw new LeadError('name');
  const ig = input.instagram?.trim().replace(/^@/, '').slice(0, 40) || null;
  const need = input.need?.trim().slice(0, 600) || null;
  const heard = input.heard?.trim().slice(0, 200) || null;
  const notes = [need, heard ? `Heard about us: ${heard}` : null].filter(Boolean).join('\n') || null;
  const source = `form${input.source ? `:${input.source.replace(/[^\w-]/g, '').slice(0, 40)}` : ''}`;

  const [recent] = await deps.sql<{ n: number }[]>`
    SELECT count(*)::int AS n FROM contacts
    WHERE business = ${b.slug} AND platform = 'web' AND updated_at > now() - interval '1 hour'`;
  if (recent!.n >= MAX_PER_HOUR) throw new LeadError('busy');

  const [row] = await deps.sql<{ id: number; repeat: boolean }[]>`
    INSERT INTO contacts (business, platform, external_id, name, phone, username, source, stage, notes, last_inbound_at)
    VALUES (${b.slug}, 'web', ${`tel:${digits}`}, ${name}, ${phone}, ${ig}, ${source}, 'qualified', ${notes}, now())
    ON CONFLICT (business, platform, external_id) DO UPDATE SET
      name = EXCLUDED.name,
      username = COALESCE(EXCLUDED.username, contacts.username),
      stage = CASE WHEN contacts.stage IN ('new', 'engaged') THEN 'qualified' ELSE contacts.stage END,
      notes = CASE WHEN EXCLUDED.notes IS NULL THEN contacts.notes
                   WHEN contacts.notes IS NULL THEN EXCLUDED.notes
                   ELSE contacts.notes || E'\n' || EXCLUDED.notes END,
      last_inbound_at = now(), updated_at = now()
    RETURNING id, (xmax <> 0) AS repeat`;
  const text = [`Formulari: ${name}, ${phone}`, ig ? `Instagram @${ig}` : null, need, heard ? `Na gjeti nga: ${heard}` : null].filter(Boolean).join('\n');
  await deps.sql`INSERT INTO messages (contact_id, direction, source, text, payload)
    VALUES (${row!.id}, 'in', 'user', ${text}, ${deps.sql.json({ form: { name, phone, instagram: ig, need, heard, source } })})`;
  await deps.alert({
    key: `lead:${row!.id}:${Date.now()}`,
    text: `📝 ${b.name}: ${row!.repeat ? 'returning' : 'new'} lead from the form: ${name}, ${phone}${ig ? `, @${ig}` : ''}${need ? `\n“${need}”` : ''}${heard ? `\nHeard about us: ${heard}` : ''}`,
    cooldownMinutes: 0,
  });
  return { contactId: row!.id, repeat: row!.repeat };
}
