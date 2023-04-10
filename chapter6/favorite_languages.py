favorite_languages = {
    'jen': "python",
    'sarsh': "c",
    "edward": "ruby",
    'phil': "python"
}
language = favorite_languages['sarsh'].title()
print(F"Sarash's favorite language is {language}.")
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")

# for name in favorite_languages.keys():
for name in favorite_languages:
    print(name.title())

for language in set(favorite_languages.values()):
    print(language.title())
