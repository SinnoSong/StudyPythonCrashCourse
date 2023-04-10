rivers = {"nile":"egypt","Yellow River":"china","Rhine":"Germany"}
for river,country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")