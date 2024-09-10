class User:

    def __init__(self, first_name, last_name, location, age):
        self.first = first_name
        self.last  = last_name
        self.location = location
        self.age = age
        self.attempts = 0



    def describe_user(self):
        print(f"{self.first} {self.last} lives in {self.location}, and is {self.age} years old.")


    def greet_user(self):
        print(f"Hello, {self.first}!")


    def increment_login_attempts(self):
        self.attempts += 1


    def reset_login_attempts(self):
        self.attempts = 0




user = User('Aaron', 'Johnson', 'Las Vegas', 30)


user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

print(f"{user.first} has logged in {user.attempts} times on monday.")

user.reset_login_attempts()

print(f"{user.first} has logged in {user.attempts} times today.")