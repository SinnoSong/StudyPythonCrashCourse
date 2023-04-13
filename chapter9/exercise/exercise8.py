import exercise5


class Privileges:
    def __init__(self) -> None:
        self.privileges = []

    def show_privileges(self):
        print(f"{self.privileges}")


class Admin(exercise5.User):
    def __init__(self, first_name, last_name, age: int) -> None:
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges()

    def update_privileges(self, new_privileges):
        for privilege in new_privileges:
            self.privileges.privileges.append(privilege)


admin = Admin("sinno", "sinno", 24)
admin.update_privileges(['can add get'])
admin.privileges.show_privileges()
