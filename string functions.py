#
# Python contains many useful built-in functions and methods to accomplish common tasks.
# join - joins a list of strings with another string as a separator.
# replace - replaces one substring in a string with another.
# startswith and endswith - determine if there is a substring at the start and end of a string, respectively.
# To change the case of a string, you can use lower and upper.
# The method split is the opposite of join turning a string with a certain separator into a list.

print(",".join(["spam","eggs","ham"]))
print("hello me".replace("me","world"))
print("this is python".startswith("this"))
print("this is python".endswith("python"))
print("hello world hi".split(" "))
print("hi".upper())  # lower

# Numeric Functions
#
# to find the maximum or minimum of some numbers or a list, you can use max or min.
# To find the distance of a number from zero (its absolute value), use abs.
# To round a number to a certain number of decimal places, use round.
# To find the total of a list, use sum.
print(min(1,2,3))
print(max(1,4,56.2,100))
print(max([1,4,56.2,100]))
print(abs(-99))
print(abs(42))
print(sum([1,2,3,4]))   # sum of list
print(round(45.4567))
print(sum((1,2)))

# List Functions

# Often used in conditional statements, all and any take a list as an argument, and return True if all or any (
# respectively) of their arguments evaluate to True (and False otherwise). The function enumerate can be used to
# iterate through the values and indices of a list simultaneously.

nums = [55,44,33,22,11]
if all([i>5 for i in nums]):
    print("all >5")
if any([i%2==0 for i in nums]):
    print("atleast one is even")

for v in enumerate(nums):
    print(v)
