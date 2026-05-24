#!/usr/bin/env python3
"""Generate all cat breed markdown files from compact data."""
import os

OUT = "src/content/breeds"
os.makedirs(OUT, exist_ok=True)

def body(n, o, ls, coat, ct0, c0, p0, e0, el, vl, cf, pf, it, sl, gn, rare):
    cl = {"hairless":"hairless","shorthair":"short","mediumhair":"semi-long","longhair":"long"}[coat]
    t_energy = "highly energetic" if el>=4 else ("moderately active" if el>=3 else "calm and relaxed")
    t_affect = "very affectionate" if cf>=4 else "moderately affectionate"
    t_kids = "excellent with children and other pets" if cf>=4 and pf>=4 else ("good with respectful children" if cf>=3 else "best suited to quiet households")
    t_intel = "high" if it>=4 else "moderate"
    t_intelp = "enjoy interactive play and puzzle toys" if it>=4 else "appreciate simple toys and games"
    t_vocal = "high" if vl>=4 else ("moderate" if vl>=3 else "low")
    t_vocalv = "are quite talkative and expressive" if vl>=4 else ("communicate as needed" if vl>=3 else "tend to be quiet and soft-spoken")
    t_adapt = "The breed thrives in active households that can provide plenty of playtime and attention." if el>=4 else ("They enjoy being lap cats and calm companionship." if el<=2 else "They strike a nice balance between playfulness and relaxation.")
    t_rare = f"a {rare.replace('-',' ')} breed" if rare!="common" else "a widely available breed"

    if coat=="longhair": t_groom = f"The {n} requires daily brushing to prevent mats and tangles. Regular professional grooming every 4-6 weeks is recommended. Pay special attention to ruff, belly, and tail areas."
    elif coat=="mediumhair": t_groom = f"The {n} needs brushing 2-3 times per week to prevent tangles and reduce shedding. The {cl} coat is relatively easy to maintain with a regular routine."
    elif coat=="shorthair": t_groom = f"The {n} requires minimal grooming. A weekly brushing with a soft brush or grooming glove is sufficient to remove loose hair and keep the coat glossy."
    else: t_groom = f"The {n} requires special care for their hairless body, including weekly bathing to remove skin oil buildup, protection from sun exposure, and warmth in cold weather."

    if el>=4: t_exercise = f"The {n} needs plenty of physical activity and mental stimulation. Provide cat trees, interactive toys, puzzle feeders, and dedicated play sessions daily. Without adequate stimulation, they may become bored or destructive."
    elif el>=3: t_exercise = f"The {n} benefits from daily interactive play sessions. Wand toys, laser pointers, and fetch games are great options. A cat tree by a window provides entertainment throughout the day."
    else: t_exercise = f"The {n} has relatively low exercise needs. Short daily play sessions with wand toys or balls are sufficient. They enjoy lounging in sunny spots and watching the world from a window perch."

    pros = []
    if it>=4: pros.append("Highly intelligent and trainable")
    if cf>=4 and pf>=4: pros.append("Excellent with children and other pets")
    if gn<=2: pros.append("Low-maintenance grooming")
    if el<=3: pros.append("Calm, adaptable personality")
    pros.append(f"Distinctive, beautiful {cl} coat")
    if rare!="common": pros.append("Rare and unique breed")

    cons = []
    if el>=4: cons.append("High energy requires significant daily playtime")
    if sl>=3: cons.append("Moderate to heavy shedding requires regular cleaning")
    if gn>=3: cons.append("Higher grooming maintenance needed")
    if vl>=4: cons.append("Can be very vocal, which may not suit quiet households")
    if rare!="common": cons.append("May be difficult to find and more expensive")
    if el<=2: cons.append("Low energy may not suit active families")

    t_fun = "playful, energetic nature" if el>=4 else ("calm, steady temperament" if el<=2 else "balanced, adaptable personality")

    return f"""## History & Origin

The {n} originated in {o}. This distinctive breed has captured the hearts of cat lovers with its unique combination of striking appearance and engaging personality.

Whether prized for working abilities, stunning looks, or wonderful temperament, the {n} has established itself as {t_rare} with a devoted following among cat enthusiasts worldwide.

## Appearance & Physical Traits

The {n} displays a beautiful {cl} coat characterized by {ct0.lower()}. The breed features {c0.lower()} coloring with {p0.lower()} patterns, complemented by {e0.lower()} eyes that give this breed its distinctive and captivating expression.

The coat is one of the breed's most defining features — {ct0.lower()}. This contributes significantly to the breed's overall appearance and care requirements.

## Personality & Temperament

The {n} is a {t_energy} companion with an engaging personality. They form strong bonds with their families and are {t_affect} with those they trust. These cats are {t_kids}.

With {t_intel} intelligence, these cats {t_intelp}. Their vocalization level is {t_vocal}, meaning they {t_vocalv}.

{t_adapt}

## Care & Grooming Guide

{t_groom}

Shedding Level: {sl}/5. Grooming Needs: {gn}/5.

Beyond coat care, these cats need standard feline maintenance: regular nail trimming, dental care, and a clean litter box. Provide scratching posts and climbing structures to satisfy natural instincts.

## Health & Lifespan

The {n} typically enjoys a lifespan of {ls}. With proper care, regular veterinary checkups, a high-quality diet, and an indoor lifestyle, many individuals live toward the upper end of this range.

Like all breeds, the {n} may be predisposed to certain health conditions. Reputable breeders screen for known genetic issues. Maintaining a healthy weight, providing dental care, and keeping vaccinations current all contribute to a long, healthy life.

## Diet & Nutrition

Feed your {n} a high-quality, protein-rich cat food appropriate for their life stage. Portion control is important to prevent obesity. Always provide fresh, clean water. Some cats enjoy puzzle feeders that make mealtime mentally enriching.

## Exercise Needs

{t_exercise}

## Is This Breed Right For You?

**Pros:**
{chr(10).join('- ' + p for p in pros)}

**Cons:**
{chr(10).join('- ' + c for c in cons)}

## Fun Facts

1. The {n} is one of the most visually distinctive cat breeds in the world.
2. Their {cl} coat is an adaptation to their origins in {o}.
3. These cats form deep, lasting bonds with their human families.
4. The breed's unique combination of traits makes them memorable companions.
5. {n} cats are celebrated for their {t_fun}.
"""

