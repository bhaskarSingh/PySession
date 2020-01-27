"""
# Concept
Object-oriented Programming (OOP) is a language model (or paradigm) in which
properties or behaviors are organized into “objects”. Some languages encourage
a more procedural style, like if you were writing a recipe - some popular examples 
are COBOL and BASIC. Languages that adopt an Object-oriented style organize things
into objects, and provide methods for objects to communicate with one another.
"""

# What is a Object ?
"""
An object can be a function, a variable, a property, a class… everything in Python
is an object. 
"""
# print("Hello World!")
# print(type(int))

# Classes
"""
Every thing or object in Python are an instance of a class.
    The number 100, -10, 0 is an instance of the class int
    The string "Hello, world" is an instance of the str (or string) class.
    
These classes, in turn, are subclasses of the master object class.
"""


# Classes vs Instances/Object
"""
You can think of a class as a “type” of something, like “Car.”
You can think of an instance as a specific thing, such as “My i10”
which is a type of “Car.”

Both classes and instances/object can have variables and methods.
    #Changing a class variable will change what is returned when
    you get that variable from an instance

    #changing an instance variable only applies to that one instance
"""

# Self
"""
self is used inside classes to refer to a bound instance variable or object.
Example ⬇️
"""


# class Car:
#     # Class Variable
#     runs = True

#     # Instance Method
#     def start(self):
#         if self.runs:
#             print("Car is started. Vroom vroom!")
#         else:
#             print("Car is broken :(")


# my_car = Car()
# print(f"my_car runs property equals {Car.runs}")
# my_car.start()

# Car.runs = False

# my_other_car = Car()
# my_other_car.start()

# another_car = Car()


# self refers to an instance

"""
runs is a class variable on the Car class
    #it exists for all instances of type Car
"""
# What happens if we call start() on the Car class instead of an instance?
# Car.start()
