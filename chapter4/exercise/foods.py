my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are :")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
print("\n")

my_foods.append("cannoli")
friend_foods.append("ice cream")
print("My favorite foods are :")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

for value in my_foods:
    print(value)

for value in friend_foods:
    print(value)
