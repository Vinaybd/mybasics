# A module in Python is a file containing
# Python definitions and statements (such as functions, classes, and variables). It allows you to organize your code into separate, reusable components.

import math
import math as m
from math import e

# print(pi)

a,b,c,d = 1,2,3,4

print(math.e**a)
print(e ** a)
print(e ** b)
print(e ** c)
print(e ** d)


# my_module.py

def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b



# main.py
# import my_module

# # Using functions from my_module
# greeting = my_module.greet("Alice")
# print(greeting)  # Output: Hello, Alice!

# result = my_module.add(3, 5)
# print(result)  # Output: 8
