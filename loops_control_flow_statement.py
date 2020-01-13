"""
Loops and control statements allow us to control the logical flow of our program.
"""

"""
for Loop(Looping in Python doesn’t look like looping in other languages)

In Javascript
for (i = 0(Initial Value); i < 5(Condition); i++(Increment)) {
  text += "The number is " + i + "<br>";
}

#Looping in Python is a simpler
The syntax is: 
for single_item in items, followed by a colon :, 
followed by a new line, a level of indentation, and
the code you’d like to consider as the body of the loop. 
That is, the code that’ll run multiple times, until there
are no more items in the collection.

colors = ["Red", "Green", "Blue", "Orange"]
for color in colors:
    print(f"The color is: {color}")
"""

"""
#Looping over a range of numbers
range(num) --> produces a sequence of integers passed in as parameter
For debugging/testing: --> For example: list(range(5)). 
(Remember that this is inefficient, so use it for testing, not in production code)

for num in range(5):
    print(f"The number is: {num}")

--> this call didn’t include the number 5.

# What if we wanted the range from 1 to 4, instead of 0 to 4?
range(start, stop, step(optional))

for num in range(2, 11, 2):
    print(f"The number is: {num}")

*** If you can’t remember how to use range, don’t forget to call help(range) from the command line. ***
"""

"""
#Looping over items with the index using enumerate(Remember, indicies in Python start at zero)

tuple unpacking
point = (2, 5, 11)
x, y, z = point

colors = ["Red", "Green", "Blue", "Orange"]
for index, item in enumerate(colors):
    print(f"Item: {item} is at index: {index}.")


#looping over dictionary 
hex_colors = {
    "Red": "#FF",
    "Green": "#008",
    "Blue": "#0000FF",
}

for color in hex_colors:
    print(f"The value of color is actually: {color}")

--> loop over the key, value pairs in a dictionary my_dict.items()

"""


"""
#Additional Resources
If you really want to be a pro at looping in a Pythonic way --> https://www.youtube.com/watch?time_continue=1855&v=OSGv2VnC0go
"""


"""
IF, ELSE, ELIF

if in Python means --> only run the rest of this code once, if the condition evaluates to True
(Anatomy)The syntax is: 
Start with the if keyword
followed by a boolean value, an expression that evaluates to True, or a value with “Truthiness”
Add a colon : (a new line)
    write the code that will run if the statement is True under a level of indentation.
    ***All the lines indented under the if statement will run if it evaluates to True***

Example:

if 3 < 5:
    print("Hello, World!")

#Using not With if Statements
---> If you only want your code to run if the expression is False, use the not keyword.

b = False
if not b:
    print("Negation in action!")

if Statements and Truthiness

if statements also work with items that have a “truthiness” to them.

For example:

--> The number 0 is False-y, any other number (including negatives) is Truth-y
--> An empty list, set, tuple or dict is False-y
        Any of those structures with items in it is Truth-y

message = "Hi there."

a = 0
if a:
    print(message)

b = -1
if b:
    print(message)

c = []
if c: 
    print(message)

d = [1, 2, 3]
if d:
    print(message)
"""


"""
if Statements and Functions
#Declaring if statements inside functions

def modify_name(name):
    if len(name) < 5:
        return name.upper()
    else:
        return name.lower()

name = "Max"
modify_name(name)
"""

"""
Nested if Statements

def num_info(num):
    if num > 0:
        print("Greater than zero")
        if num > 10:
            print("Also greater than 10.")

num_info(1)
num_info(15)
"""

"""
#How Not To Use if Statements
comparisons in Python evaluate to True or False.
With conditional statements, we check for that value implicitly.
In Python, we do not want to compare to True or False with ==

# Warning: Don't do this!
if (3 < 5) == True: # Warning: Don't do this!
    print("Hello")

Prints --> Hello

# Warning: Don't do this!
if (3 < 5) is True: # Warning: Don't do this!
    print("Hello")

Prints --> Hello
"""

"""
Do this instead:
if 3 < 5:
    print("Hello")

If we want to explicitly check if the value is explicitly set to True or False,
we can use the is keyword.

a = True        # a is set to True
b = [1, 2, 3]   # b is a list with items, is "truthy"

if a and b:     # this is True, a is True, b is "truthy"
    print("Hello")

Prints --> Hello
if a is True:   # we can explicitly check if a is True
    print("Hello")

Prints --> Hello

if b is True:   # b does not contain the actual value of True.
    print("Hello")
"""

