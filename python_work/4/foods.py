my_foods = ['pizza', 'falafel', 'carrot cake']
friend_fodds = my_foods[:]

my_foods.append("cannoli")
friend_fodds.append("ice cream")

print("My favorite foods are:")
for food in my_foods:
    print(f"\t{food.title()}")

print("\nMy friend's favorite foods are:")
for food in friend_fodds:
    print(f"\t{food.title()}")