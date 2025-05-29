# 👉Raising custom:-

#👉 The raise statement in Python is used to raise an exception.
# Try-except blocks can be used to manage exceptions, which are errors
# that happen while a programme is running. When an exception is triggered,
# the programme goes to the closest exception handler, interrupting
# the regular flow of execution.
#
# 👉The raise keyword is typically used inside a function or method,
# and is used to indicate an error condition.
# 👉We can throw an exception and immediately halt the running of
# your programme by using the raise keyword.
# 👉Python looks for the closest exception handler, which is often
# defined using a try-except block, when an exception is triggered.
# 👉If an exception handler is discovered, its code is performed,
# and the try-except block's starting point is reached again.
# 👉If an exception handler cannot be located, the software crashes and
# an error message appears.

a = int(input("Enter number between 5 and 9="))

if(a<5 or a>9):
    raise ValueError("Value should be between 5 and 9")