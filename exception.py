# exceptions they occur when something goes wrong due to incorrect code or input

# num1 = 7
# num2 = 0
# print(num1/num2)

# different exceptions
# ImportError : an import fails
# IndexError: a list is indexed with out of range number
# NameError : an unknown name variable is used
# SyntaxError : the code can't be parsed properly
# TypeError : a function is called on a value of inappropriate type
# ValueError : a function is called on a value of correct type , but with an inappropriate value.
# python has several built in exceptions like ZeroDivisionError ad OSError

# Exception Handling
# to call code when an exception occurs, we can use try/except

# try block contains code that might throw an exception. i that occurs, the code in try
# blocks stops being executed. and the code in the except block is run. if no error
# occurs except block doesn't run.

# try:
#     num1 = 7
#     num2 = 0
#     print(num1/num2)
#     print("done")
# except ZeroDivisionError:
#     print("divisor is zero pls check")
#
# try:
#     var = 10
#     print(var + "hello0")
#     print(var / 2)
# except ZeroDivisionError:
#     print("divisor is zero")
# except (ValueError, TypeError):
#     print("error")
#
try:
    word = "spam"
    print(word / 0)
except:
    print("error occured")

# # exception handling is particularly useful when dealing with user input.
#
# # finally to ensure code runs no matter what error occurs, we can use a finally statement
# # finally statement is placed at the bottom of try/except statement.
# # code within in finally statement always runs after execution of try, ad possibly except.
# #
# # try:
# #     print("hello")
# #     print(1 / 0)
# # except ZeroDivisionError:
# #     print("Divide by zero")
# # finally:
# #     print("This code will run no matter what")
#
# # finally statement even runs if an uncaught exception occurs in one of the preceding blocks.
#
# #
# # try:
# #     print(1)
# #     print(10 / 0)
# # except ZeroDivisionError:
# #     print(unknown_var)
# # finally:
# #     print("This is executed last")
#
# # Raising Exceptions
# # you can raise exceptions by using raise statement
# # print(1)
# # raise ValueError
# # print(2)
#
# name = "123"
# raise NameError("Invalid name!")  # exception can be raised with arguments
#
# # in except blocks, the raise statement ca be used without arguments to re-raise whatever excepption occured
#
# try:
#     num = 5 /0
# except:
#     print("An error occured")
#     raise