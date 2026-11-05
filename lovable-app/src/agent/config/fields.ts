import { z } from 'zod/v4';

export const PLATFORMS = ['instagram', 'facebook'] as const;
export type Platform = (typeof PLATFORMS)[number];

/** A slug used as a business, funnel or link id. */
export const id = z.string().regex(/^[a-z0-9][a-z0-9_-]*$/, 'use lowercase letters, digits, - and _');

// Meta caps button titles at 20 characters and button-template text at 640.
export const buttonTitle = z.string().min(1).max(20);
export const buttonText = z.string().min(1).max(640);
