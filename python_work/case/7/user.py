users = input("请问有多少人需要用餐? ")
users = int(users)

if users > 8:
    print(f"抱歉，暂时没有那么多位置!")
else:
    print(f"欢迎您的就餐!")