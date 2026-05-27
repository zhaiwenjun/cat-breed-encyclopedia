import { defineConfig } from 'astro/config';

import cloudflare from "@astrojs/cloudflare";

export default defineConfig({
  site: 'https://catbreedencyclopedia.com',
  output: 'static',

  build: {
    assets: 'assets',
  },

  trailingSlash: 'always',
  adapter: cloudflare()
});