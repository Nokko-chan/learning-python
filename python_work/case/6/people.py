person_1 = {"name": "sion", "age": 18}
person_2 = {"name": "nokko", "age": 10}
person_3 = {"name": "meme", "age": 20}

people = [person_1, person_2, person_3]

for user in people:
    print(f"\nName: {user['name'].title()}")
    print(f"Age: {user['age']}")