"""
#else statement
    #is what you want to run if and only if your if statement wasn’t triggered
    #An else statement is part of an if statement. If your if statement ran, your else statement will never run.

a = True
if a:
    print("Hello")
else:
    print("Goodbye")

"""

"""
# elif Means Else, If
    #if this if statement isn’t considered True, try this instead
    #You can have as many elif statements in your code as you want
        #They get evaluated in the order that they’re declared until Python finds one that’s True.
a = 5
if a > 10:
    print("Greater than 10")
elif a < 10:
    print("Less than 10")
elif a < 20:
    print("Less than 20")
else:
    print("Dunno")
"""


"""
#While Loops
    #while loops are a special type of loop in Python
    #they run forever until a condition is no longer met

counter = 0
max = 4

while counter < max:
    print(f"The count is: {counter}")
    counter = counter + 1

"""

"""
# Warning: Don't run this example

counter = 0
max = 4

while counter < max:
    print(f"The count is: {counter}")

# What happens if we don't update counter?
"""

"""
BREAK, CONTINUE, AND RETURN
    #break and continue allow you to control the flow of your loops.

#Using break
    #The break statement will completely break out of the current loop
names = ["Rose", "Ananya", "Max", "Sumit"]
for name in names:
    print(f"Hello, {name}")
    if name == "Max":
        break

#break completely, breaks out of the loop.


#Using continue
    #continue works a little differently. Instead, it goes back to the start of the loop,
    #skipping over any other statements contained within the loop.

names = ["Rose", "Ananya", "Max", "Sumit"]
for name in names:
    if name != "Max":
        continue
    print(f"Hello, {name}")

#continue continues to the start of the loop
"""

"""
#Practice

names = ["Ananya", "Rose", "Max", "Sumit"]
for name in names:
    if len(name) != 4:
        continue

    print(f"Hello, {name}")

    if name == "Sumit":
        break

print("Done!")
"""


"""
#Loop Control in while loops
    #break and continue in while

while True:
    count += 1
    if count == 5:
        print("Count reached")
        break
"""

"""
#Loops and the return statement
    #Is like closing a application forcefully from task manager

def name_length(names):
    for name in names:
        print(name)
        if name == "Sumit":
            return "Found the special name"

names = ["Max", "Sumit", "Rose"]
name_length(names)
"""


"""
#Practice Questions

def test_number(number):
    if number < 100:
        print("This is a pretty small number")
    elif number == 100:
        print("This number is alright")
    else:
        print("This number is huge!")

test_number(5)
test_number(99)
test_number(100)
test_number(8675309)



def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizzbuzz!")

fizzbuzz(3)
fizzbuzz(5)
fizzbuzz(15)


def my_func(my_list):
    if my_list:
        for item in my_list:
            if item is None:
                print("Got None!")
            else:
                print(item)
    else:
        print("Got an empty list!")

my_func([1, 2, 3])
my_func([])


for num in range(0, 3):
    print(f"Next value: {num}")

my_list = ["foo", "bar", "baz"]
for index, item in enumerate(my_list):
    print(f"Item {index}: {item}")

#Looping over dictionary

my_dict = {"foo": "bar", "hello": "world"}
for key in my_dict:
    print(f"Key: {key}")

# This is equivalent to...
for key in my_dict.keys():
    print(f"Key: {key}")

#Looping over values
for value in my_dict.values():
    print(f"Value: {value}")

#Looping over key and values in a dictionary
for key, value in my_dict.items():
    print(f"Item {key} = {value}")


#Break

for num in range(0, 100):
    print(f"Testing number {num}")
    if num == 3:
        print("Found number 3!")
        break
    print("Not yet...")

#Continue
for num in range(0, 100):
    print(f"Testing number {num}")
    if num < 3:
        continue
    elif num == 5:
        print("Found number 5!")
        break
    print("Not yet...")
"""

"""
#Using break and continue in nested loops(Difficult --> Hard)

names = ["Rose", "Max", "Sumit"]
target_letter = 'x'
for name in names:
    print(f"{name} in outer loop")
    for char in name:
        if char == target_letter:
            print(f"Found {name} with letter: {target_letter}")
            print("breaking out of inner loop")
            break

--> break in the inner loop only breaks out of the inner loop! The outer loop continues to run.
"""