def mk(name, slug, sci, desc, origin, lifespan, wm, wf, h, coat, ct,
       colors, patterns, eyes, sl, gn, el, vl, cf, pf, it, rarity,
       cats, tags, rec, rel, sim, feat, order):
    d = {
        'name':name,'slug':slug,'scientificName':sci,
        'metaTitle':f"{name} Cat Breed: Info, Pictures, Care & Facts",
        'metaDescription':desc,
        'featuredImage':f'/images/breeds/{slug}.webp',
        'featuredImageAlt':f'{name} cat showing {coat} coat',
        'origin':origin,'lifespan':lifespan,
        'weight':{'male':wm,'female':wf},'height':h,
        'coatLength':coat,'coatType':ct,
        'colors':colors,'patterns':patterns,'eyeColors':eyes,
        'sheddingLevel':sl,'groomingNeeds':gn,'energyLevel':el,
        'vocalizationLevel':vl,'childFriendly':cf,'petFriendly':pf,
        'intelligence':it,'rarity':rarity,
        'categories':cats,'tags':tags,
        'recognizedBy':rec,'relatedBreeds':rel,'similarBreeds':sim,
        'featured':feat,'order':order,
    }
    d['body'] = body(name, origin, lifespan, coat, ct, colors[0], patterns[0], eyes[0],
                     el, vl, cf, pf, it, sl, gn, rarity)
    return d

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
    with open(os.path.join(OUT, f"{b['slug']}.md"), "w", encoding="utf-8") as f:
        f.write(yaml)

# ============================================================
# COMPACT BREED DATA: name, slug, sci, desc, origin, lifespan,
# wm, wf, h, coat, ct, colors, patterns, eyes,
# sl, gn, el, vl, cf, pf, it, rarity,
# categories, tags, recognizedBy, relatedBreeds, similarBreeds,
# featured, order
# ============================================================

BREEDS = []

# Abyssinian
BREEDS.append(mk("Abyssinian","abyssinian","Felis catus","The Abyssinian is an active, intelligent, and social cat breed with a distinctive ticked coat.","Ethiopia / Southeast Asia","9-15 years","8-12 lbs (3.6-5.4 kg)","6-8 lbs (2.7-3.6 kg)","8-10 inches (20-25 cm)","shorthair","Dense, silky, fine with distinctive ticking",["Ruddy","Cinnamon","Blue","Fawn"],["Ticked tabby"],["Gold","Green","Hazel"],2,1,5,2,4,4,5,"common",["shorthair","popular","playful","intelligent"],["ticked-coat","ancient-breed","dog-like","climber"],["CFA","TICA","FIFe","GCCF"],["somali","ocicat","bengal","egyptian-mau"],["somali","singapura","oriental-shorthair"],True,1))

