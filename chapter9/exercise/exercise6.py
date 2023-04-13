import exercise4


class IceCreamStand(exercise4.Restaurant):
    def __init__(self, restaurant_name, cuisine_type) -> None:
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def update_flavors(self, list: list[str]):
        for flavor in list:
            self.flavors.append(flavor)

    def show_flavors(self):
        print(f"There are the list:{self.flavors}")


ice_cream_stand = IceCreamStand("test_name", "type")
ice_cream_stand.update_flavors(["test1", "test2"])
ice_cream_stand.show_flavors()
