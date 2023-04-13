class User:
    def __init__(self, first_name, last_name, age: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.last_name} {self.first_name}: {self.age}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reest_login_attempts(self):
        self.login_attempts = 0


user = User("sinno", 'song', 24)
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)
user.reest_login_attempts()
print(user.login_attempts)
