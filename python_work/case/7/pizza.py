prompt = "\n请输入需要添加的披萨配料: "
prompt += "(输入 'quit' 以退出程序) "

# active = True
# while active:
#     message = input(prompt)
#     if message == "quit":
#         active = False
#     else:
#         print(f"添加配料 {message}...")

# message = ""
# while message != "quit":
#     message = input(prompt)
#     if message != "quit":
#         print(f"添加配料 {message}...")

while True:
    message = input(prompt)
    if message == "quit":
        break
    print(f"添加配料 {message}...")