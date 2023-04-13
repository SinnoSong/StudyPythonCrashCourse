import random

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'f', 's', 'y', 'z', 'm']

print(f"{random.choices(values, k=4)}")
