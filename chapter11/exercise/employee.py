class Employee:
    def __init__(self, first_name: str, last_name: str, salary: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, add_count: int = 5000) -> None:
        self.salary = self.salary + add_count