BREEDS.append(mk("Aegean","aegean","Felis catus","The Aegean cat is a naturally occurring Greek breed known for its friendly personality and love of water.","Greece (Cycladic Islands)","10-15 years","9-12 lbs (4-5.5 kg)","7-10 lbs (3-4.5 kg)","9-11 inches (23-28 cm)","mediumhair","Semi-long, dense, water-resistant",["White with black","White with red","White with blue","Bicolor","Tricolor"],["Bicolor","Tricolor","Tabby"],["Green","Yellow","Blue","Odd-eyed"],3,2,3,3,4,4,4,"rare",["mediumhair","rare","playful"],["natural-breed","water-loving","greek-origin"],[],["turkish-angora","turkish-van","norwegian-forest-cat"],["turkish-van","maine-coon"],False,100))

BREEDS.append(mk("American Bobtail","american-bobtail","Felis catus","The American Bobtail is a rugged, intelligent breed with a naturally short tail.","United States","13-15 years","12-16 lbs (5.4-7.3 kg)","7-11 lbs (3.2-5 kg)","9-10 inches (23-25 cm)","shorthair","Dense, shaggy, water-resistant double coat",["Brown tabby","Silver tabby","Various colors"],["Tabby","Solid","Tortoiseshell","Bicolor"],["Gold","Green","Copper","Blue"],3,2,3,2,5,5,5,"uncommon",["shorthair","intelligent","playful"],["bobbed-tail","american-origin","dog-like"],["CFA","TICA"],["japanese-bobtail","manx","pixie-bob"],["manx","japanese-bobtail","pixie-bob"],False,10))

BREEDS.append(mk("American Curl","american-curl","Felis catus","The American Curl is known for its uniquely curled-back ears and sweet personality.","United States","12-16 years","7-10 lbs (3.2-4.5 kg)","5-8 lbs (2.3-3.6 kg)","9-12 inches (23-30 cm)","shorthair","Silky, flat-lying with distinctive curled ears",["All colors and patterns accepted"],["Solid","Tabby","Tortoiseshell","Bicolor","Colorpoint"],["All colors accepted","Blue","Green","Gold","Odd-eyed"],2,1,3,3,5,5,4,"uncommon",["shorthair","rare","playful"],["curled-ears","american-origin","family-friendly"],["CFA","TICA"],["scottish-fold","american-shorthair","american-wirehair"],["scottish-fold","munchkin"],False,15))

BREEDS.append(mk("American Shorthair","american-shorthair","Felis catus","The American Shorthair is a sturdy, friendly, and low-maintenance companion with a plush coat.","United States","15-20 years","11-15 lbs (5-6.8 kg)","8-12 lbs (3.6-5.4 kg)","8-10 inches (20-25 cm)","shorthair","Short, dense, and plush with a lustrous sheen",["White","Black","Blue","Red","Cream","Silver"],["Tabby","Solid","Tortoiseshell","Calico","Bicolor"],["Green","Gold","Copper","Blue"],3,2,3,2,5,5,4,"common",["shorthair","popular","playful"],["family-cat","mouser","low-maintenance"],["CFA","TICA","ACFA","CCA-AFC"],["british-shorthair","american-wirehair"],["british-shorthair","bombay","burmese"],True,5))

BREEDS.append(mk("American Wirehair","american-wirehair","Felis catus","The American Wirehair is distinguished by its unique crimped, wiry coat.","United States","12-15 years","8-12 lbs (3.6-5.4 kg)","6-10 lbs (2.7-4.5 kg)","9-11 inches (23-28 cm)","shorthair","Crimped, wiry, and springy; each hair is bent or hooked",["All colors and patterns accepted"],["Tabby","Solid","Tortoiseshell","Bicolor","Calico"],["Gold","Green","Copper","Blue"],2,1,3,3,4,4,4,"rare",["shorthair","rare","playful"],["wiry-coat","american-origin","unique-texture"],["CFA","TICA"],["american-shorthair","selkirk-rex","cornish-rex"],["american-shorthair","devon-rex"],False,100))

