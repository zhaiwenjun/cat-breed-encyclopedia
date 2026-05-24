#!/usr/bin/env python3
"""Cat Breed Encyclopedia - Generate all breed markdown files."""
import os

BREEDS_DIR = "src/content/breeds"
os.makedirs(BREEDS_DIR, exist_ok=True)

def write_md(b):
    yaml = "---\n"
    for k, v in b.items():
        if k == "body": continue
        if v is None: continue
        if isinstance(v, list):
            yaml += f"{k}:\n"
            for item in v:
                yaml += f'  - "{item}"\n'
        elif isinstance(v, dict):
            yaml += f"{k}:\n"
            for dk, dv in v.items():
                yaml += f'  {dk}: "{dv}"\n'
        elif isinstance(v, bool):
            yaml += f"{k}: {'true' if v else 'false'}\n"
        elif isinstance(v, (int, float)):
            yaml += f"{k}: {v}\n"
        else:
            yaml += f'{k}: "{v}"\n'
    yaml += "---\n\n" + b.get("body", "")
    with open(os.path.join(BREEDS_DIR, f"{b['slug']}.md"), "w", encoding="utf-8") as f:
        f.write(yaml)
    return b['name']

def body(n, o, ls, coat, ct, c, p, e, el, vl, cf, pf, intel, sl, gn, rare):
    cl = {"hairless":"hairless","shorthair":"short","mediumhair":"semi-long","longhair":"long"}[coat]
    c0 = c[0]
    p0 = p[0]
    e0 = e[0]
    return f"""## History & Origin

The {n} originated in {o}. This distinctive breed has captured the hearts of cat lovers with its unique combination of striking appearance and engaging personality.

Whether prized for working abilities, stunning looks, or wonderful temperament, the {n} has established itself as {"a " + rare.replace("-"," ") + " breed" if rare != "common" else "a widely available breed"} with a devoted following among cat enthusiasts worldwide.

## Appearance & Physical Traits

The {n} displays a beautiful {cl} coat characterized by {ct.lower()}. The breed features {c0.lower()} coloring with {p0.lower()} patterns, complemented by {e0.lower()} eyes that give this breed its distinctive and captivating expression.

The coat is one of the breed's most defining features — {ct.lower()}. This contributes significantly to the breed's overall appearance and care requirements.

## Personality & Temperament

The {n} is a {"highly energetic" if el >= 4 else ("moderately active" if el >= 3 else "calm and relaxed")} companion with an engaging personality. They form strong bonds with their families and are {"very affectionate" if cf >= 4 else "moderately affectionate"} with those they trust. These cats are {"excellent with children and other pets" if cf >= 4 and pf >= 4 else ("good with respectful children" if cf >= 3 else "best suited to quiet households")}.

With {"high" if intel >= 4 else "moderate"} intelligence, these cats {"enjoy interactive play and puzzle toys" if intel >= 4 else "appreciate simple toys and games"}. Their vocalization level is {"high" if vl >= 4 else ("moderate" if vl >= 3 else "low")}, meaning they {"are quite talkative and expressive" if vl >= 4 else ("communicate as needed" if vl >= 3 else "tend to be quiet and soft-spoken")}.

{"The breed thrives in active households that can provide plenty of playtime and attention." if el >= 4 else ("They enjoy being lap cats and calm companionship." if el <= 2 else "They strike a nice balance between playfulness and relaxation.")}

## Care & Grooming Guide

{"".join([
    "requires daily brushing to prevent mats and tangles. Regular professional grooming every 4-6 weeks is recommended. Pay special attention to the ruff, belly, and tail areas." if coat == "longhair" else
    "needs brushing 2-3 times per week to prevent tangles and reduce shedding. The semi-long coat is relatively easy to maintain with a regular routine." if coat == "mediumhair" else
    "requires minimal grooming. A weekly brushing with a soft brush or grooming glove is sufficient to remove loose hair and keep the coat glossy." if coat == "shorthair" else
    "requires special care for their hairless body, including weekly bathing to remove skin oil buildup, protection from sun exposure, and warmth in cold weather."
])}

Shedding Level: {sl}/5. Grooming Needs: {gn}/5.

Beyond coat care, these cats need standard feline maintenance: regular nail trimming, dental care, and a clean litter box. Provide scratching posts and climbing structures to satisfy natural instincts.

## Health & Lifespan

The {n} typically enjoys a lifespan of {ls}. With proper care, regular veterinary checkups, a high-quality diet, and an indoor lifestyle, many individuals live toward the upper end of this range.

Like all breeds, the {n} may be predisposed to certain health conditions. Reputable breeders screen for known genetic issues. Maintaining a healthy weight, providing dental care, and keeping vaccinations current all contribute to a long, healthy life.

## Diet & Nutrition

Feed your {n} a high-quality, protein-rich cat food appropriate for their life stage. Portion control is important to prevent obesity. Always provide fresh, clean water. Some cats enjoy puzzle feeders that make mealtime mentally enriching.

## Exercise Needs

{"".join([
    "The " + n + " needs plenty of physical activity and mental stimulation. Provide cat trees, interactive toys, puzzle feeders, and dedicated play sessions. These active cats thrive in homes where someone can engage them in play daily. Without adequate stimulation, they may become bored or destructive." if el >= 4 else
    "The " + n + " benefits from daily interactive play sessions to stay healthy and happy. Wand toys, laser pointers, and fetch games are great options. A cat tree by a window provides entertainment throughout the day." if el >= 3 else
    "The " + n + " has relatively low exercise needs. Short daily play sessions with wand toys or balls are sufficient. They enjoy lounging in sunny spots and watching the world from a window perch."
])}

## Is This Breed Right For You?

**Pros:**
{chr(10).join("- " + p for p in [
    *(["Highly intelligent and trainable"] if intel >= 4 else []),
    *(["Excellent with children and other pets"] if cf >= 4 and pf >= 4 else []),
    *(["Low-maintenance grooming"] if gn <= 2 else []),
    *(["Calm, adaptable personality"] if el <= 3 else []),
    f"Distinctive, beautiful {cl} coat",
    *(["Rare and unique breed"] if rare != "common" else []),
])}

**Cons:**
{chr(10).join("- " + c for c in [
    *(["High energy requires significant daily playtime"] if el >= 4 else []),
    *(["Moderate to heavy shedding"] if sl >= 3 else []),
    *(["Higher grooming maintenance needed"] if gn >= 3 else []),
    *(["Can be very vocal"] if vl >= 4 else []),
    *(["May be difficult to find and expensive"] if rare != "common" else []),
    *(["Low energy may not suit active families"] if el <= 2 else []),
])}

## Fun Facts

1. The {n} is one of the most visually distinctive cat breeds in the world.
2. Their {cl} coat is an adaptation to their origins in {o}.
3. These cats form deep, lasting bonds with their human families.
4. The breed's unique combination of traits makes them memorable companions.
5. {n} cats are celebrated for their {"playful, energetic nature" if el >= 4 else ("calm, steady temperament" if el <= 2 else "balanced, adaptable personality")}.
"""

