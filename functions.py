# functions
# code reuse or recursion
# for large programs follow DRY priciple don't repeat yourself ex: use of loops ad easy to maintain
# repetitive code follows WET principle Write Everything Twice

# any statement that consits of of word followed by information in parentheses is a function call.

print("hello workd!")
range(2, 20)
str(12)
range(10, 20, 3)


# we can define functions using def statement

def my_fun():
    print("spam")
    print("eggs")


my_fun()


def abc(word):  # word inside () is arguments we can pass multiple at a time.
    print(word + "!")


abc("hangman")
abc("reddy")


def my(x, y):
    print(x + y)


my(5, 8)  # my(int(input()),int(input()))


# fun arguments ca be used as variables inside the fun.
# they can't be referenced outside of fun definition also appies to all var in fun.

# parameters are variables in a fun def.
# arguments are the values put into parameters when fun are called.

def fun(var):
    var += 1
    print(var)


fun(7)

# print(var) # error as accessing out of scope variable

# returning from functions
def max(x, y):
    if x >= y:
        return x
    else:
        return y


print(max(4, 7))
z = max(8, 5)
print(z)

# once we return the execution stops there.

# docstrings have similar purpose to comments as they are designed to explain code

"""
    print a v  igh
"""


def mul(x, y):
    return x * y


a = 4
b = 7
operation = mul  # funnction as object
print(operation(a, b))


# functions can also be used as arguments of other functions

def add(x, y):
    return x + y


def do_twice(func, x, y):
    return func(func(x, y), func(x, y))


a = 5
b = 10
print(do_twice(add, a, b))

# modules

# modules are pieces of code that other people are writte to fullfill common tasks,
# such as geerating random numbers, mathematical operations.

# asic way use a module is import module_name at the top and then using module_name.var
# to access functions and values with name var in the module

import random  # similarly we can use from math import pi, sqrt to import certain functions.

# import some_module trying to import a unavailable module give importError
for i in range(5):
    value = random.randint(1, 6)
    print(value)

for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally finished!")

# we can import module or object under a diff name using as

from math import sqrt as square_root
print(square_root(100))