# dictionaries are data structures used to map arbitrary keys to values.
# lists can be thought of as dictionaries with integer keys with in a certain range.
# dictioaries ca e index with brakets containing keys.
ages = {"dave": 24, "mary": 42, "john": 58}
print(ages["dave"])
print(ages["mary"])

# each element is represented by key:value pair

# trying to index a key returns KeyError.
#  empty dictionary is defied as {}

primary = {
    "red": [255, 0, 0],
    "green": [0, 255, 0]
}
print(primary["green"])
print(primary["red"][0])

# only immutable objects can be used as a keys to dictionaries.
# immutable means can't be changed. lists are mutable.
# trying to use a mutable object as a dictionary key causes a TypeError.

# bad = {
#     [1,2,3]:"one two three"
# }

# just like lists, dictionary keys can be assigned to diffent values.
# however, unlike lists, a new dictionary key can can also assigned a value, not just ones that already exist.
squares = {1: 1, 2: 4, 3: "error", 4: 16}
squares[8] = 64
squares[2] = 9
print(squares)

# to determine whether a key is in a dict or not we can use in and not in, just like lists.

nums = {
    1: "one",
    2: "two",
    3: "three"
}

print(1 in nums)
print("three" in nums)
print(4 not in nums)

# get method. it does the same thing as indexing, but if the key is not found in the dictionary it returns another specified value instead("None" by default)

pairs = {
    "orange": [2, 3, 4],
    True: False,
    None: "True"
}
print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(12345, "not in dictionary"))  # key not found show message.
print(pairs.get(True, "orange"))

fib = {1: 1, 2: 1, 3: 2, 4: 3}
print(fib.get(4, 0) + fib.get(7, 5))
print(fib)

