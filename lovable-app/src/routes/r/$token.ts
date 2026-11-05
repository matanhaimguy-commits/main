import { createFileRoute } from "@tanstack/react-router";
import { guarded, linkRedirect } from "@/server/handlers.server";

// Tracked links (only for businesses with track_clicks on).
export const Route = createFileRoute("/r/$token")({
  server: {
    handlers: {
      GET: ({ params }) => guarded("tracked link", () => linkRedirect(params.token)),
    },
  },
});