def mk(n, slug, sci, desc, origin, lifespan, wm, wf, h, coat, ct, colors, patterns, eyes,
       sl, gn, el, vl, cf, pf, intel, rarity, cats, tags, rec, rel, sim, feat, order):
    return {
        'name': n, 'slug': slug, 'scientificName': sci,
        'metaTitle': f"{n} Cat Breed: Info, Pictures, Care & Facts",
        'metaDescription': desc,
        'featuredImage': f'/images/breeds/{slug}.webp',
        'featuredImageAlt': f'{n} cat showing {coat} coat characteristics',
        'origin': origin, 'lifespan': lifespan,
        'weight': {'male': wm, 'female': wf}, 'height': h,
        'coatLength': coat, 'coatType': ct,
        'colors': colors, 'patterns': patterns, 'eyeColors': eyes,
        'sheddingLevel': sl, 'groomingNeeds': gn, 'energyLevel': el,
        'vocalizationLevel': vl, 'childFriendly': cf, 'petFriendly': pf,
        'intelligence': intel, 'rarity': rarity,
        'categories': cats, 'tags': tags,
        'recognizedBy': rec, 'relatedBreeds': rel, 'similarBreeds': sim,
        'featured': feat, 'order': order,
    }

# Shorthand
B = []
A = B.append

def add(*args, **kw):
    d = mk(*args, **kw)
    d['body'] = body(d['name'], d['origin'], d['lifespan'], d['coatLength'],
                     d['coatType'], d['colors'], d['patterns'], d['eyeColors'],
                     d['energyLevel'], d['vocalizationLevel'], d['childFriendly'],
                     d['petFriendly'], d['intelligence'], d['sheddingLevel'],
                     d['groomingNeeds'], d['rarity'])
    A(d)

add("Abyssinian","abyssinian","Felis catus","The Abyssinian is an active, intelligent, and social cat breed with a distinctive ticked coat.","Ethiopia / Southeast Asia","9-15 years","8-12 lbs (3.6-5.4 kg)","6-8 lbs (2.7-3.6 kg)","8-10 inches (20-25 cm)","shorthair","Dense, silky, fine with distinctive ticking",["Ruddy","Cinnamon","Blue","Fawn"],["Ticked tabby"],["Gold","Green","Hazel"],2,1,5,2,4,4,5,"common",["shorthair","popular","playful","intelligent"],["ticked-coat","ancient-breed","dog-like","climber"],["CFA","TICA","FIFe","GCCF"],["somali","ocicat","bengal","egyptian-mau"],["somali","singapura","oriental-shorthair"],True,1)
print("Script loaded successfully, ready to generate breeds...")
print(f"Base breeds defined: {len(B)}")