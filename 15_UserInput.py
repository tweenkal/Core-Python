# 👉User input :-

a = int(input("Enter the a="))
b = int(input("Enter the b="))

sum = a + b
print("Sum=",sum)

# 👉eval() :- eval is the function in the python.
#👉 The eval() function in Python evaluates a string as a Python expression

ch = input("Enter character=")[0]
print(ch)

result = eval(input("Enter character="))
print(result)

# 👉Command line input

# 👉sys.argv is a list in Python that stores command-line arguments
# passed to a script. It's part of the sys module, which provides access
# to system-specific parameters and functions. The first element of the
# list, sys.argv[0], is the name of the script itself, and subsequent
# elements, sys.argv[1],
#
# import sys
#
# x = int(sys.argv[1])
# y = int(sys.argv[2])
#
# z = x + y
# print(z)