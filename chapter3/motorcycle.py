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
