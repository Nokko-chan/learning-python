names = ["眠眠", "诺可", "诗音", "爱丽丝"]
print(names)

print(f"欢迎, {names[0]} 参加晚宴!")
print(f"欢迎, {names[1]} 参加晚宴!")
print(f"欢迎, {names[2]} 参加晚宴!")
print(f"欢迎, {names[-1]} 参加晚宴!")

print(f"\n{names[2]} 无法赴约")

names[2] = "罗伯特"
print(names)
print(f"欢迎, {names[2]} 参加晚宴!")

print("\n将扩充晚宴人数！")

names.insert(0, "小原原")
names.insert(2, "梦美")
names.append("小圆")

print(names)
print(f"欢迎, {names[0]} 参加晚宴!")
print(f"欢迎, {names[2]} 参加晚宴!")
print(f"欢迎, {names[-1]} 参加晚宴!")
print(f"一共邀请了 {len(names)} 个人参加晚宴!")

print("\n将缩减晚宴人数！")
print(f"移除, {names.pop()}")
print(f"移除, {names.pop()}")
print(f"移除, {names.pop()}")
print(f"移除, {names.pop()}")
print(f"移除, {names.pop()}")
print(names)

del names[0]
del names[0]
print(names)