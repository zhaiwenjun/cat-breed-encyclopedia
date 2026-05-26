import fs from 'fs';
import path from 'path';
import https from 'https';
import http from 'http';

const IMAGES_DIR = path.resolve('public/images/breeds');

function fetchJSON(url) {
  return new Promise((resolve, reject) => {
    const mod = url.startsWith('https') ? https : http;
    mod.get(url, { headers: { 'Accept': 'application/json' } }, res => {
      let data = '';
      res.on('data', c => data += c);
      res.on('end', () => { try { resolve(JSON.parse(data)); } catch(e) { reject(e); } });
    }).on('error', reject);
  });
}

function download(url, dest) {
  return new Promise((resolve, reject) => {
    const mod = url.startsWith('https') ? https : http;
    const follow = (u) => {
      mod.get(u, res => {
        if (res.statusCode >= 300 && res.statusCode < 400 && res.headers.location) {
          return follow(res.headers.location);
        }
        if (res.statusCode !== 200) return reject(new Error(`HTTP ${res.statusCode}`));
        const s = fs.createWriteStream(dest);
        res.pipe(s);
        s.on('finish', () => { s.close(); resolve(); });
        s.on('error', reject);
      }).on('error', reject);
    };
    follow(url);
  });
}

const sleep = ms => new Promise(r => setTimeout(r, ms));

// Aliases for breeds named differently in Cat API
const ALIASES = {
  'don-sphynx': 'donskoy',
  'minuet': 'napoleon',
  'norwegian-forest-cat': 'norwegian forest',
  'scottish-straight': 'scottish fold',
  'oriental-longhair': 'oriental shorthair',
  'tonkinese-longhair': 'tonkinese',
  'chantilly-tiffany': 'tiffany',
  'colorpoint-shorthair': 'colorpoint shorthair',
};

async function main() {
  const slugs = fs.readdirSync('src/content/breeds')
    .filter(f => f.endsWith('.md'))
    .map(f => f.replace('.md', ''));

  console.log(`Downloading images for ${slugs.length} breeds...\n`);

  // Fetch Cat API breed list
  let apiBreeds;
  try {
    apiBreeds = await fetchJSON('https://api.thecatapi.com/v1/breeds');
    console.log(`Cat API: ${apiBreeds.length} breeds available\n`);
  } catch(e) {
    console.error('Cannot reach Cat API:', e.message);
    process.exit(1);
  }

  // Build lookup by normalized name
  const byName = {};
  for (const b of apiBreeds) {
    byName[b.name.toLowerCase().replace(/[^a-z0-9]/g, '')] = b;
  }

  if (!fs.existsSync(IMAGES_DIR)) fs.mkdirSync(IMAGES_DIR, { recursive: true });

  let ok = 0, fail = 0;

  for (const slug of slugs) {
    const dest = path.join(IMAGES_DIR, `${slug}.jpg`);

    // Skip if valid image already exists
    if (fs.existsSync(dest) && fs.statSync(dest).size > 2000) {
      console.log(`  SKIP ${slug}`);
      ok++;
      continue;
    }

    // Find API breed by slug or alias
    const lookupKey = slug.replace(/-/g, '');
    const aliasKey = (ALIASES[slug] || '').replace(/[^a-z0-9]/g, '');
    let breed = byName[lookupKey] || byName[aliasKey];

    let url = null;

    // Direct image from breed data (no API call needed)
    if (breed?.image?.url) {
      url = breed.image.url;
    } else if (breed?.reference_image_id) {
      url = `https://cdn2.thecatapi.com/images/${breed.reference_image_id}.jpg`;
    }

    // Search API for breed-specific image
    if (!url && breed) {
      try {
        const r = await fetchJSON(`https://api.thecatapi.com/v1/images/search?breed_ids=${breed.id}&limit=1`);
        if (r[0]?.url) url = r[0].url;
      } catch(e) {}
      await sleep(600);
    }

    // Fallback: random cat image
    if (!url) {
      try {
        const r = await fetchJSON('https://api.thecatapi.com/v1/images/search?limit=1');
        if (r[0]?.url) url = r[0].url;
      } catch(e) {}
      await sleep(600);
    }

    if (!url) { console.log(`  FAIL ${slug} - no image available`); fail++; continue; }

    // Download the image
    try {
      await download(url, dest);
      if (fs.statSync(dest).size < 500) throw new Error('file too small');
      ok++;
      console.log(`  OK   ${slug}`);
    } catch(e) {
      if (fs.existsSync(dest)) fs.unlinkSync(dest);
      console.log(`  FAIL ${slug}: ${e.message}`);
      fail++;
    }
    await sleep(200);
  }

  // Default image
  try {
    const r = await fetchJSON('https://api.thecatapi.com/v1/images/search?limit=1');
    if (r[0]?.url) {
      await download(r[0].url, path.join(IMAGES_DIR, 'default.jpg'));
      console.log('  OK   default');
    }
  } catch(e) {
    console.log('  FAIL default');
  }

  // Clean up old invalid .svg/.webp files
  for (const f of fs.readdirSync(IMAGES_DIR)) {
    if (f.endsWith('.svg') || f.endsWith('.webp')) {
      fs.unlinkSync(path.join(IMAGES_DIR, f));
      console.log(`  DEL  ${f}`);
    }
  }

  // Update all source references from .svg/.webp -> .jpg
  function updateRefs(dir) {
    for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
      const p = path.join(dir, e.name);
      if (e.isDirectory() && !['node_modules', '.git', 'dist'].includes(e.name)) {
        updateRefs(p);
      } else if (/\.(md|astro|ts|js|mjs)$/.test(e.name)) {
        let c = fs.readFileSync(p, 'utf-8');
        const n = c.replace(/\/images\/breeds\/([\w-]+)\.(svg|webp)/g, '/images/breeds/$1.jpg');
        if (n !== c) {
          fs.writeFileSync(p, n, 'utf-8');
          console.log(`  REF  ${path.relative('.', p)}`);
        }
      }
    }
  }
  updateRefs('src');
  updateRefs('scripts');

  console.log(`\nDone! Downloaded: ${ok}, Failed: ${fail}`);
}

main().catch(console.error);
