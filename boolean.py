# # boolean type True or False, also return when compared like 2==3
#
# var1 = True
#
# print(var1)
# print(2==3)
#
# print("hello" == "hello")
#
# # comparison operators or rational operators
# print(1 != 1)
# print("eleven" != "seven")
#
# # similarly we can use >, < int,float can also be compared
# print(7 == 7.0)   # will be true as both are numbers and comparing
#
# print("andie" > "wndy")
# # compare strings lexicographically the alphabetical or
# # order of word is based on the alphabetical order of component letters
#
# # boolean logic  and, or, not
# print(1 == 1 and 2 == 2)
# print( 1 == 1 and 2 == 3)
# print( 1 !=1 and 2 == 2)
# print(2 < 1 and 3 > 6)
#
# print(1 == 1 or 2 == 2)
# print(1 == 1 or 2 == 3)
# print(1 != 1 or 2 == 2)
# print(2 < 1 or 3 > 6)
#
# print(not 1 == 1)
# print(not 1 > 7)

# operator precedence same as order of operations
print(False == False or True)
print(False == (False or True))
print((False == False) or True)

# chaining conditions
grade = 88
if grade >= 70 and grade <= 100:
    print("passed")