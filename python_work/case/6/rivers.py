rivers = {
    "yellow river": "china",
    "yangtze river": "china",
    "nile": "egypt",
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nRivers:")
for river in sorted(rivers.keys()):
    print(f"\t{river.title()}")

print("\nCountrys:")
for country in set(rivers.values()):
    print(f"\t{country.title()}")