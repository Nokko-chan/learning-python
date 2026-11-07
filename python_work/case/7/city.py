places = {}

active = True
while active:
    name = input("\n请输入您的名字: ")
    place = input("请输入您喜欢的地方: ")
    places[name] = place

    repeat = input("还有继续调查吗? (yes/no) ")
    if repeat == "no":
        active = False

print(f"\n--- 调查结果 ---")
for name, place in places.items():
    print(f"{name} 喜欢的地方是 {place}.")