import { createFileRoute } from "@tanstack/react-router";
import { connectCallback, guarded } from "@/server/handlers.server";

// Meta sends the admin back here after login. Add this URL to Facebook Login → Valid OAuth Redirect URIs.
export const Route = createFileRoute("/api/connect/callback")({
  server: {
    handlers: {
      GET: ({ request }) => guarded("connect callback", () => connectCallback(request)),
    },
  },
});
