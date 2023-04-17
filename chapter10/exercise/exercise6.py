try:
    number1 = input("First number: ")
    number2 = input("Second number: ")
    print(int(number1) + int(number2))
except ValueError:
    print("Invalid input")
