motorcycles: list[str] = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles)

# delete element
del motorcycles[0]
print(motorcycles)

popped_motorcycle: str = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned}")

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

print(motorcycles)
motorcycles.remove("yamaha")
print(motorcycles)
