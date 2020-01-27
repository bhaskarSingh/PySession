# Methods

"""
Classes can also have class methods
    # Which are shared among all the instances of certain types
"""
"""
class Car:
    runs = True
    number_of_wheels = 4

    @classmethod
    def get_number_of_wheels(cls):
        return cls.number_of_wheels

    def start(self):
        if self.runs:
            print("Car is started. Vroom vroom!")
        else:
            print("Car is broken :(")

my_car = Car()
print(f"Cars have {Car.get_number_of_wheels()} wheels.")
# Overriding instance variable
my_car.number_of_wheels = 6
# Accessing newly assigned instance variable value
print(f"My car has {my_car.number_of_wheels} wheels.")
# Calling class method on instance variable
print(f"My car has {my_car.get_number_of_wheels()} wheels.")
"""


# type, isinstance, issubclass
# built-in functions for inspecting classes and types

# type() --> function returns the type of the object you pass it
"""
type(42)
type("Hello world!")
type(my_car)
"""

# isinstance(object, class) --> function takes an object and a class, and returns
# True if the object you pass it is an instance of the class

"""
isinstance(42, int)
isinstance("Hello world!", str)
isinstance(my_car, float)
isinstance(my_car, Car)
"""

# issubclass --> function takes two classes, and returns
# True if the first class is a subclass of the second

"""
issubclass(bool, int)
issubclass(int, object)
issubclass(bool, object)

"""

# Why is 0, considered as False in python ?
"""
print(type(0))
print(bool(0))
"""


# Magic Methods(__methodname__)
# Methods that are bracketed by underscores are sometimes called “magic methods.”
"""
__init__() is an optional method that gets run when we instantiate an instance of a class
    # Here we can include setting instance variables which can take arguments too
Example ⬇️
"""


"""
class Car:
    runs = True

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        if self.runs:
            print(f"Your {self.make} {self.model} is started. Vroom vroom!")
        else:
            print(f"Your {self.make} {self.model} is broken :(")

my_car = Car("Ford", "Thunderbird")
my_car.start()

"""


# __str__ and __repr__(Both functions return a string representation of an object)
# __str__ --> should return readable end-user output / maps to the built-in function str()
# __repr__ --> should return the Python code necessary to rebuild the object / maps to the built-in function repr()


"""
import datetime
now = datetime.datetime.now()
print(str(now))
print(repr(now))
"""


# Setting __str__() and __repr__() methods in our custom classes
"""
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __str__(self):
        return f"<<Car object: {self.make} {self.model}>>"

    def __repr__(self):
        return f"Car('{self.make}', '{self.model}')"


my_car = Car("Ford", "Explorer")
print(f"This object is a {str(my_car)}")
print(f"To reproduce it, type: {repr(my_car)}")
"""
