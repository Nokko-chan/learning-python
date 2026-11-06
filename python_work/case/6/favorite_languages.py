favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

favorite_languages_names = favorite_languages.keys()
friends = ["jen", "nokko", "sion", "edward"]

for friend in friends:
    if friend in favorite_languages_names:
        print(f"你好, {friend.title()}! 感谢参与我们的调查!")
    else:
        print(f"{friend.title()},请问你需要参与我们的调查吗?")