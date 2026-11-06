cities = {
    "tokoyo": {
        "country": "japan",
        "population": 14186237,
        "face": "日本国首都",
    },
    "kyoto": {
        "country": "japan",
        "population": 1463723,
        "face": "古称平安京，位于日本西部",
    },
    "bejin": {
        "country": "china",
        "population": 218000000,
        "face": "中国首都",
    },
}

for city, city_info in cities.items():
    country = city_info["country"]
    population = city_info["population"]
    face = city_info["face"]
    print(f"\nCity: {city.title()}:")
    print(f"\tCountry: {country.title()}")
    print(f"\tPopulation: {population}")
    print(f"\tFace: {face}.")