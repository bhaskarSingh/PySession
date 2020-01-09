"""
Functions help us organize our code in a way that’s reusable
and accept arguments and defaults where needed.
"""

"""
#Anatomy of a function
1.def: the def keyword, telling Python we’re about to start a function definition
2.a name for the function
3.(: opening parenthesis
4.(optional) the names of one or more arguments, separated with ,
5.(optional) the names and values of one or more default arguments, separated with (,)
6.) closing parenthesis
7.: a colon, to indicate the start of the function
"""

"""
#example
def hello_world():
    print("Hello, World!")

def sum(x, y):
    return x + y
"""

"""
# return statement
A return statement is a way to “short-circuit” the function.
--> Using a return statement, you can optionally pass back data to the caller of your function.

with no return statement
--> If a function doesn’t have a return statement, it implicitly returns None

with a return statement, but no value
--> it also returns None

with a return statement and a value
-->  To return a value from a function, just type it after the return statement
"""

"""
#Indentation
Anything that’s indented one level deep under the function declaration is part of the function
"""


"""
#Positional arguments are required
#Positional arguments are all required, and must be given in the order they are declared.
#Example
def say_greeting(name, greeting):
    print(f"{greeting}, {name}.")

say_greeting("Hello!", "Sam") #Wrong order

#Keyword arguments with default values
#Arguments that have default values are called keyword arguments
#defaults arguments can be overridden when needed
#Example

def say_greeting_with_default(name, greeting="Hello", punctuation="!"):
    print(f"{greeting}, {name}{punctuation}")


#Order matters!
#All of the required arguments go first. They are then followed by the optional keyword arguments.
#What will happen if below function is executed ?

def say_greeting(greeting="Hello", name):
    print("Hmm, will this work?")


#You can pass in none, some, or all of the keyword arguments.

def create_query(language="JavaScipt", rating=1, sort="desc"):
    return f"language:{language} rating:{rating} sort:{sort}"

create_query()
create_query("Ruby")

--> If your function takes keyword arguments, you can provide zero, one, or all of them when you call it
--> You don’t need to pass these arguments in order either


#You can pass in required parameters by keyword
def say_greeting(name, greeting):
    print(f"{greeting}, {name}.")

say_greeting("Nina", "Hello")
say_greeting(name="Sam", greeting="Konnichiwa")
"""

"""
#!!!!Caveat!!!!
#Never use mutable types, like lists as a default argument
#You ask Why? Because it won’t work like you’d expect it to.

# Don't do this!

def add_five_to_list(my_list=[]):
    my_list.append(5)
    return my_list

# This works like we expected it to.
add_five_to_list() # result : [5]

add_five_to_list() # result : [5, 5]

# We see that the original `my_list` is still being modified.
add_five_to_list() #result : [5, 5, 5]


----Solution----

def add_five_to_list(my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(5)
    return my_list

----Solution----

In Python, default arguments are evaluated only once – when the function is defined.
Not each time the function is called. that means if you use a value that can be changed,
it won’t behave like you’d expect it to.
"""

"""
#Naming Functions and Arguments
Python is a dynamic language (sometimes called duck-typed) 

-->Try to avoid single character names for your functions and variables, unless they have meaning in math.
-->For sequences, like lists, it’s appropriate to name them in the plural.
-->Make variable called name to be a single string, and a variable called names to be a list of strings.
Awesome resource for understanding naming convention in python: https://www.youtube.com/watch?v=YklKUuDpX5c
"""

"""
#Scope inside a function
    --> scoping in Python happens with whitespace
    --> it’s scope changes to a new internal scope.
    It has access to the variables defined outside of it, but it can’t change them.
    --> Once the function is done running, its scope goes away, as do its defined variables.

def my_captain_info():
    my_captain_account = "nnja"
    print(f"Account inside function: {my_captain_account}")

print(f"Account outside of function: {my_captain_account}")


#Using variables defined outside of the function
--> You can’t change variables defined outside of the function inside of the function.

name = "Bhaskar"
print(f"Name outside of function: {name}")

def try_change_name():
    name = "Max"
    print(f"Name inside of function: {name}")

print(f"Name outside of function: {name}")

*** A good rule of thumb is to name variables clearly, 
and minimize how many variables we declare outside of functions ***

*** A constant is a value that we expect to use several times within our program,
but we never expect to change it programmatically. ***

ACCOUNT_NAME = "Bhaskar"

def my_captain_info():
    print(f"Account inside function: {ACCOUNT_NAME}")
"""

"""
Practice
The Importance of Whitespace(defines function scope in python)

def add_numbers(x, y):
return x + y


#Function Scope(scoping in Python happens with whitespace)

x = 1
y = 2
def add_numbers(x, y):
    print(f"Inside the function, x = {x} and y = {y}")
    return x + y

print(f"Outside the function, x = {x} and y = {y}")
print(f"The sum of 5 and 6 is {add_numbers(5, 6)}")


#Positional Arguments vs Keyword Arguments

-->generic function for doing math

def calculate_numbers(x, y, operation="add"):
    if operation == "add":
        return x + y
    elif operation == "subtract":
        return x - y

calculate_numbers(2, 3)
calculate_numbers(2, 3, "subtract")
calculate_numbers(2, 3, operation="subtract")
"""
