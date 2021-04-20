# to combine  strings and non-strings we have converted non strings to strings then add them.
# string formating provides more powerful way to embed non-strings with in strings.

nums = [4,5,6]
msg = "Nummbers:{0} {1} {2}".format(nums[0], nums[1], nums[2])
print(msg)

# string formating with named argumemts

a = "{x}, {y}".format(x=5,y=12)
print(a)