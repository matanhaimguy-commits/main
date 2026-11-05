import "@tanstack/react-start/server-only";
import { z } from "zod/v4";
import { getDb } from "./db.server";
import {
  checkStudioToken,
  clientsForStudio,
  ContentError,
  FunnelUpsertInput,
  ItemInput,
  itemResults,
  listItems,
  signedUpload,
  UploadInput,
  upsertFunnel,
  upsertItem,
} from "./content.server";

/** /api/content/* for the studio. Every call needs `Authorization: Bearer <studio token>`. */

const json = (body: unknown, status = 200) =>
  new Response(JSON.stringify(body), { status, headers: { "content-type": "application/json; charset=utf-8" } });

type Endpoint = "clients" | "items" | "upload" | "funnels" | "results";

export async function contentApi(request: Request, endpoint: Endpoint): Promise<Response> {
  const sql = getDb();
  if (!(await checkStudioToken(sql, request))) return json({ error: "Missing or wrong studio token." }, 401);
  const url = new URL(request.url);
  try {
    if (request.method === "GET") {
      switch (endpoint) {
        case "clients":
          return json({ clients: await clientsForStudio(sql) });
        case "items":
          return json({
            items: await listItems(sql, {
              business: url.searchParams.get("business") ?? undefined,
              status: url.searchParams.get("status") ?? undefined,
              limit: Math.min(500, Number(url.searchParams.get("limit") ?? 200) || 200),
            }),
          });
        case "results": {
          const business = url.searchParams.get("business");
          if (!business) return json({ error: "Add ?business=<slug>." }, 400);
          const days = Math.min(120, Math.max(1, Number(url.searchParams.get("days") ?? 30) || 30));
          return json({ results: await itemResults(sql, business, days) });
        }
        default:
          return json({ error: "Use POST." }, 405);
      }
    }
    if (request.method !== "POST") return json({ error: "Method not allowed." }, 405);
    const body = await request.json().catch(() => null);
    switch (endpoint) {
      case "items": {
        const many = z.object({ items: z.array(ItemInput).min(1).max(30) }).safeParse(body);
        if (many.success) {
          const saved = [];
          for (const item of many.data.items) saved.push(await upsertItem(sql, item));
          return json({ items: saved });
        }
        const one = ItemInput.safeParse(body);
        if (!one.success) return json({ error: "Invalid item.", details: z.prettifyError(one.error) }, 400);
        return json({ item: await upsertItem(sql, one.data) });
      }
      case "upload": {
        const input = UploadInput.safeParse(body);
        if (!input.success) return json({ error: "Invalid upload request.", details: z.prettifyError(input.error) }, 400);
        return json(await signedUpload(input.data));
      }
      case "funnels": {
        const input = FunnelUpsertInput.safeParse(body);
        if (!input.success) return json({ error: "Invalid funnel request.", details: z.prettifyError(input.error) }, 400);
        const res = await upsertFunnel(sql, input.data);
        return json(res, res.ok ? 200 : 422);
      }
      default:
        return json({ error: "Use GET." }, 405);
    }
  } catch (err) {
    if (err instanceof ContentError) return json({ error: err.message }, err.status);
    throw err;
  }
}
