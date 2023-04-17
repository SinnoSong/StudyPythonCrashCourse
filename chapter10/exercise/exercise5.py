filename = 'exercise5.txt'
with open(filename, 'w') as file_object:
    while True:
        reason = input("Enter a reason: ")
        if reason == 'quit':
            break
        else:
            file_object.write(reason)
