def greet_users(names: list[str]):
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


usernames = ['sinno', 'dabing', 'mengde']
greet_users(usernames)
