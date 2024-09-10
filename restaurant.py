class Restaurant:

    def __init__(self, name, food_type):
        self.name = name
        self.type =food_type


    def describe_restaurant(self):
        print(f"Our restaurant, {self.name}, proudly serves {self.type} food.")

    def open_restaurant(self):
        print(f"{self.name} is open for business!")


restaurant = Restaurant('In N Out', 'American')