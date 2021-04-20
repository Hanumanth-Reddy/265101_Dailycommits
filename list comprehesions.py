# list comprehensions are useful way of quickly creating lists whose contents obey a simple rule.
# they are inspired by set-builder notation in maths
cubes = [i ** 3 for i in range(5)]
print(cubes)

# they can also contain an if statement to enforce a condition o values i the list

evens = [i ** 2 for i in range(10) if i ** 2 % 2 == 0]
print(evens)

# trying to create a list in a very extesive rage will result in MemoryError ad rus out of memory this ca e overcomed y geerators
# evens = [2*i for i in range(10**100)]
# print(evens)