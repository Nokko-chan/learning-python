number = input("请输入一个数字: ")
number = int(number)

if number % 10 == 0:
    print(f"\n数字 {number} 是 10 的倍数.")
else:
    print(f"\n数字 {number} 不是 10 的倍数.")