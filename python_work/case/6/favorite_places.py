favorite_places = {
    "nokko": ["tokyo", "osaka", "nagoya"],
    "meme": ["tokoyo", "kyoto"],
    "sion": ["hokkaido", "osaka"]
}


for name, places in favorite_places.items():
    print(f"\n{name.title()}:")
    for place in places:
        print(f"\t-{place.title()}")