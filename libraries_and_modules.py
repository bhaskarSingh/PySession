# Standard Library
"""
Python has always had a “batteries included” philosophy - having a rich
and versatile standard library which is immediately available, without 
making the user download separate packages.
"""

# The full list of standard libraries can be found in the python documentation
# Link: https://docs.python.org/3/library/

"""
import datetime
right_now = datetime.datetime.now()
print(right_now)
print(repr(right_now))
"""
# Getting no of days from new year
# new_years = datetime.datetime(2020, 1, 1, 0, 0)
# print(new_years)
# delta = right_now - new_years
# print(delta)


#Modules and Imports
"""
Python has a simple package structure. Any directory with a file named __init__.py
can be considered a Python module.

**In Python3: __init__.py file is no longer required, 
but it’s still supported and can be useful.**
"""

# Creating module in python for add_numbers function
"""
def add_numbers(x, y):
    return x + y
"""

# Best Practices
"""
#You can import everything from a module into the local namespace using *:
from my_math_functions import *
add_numbers(1, 2)

** This isn’t a good practice **
#Because it’s hard to tell where a specific function is coming from without the namespace context.
#function names can conflict, and this can make things very difficult to debug.


#Better Approach: import functions specifically
from my_math_functions import add_numbers
add_numbers(1, 2)


#Even better way is to just import the module and use it in calls to maintain the namespace context:
import my_math_functions
my_math_functions.add_numbers(1, 2)

#This can be slightly more verbose, but unless it makes your function calls ridiculously long,
#it generally makes things much easier to debug.
#Use as keyword to make things little easier

import my_math_functions as mmf
mmf.add_numbers(1, 2)
"""


# What is a Python Path ?
"""
#This is a list of paths on your system where Python will look for packages.
#You can also install your modules just like any other external modules
"""


# PYPI(the Python Package Index)
"""
-> awesome service that helps you find and install software developed and shared by the Python community.
-> #You can browse the site at pypi.org,
-> #but most of the time you will probably interact with it through Python’s pip tool.
"""

"""
#You can use the pip tool to install the latest version of a module
#and its dependencies from the Python Packaging Index:

pip install SomePackage
"""

# Practice Time
"""
#Create a new file and use the os module to see if you can get a file listing
#for the folder your new file is in.

import os
my_folder = os.getcwd()
print(f"Here are the files in {my_folder}:")
with os.scandir(my_folder) as folder:
    for entry in folder:
        print(f" - {entry.name}")


#using sys to get the arguments passed into our program from the command line,
#and to figure out what kind of computer we’re using:

import sys

arguments = sys.argv
print(f"We received the following arguments:")

for arg in arguments:
    print(f" - {arg}")

print(f"We are running on a '{sys.platform}' machine")
"""