BREEDS.append(mk("Australian Mist","australian-mist","Felis catus","The Australian Mist is a gentle, playful breed with a spotted or marbled coat developed in Australia.","Australia","12-16 years","10-14 lbs (4.5-6.4 kg)","7-10 lbs (3.2-4.5 kg)","8-10 inches (20-25 cm)","shorthair","Short, glossy, and resilient",["Brown","Blue","Chocolate","Lilac","Gold","Peach"],["Spotted","Marbled"],["Green","Gold","Aqua"],2,1,3,2,5,5,4,"rare",["shorthair","rare","playful"],["australian-origin","spotted","family-cat"],["ACF","WCF"],["burmese","abyssinian","bengal"],["burmese","ocicat","bengal"],False,100))

BREEDS.append(mk("Balinese","balinese","Felis catus","The Balinese is an elegant longhaired Siamese with a silky coat and striking blue eyes.","United States","12-20 years","5-10 lbs (2.3-4.5 kg)","5-8 lbs (2.3-3.6 kg)","8-11 inches (20-28 cm)","longhair","Silky, fine, medium-length single coat without undercoat",["Seal point","Blue point","Chocolate point","Lilac point"],["Colorpoint"],["Deep blue"],2,2,4,5,4,4,5,"uncommon",["longhair","vocal","intelligent","hypoallergenic"],["siamese-variant","colorpoint","vocal","hypoallergenic"],["CFA","TICA","FIFe","GCCF"],["siamese","oriental-longhair","javanese","himalayan"],["siamese","oriental-longhair","himalayan"],False,20))

BREEDS.append(mk("Bambino","bambino","Felis catus","The Bambino combines Sphynx hairlessness with Munchkin short legs for a tiny, warm companion.","United States","9-14 years","5-9 lbs (2.3-4.1 kg)","4-7 lbs (1.8-3.2 kg)","5-7 inches (13-18 cm)","hairless","Hairless with peach-fuzz down; wrinkled and warm to touch",["All skin colors and patterns"],["Solid","Patterned"],["All colors","Blue","Green","Gold"],1,3,4,2,5,4,4,"very-rare",["hairless","rare","playful"],["hairless","short-legs","designer-breed"],["TICA"],["sphynx","munchkin","minskin","peterbald"],["sphynx","munchkin","minskin"],False,100))

BREEDS.append(mk("Bengal","bengal","Prionailurus bengalensis x Felis catus","The Bengal cat dazzles with a wild leopard-like coat and an energetic, intelligent personality.","United States","12-16 years","10-18 lbs (4.5-8.2 kg)","8-12 lbs (3.6-5.4 kg)","13-16 inches (33-41 cm)","shorthair","Short, dense, pelt-like with remarkable soft feel and glitter effect",["Brown/black tabby","Silver tabby","Snow","Blue"],["Spotted","Marbled","Rosetted"],["Green","Gold","Blue","Aqua"],2,1,5,3,4,4,5,"uncommon",["shorthair","popular","intelligent","playful","large","hypoallergenic"],["wild-look","glitter-coat","active","hypoallergenic"],["TICA","CFA","GCCF","FIFe"],["egyptian-mau","ocicat","savannah","toyger"],["ocicat","egyptian-mau","toyger","savannah"],True,2))

BREEDS.append(mk("Birman","birman","Felis catus","The Birman has blue eyes, white-gloved paws, and a gentle temperament as the Sacred Cat of Burma.","France (possibly Burma)","12-16 years","9-15 lbs (4.1-6.8 kg)","6-10 lbs (2.7-4.5 kg)","8-10 inches (20-25 cm)","longhair","Silky, medium-length single coat without undercoat",["Seal point","Blue point","Chocolate point","Lilac point"],["Colorpoint with white gloves"],["Deep sapphire blue"],2,2,2,2,4,4,4,"uncommon",["longhair","calm","popular"],["white-paws","blue-eyes","sacred-birman","gentle"],["CFA","TICA","FIFe","GCCF"],["ragdoll","himalayan","balinese","siamese"],["ragdoll","himalayan","balinese"],True,8))

BREEDS.append(mk("Bombay","bombay","Felis catus","The Bombay is a sleek, panther-like cat with a glossy black coat and copper eyes.","United States","12-16 years","8-15 lbs (3.6-6.8 kg)","6-12 lbs (2.7-5.4 kg)","9-13 inches (23-33 cm)","shorthair","Short, fine, satiny with patent-leather shine",["Black"],["Solid"],["Copper","Gold"],2,1,3,3,4,4,4,"uncommon",["shorthair","playful"],["panther-look","black-cat","dog-like","lap-cat"],["CFA","TICA"],["burmese","american-shorthair","british-shorthair"],["burmese","havana-brown","british-shorthair"],False,25))

