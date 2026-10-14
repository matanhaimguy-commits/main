import { MutationCache, QueryCache, QueryClient } from "@tanstack/react-query";
import { createRouter } from "@tanstack/react-router";
import { routeTree } from "./routeTree.gen";

/** Server functions throw UNAUTHENTICATED when the admin session has expired. */
const isUnauthenticated = (err: unknown) => err instanceof Error && err.message.includes("UNAUTHENTICATED");

function toLogin(err: unknown) {
  if (isUnauthenticated(err) && typeof window !== "undefined" && window.location.pathname !== "/login") {
    window.location.assign("/login");
  }
}

export const getRouter = () => {
  const queryClient = new QueryClient({
    queryCache: new QueryCache({ onError: toLogin }),
    mutationCache: new MutationCache({ onError: toLogin }),
    defaultOptions: {
      queries: {
        retry: (count, err) => !isUnauthenticated(err) && count < 1,
        refetchOnWindowFocus: false,
        staleTime: 5_000,
      },
    },
  });

  const router = createRouter({
    routeTree,
    context: { queryClient },
    scrollRestoration: true,
    defaultPreloadStaleTime: 0,
  });

  return router;
};
