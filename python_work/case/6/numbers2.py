numbers = {
    "sion": [10, 20, 30],
    "nokko": [8, 9, 10],
    "meme": [6, 20],
    "alice": [20],
    "john": [42, 12],
}

for name, number_list in numbers.items():
    print(f"\nName: {name.title()}")
    for num in number_list:
        print(f"\t{num}")