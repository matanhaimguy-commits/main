import random, json
seed = random.randint(100000, 999999); random.seed(seed)
LENSES = ["winner-sweep-by-category-family","geo-import-gap","demographic-flip","format-flip",
          "offer-gap-raid","rising-star-sweep","marketplace-reverse","review-mine-wedge",
          "adjacent-pain-chain","problem-forum-ethnography"]
FAMILIES = ["sleep & night comfort","personal care & grooming","skin & body appearance","hair & scalp",
            "oral care","foot & gait","pain & tension relief","posture & desk life","home cleaning & order",
            "kitchen & food prep","laundry & garment care","pets: dogs","pets: cats","car & commute",
            "garage, DIY & tools","garden & outdoor","travel & packing","fitness & recovery",
            "work gear & trades","bathroom & shower","bedroom textiles & climate","tech-adjacent accessories",
            "baby & toddler practical (non-safety-critical)","seasonal-evergreen comfort (heat/cold)"]
SOURCE_GEOS = ["US","UK","DE","FR","NL","SE","DK","AU","CA","IT","ES"]
GRAVITY = ["GLP-1-adjacent","cortisol-face","generic anti-aging serum","rosemary/caffeine hair serum",
           "mouth tape","posture corrector","blue-light glasses","LED teeth whitening","gua sha",
           "collagen","beef tallow skincare","generic magnesium sleep","cold plunge","under-eye patches"]
draw = {"run_seed": seed,
        "lenses": random.sample(LENSES, 3),
        "families": random.sample(FAMILIES, 5),
        "geo_import_sources": random.sample(SOURCE_GEOS, 3),
        "hard_banned_gravity_wells": random.sample(GRAVITY, 3)}
print(json.dumps(draw, indent=1))
