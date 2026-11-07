sandwich_orders = ["芝士三明治", "火腿三明治", "鸡蛋三明治"]
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"正在制作三明治: {sandwich}...")
    finished_sandwiches.append(sandwich)

print(f"\n--- 已完成 ---")
for sandwich in finished_sandwiches:
    print(sandwich)