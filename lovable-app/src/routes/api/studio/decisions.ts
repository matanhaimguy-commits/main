import { createFileRoute } from "@tanstack/react-router";
import { guarded } from "@/server/handlers.server";
import { getDecisions, postDecisions, withStudioToken } from "@/server/studio/index.server";

// The owner's checkpoints: the studio asks and reads the answers (needs the studio token).
// See src/server/studio/api-decisions.server.ts.
export const Route = createFileRoute("/api/studio/decisions")({
  server: {
    handlers: {
      GET: ({ request }) => guarded("studio decisions", () => withStudioToken(request, getDecisions)),
      POST: ({ request }) => guarded("studio decisions", () => withStudioToken(request, postDecisions)),
    },
  },
});
