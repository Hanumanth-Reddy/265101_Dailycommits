# lists
# lists are used to store items
# syntax is [] with commas separating each element

words = ['hello, ', 'world', '!']

print(words[0]+words[1]+words[2])
words[1] = "hanumanth"  # modify element
print(words[0]+words[1]+words[2])
print(words)

# empty list for use later
empty_list = []
print(empty_list)

# typically a list will contain 1 type items
# it is possible to include diff types of items

number = 3
things = ["string", 0, [1, 2, number], 4.56]
print(things[0])
print(things[1])
print(things[2][1])
print(things[3])

# nested lists can be used to represent 2d grids such as matrix

m = [
    [1, 2, 3],
    [4, 5, 6]
]
print(m[1][0])

# list with strings
# string behaves as though you are indexing each element or char in string

str = 'hello world!'
print(str)
print(str[6])

# list operations

num = [7, 7, 7, 7, 7]
num[2] = 5  # replace
print(num)
# add and multiply lists

nums = [1, 2, 3]
print(nums + [4, 5, 6])
print(nums * 3)

# in operator with lists

words = ["spam", "eggs"]
print("spam" in words)   # gives boolean

# not operator in lists

nums = [1, 2, 3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)

# list functions
nums = [1, 2, 3]
nums.append(4)  # dot before append is there as it is a method of list class
print(nums)
print(len(nums))  # len is written before list it is being called on, without a dot

#insert method

words = ["python", "fun"]
index =1
words.insert(index, "is")  # elements after the inserted item are shifted to right
print(words)

# index method
# index method finds he 1st occurance of list item and return s its index

letters = ["p", "r", "p"]
print(letters.index("r"))
print(letters.index("p"))

# more functions for lists

print(max(letters))  # max value in list
print(min(letters))  # min value in list
print(letters.count("p"))  # how many times an items occurs in a list
letters.remove("p")  # remove an element
print(letters)
letters.reverse()   # reverse items in a list
print(letters)
print(letters[-1])  # negative index means start from end
print(letters[0:2])   # range end will not be counted
