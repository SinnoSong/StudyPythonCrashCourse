pizzas = ['pizza1', 'pizza2', 'pizza3']
friend_pizzas = pizzas[:]
pizzas.append('pizza test')
friend_pizzas.append('pizza4')

print("My favorite pizzas are:")
for value in pizzas:
    print(value)

print("My friend's favorite pizzas are:")
for value in friend_pizzas:
    print(value)
