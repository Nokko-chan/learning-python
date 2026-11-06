content = {
    "int": "数据类型：数字，用于运算",
    "string": "数据类型：字符串，用于存储字符",
    "list": "数据类型：列表，可用于存储一系列的对象",
    "tuple": "数据类型：元组，元组相当于不可变的列表",
    "dict": "数据类型：字典，字典可以存储键与值相关联的键值对",
    "set": "数据类型：集合，集合用于去重元素"
}

for key, value in content.items():
    print(f"{key.title()}:")
    print(f"\t{value}.\n")