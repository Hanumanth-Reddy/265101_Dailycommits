# Slicing

# list slicing
# list slices provide a more advanced way of retrieving values from a list.
# basic list slicing involves indexing a list with two colon-separated integers.
# this returns a new list containing all the values in the old list  between the indices

squares = [0,1,4,9,16,25,36,49,64,81]
print(squares[2:6])
print(squares[0:1])
print(squares[-4:-1])

print(squares[:7]) # specifying end
print(squares[7:]) # specifying start

# slicing can alsoS be done on tuples in a same way.

# list slices can also have a third number, representing the step, to include only alternate values in the slice.

print(squares[::2])
print(squares[2:8:3])

print(squares[::-1])  # to reverse a list using slice
print(squares[1:-1])
print(squares[7:5:-1])
