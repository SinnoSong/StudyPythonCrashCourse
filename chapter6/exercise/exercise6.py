favorite_languages = {
    'jen': "python",
    'sarsh': "c",
    "edward": "ruby",
    'phil': "python"
}
names = ['sarsh', 'phil', 'tom']
for name in names:
    if name in favorite_languages.keys():
        print(f"Thank you {name}")
    else:
        print(f"{name},welcome you!")
