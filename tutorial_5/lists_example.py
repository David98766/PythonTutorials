# Python program to demonstrate List

# In Python, lists are a MUTABLE data type (values be modified).
# they are an ordered collection of data values
# lists are dynamic and can contain objects of different data types
#List elements can be accessed by index number.

list = ["mango", "strawberry", "orange",
        "apple", "banana", 123, True] # True is a boolean value, not a string.
print(list)

# we can specify the range of the index by specifying where to start and where to end
print(list[2:4])

# we can also change the item in the  list by using its index number
list[1] = "grapes"
# strawberry is now grapes
print(list[1])

# The alternatives to lists in Python would be arrays, and tuples.
# Arrays are more memory efficient, but less functional
# Tuples are immutable, and are not dynamic.