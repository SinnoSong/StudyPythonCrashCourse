class Restaurant:
    def __init__(self, restaurant_name, cuisine_type) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"name is {self.restaurant_name}")
        print(f"cuisine is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")


restaurant = Restaurant("test", "abc")
restaurant.describe_restaurant()
restaurant.open_restaurant()
