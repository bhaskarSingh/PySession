# Inheritance
"""
Properties
1.Class inheritance is a very useful Object-oriented Programming construct for
sharing and reusing code.

2.Inheritance makes it possible to break up and organize your code into a hierarchy,
from generic to specific.

3.Objects that belong to classes that are higher up in the hierarchy (more generic)
are accessible by subclasses, but not vice versa.

Example ⬇️
"""

# issubclass --> function takes two classes, and returns
# True if the first class is a subclass of the second

"""
issubclass(bool, int)
issubclass(int, object)
issubclass(bool, object)
"""

# Subclassing custom classes(Inheritance)
"""
class Vehicle:

    def __init__(self, make, model, fuel="gas"):
        self.make = make
        self.model = model
        self.fuel = fuel


class Car(Vehicle):

    def __init__(self, make, model, fuel="gas"):
        super().__init__(make, model, fuel)


# from vehicle import Vehicle, Car
my_car = Car("Ford", "Explorer")
print(type(my_car))
print(my_car.fuel)
print(isinstance(my_car, Car))
print(isinstance(my_car, Vehicle))
print(issubclass(Car, Vehicle))
"""

# Overriding Variables in a Subclass
"""
class Vehicle:
    number_of_wheels = 4

    def __init__(self, make, model, fuel="gas"):
        self.make = make
        self.model = model
        self.fuel = fuel


class Car(Vehicle):

    def __init__(self, make, model, fuel="gas"):
        super().__init__(make, model, fuel)


class Truck(Vehicle):
    number_of_wheels = 6

    def __init__(self, make, model, fuel="diesel"):
        super().__init__(make, model, fuel)


class Motorcycle(Vehicle):
    number_of_wheels = 2


my_truck = Truck("Ford", "F350")
print(type(my_truck))
print(my_truck.fuel)
print(my_truck.number_of_wheels)
"""

"""
# Multiple Inheritance in Python
# Can Python classes inherit from multiple parent classes?


we won’t have time to cover the topic of Multiple inheritance in this course,
because it’s out of scope.
"""


# Practice Time

"""
# Class Variables

class Vehicle:

    number_of_wheels = 4

    def __init__(self, make, model, fuel="gas"):
        self.make = make
        self.model = model
        self.fuel = fuel

daily_driver = Vehicle("Ford", "Explorer")

daily_driver.number_of_wheels = 3

# What will be the expected out here ?

# Instance variables
print(
    f"I drive a {daily_driver.make} {daily_driver.model}. It runs on {daily_driver.fuel}.")
print(f"My {daily_driver.model} has {daily_driver.number_of_wheels} wheels.")

# Class variable
print(f"Most vehicles have {Vehicle.number_of_wheels} wheels.")

"""

"""
# Inheritance

class Vehicle:

    def __init__(self, make, model, fuel="gas"):
        self.make = make
        self.model = model
        self.fuel = fuel


class Car(Vehicle):

    number_of_wheels = 4


class Truck(Vehicle):

    number_of_wheels = 6

    def __init__(self, make, model, fuel="diesel"):
        super().__init__(make, model, fuel)

# What will be the expected output ⬇️ ?


daily_driver = Car("Ford", "Explorer")
print(f"I drive a {daily_driver.make} {daily_driver.model}. "
      f"It uses {daily_driver.fuel} and has {daily_driver.number_of_wheels} wheels.")

truck = Truck("Ford", "F350")
print(f"I also have a {truck.make} {truck.model}. "
      f"It uses {truck.fuel} and has {truck.number_of_wheels} wheels.")

#print(f"My daily driver is a {type(daily_driver)} and my truck is a {type(truck)}")

# print(f"Is my daily driver a car? {isinstance(daily_driver, Car)}")
# print(f"Is my truck a Vehicle? {isinstance(truck, Vehicle)}")
# print(f"Is my truck a Car? {isinstance(truck, Car)}")

# print(f"Is a Truck a subclass of Vehicle? {issubclass(Truck, Vehicle)}")
"""
