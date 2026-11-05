const SAFE_HREF = /^(https?:\/\/|mailto:|#|\/(?!\/))/i;

/** The link if it opens a web page, an email, a place on this page or a path on this site; null otherwise. */
export const safeHref = (href: string): string | null => (SAFE_HREF.test(href.trim()) ? href.trim() : null);
