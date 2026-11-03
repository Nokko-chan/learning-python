my_pizzas = ["durian pizza", "cheese pizza", "hot dog pizza"]
friend_pizzas = my_pizzas.copy()

my_pizzas.append("chicken pizza")
friend_pizzas.append("fruit pizza")

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(f"\t{pizza.title()}")

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"\t{pizza.title()}")