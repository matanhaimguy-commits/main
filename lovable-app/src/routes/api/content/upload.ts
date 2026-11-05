import { createFileRoute } from "@tanstack/react-router";
import { contentApi } from "@/server/content-api.server";
import { guarded } from "@/server/handlers.server";

// Growth Engine studio API (needs the studio token). See src/server/content-api.server.ts.
export const Route = createFileRoute("/api/content/upload")({
  server: {
    handlers: {
      POST: ({ request }) => guarded("content upload", () => contentApi(request, "upload")),
    },
  },
});