BREEDS.append(mk("British Shorthair","british-shorthair","Felis catus","The British Shorthair is a calm, dignified cat with a plush teddy-bear coat and round features.","United Kingdom","12-20 years","12-17 lbs (5.4-7.7 kg)","7-12 lbs (3.2-5.4 kg)","12-14 inches (30-36 cm)","shorthair","Short, dense, plush, and crisp with firm teddy bear texture",["Blue","Lilac","Chocolate","Cream","Black","White"],["Solid","Tabby","Bicolor","Tortoiseshell","Colorpoint"],["Copper","Gold","Blue","Green"],3,2,2,1,4,4,4,"common",["shorthair","popular","calm","large"],["teddy-bear","chubby-cheeks","calm","independent"],["CFA","TICA","FIFe","GCCF"],["american-shorthair","scottish-fold","chartreux","russian-blue"],["chartreux","russian-blue","american-shorthair"],True,3))

BREEDS.append(mk("Burmese","burmese","Felis catus","The Burmese is a sleek, muscular cat with a people-oriented, affectionate personality.","Burma (Myanmar) / Thailand","12-18 years","8-12 lbs (3.6-5.4 kg)","6-10 lbs (2.7-4.5 kg)","9-13 inches (23-33 cm)","shorthair","Short, fine, glossy, and satin-like with almost no undercoat",["Sable","Champagne","Blue","Platinum"],["Solid"],["Gold","Yellow"],1,1,3,3,5,4,4,"uncommon",["shorthair","popular","playful"],["lap-cat","people-oriented","satin-coat"],["CFA","TICA","FIFe","GCCF"],["bombay","tonkinese","siamese","burmilla"],["bombay","tonkinese","burmilla"],False,30))

BREEDS.append(mk("Burmilla","burmilla","Felis catus","The Burmilla combines Burmese charm with a stunning tipped silver coat for elegant beauty.","United Kingdom","10-15 years","8-12 lbs (3.6-5.4 kg)","6-10 lbs (2.7-4.5 kg)","10-12 inches (25-30 cm)","shorthair","Short, dense, silky with distinctive silver or golden tipping",["Silver tipped","Golden tipped"],["Tipped"],["Green","Gold"],2,2,3,3,4,4,4,"rare",["shorthair","rare","playful"],["tipped-coat","burmese-relative","silver"],["GCCF","FIFe","TICA"],["burmese","chinchilla","asian"],["burmese","chinchilla"],False,100))

BREEDS.append(mk("Chantilly-Tiffany","chantilly-tiffany","Felis catus","The Chantilly-Tiffany is a rare semi-longhair with a rich chocolate coat and golden eyes.","United States","11-15 years","8-14 lbs (3.6-6.4 kg)","6-10 lbs (2.7-4.5 kg)","8-10 inches (20-25 cm)","mediumhair","Semi-long, silky, and soft; does not mat easily",["Chocolate","Cinnamon","Fawn","Blue"],["Solid"],["Gold","Yellow"],2,2,3,2,4,4,4,"very-rare",["mediumhair","rare","calm"],["chocolate-coat","rare-breed","semi-longhair"],["ACFA"],["burmese","havana-brown","turkish-angora"],["burmese","havana-brown"],False,100))

BREEDS.append(mk("Chartreux","chartreux","Felis catus","The Chartreux is a rare French breed with a blue-gray wooly coat and copper eyes.","France","12-15 years","10-16 lbs (4.5-7.3 kg)","7-11 lbs (3.2-5 kg)","9-11 inches (23-28 cm)","shorthair","Medium-short, wooly, dense double coat with plush texture",["Blue-gray"],["Solid"],["Copper","Gold"],3,2,2,1,4,4,5,"rare",["shorthair","rare","calm","large"],["french-origin","blue-coat","wooly","quiet"],["CFA","TICA","FIFe","GCCF"],["british-shorthair","russian-blue","korat"],["british-shorthair","russian-blue","korat"],False,100))

BREEDS.append(mk("Cheetoh","cheetoh","Felis catus","The Cheetoh is a large hybrid breed combining Bengal spots with Ocicat size for a wild look.","United States","12-16 years","15-23 lbs (6.8-10.4 kg)","12-18 lbs (5.4-8.2 kg)","12-18 inches (30-46 cm)","shorthair","Short, soft, dense, and rosetted like a wild cat",["Brown spotted","Silver spotted","Snow spotted","Gold spotted"],["Spotted/Rosetted"],["Green","Gold","Hazel","Blue"],2,1,4,2,4,4,5,"very-rare",["shorthair","rare","large","playful","intelligent"],["rosetted","large","bengal-ocicat-hybrid"],["TICA"],["bengal","ocicat","savannah","toyger"],["bengal","savannah","ocicat"],False,100))

