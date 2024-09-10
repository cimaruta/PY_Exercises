class Restaurant:

    def __init__(self, name, food_type):
        self.name = name
        self.type =food_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Our restaurant, {self.name}, proudly serves {self.type} food.")

    def open_restaurant(self):
        print(f"{self.name} is open for business!")


    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number
        

restaurant = Restaurant('In N Out', 'American')

restaurant.describe_restaurant()

restaurant.open_restaurant()

restaurant.set_number_served(100_000)

print(f"We served {restaurant.number_served} people on monday.")

restaurant.set_number_served(150_000)

print(f"We served {restaurant.number_served} people on tuesday.")

restaurant.increment_number_served(50_000)

print(f"We plan to serve {restaurant.number_served} people on wednesday.")