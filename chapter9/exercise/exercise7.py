import exercise5


class Admin(exercise5.User):
    def __init__(self, first_name, last_name, age: int) -> None:
        super().__init__(first_name, last_name, age)
        self.privileges = []

    def update_privileges(self, new_privileges):
        for privilege in new_privileges:
            self.privileges.append(privilege)

    def show_privileges(self):
        print(f"{self.privileges}")


admin = Admin("sinno", 'song', 24)
admin.update_privileges(['can add post', 'can delete post'])
admin.show_privileges()
