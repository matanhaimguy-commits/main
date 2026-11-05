<!-- LOVABLE:BEGIN -->
> [!IMPORTANT]
> This project is connected to [Lovable](https://lovable.dev). Avoid rewriting
> published git history — force pushing, or rebasing/amending/squashing commits
> that are already pushed — as it rewrites history on Lovable's side and the
> user will likely lose their project history.
>
> Commits you push to the connected branch sync back to Lovable and show up in
> the editor, so keep the branch in a working state.
<!-- LOVABLE:END -->

# Working on this project

Read README.md first. In short:

- The backend lives in this app: `src/agent/` (engine), `src/server/` (server-only glue),
  `src/routes/api/` (Meta webhook, scheduled tick, Facebook login). Do not move it into
  Supabase edge functions.
- All database access goes through `src/agent/db/sql.ts` (the `agent_sql()` function over REST
  with the service-role key). Do not add the Supabase JS client for server code, and never
  query these tables from the browser: every table has RLS on with no policies.
- Schema changes go in a new file under `supabase/migrations/` and must be applied to the
  database by hand; they are not applied automatically.
- Never commit tokens or keys. Secrets live in the dashboard Settings (encrypted) or in
  Lovable Cloud → Secrets.
- Real messages to customers are off by default (dry run). Do not change that default.
- Before pushing: `npx tsc --noEmit -p .`, `bun run test`, `bun run build`.
