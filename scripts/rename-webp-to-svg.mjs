import fs from 'fs';
import path from 'path';

const IMAGES_DIR = path.resolve('public/images/breeds');

// Rename all .webp files to .svg (they contain SVG content)
const files = fs.readdirSync(IMAGES_DIR).filter(f => f.endsWith('.webp'));

for (const file of files) {
  const oldPath = path.join(IMAGES_DIR, file);
  const newPath = path.join(IMAGES_DIR, file.replace('.webp', '.svg'));
  fs.renameSync(oldPath, newPath);
  console.log(`Renamed: ${file} -> ${file.replace('.webp', '.svg')}`);
}

// Update all breed .md files
const BREEDS_DIR = path.resolve('src/content/breeds');
const mdFiles = fs.readdirSync(BREEDS_DIR).filter(f => f.endsWith('.md'));

for (const file of mdFiles) {
  const filePath = path.join(BREEDS_DIR, file);
  let content = fs.readFileSync(filePath, 'utf-8');
  content = content.replace(/\/images\/breeds\/(\w[\w-]*)\.webp/g, '/images/breeds/$1.svg');
  fs.writeFileSync(filePath, content, 'utf-8');
  console.log(`Updated: ${file}`);
}

// Update siteConfig
const configPath = path.resolve('src/data/siteConfig.ts');
let config = fs.readFileSync(configPath, 'utf-8');
config = config.replace("/images/breeds/default.jpg", "/images/breeds/default.jpg");
fs.writeFileSync(configPath, config, 'utf-8');
console.log('Updated: siteConfig.ts');

// Update schema.ts
const schemaPath = path.resolve('src/utils/schema.ts');
let schema = fs.readFileSync(schemaPath, 'utf-8');
schema = schema.replace("/images/breeds/default.jpg", "/images/breeds/default.jpg");
fs.writeFileSync(schemaPath, schema, 'utf-8');
console.log('Updated: schema.ts');

// Update components
const components = [
  'src/components/breed/BreedCard.astro',
  'src/components/breed/BreedHero.astro',
  'src/components/layout/BaseHead.astro',
];

for (const comp of components) {
  const compPath = path.resolve(comp);
  if (fs.existsSync(compPath)) {
    let content = fs.readFileSync(compPath, 'utf-8');
    content = content.replace(/\/images\/breeds\/default\.webp/g, '/images/breeds/default.jpg');
    fs.writeFileSync(compPath, content, 'utf-8');
    console.log(`Updated: ${comp}`);
  }
}

console.log('\nDone! All .webp references updated to .svg');
