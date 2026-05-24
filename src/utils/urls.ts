import { siteConfig } from '@data/siteConfig';

export function canonicalURL(path: string): string {
  const normalized = path.endsWith('/') ? path : `${path}/`;
  return `${siteConfig.url}${normalized}`;
}

export function breedURL(slug: string): string {
  return canonicalURL(`breeds/${slug}`);
}

export function categoryURL(slug: string): string {
  return canonicalURL(`categories/${slug}`);
}