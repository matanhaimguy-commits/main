import { createFileRoute } from "@tanstack/react-router";
import { guarded } from "@/server/handlers.server";
import { postSynced, withStudioToken } from "@/server/studio/index.server";

// The studio took these answers in (needs the studio token). See src/server/studio/api-synced.server.ts.
export const Route = createFileRoute("/api/studio/synced")({
  server: {
    handlers: {
      POST: ({ request }) => guarded("studio synced", () => withStudioToken(request, postSynced)),
    },
  },
});
