# Advance Data Types
# list, tuple, dict and set: container objects
# Allow us to organize other types of objects/Data Types into one data structure


"""
list/[] //Retain the order of items in them
#Use: for storing similar items, where items need to be added or removed
"""

# empty list ---> [] / list() (Built-In-Method)(Cause everything is an object in python)

# names = ["Nina", "Amir", "Max", "Nina"]

# check length len() - Built-In-Method it is not present on the list

# Access list item using index, starts at zero

# Slicing a list
# my_list = ["h", "e", "l", "l", "o", "w", "o", "r", "l", "d", "!"]
# my_list[4:6]
# my_list[4:]
# my_list[-2:]

# Sorting list
# 1 sorted() --> returns a copy of sorted list
# 2 list_variable.sort() --> In Place / list_variable.reverse() --> In Place

# Adding/Updating items in the list
# append() --> Add an item to the end of the list
# insert() --> Add an item to arbitrary
# extend() --> combine two list
# update --> list_variable_name[index] = "new value"

# list lookup(Search Methods)
# In keyword for checking if item is present in the list or not
# index() --> check at which index item is present
# count() --> check how many times a item occurs in a list

# removing items in a list
# remove("Item Name") --> removes first instance of item in place
# pop() --> Remove and return item at index (default last)

# Common Mistakes
# (leaving comma for separting values) [1, 2, 3 4]


"""Tuple useful for storing a snapshot of related immutable items"""

# creating empty and one item tuple

# For creating Tuple () are optional but comma is required

# Tuples values can't be modified

# Unpacking tuples

# Lookup/Search in tuples(using index method & in operator)


"""
Sets
    #stores immutable types in a unsorted way(don't have any order)
    #Item can only be contained in the set once, on duplicates are allowed
    #Benefit:fast membership test
"""

# Creating empty set(with set(), {} this will create dict)

# Sets with items

# Sets can only contain immutable types(hash() -->  representing an immutable data type with a unique numerical representation)

# Sets can be used to de-duplicate the items in a list

# Adding item to a set(add())

# Removing item from a set(discard(item) --> doesn't throw error incase no value is found / remove(item) --> throws error incase no value found)

# updating a set (update(sequence))

# Set Operations
# s.union(t) or s|t --> creates a new set with all the items from both s and t
# s.intersection(t) or s & t --> creates a new set only containing item that are both in s and t
# s.difference(t)--> creates a new set with item in s but not in t


"""
Dictionaries
    #allow us to store our data in key, value pairs
    #are mutable, but, dictionary keys can only be immutable types
"""

# Q: What happens when we try to access a key in a dictionary with square bracket notation,
# but the key isn’t present?

# Accessing items in a dictionary(dict_variable[key] or dict_variable.get(key, default_value));

# Adding items to a dictionary

# Removing items from a dictionary(del dict[key] or dict.pop(key, default_value))

# Combining two dictionary(update())

# Useful methods
# my_dict.keys() --> Get all the keys in a dictionary
# my_dict.values() --> Getting all the values in a dictionary
# my_dict.items() --> Getting all the items (key, value pairs) in a dictionary


# Boolean Logic: allows you to test your assumptions(True and False --> keywords in python)
# bool(expression) --> test assumptions about an expression that returns True or False

# Truthiness
"""
int --> 0 is False, all other numbers are True (including negative)
list, tuple, set, dict --> empty container evaluates to False, container with items evaluates to `True)
None --> False, is commonly used as a placeholder to mean “I haven’t set this value yet.”
"""

# Comparisons
# Strings are compared lexicographically, (ASCII value of the character)
# Hint: capital letters come before lower case ones
"""
"T" < "t"
"a" < "b"
"bat" < "cat"
"""

"""
a = [1, 2, 3]
b = [1, 2, 3]
a === b ? True or False
a is b ? True or False
"""

"""
a = True
a is True

b = False
b is False

c = None
c is None

c is not None
False
"""


# and, or, not Boolean Logic

"""
a and b -->	For a and b, if a is false, a is returned. Otherwise b is returned.
If a and b are both boolean values, the expression evaluates toTrue if both a and b are True.

a = True    # a is True
b = True
a and b     # True is returned. (value of b)
a = False   # a is False
b = True
a and b     # False is returned. (value of a)
a = False   # a is False
b = False
a and b     # False is returned. (value of a)
"""

"""
a or b --> For a or b, if a is false, b is returned. If a is true, a is returned.
a or b evaluates to True if either (or both) of the expressions are true.

a = True    # a is true
b = True
a or b      # True is returned (value of a)
a = False   # a is false
b = True
a or b      # True is returned (value of b)
0 or 1      # 0 is false. Return 1.
"""

"""
not a --> not a reverses the boolean value of a. If it was true, it will return False.
If it was false, it will return True.

a = True
not a  # not returns the opposite. True -> False
a = False
not a  # not returns the opposite. False -> True
"""

"""
#Practice
True or False
[] or [1, 2, 3]
"Hello" or None
5 and 0
[1] and [1, 2, 3]


a = False
b = False
c = False
a or b or c
b = True
a or b or c
a and b and c
a = True
c = True
a and b and c
"""
