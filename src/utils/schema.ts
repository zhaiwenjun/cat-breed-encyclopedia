import { siteConfig } from '@data/siteConfig';
import type { BreedFrontmatter } from '@types/breed';
import { breedURL } from './urls';

export function organizationSchema() {
  return {
    '@context': 'https://schema.org',
    '@type': 'Organization',
    name: siteConfig.name,
    url: siteConfig.url,
    logo: `${siteConfig.url}/favicon.svg`,
    description: siteConfig.description,
  };
}

export function websiteSchema() {
  return {
    '@context': 'https://schema.org',
    '@type': 'WebSite',
    name: siteConfig.name,
    url: siteConfig.url,
    description: siteConfig.description,
    potentialAction: {
      '@type': 'SearchAction',
      target: {
        '@type': 'EntryPoint',
        urlTemplate: `${siteConfig.url}breeds/?s={search_term_string}`,
      },
      'query-input': 'required name=search_term_string',
    },
  };
}

export function animalBreedSchema(breed: BreedFrontmatter) {
  return {
    '@context': 'https://schema.org',
    '@type': 'AnimalBreed',
    name: breed.name,
    description: breed.metaDescription,
    image: breed.featuredImage.startsWith('http') ? breed.featuredImage : `${siteConfig.url}${breed.featuredImage}`,
    additionalProperty: [
      { '@type': 'PropertyValue', name: 'Origin', value: breed.origin },
      { '@type': 'PropertyValue', name: 'Lifespan', value: breed.lifespan },
      { '@type': 'PropertyValue', name: 'Coat Length', value: breed.coatLength },
      { '@type': 'PropertyValue', name: 'Energy Level', value: `${breed.energyLevel}/5` },
      { '@type': 'PropertyValue', name: 'Shedding Level', value: `${breed.sheddingLevel}/5` },
      { '@type': 'PropertyValue', name: 'Child Friendly', value: `${breed.childFriendly}/5` },
      { '@type': 'PropertyValue', name: 'Intelligence', value: `${breed.intelligence}/5` },
      { '@type': 'PropertyValue', name: 'Rarity', value: breed.rarity },
    ],
    ...(breed.scientificName ? {
      species: { '@type': 'Species', name: breed.scientificName },
    } : {}),
  };
}

export function breadcrumbListSchema(items: Array<{ name: string; url?: string }>) {
  return {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: items.map((item, i) => ({
      '@type': 'ListItem',
      position: i + 1,
      name: item.name,
      ...(item.url ? { item: item.url } : {}),
    })),
  };
}

export function faqPageSchema(qa: Array<{ question: string; answer: string }>) {
  return {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    mainEntity: qa.map((q) => ({
      '@type': 'Question',
      name: q.question,
      acceptedAnswer: {
        '@type': 'Answer',
        text: q.answer,
      },
    })),
  };
}

export function collectionPageSchema(name: string, description: string, url: string) {
  return {
    '@context': 'https://schema.org',
    '@type': 'CollectionPage',
    name,
    description,
    url,
    isPartOf: {
      '@type': 'WebSite',
      name: siteConfig.name,
      url: siteConfig.url,
    },
  };
}