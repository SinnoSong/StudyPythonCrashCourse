filename1 = 'cats.txt'
filename2 = 'dogs.txt'
try:
    with open(filename1) as file_object:
        contents = file_object.read()
        print(contents)
    with open(filename2) as file_object:
        contents2 = file_object.read()
        print(contents2)
except FileNotFoundError:
    pass
