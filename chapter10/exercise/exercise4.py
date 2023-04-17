file_name = "guest_book.txt"

with open(file_name, "a") as file_object:
    while True:
        name = input("Enter your name: ")
        if name == "":
            break
        else:
            file_object.write(name + "\n")
