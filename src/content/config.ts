import { defineCollection, z } from 'astro:content';

const breedsCollection = defineCollection({
  type: 'content',
  schema: z.object({
    name: z.string(),
    scientificName: z.string().optional(),
    metaTitle: z.string(),
    metaDescription: z.string(),
    featuredImage: z.string(),
    featuredImageAlt: z.string(),
    origin: z.string(),
    lifespan: z.string(),
    weight: z.object({ male: z.string(), female: z.string() }),
    height: z.string(),
    coatLength: z.enum(['hairless', 'shorthair', 'mediumhair', 'longhair']),
    coatType: z.string(),
    colors: z.array(z.string()),
    patterns: z.array(z.string()),
    eyeColors: z.array(z.string()),
    sheddingLevel: z.number().min(1).max(5),
    groomingNeeds: z.number().min(1).max(5),
    energyLevel: z.number().min(1).max(5),
    vocalizationLevel: z.number().min(1).max(5),
    childFriendly: z.number().min(1).max(5),
    petFriendly: z.number().min(1).max(5),
    intelligence: z.number().min(1).max(5),
    rarity: z.enum(['common', 'uncommon', 'rare', 'very-rare']),
    categories: z.array(z.string()),
    tags: z.array(z.string()),
    recognizedBy: z.array(z.string()).default([]),
    relatedBreeds: z.array(z.string()).default([]),
    similarBreeds: z.array(z.string()).default([]),
    featured: z.boolean().default(false),
    order: z.number().default(100),
  }),
});

const categoriesCollection = defineCollection({
  type: 'content',
  schema: z.object({
    name: z.string(),
    description: z.string(),
    metaTitle: z.string(),
    metaDescription: z.string(),
    featuredImage: z.string().optional(),
    icon: z.string().optional(),
    order: z.number().default(10),
  }),
});

export const collections = {
  breeds: breedsCollection,
  categories: categoriesCollection,
};