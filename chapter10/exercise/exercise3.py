filename = 'guest.txt'
name = input("Please input your name")

with open(filename, 'w') as f_obj:
    f_obj.write(name)
