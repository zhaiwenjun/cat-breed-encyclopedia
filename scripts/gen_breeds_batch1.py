#!/usr/bin/env python3
"""Generate breed markdown files for Cat Breed Encyclopedia."""
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
    yaml += "---\n\n"
    yaml += b.get("body", "")
    path = os.path.join(BREEDS_DIR, f"{b['slug']}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(yaml)
    return b['name']

def gen_body(b):
    coat = b['coatLength']
    coat_label = {"hairless":"hairless","shorthair":"short","mediumhair":"semi-long","longhair":"long"}[coat]
    rare = b['rarity']
    c = b['colors'][0]
    p = b['patterns'][0]
    e = b['eyeColors'][0]
    el = b['energyLevel']
    vl = b['vocalizationLevel']
    intel = b['intelligence']
    cf = b['childFriendly']
    pf = b['petFriendly']
    sl = b['sheddingLevel']
    gn = b['groomingNeeds']
    n = b['name']
    o = b['origin']
    ls = b['lifespan']
    wm = b['weight']['male']
    wf = b['weight']['female']
    h = b['height']
    ct = b['coatType']

    energy_txt = "highly energetic" if el >= 4 else ("moderately active" if el >= 3 else "calm and relaxed")
    aff_txt = "very affectionate" if cf >= 4 else "moderately affectionate"
    kid_txt = "excellent with children and other pets" if cf >= 4 and pf >= 4 else ("good with respectful children" if cf >= 3 else "best suited to quiet households")
    intel_txt = "high" if intel >= 4 else "moderate"
    intel_play = "enjoy interactive play and puzzle toys" if intel >= 4 else "appreciate simple toys and games"
    vocal_txt = "high" if vl >= 4 else ("moderate" if vl >= 3 else "low")
    vocal_verb = "are quite talkative and expressive" if vl >= 4 else ("communicate as needed" if vl >= 3 else "tend to be quiet and soft-spoken")
    rarity_txt = f"a {rare.replace('-',' ')} breed" if rare != "common" else "a widely available breed"

    if coat == "longhair":
        groom_txt = "requires daily brushing to prevent mats and tangles. Regular professional grooming every 4-6 weeks is recommended. Pay special attention to the ruff, belly, and tail areas."
    elif coat == "mediumhair":
        groom_txt = "needs brushing 2-3 times per week to prevent tangles and reduce shedding. The semi-long coat is relatively easy to maintain with a regular routine."
    elif coat == "shorthair":
        groom_txt = "requires minimal grooming. A weekly brushing with a soft brush or grooming glove is sufficient to remove loose hair and keep the coat glossy. These cats are fastidious self-groomers."
    else:
        groom_txt = "requires special care for their hairless body, including weekly bathing to remove skin oil buildup, protection from sun exposure, and warmth in cold weather."

    pros = []
    if intel >= 4: pros.append("Highly intelligent and trainable")
    if cf >= 4 and pf >= 4: pros.append("Excellent with children and other pets")
    if gn <= 2: pros.append("Low-maintenance grooming")
    if el <= 3: pros.append("Calm, adaptable personality")
    pros.append(f"Distinctive, beautiful {coat_label} coat")
    if rare != "common": pros.append("Rare and unique breed")

    cons = []
    if el >= 4: cons.append("High energy requires significant daily playtime and stimulation")
    if sl >= 3: cons.append("Moderate to heavy shedding requires regular cleaning")
    if gn >= 3: cons.append("Higher grooming maintenance needed")
    if vl >= 4: cons.append("Can be very vocal, which may not suit quiet households")
    if rare != "common": cons.append("May be difficult to find and more expensive")
    if el <= 2: cons.append("Low energy may not suit active families seeking a playful cat")

    body = f"""## History & Origin

The {n} originated in {o}. This distinctive breed has captured the hearts of cat lovers with its unique combination of striking appearance and engaging personality. The breed was developed and refined by dedicated breeders who carefully selected for the traits that define the {n} today.

Whether prized for their working abilities, stunning looks, or wonderful temperament, the {n} has established itself as {rarity_txt} with a devoted following among cat enthusiasts worldwide.

## Appearance & Physical Traits

The {n} is a beautiful breed with a {coat_label} coat characterized by {ct.lower()}. The breed displays a stunning range of colors including {c.lower()}, with {p.lower()} patterns that enhance their visual appeal. Their eyes typically present as {e.lower()}, adding to their distinctive and captivating expression.

Males typically weigh {wm}, while females average {wf}. The breed stands approximately {h} at the shoulder. These cats have a well-balanced, proportional build that reflects their breed heritage.

The coat is one of the breed's most defining features — {ct.lower()}. This coat type contributes significantly to the breed's overall appearance and care requirements.

## Personality & Temperament

The {n} is a {energy_txt} companion with an engaging personality. They form strong bonds with their families and are {aff_txt} with those they trust. These cats are {kid_txt}.

With {intel_txt} intelligence, {n} cats {intel_play}. They thrive on interaction and mental stimulation. Their vocalization level is {vocal_txt}, meaning they {vocal_verb}.

The breed adapts {'well' if el <= 3 else 'best to active households that can provide plenty of playtime and attention'} to home living. They {('enjoy being lap cats and calm companionship' if el <= 2 else 'are playful and engaged companions' if el >= 4 else 'strike a nice balance between playfulness and relaxation')}.

## Care & Grooming Guide

The {n} {groom_txt}

Shedding Level: {sl}/5. Grooming Needs: {gn}/5.

Beyond coat care, these cats need standard feline maintenance: regular nail trimming, dental hygiene with brushing and veterinary checkups, and a clean litter box. Provide scratching posts of various textures and climbing structures to satisfy natural instincts.

## Health & Lifespan

The {n} typically enjoys a lifespan of {ls}. With proper care, regular veterinary checkups, a high-quality diet, and an indoor lifestyle, many individuals live toward the upper end of this range.

Like all breeds, the {n} may be predisposed to certain health conditions. Reputable breeders screen for known genetic issues. Maintaining a healthy weight, providing dental care, and keeping vaccinations current all contribute to a long, healthy life.

## Diet & Nutrition

Feed your {n} a high-quality, protein-rich cat food appropriate for their life stage (kitten, adult, or senior). Portion control is important, as some individuals may tend to overeat. Always provide fresh, clean water. Some cats enjoy puzzle feeders that make mealtime mentally enriching.

## Exercise Needs

{'The ' + n + ' needs plenty of physical activity and mental stimulation. Provide cat trees, interactive toys, puzzle feeders, and dedicated play sessions. These active cats thrive in homes where someone can engage them in play daily. Without adequate stimulation, they may become bored or destructive.' if el >= 4 else 'The ' + n + ' benefits from daily interactive play sessions to stay healthy and happy. Wand toys, laser pointers, and fetch games are great options. A cat tree by a window provides entertainment and enrichment throughout the day.' if el >= 3 else 'The ' + n + ' has relatively low exercise needs. Short daily play sessions with wand toys or balls are sufficient. They enjoy lounging in sunny spots and watching the world from a window perch.'}

## Is This Breed Right For You?

**Pros:**
{chr(10).join('- ' + p for p in pros)}

**Cons:**
{chr(10).join('- ' + c for c in cons)}

## Fun Facts

1. The {n} is one of the most visually distinctive cat breeds in the world.
2. Their {coat_label} coat is an adaptation to their origins in {o}.
3. These cats form deep, lasting bonds with their human families.
4. The breed's unique combination of traits makes them memorable companions.
5. {n} cats are celebrated for their {('playful, energetic nature' if el >= 4 else 'calm, steady temperament' if el <= 2 else 'balanced, adaptable personality')}.
"""
    return body

# Build breed data
def mk(n, slug, sci, desc, origin, lifespan, wm, wf, h, coat, ct, colors, patterns, eyes,
       sl, gn, el, vl, cf, pf, intel, rarity, cats, tags, rec, rel, sim, feat, order):
    meta_title = f"{n} Cat Breed: Info, Pictures, Care & Facts"
    return {
        'name': n, 'slug': slug, 'scientificName': sci,
        'metaTitle': meta_title, 'metaDescription': desc,
        'featuredImage': f'/images/breeds/{slug}.webp',
        'featuredImageAlt': f'{n} cat with {coat} coat',
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

BREEDS = []
B = BREEDS.append  # shorthand

# === A ===
B(mk("Abyssinian","abyssinian","Felis catus","The Abyssinian is an active, intelligent, and social cat breed with a distinctive ticked coat. Learn about Abyssinian personality, care, health, and more.","Ethiopia / Southeast Asia","9-15 years","8-12 lbs (3.6-5.4 kg)","6-8 lbs (2.7-3.6 kg)","8-10 inches (20-25 cm)","shorthair","Dense, silky, fine with distinctive ticking",["Ruddy","Cinnamon","Blue","Fawn"],["Ticked tabby"],["Gold","Green","Hazel"],2,1,5,2,4,4,5,"common",["shorthair","popular","playful","intelligent"],["ticked-coat","ancient-breed","dog-like","climber"],["CFA","TICA","FIFe","GCCF"],["somali","ocicat","bengal","egyptian-mau"],["somali","singapura","oriental-shorthair"],True,1))

B(mk("Aegean","aegean","Felis catus","The Aegean cat is a naturally occurring Greek breed known for its friendly personality and love of water. Discover this rare Mediterranean breed.","Greece (Cycladic Islands)","10-15 years","9-12 lbs (4-5.5 kg)","7-10 lbs (3-4.5 kg)","9-11 inches (23-28 cm)","mediumhair","Semi-long, dense, water-resistant",["White with black","White with red","White with blue","Bicolor","Tricolor"],["Bicolor","Tricolor","Tabby"],["Green","Yellow","Blue","Odd-eyed"],3,2,3,3,4,4,4,"rare",["mediumhair","rare","playful"],["natural-breed","water-loving","greek-origin"],[],["turkish-angora","turkish-van","norwegian-forest-cat"],["turkish-van","maine-coon"],False,100))

B(mk("American Bobtail","american-bobtail","Felis catus","The American Bobtail is a rugged, intelligent breed with a naturally short tail. Learn about this distinctive American breed's personality, grooming, and care.","United States","13-15 years","12-16 lbs (5.4-7.3 kg)","7-11 lbs (3.2-5 kg)","9-10 inches (23-25 cm)","shorthair","Dense, shaggy, water-resistant double coat",["Brown tabby","Silver tabby","Various colors"],["Tabby","Solid","Tortoiseshell","Bicolor"],["Gold","Green","Copper","Blue"],3,2,3,2,5,5,5,"uncommon",["shorthair","intelligent","playful"],["bobbed-tail","american-origin","dog-like"],["CFA","TICA"],["japanese-bobtail","manx","pixie-bob"],["manx","japanese-bobtail","pixie-bob"],False,10))

B(mk("American Curl","american-curl","Felis catus","The American Curl is known for its uniquely curled-back ears and sweet personality. Learn about this distinctive breed's care, temperament, and health.","United States","12-16 years","7-10 lbs (3.2-4.5 kg)","5-8 lbs (2.3-3.6 kg)","9-12 inches (23-30 cm)","shorthair","Silky, flat-lying with curled ears",["All colors and patterns accepted"],["Solid","Tabby","Tortoiseshell","Bicolor","Colorpoint"],["All colors accepted","Blue","Green","Gold","Odd-eyed"],2,1,3,3,5,5,4,"uncommon",["shorthair","rare","playful"],["curled-ears","american-origin","family-friendly"],["CFA","TICA"],["scottish-fold","american-shorthair","american-wirehair"],["scottish-fold","munchkin"],False,15))

B(mk("American Shorthair","american-shorthair","Felis catus","The American Shorthair is a sturdy, friendly, and low-maintenance companion. Learn about its history, temperament, grooming needs, and health in our complete guide.","United States","15-20 years","11-15 lbs (5-6.8 kg)","8-12 lbs (3.6-5.4 kg)","8-10 inches (20-25 cm)","shorthair","Short, dense, and plush with a lustrous sheen",["White","Black","Blue","Red","Cream","Silver"],["Tabby","Solid","Tortoiseshell","Calico","Bicolor"],["Green","Gold","Copper","Blue"],3,2,3,2,5,5,4,"common",["shorthair","popular","playful"],["family-cat","mouser","low-maintenance"],["CFA","TICA","ACFA","CCA-AFC"],["british-shorthair","american-wirehair"],["british-shorthair","bombay","burmese"],True,5))

B(mk("American Wirehair","american-wirehair","Felis catus","The American Wirehair is distinguished by its unique crimped, wiry coat. Discover this rare American breed's personality and care needs.","United States","12-15 years","8-12 lbs (3.6-5.4 kg)","6-10 lbs (2.7-4.5 kg)","9-11 inches (23-28 cm)","shorthair","Crimped, wiry, and springy; each hair is bent or hooked",["All colors and patterns accepted"],["Tabby","Solid","Tortoiseshell","Bicolor","Calico"],["Gold","Green","Copper","Blue"],2,1,3,3,4,4,4,"rare",["shorthair","rare","playful"],["wiry-coat","american-origin","unique-texture"],["CFA","TICA"],["american-shorthair","selkirk-rex","cornish-rex"],["american-shorthair","devon-rex"],False,100))

B(mk("Australian Mist","australian-mist","Felis catus","The Australian Mist is a gentle, playful breed developed in Australia with a spotted or marbled coat. Discover this affectionate breed.","Australia","12-16 years","10-14 lbs (4.5-6.4 kg)","7-10 lbs (3.2-4.5 kg)","8-10 inches (20-25 cm)","shorthair","Short, glossy, and resilient",["Brown","Blue","Chocolate","Lilac","Gold","Peach"],["Spotted","Marbled"],["Green","Gold","Aqua"],2,1,3,2,5,5,4,"rare",["shorthair","rare","playful"],["australian-origin","spotted","family-cat"],["ACF","WCF"],["burmese","abyssinian","bengal"],["burmese","ocicat","bengal"],False,100))

# === B ===
B(mk("Balinese","balinese","Felis catus","The Balinese is an elegant longhaired Siamese with a silky coat and striking blue eyes. Learn about this vocal, affectionate breed.","United States","12-20 years","5-10 lbs (2.3-4.5 kg)","5-8 lbs (2.3-3.6 kg)","8-11 inches (20-28 cm)","longhair","Silky, fine, medium-length single coat without undercoat",["Seal point","Blue point","Chocolate point","Lilac point"],["Colorpoint"],["Deep blue"],2,2,4,5,4,4,5,"uncommon",["longhair","vocal","intelligent","hypoallergenic"],["siamese-variant","colorpoint","vocal","hypoallergenic"],["CFA","TICA","FIFe","GCCF"],["siamese","oriental-longhair","javanese","himalayan"],["siamese","oriental-longhair","himalayan"],False,20))

B(mk("Bengal","bengal","Prionailurus bengalensis x Felis catus","The Bengal cat dazzles with a wild leopard-like coat and an energetic, intelligent personality. Learn about Bengal care, temperament, and more.","United States","12-16 years","10-18 lbs (4.5-8.2 kg)","8-12 lbs (3.6-5.4 kg)","13-16 inches (33-41 cm)","shorthair","Short, dense, and pelt-like with remarkable soft, silky feel and glitter effect",["Brown/black tabby","Silver tabby","Snow","Blue"],["Spotted","Marbled","Rosetted"],["Green","Gold","Blue","Aqua"],2,1,5,3,4,4,5,"uncommon",["shorthair","popular","intelligent","playful","large","hypoallergenic"],["wild-look","glitter-coat","active","hypoallergenic"],["TICA","CFA","GCCF","FIFe"],["egyptian-mau","ocicat","savannah","toyger"],["ocicat","egyptian-mau","toyger","savannah"],True,2))

B(mk("Birman","birman","Felis catus","The Birman, known as the Sacred Cat of Burma, has blue eyes, white-gloved paws, and a gentle temperament. Discover this beautiful breed.","France (possibly Burma)","12-16 years","9-15 lbs (4.1-6.8 kg)","6-10 lbs (2.7-4.5 kg)","8-10 inches (20-25 cm)","longhair","Silky, medium-length single coat without undercoat",["Seal point","Blue point","Chocolate point","Lilac point"],["Colorpoint with white gloves"],["Deep sapphire blue"],2,2,2,2,4,4,4,"uncommon",["longhair","calm","popular"],["white-paws","blue-eyes","sacred-birman","gentle"],["CFA","TICA","FIFe","GCCF"],["ragdoll","himalayan","balinese","siamese"],["ragdoll","himalayan","balinese"],True,8))

B(mk("Bombay","bombay","Felis catus","The Bombay is a sleek, panther-like cat with a glossy black coat and copper eyes. Discover this affectionate, dog-like breed.","United States","12-16 years","8-15 lbs (3.6-6.8 kg)","6-12 lbs (2.7-5.4 kg)","9-13 inches (23-33 cm)","shorthair","Short, fine, satiny with patent-leather shine",["Black"],["Solid"],["Copper","Gold"],2,1,3,3,4,4,4,"uncommon",["shorthair","playful"],["panther-look","black-cat","dog-like","lap-cat"],["CFA","TICA"],["burmese","american-shorthair","british-shorthair"],["burmese","havana-brown","british-shorthair"],False,25))

B(mk("British Shorthair","british-shorthair","Felis catus","The British Shorthair is a calm, dignified cat with a plush teddy-bear coat. Discover this easygoing breed's care and temperament.","United Kingdom","12-20 years","12-17 lbs (5.4-7.7 kg)","7-12 lbs (3.2-5.4 kg)","12-14 inches (30-36 cm)","shorthair","Short, dense, plush, and crisp with firm teddy bear texture",["Blue","Lilac","Chocolate","Cream","Black","White"],["Solid","Tabby","Bicolor","Tortoiseshell","Colorpoint"],["Copper","Gold","Blue","Green"],3,2,2,1,4,4,4,"common",["shorthair","popular","calm","large"],["teddy-bear","chubby-cheeks","calm","independent"],["CFA","TICA","FIFe","GCCF"],["american-shorthair","scottish-fold","chartreux","russian-blue"],["chartreux","russian-blue","american-shorthair"],True,3))

B(mk("Burmese","burmese","Felis catus","The Burmese is a sleek, muscular cat with a people-oriented personality. Discover this affectionate breed's care and temperament.","Burma (Myanmar) / Thailand","12-18 years","8-12 lbs (3.6-5.4 kg)","6-10 lbs (2.7-4.5 kg)","9-13 inches (23-33 cm)","shorthair","Short, fine, glossy, and satin-like with almost no undercoat",["Sable","Champagne","Blue","Platinum"],["Solid"],["Gold","Yellow"],1,1,3,3,5,4,4,"uncommon",["shorthair","popular","playful"],["lap-cat","people-oriented","satin-coat"],["CFA","TICA","FIFe","GCCF"],["bombay","tonkinese","siamese","burmilla"],["bombay","tonkinese","burmilla"],False,30))

B(mk("Burmilla","burmilla","Felis catus","The Burmilla combines Burmese charm with a stunning tipped silver coat. Discover this elegant, playful, and affectionate breed.","United Kingdom","10-15 years","8-12 lbs (3.6-5.4 kg)","6-10 lbs (2.7-4.5 kg)","10-12 inches (25-30 cm)","shorthair","Short, dense, silky with distinctive tipping",["Silver tipped","Golden tipped"],["Tipped"],["Green","Gold"],2,2,3,3,4,4,4,"rare",["shorthair","rare","playful"],["tipped-coat","burmese-relative","silver"],["GCCF","FIFe","TICA"],["burmese","chinchilla","asian"],["burmese","chinchilla"],False,100))

# === C ===
B(mk("Chartreux","chartreux","Felis catus","The Chartreux is a rare French breed with a blue-gray wooly coat and copper eyes. Discover this quiet, observant ancient breed.","France","12-15 years","10-16 lbs (4.5-7.3 kg)","7-11 lbs (3.2-5 kg)","9-11 inches (23-28 cm)","shorthair","Medium-short, wooly, dense double coat with plush texture",["Blue-gray"],["Solid"],["Copper","Gold"],3,2,2,1,4,4,5,"rare",["shorthair","rare","calm","large"],["french-origin","blue-coat","wooly","quiet"],["CFA","TICA","FIFe","GCCF"],["british-shorthair","russian-blue","korat"],["british-shorthair","russian-blue","korat"],False,100))

B(mk("Cornish Rex","cornish-rex","Felis catus","The Cornish Rex has a distinctive wavy, down-soft coat and an active, playful personality. Learn about this unique curly-coated breed.","United Kingdom (Cornwall)","12-15 years","6-10 lbs (2.7-4.5 kg)","5-8 lbs (2.3-3.6 kg)","8-12 inches (20-30 cm)","shorthair","Short, soft, wavy, plush like crushed velvet; no guard hairs",["All colors and patterns"],["Solid","Tabby","Tortoiseshell","Bicolor","Colorpoint"],["All colors","Gold","Green","Blue"],1,1,5,3,5,5,5,"uncommon",["shorthair","hypoallergenic","playful","intelligent"],["curly-coat","hypoallergenic","rex","velvet-coat"],["CFA","TICA","FIFe","GCCF"],["devon-rex","selkirk-rex","sphynx"],["devon-rex","selkirk-rex"],False,35))

B(mk("Cymric","cymric","Felis catus","The Cymric is the longhaired variety of the Manx, with a rounded appearance and tailless gene. Discover this plush, dog-like breed.","Isle of Man / Canada","8-14 years","10-14 lbs (4.5-6.4 kg)","8-10 lbs (3.6-4.5 kg)","7-10 inches (18-25 cm)","longhair","Medium-long, dense, and plush double coat",["All colors and patterns"],["Tabby","Solid","Tortoiseshell","Calico","Bicolor"],["Gold","Copper","Green","Hazel","Blue"],3,3,3,2,5,5,5,"uncommon",["longhair","rare","playful","intelligent"],["tailless","manx-variant","plush-coat","rounded"],["CFA","TICA"],["manx","japanese-bobtail","american-bobtail"],["manx","american-bobtail"],False,100))

# === D ===
B(mk("Devon Rex","devon-rex","Felis catus","The Devon Rex sports large bat-like ears, a wavy coat, and an impish personality. Discover this mischievous, people-loving breed.","United Kingdom (Devon)","10-15 years","6-9 lbs (2.7-4.1 kg)","5-8 lbs (2.3-3.6 kg)","10-12 inches (25-30 cm)","shorthair","Short, soft, wavy, and curly; extremely fine texture",["All colors and patterns"],["Solid","Tabby","Tortoiseshell","Bicolor","Colorpoint"],["All colors"],1,1,5,3,5,5,5,"uncommon",["shorthair","hypoallergenic","playful","intelligent"],["bat-ears","pixie-face","hypoallergenic","rex"],["CFA","TICA","FIFe","GCCF"],["cornish-rex","selkirk-rex","sphynx"],["cornish-rex","sphynx"],False,40))

B(mk("Don Sphynx","don-sphynx","Felis catus","The Don Sphynx (Donskoy) is a hairless breed from Russia with a unique, affectionate personality. Discover this distinctive, warm-to-touch companion.","Russia","12-15 years","8-12 lbs (3.6-5.4 kg)","6-10 lbs (2.7-4.5 kg)","9-12 inches (23-30 cm)","hairless","Hairless with wrinkled skin; some have light peach fuzz in winter",["Skin-colored","Any skin pattern"],["Solid","Patterned skin"],["All colors"],1,3,4,3,4,4,5,"rare",["hairless","rare","hypoallergenic","intelligent"],["hairless","russian-origin","unique","hypoallergenic"],["TICA","FIFe"],["sphynx","peterbald","bambino"],["sphynx","peterbald"],False,100))

# === E ===
B(mk("Egyptian Mau","egyptian-mau","Felis catus","The Egyptian Mau is the only naturally spotted domestic cat breed, with gooseberry green eyes and incredible speed. Discover this ancient breed.","Egypt","12-15 years","8-14 lbs (3.6-6.4 kg)","6-10 lbs (2.7-4.5 kg)","8-10 inches (20-25 cm)","shorthair","Medium-short, silky, fine with glossy sheen",["Silver","Bronze","Smoke"],["Spotted tabby"],["Gooseberry green"],2,1,4,3,3,3,5,"rare",["shorthair","rare","intelligent","playful"],["spotted","fastest-domestic-cat","ancient-breed"],["CFA","TICA","FIFe"],["abyssinian","bengal","ocicat","savannah"],["bengal","ocicat","abyssinian"],False,100))

B(mk("European Shorthair","european-shorthair","Felis catus","The European Shorthair is a natural breed from Europe with a sturdy build and excellent hunting abilities. Discover this hardy breed.","Europe (Sweden/Finland)","15-20 years","9-14 lbs (4.1-6.4 kg)","7-11 lbs (3.2-5 kg)","9-11 inches (23-28 cm)","shorthair","Short, dense, glossy, and weather-resistant",["All natural colors"],["Tabby","Solid","Tortoiseshell","Bicolor"],["Green","Gold","Copper","Blue","Odd-eyed"],3,1,4,2,4,4,4,"common",["shorthair","popular","playful"],["natural-breed","european-origin","mouser","hardy"],["FIFe","WCF"],["american-shorthair","british-shorthair"],["american-shorthair","british-shorthair"],False,100))

B(mk("Exotic Shorthair","exotic-shorthair","Felis catus","The Exotic Shorthair is essentially a short-haired Persian with the same sweet personality. Discover this easy-care Persian alternative.","United States","12-15 years","9-14 lbs (4.1-6.4 kg)","7-12 lbs (3.2-5.4 kg)","10-12 inches (25-30 cm)","shorthair","Short, thick, dense, plush, and soft",["All colors and patterns"],["Solid","Tabby","Tortoiseshell","Bicolor","Colorpoint"],["Copper","Gold","Blue","Odd-eyed"],3,2,2,1,4,4,3,"uncommon",["shorthair","calm","popular"],["flat-face","persian-relative","low-energy"],["CFA","TICA","FIFe","GCCF"],["persian","british-shorthair","scottish-fold"],["persian","british-shorthair"],False,45))

# === F ===
B(mk("Foldex","foldex","Felis catus","The Foldex combines folded ears with a round, plush body. Discover this uniquely Canadian breed's sweet personality.","Canada","12-15 years","7-13 lbs (3.2-5.9 kg)","6-10 lbs (2.7-4.5 kg)","8-10 inches (20-25 cm)","shorthair","Short, dense, and plush",["All colors and patterns"],["Solid","Tabby","Tortoiseshell","Bicolor","Colorpoint"],["All colors"],3,2,2,2,4,4,4,"rare",["shorthair","rare","calm"],["folded-ears","canadian-origin","plush"],["CCA-AFC"],["scottish-fold","exotic-shorthair","british-shorthair"],["scottish-fold","exotic-shorthair"],False,100))

# === G ===
B(mk("German Rex","german-rex","Felis catus","The German Rex is one of the oldest curly-coated breeds with a silky, wavy coat and gentle personality. Discover this rare breed.","Germany","10-15 years","7-10 lbs (3.2-4.5 kg)","5-8 lbs (2.3-3.6 kg)","8-10 inches (20-25 cm)","shorthair","Short, silky, and wavy with a plush feel",["All colors and patterns"],["Solid","Tabby","Tortoiseshell","Bicolor"],["All colors"],1,1,4,3,4,4,5,"very-rare",["shorthair","rare","hypoallergenic","playful"],["curly-coat","german-origin","rex","hypoallergenic"],["FIFe","WCF"],["cornish-rex","devon-rex","selkirk-rex"],["cornish-rex","devon-rex"],False,100))

# === H ===
B(mk("Havana Brown","havana-brown","Felis catus","The Havana Brown is a rare breed with a stunning mahogany-brown coat and green eyes. Discover this charming, people-oriented breed.","United Kingdom","12-15 years","6-10 lbs (2.7-4.5 kg)","5-8 lbs (2.3-3.6 kg)","8-10 inches (20-25 cm)","shorthair","Short to medium, smooth, glossy, and rich",["Mahogany brown","Chestnut brown"],["Solid"],["Green"],2,1,3,3,4,4,4,"very-rare",["shorthair","rare"],["brown-coat","rare-breed","people-oriented"],["CFA","TICA"],["siamese","burmese","russian-blue"],["burmese","bombay"],False,100))

B(mk("Himalayan","himalayan","Felis catus","The Himalayan is a Persian with Siamese colorpoints, combining a luxurious long coat with striking blue eyes. Discover this calm breed.","United States","9-15 years","9-14 lbs (4.1-6.4 kg)","7-11 lbs (3.2-5 kg)","10-12 inches (25-30 cm)","longhair","Long, thick, silky, and flowing with dense undercoat",["Seal point","Blue point","Chocolate point","Lilac point","Flame point","Cream point"],["Colorpoint"],["Deep blue"],4,5,2,2,3,3,3,"common",["longhair","popular","calm"],["colorpoint","persian-type","flat-face","blue-eyes"],["CFA","TICA","FIFe","GCCF"],["persian","siamese","ragdoll","birman"],["persian","ragdoll","birman"],False,50))

# === J ===
B(mk("Japanese Bobtail","japanese-bobtail","Felis catus","The Japanese Bobtail has a distinctive pom-pom tail and is a symbol of good luck in Japan. Discover this active, vocal breed.","Japan","12-16 years","6-10 lbs (2.7-4.5 kg)","5-8 lbs (2.3-3.6 kg)","8-9 inches (20-23 cm)","shorthair","Soft, silky, and medium-short without noticeable undercoat",["Calico","Bicolor","Tortoiseshell","Solid"],["Calico","Bicolor","Tortoiseshell","Tabby","Solid"],["All colors","Odd-eyed common"],2,1,5,4,5,4,5,"rare",["shorthair","rare","playful","vocal"],["bobbed-tail","lucky-cat","japanese-origin","pom-pom-tail"],["CFA","TICA","FIFe"],["american-bobtail","manx","kurilian-bobtail"],["american-bobtail","manx"],False,100))

B(mk("Javanese","javanese","Felis catus","The Javanese is a colorpoint longhair breed related to the Balinese and Siamese. Discover this elegant, vocal, and intelligent breed.","United States","10-15 years","5-10 lbs (2.3-4.5 kg)","5-8 lbs (2.3-3.6 kg)","8-10 inches (20-25 cm)","longhair","Silky, fine, medium-length single coat",["Lynx point","Tortie point","Red/Cream point"],["Colorpoint with lynx or tortie markings"],["Deep blue"],2,2,4,4,4,4,5,"rare",["longhair","vocal","intelligent"],["colorpoint","siamese-relative","balinese-relative"],["CFA"],["balinese","siamese","oriental-longhair"],["balinese","oriental-longhair","siamese"],False,100))

# === K ===
B(mk("Khao Manee","khao-manee","Felis catus","The Khao Manee is an ancient Thai breed with a pure white coat and striking eyes. Discover this royal 'White Gem' breed.","Thailand","10-14 years","8-12 lbs (3.6-5.4 kg)","6-8 lbs (2.7-3.6 kg)","10-12 inches (25-30 cm)","shorthair","Short, smooth, close-lying, and glossy",["Pure white"],["Solid white"],["Blue","Gold","Green","Odd-eyed"],2,1,3,3,4,4,4,"very-rare",["shorthair","rare","intelligent"],["white-cat","thai-origin","odd-eyed","royal-breed"],["TICA","CFA"],["siamese","oriental-shorthair","turkish-angora"],["turkish-angora","foreign-white"],False,100))

B(mk("Korat","korat","Felis catus","The Korat is a rare Thai breed with a heart-shaped face and silver-blue coat symbolizing good fortune. Discover this ancient, affectionate breed.","Thailand","10-15 years","6-10 lbs (2.7-4.5 kg)","5-8 lbs (2.3-3.6 kg)","9-13 inches (23-33 cm)","shorthair","Short, fine, glossy with silver tips creating halo effect",["Silver-tipped blue"],["Solid with silver tipping"],["Peridot green"],2,1,3,3,3,3,5,"rare",["shorthair","rare","intelligent"],["blue-coat","thai-origin","good-luck","heart-face"],["CFA","TICA","FIFe","GCCF"],["russian-blue","chartreux","british-shorthair"],["russian-blue","chartreux"],False,100))

B(mk("Kurilian Bobtail","kurilian-bobtail","Felis catus","The Kurilian Bobtail is a natural Russian breed with a distinctive pom-pom tail and excellent fishing skills. Discover this strong breed.","Russia (Kuril Islands)","15-20 years","11-15 lbs (5-6.8 kg)","8-12 lbs (3.6-5.4 kg)","9-12 inches (23-30 cm)","shorthair","Dense, plush, water-resistant; also comes in longhair",["Red","Gray","Brown tabby","All colors"],["Tabby","Solid","Tortoiseshell","Bicolor"],["Gold","Green","Copper"],3,2,4,2,4,4,5,"rare",["shorthair","rare","playful","large"],["bobbed-tail","russian-origin","fishing-cat"],["TICA","FIFe","WCF"],["japanese-bobtail","american-bobtail","maine-coon"],["japanese-bobtail","maine-coon"],False,100))

# === L ===
B(mk("LaPerm","laperm","Felis catus","The LaPerm has a unique curly, permed-looking coat and an affectionate personality. Discover this distinctive breed.","United States","10-15 years","8-12 lbs (3.6-5.4 kg)","6-8 lbs (2.7-3.6 kg)","6-10 inches (15-25 cm)","shorthair","Curly, springy ringlets; comes in both shorthair and longhair",["All colors and patterns"],["Tabby","Tortoiseshell","Calico","Solid"],["All colors"],2,2,3,2,5,5,4,"rare",["shorthair","rare","hypoallergenic","playful"],["curly-coat","rex-type","hypoallergenic"],["CFA","TICA","FIFe"],["cornish-rex","devon-rex","selkirk-rex"],["selkirk-rex","cornish-rex"],False,100))

B(mk("Lykoi","lykoi","Felis catus","The Lykoi, or 'Werewolf Cat,' has a unique partially hairless coat that gives it a wolf-like appearance. Discover this fascinating rare breed.","United States","12-15 years","6-12 lbs (2.7-5.4 kg)","4-8 lbs (1.8-3.6 kg)","8-10 inches (20-25 cm)","shorthair","Partially hairless with roan pattern; sparse coat that molts",["Black roan"],["Roan"],["Gold","Green"],2,2,3,2,4,4,5,"very-rare",["shorthair","rare","hypoallergenic","intelligent"],["werewolf-cat","roan-coat","unique","rare"],["TICA"],["sphynx","devon-rex","cornish-rex"],["sphynx","devon-rex"],False,100))

# === M ===
B(mk("Maine Coon","maine-coon","Felis catus","The Maine Coon is the gentle giant of cats, known for its large size, tufted ears, and dog-like personality. Discover this beloved breed.","United States (Maine)","12-15 years","15-25 lbs (6.8-11.3 kg)","8-15 lbs (3.6-6.8 kg)","10-16 inches (25-41 cm)","longhair","Heavy, shaggy, water-resistant double coat; longer on ruff and tail",["Brown tabby","All colors"],["Tabby","Solid","Tortoiseshell","Bicolor","Calico"],["Gold","Green","Copper","Blue","Odd-eyed"],4,3,3,3,5,5,5,"common",["longhair","popular","large","playful","intelligent"],["gentle-giant","tufted-ears","dog-like","largest-domestic-breed"],["CFA","TICA","FIFe","GCCF"],["norwegian-forest-cat","siberian","ragdoll","ragamuffin"],["norwegian-forest-cat","siberian","ragdoll"],True,4))

B(mk("Manx","manx","Felis catus","The Manx is a tailless or short-tailed breed from the Isle of Man with a rounded appearance and dog-like loyalty. Discover this unique breed.","Isle of Man","8-14 years","10-14 lbs (4.5-6.4 kg)","8-10 lbs (3.6-4.5 kg)","7-10 inches (18-25 cm)","shorthair","Double coat that is short, dense, and plush; also longhair (Cymric)",["All colors and patterns"],["Tabby","Solid","Tortoiseshell","Calico","Bicolor"],["Gold","Copper","Green","Hazel","Blue"],3,2,3,2,5,5,5,"uncommon",["shorthair","rare","intelligent","playful"],["tailless","rounded-appearance","dog-like"],["CFA","TICA","GCCF","FIFe"],["japanese-bobtail","american-bobtail","cymric"],["american-bobtail","japanese-bobtail"],False,55))

B(mk("Munchkin","munchkin","Felis catus","The Munchkin is known for its short legs from a natural genetic mutation, with a playful personality. Discover this distinctive breed.","United States","12-15 years","6-9 lbs (2.7-4.1 kg)","4-8 lbs (1.8-3.6 kg)","5-7 inches (13-18 cm)","shorthair","Plush, dense; comes in both shorthair and longhair",["All colors and patterns"],["Solid","Tabby","Tortoiseshell","Bicolor","Colorpoint"],["All colors"],2,2,4,2,5,4,4,"uncommon",["shorthair","rare","playful"],["short-legs","dwarf-breed","playful"],["TICA"],["singapura","devon-rex","american-curl"],["singapura","minuet"],False,100))

# === N ===
B(mk("Nebelung","nebelung","Felis catus","The Nebelung is a rare longhaired breed with a shimmering blue-gray coat and green eyes. Discover this elegant, loyal breed.","United States","11-16 years","8-12 lbs (3.6-5.4 kg)","7-10 lbs (3.2-4.5 kg)","9-13 inches (23-33 cm)","longhair","Semi-long, silky, fine with silver tipping creating shimmer",["Blue-gray with silver tips"],["Solid with silver tipping"],["Green","Yellow-green"],3,3,2,2,4,4,5,"very-rare",["longhair","rare","calm","intelligent"],["blue-coat","russian-blue-relative","shimmering","loyal"],["TICA","CFA"],["russian-blue","chartreux","maine-coon"],["russian-blue","chartreux"],False,100))

B(mk("Norwegian Forest Cat","norwegian-forest-cat","Felis catus","The Norwegian Forest Cat is a large, rugged natural breed from Scandinavia. Discover this majestic 'Wegie' breed.","Norway","14-16 years","13-22 lbs (5.9-10 kg)","9-13 lbs (4.1-5.9 kg)","9-12 inches (23-30 cm)","longhair","Long, thick, glossy, water-resistant double coat with wooly undercoat",["Brown tabby","All colors"],["Tabby","Solid","Tortoiseshell","Bicolor","Calico"],["Green","Gold","Copper","Blue"],4,3,3,2,5,5,5,"uncommon",["longhair","large","playful","intelligent","hypoallergenic"],["scandinavian","viking-cat","waterproof-coat"],["CFA","TICA","FIFe","GCCF"],["maine-coon","siberian","turkish-angora","ragdoll"],["maine-coon","siberian"],True,12))

# === O ===
B(mk("Ocicat","ocicat","Felis catus","The Ocicat has a wild spotted appearance but is 100% domestic. Discover this athletic, dog-like breed with no wild blood.","United States","12-18 years","12-15 lbs (5.4-6.8 kg)","8-11 lbs (3.6-5 kg)","9-11 inches (23-28 cm)","shorthair","Short, smooth, satiny, and close-lying",["Tawny","Chocolate","Cinnamon","Blue","Lavender","Fawn"],["Spotted tabby"],["All colors except blue"],2,1,4,3,5,5,5,"uncommon",["shorthair","intelligent","playful","large"],["wild-look","spotted","dog-like","no-wild-blood"],["CFA","TICA","FIFe","GCCF"],["bengal","egyptian-mau","abyssinian","savannah"],["bengal","egyptian-mau","toyger"],False,60))

B(mk("Oriental Shorthair","oriental-shorthair","Felis catus","The Oriental Shorthair is sleek with oversized ears and 300+ color varieties. Discover this vocal, affectionate Siamese relative.","United Kingdom","12-15 years","8-12 lbs (3.6-5.4 kg)","5-10 lbs (2.3-4.5 kg)","9-11 inches (23-28 cm)","shorthair","Short, fine, silky, close-lying",["300+ varieties: Ebony, White, Blue, Chestnut, Lavender"],["Solid","Tabby","Tortoiseshell","Bicolor","Smoke"],["Green","Blue","Odd-eyed"],2,1,4,5,4,4,5,"uncommon",["shorthair","vocal","intelligent","playful"],["large-ears","sleek","300-colors","siamese-relative"],["CFA","TICA","FIFe","GCCF"],["siamese","oriental-longhair","balinese","javanese"],["siamese","balinese","peterbald"],False,65))

B(mk("Oriental Longhair","oriental-longhair","Felis catus","The Oriental Longhair combines the elegant Oriental body with a silky semi-long coat. Discover this vocal, beautiful breed.","United Kingdom","12-15 years","8-12 lbs (3.6-5.4 kg)","5-10 lbs (2.3-4.5 kg)","9-11 inches (23-28 cm)","longhair","Semi-long, fine, and silky with a plumed tail",["300+ varieties"],["Solid","Tabby","Tortoiseshell","Bicolor","Smoke"],["Green","Blue","Odd-eyed"],3,2,4,5,4,4,5,"rare",["longhair","vocal","intelligent","rare"],["oriental-type","plumed-tail","vocal"],["TICA","FIFe","GCCF"],["oriental-shorthair","siamese","balinese","angora"],["balinese","turkish-angora","siamese"],False,100))

print("Breeds data loaded:", len(BREEDS))