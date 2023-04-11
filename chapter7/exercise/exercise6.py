active = True
while active:
    message = input("pizza topping:")
    if message == 'quit':
        active = False
    else:
        print(message)
