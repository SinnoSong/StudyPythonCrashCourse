class Restaurant:
    def __init__(self, restaurant_name, cuisine_type) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"name is {self.restaurant_name}")
        print(f"cuisine is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")

    def read_number_served(self):
        print(f"number_served:{self.number_served}")

    def update_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, count):
        self.number_served += count


restaurant = Restaurant("test", "abc")
restaurant.update_number_served(10)
restaurant.read_number_served()
restaurant.increment_number_served(5)
restaurant.read_number_served()
