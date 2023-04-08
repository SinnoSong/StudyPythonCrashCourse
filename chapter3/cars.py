cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

cars.reverse()
print(cars)
length = len(cars)
print(f"length is {length}")
