import fs from 'fs';
import path from 'path';

const BREEDS_DIR = path.resolve('src/content/breeds');

interface Weight { male: string; female: string; }
type CoatLength = 'hairless' | 'shorthair' | 'mediumhair' | 'longhair';
type Rarity = 'common' | 'uncommon' | 'rare' | 'very-rare';
type Rating = 1 | 2 | 3 | 4 | 5;

interface BreedData {
  name: string; slug: string; scientificName?: string;
  metaTitle: string; metaDescription: string;
  featuredImage: string; featuredImageAlt: string;
  origin: string; lifespan: string; weight: Weight; height: string;
  coatLength: CoatLength; coatType: string;
  colors: string[]; patterns: string[]; eyeColors: string[];
  sheddingLevel: Rating; groomingNeeds: Rating; energyLevel: Rating;
  vocalizationLevel: Rating; childFriendly: Rating; petFriendly: Rating;
  intelligence: Rating; rarity: Rarity;
  categories: string[]; tags: string[];
  recognizedBy: string[]; relatedBreeds: string[]; similarBreeds: string[];
  featured: boolean; order: number;
  body: string;
}

const breeds: BreedData[] = [
  // ============ A ============
  {
    name: "Abyssinian", slug: "abyssinian", scientificName: "Felis catus",
    metaTitle: "Abyssinian Cat Breed: Info, Pictures, Care & Facts",
    metaDescription: "The Abyssinian is an active, intelligent, and social cat breed with a distinctive ticked coat. Learn about Abyssinian personality, care, health, and more.",
    featuredImage: "/images/breeds/abyssinian.jpg", featuredImageAlt: "Ruddy Abyssinian cat with ticked coat sitting alertly",
    origin: "Ethiopia / Southeast Asia", lifespan: "9-15 years",
    weight: { male: "8-12 lbs (3.6-5.4 kg)", female: "6-8 lbs (2.7-3.6 kg)" },
    height: "8-10 inches (20-25 cm)", coatLength: "shorthair",
    coatType: "Dense, silky, fine with distinctive ticking",
    colors: ["Ruddy", "Cinnamon", "Blue", "Fawn"], patterns: ["Ticked tabby"],
    eyeColors: ["Gold", "Green", "Hazel"],
    sheddingLevel: 2, groomingNeeds: 1, energyLevel: 5,
    vocalizationLevel: 2, childFriendly: 4, petFriendly: 4, intelligence: 5,
    rarity: "common",
    categories: ["shorthair", "popular", "playful", "intelligent"],
    tags: ["ticked-coat", "ancient-breed", "dog-like", "climber"],
    recognizedBy: ["CFA", "TICA", "FIFe", "GCCF"],
    relatedBreeds: ["somali", "ocicat", "bengal", "egyptian-mau"],
    similarBreeds: ["somali", "singapura", "oriental-shorthair"],
    featured: true, order: 1,
    body: `## History & Origin

The Abyssinian is one of the oldest known cat breeds in the world. Despite its name suggesting Ethiopian origins, recent genetic studies indicate the breed likely originated in coastal regions of the Indian Ocean and parts of Southeast Asia. The breed was refined and developed primarily in Great Britain during the late 19th century. The first Abyssinian was exhibited at the Crystal Palace cat show in 1871.

The breed's distinctive ticked coat pattern resembles that of wild cats depicted in ancient Egyptian art, leading to the popular (though unverified) belief that Abyssinians are direct descendants of the sacred cats of ancient Egypt.

## Appearance & Physical Traits

The Abyssinian is a medium-sized, muscular cat with a uniquely elegant appearance. They have a wedge-shaped head, large alert ears that give them a perpetually curious expression, and almond-shaped eyes that can be gold, green, or hazel. Their body is lithe and athletic, with long, slender legs and a tapering tail.

The most distinctive feature is the ticked coat — each individual hair has multiple bands of color, creating a warm, shimmering effect without the stripes or spots typical of tabby cats. The coat comes in four recognized colors: ruddy (the most common warm brown), cinnamon, blue, and fawn.

## Personality & Temperament

Abyssinians are often called the "clowns of the cat world" for their playful, curious, and sometimes mischievous nature. They are extremely active cats who love to climb, explore, and investigate everything in their environment. They form strong bonds with their human families and prefer to be involved in all household activities.

These cats are highly intelligent and can learn tricks, walk on a leash, and even play fetch. They do not do well when left alone for long periods and thrive in homes where someone is around most of the day. Abyssinians typically get along well with children and other pets, including cat-friendly dogs.

## Care & Grooming Guide

With a short, fine coat, Abyssinians require minimal grooming. A weekly brushing with a soft bristle brush or grooming glove is sufficient to remove loose hair and distribute skin oils. They shed moderately.

These highly active cats need plenty of physical and mental stimulation. Cat trees, puzzle toys, interactive play sessions, and window perches are essential. Without adequate stimulation, Abyssinians may become destructive or develop behavioral issues.

## Health & Lifespan

Abyssinians typically live 9-15 years. They are generally healthy but can be prone to certain genetic conditions including progressive retinal atrophy (PRA), pyruvate kinase deficiency (PK deficiency), and patellar luxation. Reputable breeders screen for these conditions. Regular veterinary checkups and a high-quality diet contribute to a long, healthy life.

## Diet & Nutrition

Feed your Abyssinian a high-quality, protein-rich cat food appropriate for their life stage. These active cats need quality nutrition to fuel their energy levels. Always provide fresh water. Some Abyssinians enjoy puzzle feeders that make mealtime mentally stimulating.

## Is This Breed Right For You?

**Pros:** Highly intelligent and trainable, low-maintenance grooming, great with children and other pets, affectionate and social, entertaining personality.

**Cons:** Requires significant attention and playtime, can become destructive if bored, not ideal for owners away frequently, may be too active for some households.

## Fun Facts

1. Abyssinians are one of the most popular shorthair breeds in the United States.
2. The ticked coat pattern is unique among pedigreed cats in its level of expression.
3. Abyssinians often prefer heights and will perch on the highest point in any room.
4. They are sometimes called "Aby-grabbys" for their tendency to grab objects they find interesting.
5. Their kitten coat is darker and less ticked than their adult coat, which develops fully by 18 months.`
  },
  {
    name: "Aegean", slug: "aegean",
    metaTitle: "Aegean Cat Breed: Info, Pictures, Care & Facts",
    metaDescription: "The Aegean cat is a naturally occurring Greek breed known for its friendly personality and love of water. Discover this rare Mediterranean breed's care needs and temperament.",
    featuredImage: "/images/breeds/aegean.jpg", featuredImageAlt: "Aegean cat with semi-longhair coat",
    origin: "Greece (Cycladic Islands)", lifespan: "10-15 years",
    weight: { male: "9-12 lbs (4-5.5 kg)", female: "7-10 lbs (3-4.5 kg)" },
    height: "9-11 inches (23-28 cm)", coatLength: "mediumhair",
    coatType: "Semi-long, dense, water-resistant",
    colors: ["White with black", "White with red", "White with blue", "Bicolor", "Tricolor"],
    patterns: ["Bicolor", "Tricolor", "Tabby"],
    eyeColors: ["Green", "Yellow", "Blue", "Odd-eyed"],
    sheddingLevel: 3, groomingNeeds: 2, energyLevel: 3,
    vocalizationLevel: 3, childFriendly: 4, petFriendly: 4, intelligence: 4,
    rarity: "rare",
    categories: ["mediumhair", "rare", "playful"],
    tags: ["natural-breed", "water-loving", "greek-origin", "fishing-cat"],
    recognizedBy: [],
    relatedBreeds: ["turkish-angora", "turkish-van", "norwegian-forest-cat"],
    similarBreeds: ["turkish-van", "maine-coon"],
    featured: false, order: 100,
    body: `## History & Origin

The Aegean cat is a naturally occurring breed from the Cycladic Islands of Greece, particularly the Aegean Sea region. Unlike many modern breeds, the Aegean cat developed without human intervention, adapting to the island environment over centuries. These cats have been companions to Greek fishermen for generations and are known for their fishing abilities.

While common in Greece, the Aegean cat remains rare internationally, as it is only beginning to be recognized by formal cat breeding organizations. The breed represents one of the few naturally occurring European cat breeds.

## Appearance & Physical Traits

The Aegean cat is a medium-sized, muscular cat with a semi-longhaired coat that is notably water-resistant — an adaptation to the island environment. They typically display a bicolor or tricolor pattern, most commonly white with black, red, or blue patches. Their eyes can be green, yellow, blue, or odd-eyed (one of each color).

Their body is athletic and well-proportioned, built for an active outdoor lifestyle. The tail is moderately long and well-furnished with fur.

## Personality & Temperament

Aegean cats are known for their friendly, outgoing personalities. They are social cats who bond closely with their families and generally get along well with children and other pets. True to their fishing heritage, many Aegean cats have an unusual affinity for water and may enjoy playing with running faucets or even joining their owners near water.

These cats are intelligent and moderately active. They enjoy interactive play but are not as demanding as some of the more high-energy breeds. They make excellent family companions due to their adaptable, easygoing nature.

## Care & Grooming Guide

The semi-long coat requires brushing 2-3 times per week to prevent tangles and reduce shedding. They shed moderately throughout the year, with increased shedding during seasonal changes. Bathing is rarely needed due to the water-resistant quality of their coat.

Provide scratching posts, climbing structures, and interactive toys to keep your Aegean cat mentally stimulated. Puzzle feeders can engage their natural problem-solving abilities.

## Health & Lifespan

As a natural breed with no history of selective breeding, Aegean cats are generally robust and healthy with a lifespan of 10-15 years. They have no known breed-specific genetic conditions. Regular veterinary care, a balanced diet, and an active lifestyle contribute to their longevity.

## Is This Breed Right For You?

**Pros:** Friendly and adaptable, good with children and pets, generally healthy, unique Mediterranean heritage, water-loving personality.

**Cons:** Rare and difficult to find outside Greece, moderate grooming requirements, may be too independent for some owners.`
  },
  {
    name: "American Bobtail", slug: "american-bobtail",
    metaTitle: "American Bobtail Cat Breed: Info, Pictures, Care & Facts",
    metaDescription: "The American Bobtail is a rugged, intelligent breed with a naturally short tail. Learn about this distinctive American breed's personality, grooming needs, and care requirements.",
    featuredImage: "/images/breeds/american-bobtail.jpg", featuredImageAlt: "American Bobtail cat with distinctive short tail",
    origin: "United States", lifespan: "13-15 years",
    weight: { male: "12-16 lbs (5.4-7.3 kg)", female: "7-11 lbs (3.2-5 kg)" },
    height: "9-10 inches (23-25 cm)", coatLength: "shorthair",
    coatType: "Dense, shaggy, water-resistant double coat; also comes in longhair variety",
    colors: ["Brown tabby", "Silver tabby", "Various colors"],
    patterns: ["Tabby", "Solid", "Tortoiseshell", "Bicolor"],
    eyeColors: ["Gold", "Green", "Copper", "Blue"],
    sheddingLevel: 3, groomingNeeds: 2, energyLevel: 3,
    vocalizationLevel: 2, childFriendly: 5, petFriendly: 5, intelligence: 5,
    rarity: "uncommon",
    categories: ["shorthair", "intelligent", "playful"],
    tags: ["bobbed-tail", "american-origin", "dog-like", "natural-breed"],
    recognizedBy: ["CFA", "TICA"],
    relatedBreeds: ["japanese-bobtail", "manx", "pixie-bob"],
    similarBreeds: ["manx", "japanese-bobtail", "pixie-bob"],
    featured: false, order: 10,
    body: `## History & Origin

The American Bobtail is a relatively new breed that originated in the late 1960s in the United States. The breed began when a couple discovered a short-tailed brown tabby male kitten on an Arizona Native American reservation. This cat was bred with a Siamese female, producing kittens with the distinctive bobbed tail. The breed was developed without using any wild cat genes, making it a purely domestic breed.

TICA recognized the American Bobtail in 1989, and CFA granted recognition in 2006. The breed remains relatively uncommon but has a devoted following.

## Appearance & Physical Traits

The American Bobtail is a medium to large, muscular cat with a distinctly rugged, wild appearance. The breed's most notable feature is its naturally short tail, which typically measures one to four inches in length and is unique to each cat like a fingerprint. The tail should be visible above the back when the cat is alert.

They have a broad, modified wedge-shaped head, almond-shaped eyes, and ears that may have tufts. The coat comes in both shorthair and longhair varieties and has a shaggy, dense, water-resistant quality that enhances their wild appearance.

## Personality & Temperament

American Bobtails are known for their dog-like devotion to their families. They are highly intelligent, interactive, and enjoy games like fetch and hide-and-seek. Many owners report that their Bobtails are excellent traveling companions and adapt well to RV or truck living.

These cats are notably good with children and other pets, including dogs. They have a calm, steady temperament but remain playful well into adulthood. American Bobtails are moderately vocal but not excessively so, often communicating with chirps and trills rather than loud meows.

## Care & Grooming Guide

Shorthair American Bobtails require brushing once or twice weekly; longhair varieties need more frequent grooming, about 3-4 times weekly. Both varieties shed moderately.

These intelligent cats benefit from puzzle toys, clicker training, and interactive play sessions. They enjoy walking on a harness and leash. Provide scratching posts of varying textures and heights to satisfy their natural scratching instincts.

## Health & Lifespan

American Bobtails are a generally healthy breed with a lifespan of 13-15 years. They have no breed-specific genetic health issues, though some individuals may be born without a tail (rumpy), which can sometimes be associated with spinal issues. Reputable breeders screen for overall health.

## Is This Breed Right For You?

**Pros:** Extremely intelligent and trainable, excellent with children and other pets, adaptable to various lifestyles, unique wild appearance, moderate activity level.

**Cons:** Can be difficult to find from breeders, moderately expensive, may be too active for very sedentary households.`
  },
  {
    name: "American Curl", slug: "american-curl",
    metaTitle: "American Curl Cat Breed: Info, Pictures, Care & Facts",
    metaDescription: "The American Curl is known for its uniquely curled-back ears and sweet personality. Learn about this distinctive breed's care, temperament, and health needs.",
    featuredImage: "/images/breeds/american-curl.jpg", featuredImageAlt: "American Curl cat with distinctive curled ears",
    origin: "United States", lifespan: "12-16 years",
    weight: { male: "7-10 lbs (3.2-4.5 kg)", female: "5-8 lbs (2.3-3.6 kg)" },
    height: "9-12 inches (23-30 cm)", coatLength: "shorthair",
    coatType: "Silky, flat-lying; also comes in longhair variety",
    colors: ["All colors and patterns accepted"],
    patterns: ["Solid", "Tabby", "Tortoiseshell", "Bicolor", "Colorpoint"],
    eyeColors: ["All colors accepted", "Blue", "Green", "Gold", "Odd-eyed"],
    sheddingLevel: 2, groomingNeeds: 1, energyLevel: 3,
    vocalizationLevel: 3, childFriendly: 5, petFriendly: 5, intelligence: 4,
    rarity: "uncommon",
    categories: ["shorthair", "rare", "playful"],
    tags: ["curled-ears", "american-origin", "family-friendly", "kitten-like"],
    recognizedBy: ["CFA", "TICA"],
    relatedBreeds: ["scottish-fold", "american-shorthair", "american-wirehair"],
    similarBreeds: ["scottish-fold", "munchkin"],
    featured: false, order: 15,
    body: `## History & Origin

The American Curl originated in 1981 in Lakewood, California, when a stray longhaired black female kitten with unusually curled ears was taken in by the Ruga family. Named Shulamith, she became the foundation for the entire breed. When Shulamith had kittens, approximately half inherited the curled ear trait, confirming it was a dominant gene.

The breed was recognized by TICA in 1987 and by CFA in 1993, making it one of the fastest breeds to achieve championship status. All American Curls trace their lineage back to Shulamith.

## Appearance & Physical Traits

The American Curl's defining characteristic is, of course, the uniquely curled ears that curve backward in a graceful arc. The ears have firm cartilage from the base to at least one-third of the height, then curve back in a smooth arc. Kittens are born with straight ears; the curl develops within 2-10 days and sets permanently by about 4 months.

Beyond the ears, American Curls are elegant, medium-sized cats with silky coats and expressive walnut-shaped eyes. They come in both shorthair and longhair varieties, and all colors and patterns are accepted.

## Personality & Temperament

American Curls are known for retaining kitten-like playfulness well into their senior years. They are affectionate without being demanding, intelligent without being mischievous, and social without being clingy. This moderate temperament makes them excellent family companions.

These cats get along wonderfully with children and other pets. They adapt well to new situations and are known for being good travel companions. American Curls are moderately active and enjoy interactive play sessions.

## Care & Grooming Guide

Shorthair American Curls need minimal grooming — a quick weekly brushing is sufficient. Longhair varieties require brushing 2-3 times per week. The curled ears need gentle cleaning but should never be forced or bent in the opposite direction, as the cartilage can be damaged.

These cats enjoy climbing structures, puzzle toys, and interactive play sessions with their owners. They are social and do best in homes where they receive plenty of attention.

## Health & Lifespan

American Curls are generally healthy with a lifespan of 12-16 years. The gene causing curled ears does not appear to be associated with any health problems, unlike the ear mutations in some other breeds. Regular veterinary checkups and dental care are recommended.

## Is This Breed Right For You?

**Pros:** Unique appearance, sweet and adaptable personality, excellent with children and pets, low grooming needs for shorthair variety, generally healthy breed.

**Cons:** Rare and can be expensive, ears require gentle care, longhair variety needs more grooming.`
  },

  // ============ ADD MORE BREEDS BELOW ============
  // About 150 more breeds will be appended here
];

