import { createFileRoute } from "@tanstack/react-router";
import { guarded } from "@/server/handlers.server";
import { getRuns, postRun, withStudioToken } from "@/server/studio/index.server";

// Production runs for the Studio page (needs the studio token). See src/server/studio/api-runs.server.ts.
export const Route = createFileRoute("/api/studio/runs")({
  server: {
    handlers: {
      GET: ({ request }) => guarded("studio runs", () => withStudioToken(request, getRuns)),
      POST: ({ request }) => guarded("studio runs", () => withStudioToken(request, postRun)),
    },
  },
});
