# This is an example project, showing a program that analyzes a sample file to find what percentage of the text each
# character occupies.
#
# filename = input("enter a file")
# with open(filename) as f:
#     text = f.read()
#
# print(text)


# This part of the program shows a function that counts how many times
# a character occurs in a string.

def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
        return count


# This function takes as its arguments the text of the file and one character, returning the number of times that character appears in the text.
# Now we can call it for our file.
filename = input("enter file name: ")
with open(filename) as f:
    text = f.read()
print(count_char(text, "p"))

# The next part of the program finds what percentage of the text each character of the alphabet occupies.
for char in "abcdefghijklmnopqrstuvwxyz":
  perc = 100 * count_char(text, char) / len(text)
  print("{0} - {1}%".format(char, round(perc, 2)))
