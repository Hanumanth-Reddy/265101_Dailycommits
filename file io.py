# file operations:

# OPENING FILES:

# file must be opened before we edit it

my_file = open("1.py")
# argument of open fun is path to the file. if file is in PWD just specify name.

# specify modes while opening a file like r, w, wb etc

# w - write mode, r - read mode, a - append and adding "b" to mode opens file in binary mode.
# which is used for non text files such as images and sound files
# r+ opens the file in read and write.
#
# file = open("1.py", "w")
#
# open("1.py", "r")
#
# open("1.py", "wb")
#
#
# # closing file using close()
# file.close()


# READING FROM FILES

# read method
#
# file = open("1.py","r")
# cont = file.read()
# print(cont)
# file.close()
#
# file = open("1.py","r")
# print(file.read(16))   # read number of bytes
# print(file.read(4))
# print(file.read(4))
# print(file.read())  # print(file.read())
# file.close()

# just like passing no arguments , negative values will return the entire contents.


# after all the contents in a file have been read, any attempts to read further
# from that file return an empty string as we trying to read from EOF.

# file = open("1.py", "r")
# file.read()
# print("Re-reading")
# print(file.read())
# print("Finished")
# file.close()

# readlines method to return a list in which each element is aline in the file.
# file = open("1.py")
# print(file.readlines())

# using for loop to iterate through the lines in the file
# file = open("1.py")
# for line in file:
#     print(line)
#
# file.close()


# WRITING INTO FILES
file = open("writetrial.txt", "w")
file.write("How are u hanumanth")
file.close()

# delete a file we must import OS module
# import os
# os.remove("writetrial.txt")
# similarly path.exists to check file whether file exists or not rmdir to remove empty directory

# from os import remove
# remove("writetrial.txt")

try:
    f = open("1.py")
    print(f.read())
finally:          # to make sure file always closes even if error occurs
    f.close()

# another way is to use WITH which will create a temp var, which is accessed in the indented block
# of the with statement

# file automatically closed at the  end of with statement, even if exceptions occur within it

with open("1.py") as f:
    print(f.read())
