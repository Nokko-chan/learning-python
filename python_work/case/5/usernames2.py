current_users = ['sion', 'alice', 'nokko', 'meme', 'eden']
new_users = ['meme', 'yumemi', 'sakura', 'alice', 'john']

for new_user in new_users:
    if new_user in current_users:
        print(f"用户名 {new_user} 已经存在!")
    else:
        print(f"添加新用户: {new_user}..")
        current_users.append(new_user)

print(f"\n当前用户:")
for current_user in current_users:
    print(f"\t{current_user}")