BREEDS.append(mk("Colorpoint Shorthair","colorpoint-shorthair","Felis catus","The Colorpoint Shorthair is a Siamese in non-traditional point colors with elegance and voice.","United States","12-15 years","8-12 lbs (3.6-5.4 kg)","5-10 lbs (2.3-4.5 kg)","8-10 inches (20-25 cm)","shorthair","Very short, fine, glossy, and close-lying",["Red point","Cream point","Lynx point","Tortie point"],["Colorpoint"],["Deep vivid blue"],1,1,4,5,4,3,5,"uncommon",["shorthair","vocal","intelligent","playful"],["colorpoint","siamese-relative","vocal"],["CFA","TICA"],["siamese","balinese","oriental-shorthair","javanese"],["siamese","balinese"],False,100))

BREEDS.append(mk("Cornish Rex","cornish-rex","Felis catus","The Cornish Rex has a distinctive wavy velvet coat and an active, playful, intelligent personality.","United Kingdom (Cornwall)","12-15 years","6-10 lbs (2.7-4.5 kg)","5-8 lbs (2.3-3.6 kg)","8-12 inches (20-30 cm)","shorthair","Short, soft, wavy, plush like crushed velvet; no guard hairs",["All colors and patterns"],["Solid","Tabby","Tortoiseshell","Bicolor","Colorpoint"],["All colors","Gold","Green","Blue"],1,1,5,3,5,5,5,"uncommon",["shorthair","hypoallergenic","playful","intelligent"],["curly-coat","hypoallergenic","rex","velvet-coat"],["CFA","TICA","FIFe","GCCF"],["devon-rex","selkirk-rex","sphynx"],["devon-rex","selkirk-rex"],False,35))

BREEDS.append(mk("Cymric","cymric","Felis catus","The Cymric is the longhaired variety of the Manx, with a rounded appearance and tailless gene.","Isle of Man / Canada","8-14 years","10-14 lbs (4.5-6.4 kg)","8-10 lbs (3.6-4.5 kg)","7-10 inches (18-25 cm)","longhair","Medium-long, dense, and plush double coat",["All colors and patterns"],["Tabby","Solid","Tortoiseshell","Calico","Bicolor"],["Gold","Copper","Green","Hazel","Blue"],3,3,3,2,5,5,5,"uncommon",["longhair","rare","playful","intelligent"],["tailless","manx-variant","plush-coat","rounded"],["CFA","TICA"],["manx","japanese-bobtail","american-bobtail"],["manx","american-bobtail"],False,100))

BREEDS.append(mk("Devon Rex","devon-rex","Felis catus","The Devon Rex sports large bat-like ears, a wavy coat, and an impish, people-loving personality.","United Kingdom (Devon)","10-15 years","6-9 lbs (2.7-4.1 kg)","5-8 lbs (2.3-3.6 kg)","10-12 inches (25-30 cm)","shorthair","Short, soft, wavy, and curly; extremely fine texture",["All colors and patterns"],["Solid","Tabby","Tortoiseshell","Bicolor","Colorpoint"],["All colors"],1,1,5,3,5,5,5,"uncommon",["shorthair","hypoallergenic","playful","intelligent"],["bat-ears","pixie-face","hypoallergenic","rex"],["CFA","TICA","FIFe","GCCF"],["cornish-rex","selkirk-rex","sphynx"],["cornish-rex","sphynx"],False,40))

BREEDS.append(mk("Don Sphynx","don-sphynx","Felis catus","The Don Sphynx (Donskoy) is a hairless breed from Russia with a unique, affectionate personality.","Russia","12-15 years","8-12 lbs (3.6-5.4 kg)","6-10 lbs (2.7-4.5 kg)","9-12 inches (23-30 cm)","hairless","Hairless with wrinkled skin; some have light peach fuzz in winter",["Skin-colored","Any skin pattern"],["Solid","Patterned skin"],["All colors"],1,3,4,3,4,4,5,"rare",["hairless","rare","hypoallergenic","intelligent"],["hairless","russian-origin","unique","hypoallergenic"],["TICA","FIFe"],["sphynx","peterbald","bambino"],["sphynx","peterbald"],False,100))

print(f"Total breeds in data: {len(BREEDS)}")
print("First 3 breeds:", BREEDS[0]['name'], BREEDS[1]['name'], BREEDS[2]['name'])