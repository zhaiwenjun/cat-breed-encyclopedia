export interface BreedFrontmatter {
  name: string;
  slug?: string;
  scientificName?: string;
  metaTitle: string;
  metaDescription: string;
  featuredImage: string;
  featuredImageAlt: string;
  origin: string;
  lifespan: string;
  weight: { male: string; female: string };
  height: string;
  coatLength: 'hairless' | 'shorthair' | 'mediumhair' | 'longhair';
  coatType: string;
  colors: string[];
  patterns: string[];
  eyeColors: string[];
  sheddingLevel: 1 | 2 | 3 | 4 | 5;
  groomingNeeds: 1 | 2 | 3 | 4 | 5;
  energyLevel: 1 | 2 | 3 | 4 | 5;
  vocalizationLevel: 1 | 2 | 3 | 4 | 5;
  childFriendly: 1 | 2 | 3 | 4 | 5;
  petFriendly: 1 | 2 | 3 | 4 | 5;
  intelligence: 1 | 2 | 3 | 4 | 5;
  rarity: 'common' | 'uncommon' | 'rare' | 'very-rare';
  categories: string[];
  tags: string[];
  recognizedBy: string[];
  relatedBreeds: string[];
  similarBreeds: string[];
  featured: boolean;
  order: number;
}

export interface CategoryFrontmatter {
  name: string;
  slug?: string;
  description: string;
  metaTitle: string;
  metaDescription: string;
  featuredImage?: string;
  icon?: string;
  order: number;
}