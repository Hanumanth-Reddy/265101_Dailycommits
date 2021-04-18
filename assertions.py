# Assertions
# an assertion is as sanity check that you can turn on and off when u have finished testing the program
# an expression is tested and if the result comes up false, an exception is raised

# assertions are carried out through use of assert statements
# print(1)
# assert 2 + 2 == 4
# print(2)
# assert  1 + 1 == 3
# print(3)

# most programmers use assertion at the start of functions to check for valid input and after
# function call to check for valid output
#
# print(0)
# assert "h" != "w"
# print(1)
# assert False
# print(2)
# assert True
# print(3)


# assert can take a 2nd argument that is passed to the AssertionError raised if assertion fails

temp = -10
assert (temp >= 0), "colder Than absolute Zero!"
