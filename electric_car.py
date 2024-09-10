class Car:
    """A simple attempt to represent a car."""


    def __init__(self, make, model, year):
       """Initialize attributes to describe a car."""
       self.make = make
       self.model = model
       self.year = year
       self.odometer_reading = 0


    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


    def read_odometer(self):
        print(f"This  car has {self.odometer_reading} miles on it.")


    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You cant roll back an odometer!')


    def increment_odometer(self, miles):
        self.odometer_reading += miles



class Battery:
    """A simple attempt to model a battery for an electric car."""


    def __init__(self, battery_size=40):
        """Initiallize the battery's atributes."""
        self.battery_size = battery_size


    def describe_battery(self):
        """"Print a statement describing the battery."""
        print(f"This car has a {self.battery_size}-KWh battery.")


    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"this car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()



my_leaf = ElectricCar('Nissan', 'leaf', 2024)

print(my_leaf.get_descriptive_name())

my_leaf.battery.describe_battery()

my_leaf.battery.get_range()