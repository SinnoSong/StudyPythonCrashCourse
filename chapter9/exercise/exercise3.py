class User:
    def __init__(self, first_name, last_name, age: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f"{self.last_name} {self.first_name}: {self.age}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}")


user1 = User("sinno", "song", 24)
user1.describe_user()
user1.greet_user()
user2 = User("moon", "gou", 25)
user2.describe_user()
user2.greet_user()
