class Dog:
    """狗"""

    def __init__(self, name, age) -> None:
        """初始化name 和age"""
        self.name = name
        self.age = age

    def sit(self) -> None:
        print(f"{self.name} is now sitting.")

    def roll_over(self) -> None:
        print(f"{self.name} rolled over!")


my_dog = Dog("Willie", 6)
your_dog = Dog("Lucy", 3)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog's is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog's is {your_dog.age} years old.")
