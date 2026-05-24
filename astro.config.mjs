import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://catbreedencyclopedia.com',
  output: 'static',
  build: {
    assets: 'assets',
  },
  trailingSlash: 'always',
});