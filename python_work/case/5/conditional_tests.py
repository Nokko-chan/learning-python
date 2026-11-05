name = "alice"
age = 18
age_0 = 16
age_1 = 20
usernames = ['alice', 'nokko', 'meme']

print(name == "alice")
print(name != "alice")
print(name.title() == "Alice")
print(name.upper() == "NOKKO")
print()

print(age == 18)
print(age != 19)
print(age > 18) 
print(age >= 18)
print(age < 18)
print(age <= 18)
print()

print(age_0 >= 16 and age_1 >= 16)
print(age_0 <= 18 or age_1 <= 18)
print()

print('alice' in usernames)
print('meme' not in usernames)