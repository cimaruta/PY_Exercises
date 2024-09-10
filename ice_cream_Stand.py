class Restaurant:

    def __init__(self, name, food_type):
        self.name = name
        self.type =food_type


    def describe_restaurant(self):
        print(f"Our restaurant, {self.name}, proudly serves {self.type} food.")

    def open_restaurant(self):
        print(f"{self.name} is open for business!")


restaurant = Restaurant('In N Out', 'American')


class IceCreamStand(Restaurant):

    def __init__(self, name, food_type, *flavors):
        super().__init__(name, food_type)
        self.flavors = flavors


    def describe_flavors(self):
        print("Our flavors of the day include:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")




icecreamstand = IceCreamStand("Frozen Delights", "Ice Cream", "Chocolate", "Vanilla", "Pistachio")


icecreamstand.describe_restaurant()
icecreamstand.open_restaurant()
icecreamstand.describe_flavors()