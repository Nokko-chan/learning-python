# for value in range(1, 1000000):
#    print(value)

# numbers = list(range(1, 1000001))
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# for value in range(3, 31, 3):
#    print(value)

# cubes = []
# for value in range(1, 11):
#     cubes.append(value**3)

# for cube in cubes:
#     print(cube)

cubes = [value**3 for value in range(1, 11)]
print(cubes)