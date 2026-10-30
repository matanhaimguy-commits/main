import { createCipheriv, createDecipheriv, createHash, randomBytes } from 'node:crypto';
import type { Sql } from './sql';

// ---- token encryption -------------------------------------------------------------

function key(secret: string): Buffer {
  return createHash('sha256').update(`social-agent:page-tokens:${secret}`).digest();
}

export function encryptToken(token: string, secret: string): string {
  const iv = randomBytes(12);
  const cipher = createCipheriv('aes-256-gcm', key(secret), iv);
  const enc = Buffer.concat([cipher.update(token, 'utf8'), cipher.final()]);
  return [iv, cipher.getAuthTag(), enc].map((b) => b.toString('base64url')).join('.');
}

/** Returns undefined when the secret changed (the Page must be connected again). */
export function decryptToken(blob: string, secret: string): string | undefined {
  try {
    const [iv, tag, enc] = blob.split('.').map((p) => Buffer.from(p, 'base64url'));
    const decipher = createDecipheriv('aes-256-gcm', key(secret), iv!);
    decipher.setAuthTag(tag!);
    return Buffer.concat([decipher.update(enc!), decipher.final()]).toString('utf8');
  } catch {
    return undefined;
  }
}

// ---- connections --------------------------------------------------------------------

export interface Connection {
  page_id: string;
  page_name: string;
  instagram_id: string | null;
  instagram_username: string | null;
  business: string | null;
  token_enc: string;
  subscribed_at: Date | null;
  connected_at: Date;
}

export async function listConnections(sql: Sql): Promise<Connection[]> {
  return sql<Connection[]>`SELECT * FROM meta_connections ORDER BY page_name`;
}

export async function upsertConnection(
  sql: Sql,
  c: { pageId: string; pageName: string; instagramId?: string; instagramUsername?: string; tokenEnc: string },
) {
  await sql`
    INSERT INTO meta_connections (page_id, page_name, instagram_id, instagram_username, token_enc)
    VALUES (${c.pageId}, ${c.pageName}, ${c.instagramId ?? null}, ${c.instagramUsername ?? null}, ${c.tokenEnc})
    ON CONFLICT (page_id) DO UPDATE SET page_name = EXCLUDED.page_name, instagram_id = EXCLUDED.instagram_id,
      instagram_username = EXCLUDED.instagram_username, token_enc = EXCLUDED.token_enc, updated_at = now()`;
}

/** Points a Page at a business (or at none). One Page per business. */
export async function assignConnection(sql: Sql, pageId: string, business: string | null) {
  await sql.begin(async (tx) => {
    if (business) await tx`UPDATE meta_connections SET business = NULL WHERE business = ${business} AND page_id <> ${pageId}`;
    await tx`UPDATE meta_connections SET business = ${business}, updated_at = now() WHERE page_id = ${pageId}`;
  });
}

export async function markSubscribed(sql: Sql, pageId: string) {
  await sql`UPDATE meta_connections SET subscribed_at = now() WHERE page_id = ${pageId}`;
}

export async function deleteConnection(sql: Sql, pageId: string) {
  await sql`DELETE FROM meta_connections WHERE page_id = ${pageId}`;
}

// ---- app state ----------------------------------------------------------------------

export async function setState(sql: Sql, key: string, value: unknown) {
  await sql`INSERT INTO app_state (key, value) VALUES (${key}, ${sql.json(value as any)})
    ON CONFLICT (key) DO UPDATE SET value = EXCLUDED.value, updated_at = now()`;
}

export async function getState<T = any>(sql: Sql, key: string): Promise<{ value: T; updated_at: Date } | undefined> {
  const [row] = await sql<{ value: T; updated_at: Date }[]>`SELECT value, updated_at FROM app_state WHERE key = ${key}`;
  return row;
}
