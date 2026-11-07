prompt = "\n请输入您的年龄:"
prompt += "\n(输入 'quit' 退出) "

# active = True
# while active:
#     age = input(prompt)
#     if age == "quit":
#         active = False
#     else:
#         age = int(age)

#         if age < 3:
#             price = 0
#         elif age < 12:
#             price = 10
#         elif age >= 12:
#             price = 15
#         print(f"\n您的票价为 ${price}.")

# age = 0
# while age != "quit":
#     age = input(prompt)
#     if age != "quit":
#         age = int(age)
#         if age < 3:
#             price = 0
#         elif age < 12:
#             price = 10
#         elif age >= 12:
#             price = 15
#         print(f"您的票价为: ${price}.")

while True:
    age = input(prompt)
    if age == "quit":
        break
    
    age = int(age)
    if age < 3:
        price = 0
    elif age < 12:
        price = 10
    elif age >= 12:
        price = 15
    print(f"您的票价为: ${price}.")