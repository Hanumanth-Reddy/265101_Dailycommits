# Functional programming is a style of programming that (as the name suggests) is based around functions.
# A key part of functional programming is higher-order functions. We have seen this idea briefly in the previous
# lesson on functions as objects. Higher-order functions take other functions as arguments, or return them as results.


def apply_twice(func,arg):
    return func(func(arg))

def add(x):
    return x+5

print(apply_twice(add,10))


# Pure Functions
#
#
# Functional programming seeks to use pure functions. Pure functions have no side effects, and return a value that
# depends only on their arguments.
# This is how functions in math work: for example, The cos(x) will, for the same value of x, always return the same result.
# Below are examples of pure and impure functions.

def pure_function(x, y):
  temp = x + 2*y
  return temp / (2*x + y)

# Impure function:
some_list = []

def impure(arg):
  some_list.append(arg)
#
# The function above is not pure, because it changed the state of some_list.



# Pure Functions
#
#
# Using pure functions has both advantages and disadvantages.
# Pure functions are:
# - easier to reason about and test.
# - more efficient. Once the function has been evaluated for an input, the result can be stored and referred to
# the next time the function of that input is needed, reducing the number of times the function is called. This is called memoization.
# - easier to run in parallel.
# The main disadvantage of using only pure functions is that they majorly complicate the otherwise simple task of I/O,
# since this appears to inherently require side effects.
# They can also be more difficult to write in some situations.