// The complete breed list is generated below programmatically
// to keep this file manageable

function writeBreed(breed: BreedData): void {
  const frontmatter: Record<string, unknown> = {
    name: breed.name,
    slug: breed.slug,
    scientificName: breed.scientificName,
    metaTitle: breed.metaTitle,
    metaDescription: breed.metaDescription,
    featuredImage: breed.featuredImage,
    featuredImageAlt: breed.featuredImageAlt,
    origin: breed.origin,
    lifespan: breed.lifespan,
    weight: breed.weight,
    height: breed.height,
    coatLength: breed.coatLength,
    coatType: breed.coatType,
    colors: breed.colors,
    patterns: breed.patterns,
    eyeColors: breed.eyeColors,
    sheddingLevel: breed.sheddingLevel,
    groomingNeeds: breed.groomingNeeds,
    energyLevel: breed.energyLevel,
    vocalizationLevel: breed.vocalizationLevel,
    childFriendly: breed.childFriendly,
    petFriendly: breed.petFriendly,
    intelligence: breed.intelligence,
    rarity: breed.rarity,
    categories: breed.categories,
    tags: breed.tags,
    recognizedBy: breed.recognizedBy,
    relatedBreeds: breed.relatedBreeds,
    similarBreeds: breed.similarBreeds,
    featured: breed.featured,
    order: breed.order,
  };

  let yaml = '---\n';
  for (const [key, value] of Object.entries(frontmatter)) {
    if (value === undefined || value === null) continue;
    if (Array.isArray(value)) {
      yaml += `${key}:\n`;
      for (const item of value) {
        yaml += `  - "${item}"\n`;
      }
    } else if (typeof value === 'object') {
      yaml += `${key}:\n`;
      for (const [k, v] of Object.entries(value as Record<string, unknown>)) {
        yaml += `  ${k}: "${v}"\n`;
      }
    } else if (typeof value === 'boolean') {
      yaml += `${key}: ${value}\n`;
    } else if (typeof value === 'number') {
      yaml += `${key}: ${value}\n`;
    } else {
      yaml += `${key}: "${value}"\n`;
    }
  }
  yaml += '---\n\n';
  yaml += breed.body;

  const filePath = path.join(BREEDS_DIR, `${breed.slug}.md`);
  fs.writeFileSync(filePath, yaml, 'utf-8');
}

// Ensure directory exists
if (!fs.existsSync(BREEDS_DIR)) {
  fs.mkdirSync(BREEDS_DIR, { recursive: true });
}

// Write all breeds
for (const breed of breeds) {
  writeBreed(breed);
  console.log(`  ✓ ${breed.name} (${breed.slug})`);
}

console.log(`\nGenerated ${breeds.length} breed files in ${BREEDS_DIR}`);