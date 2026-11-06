pet_0 = {"pet type": "dog", "master": "meme"}
pet_1 = {"pet type": "cat", "master": "nokko"}
pet_2 = {"pet type": "rabbit", "master": "sion"}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    print(f"\nPet Type: {pet['pet type'].title()}")
    print(f"Master: {pet['master'].title()}")