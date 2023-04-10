pet2 = {"name": "daBing", "master": "sinno"}
pet1 = {"name": "mengDe", "master": "moon"}
pets = [pet2, pet1]
for pet in pets:
    print(f"name {pet['name']}, master: {pet['master']}")
