# 👉Exception handling:-
# 👉Errors:-
# 👉Three types of error:-
# 1)compile time error 2)logical error 3)run time error
# 👉that code have a multiple statements and one of the statement you
# have syntax error
from logging import exception

from django.db.models.expressions import result
from reportlab.lib.PyFontify import keyPat

# 1)Compile time error:-
# 👉exa of :- 1)missing(:) 2)wrong spelling etc... is called the compile
# time error.
# 👉compile time error is most easy because it is the developer side

# 2)Logical error:-
# 👉Logical error means code is compile and give the output but not
# give the correct output its called logical error for exa.. 3+2 =5
# but give me the output is ans 4 then it is logical error.
# 👉Logical error is again to easy tp handle because the developer is to
# test the application and test the specific testing team again.to test is
# software is different bugs so logical error is come normally bugs as well

# 3)run time error:-
# 👉run time error means the code is compile properly not a compile error ,
# not a logical error give me output is right but user input not properly
# like 6/0 is not possible its called the runtime error for exa.divide by
# zero
# 👉run time error is not mistack for the developer is done by the user
# 👉statement is divided into two parts:-
# 1)Normal statement  :- not will give the error
# 2)critical statement
# 👉Exception is handling the error
# 👉exception block is execute for the only error
#👉finally block is the the doesnt metter for exception or not this is
# execute.finally block will be execute  if we  get error as well as if we
# dont get the error
# 👉different type of error we have the except different type of block
# 👉types of the error exception :- 1)Zerodivisionbyerror 2)valueerror
# 👉zero division error:=

a = 5
b = 0
try:
    print("Resource open")
    print(a/b)

except Exception as e:
    print("hey do not divide the number of zero",e)

finally:
    print("Resource closed")


# multiplication table

a = input("Enter number=")
print(f"Multiplication table of {a} is : ")

try:
    no = int(a)
    for i in range(1,11):
        print(f"{(no)} X {i} = {int(no * i)}")

except:
    print("sorry you enter the Invalid input")

print("Programme finished")



# value error and index error

try:
    num = int(input("Enter no="))
    a = [6,7]
    print(a[num])

except ValueError:
    print("Number entered in not int")

except IndexError:
    print("Index error")

# Divide by Zero :- ZeroDivisionError
# Task: Write a function that takes two numbers and divides them.
# Use a try-except block to handle ZeroDivisionError and print
# "Cannot divide by zero."

try:
    a = int(input("Enter no1="))
    b = int(input("Enter no2="))
    c = a / b
    print(c)

except ZeroDivisionError:
    print("Can not divide by zero")


# Dictionary Key Error :- KeyError
# Task: Create a dictionary with a few key-value pairs.
# Ask the user for a key and print the value.
# Handle the error if the key doesn’t exist.

student = {'name' : 'twinkle' , 'age' : 21 , 'course' : 'BCA'}

key = input("Enter the key=")

try:
    print("value=",student[key])

except KeyError:
    print("if key doesnt exist")


# Type Error :- TypeError
# Task: Create a program that tries to add a string and an integer.
# Handle the TypeError when this happens.

try:
    # result = "hello" + str(5)
    result = "hello" + 5
    print(result)

except TypeError:
    print("Error: You cannot add a string and an integer.")


# FileNotFoundError

try:
    file = open("data.txt","r")
    print(file.read())

except FileNotFoundError:
    print("Error: File not found. Please check the file name.")


# AttributeError
try:
    text = "hello world!"
    text.append("!")

except AttributeError:
    print("Error: This object does not have that attribute or method.")


# NameError
try:
    # x = 6
    print(x)
except NameError:
    print("Error: The variable 'x' is not defined.")


# ImportError :- ImportError is a Python exception that occurs when
# Python fails to import a module or a specific object from a module.

try:
    # from math import sqrt
    # print("Import successfully",sqrt(16))
    from math import fake_function

except ImportError:
    print("Error: Could not import the specified object from the module.")

# ModuleNotFoundError:-ModuleNotFoundError is a Python exception that
# occurs when you try to import a module that doesn’t exist

try:
    # import math
    # print("Module import succesfully")
    import fake_function

except ModuleNotFoundError:
    print("Error: Module not found. Please check the module name.")

# OverflowError :-OverflowError in Python occurs when a numeric
# calculation exceeds the maximum limit that a number can hold.

import math
try:
    # result = math.exp(5)
    result = math.exp(710)  #709 sudhi thase approximatly
    print("Result=",result)

except OverflowError:
    print("OverflowError: Number too large to handle.")


# MemoryError:-MemoryError in Python occurs when your program tries
# to use more memory than your system can provide.

try:
    # char = "a" * 1000
    # char = "a" * 10**100
    print("string created successfully!!!")

except MemoryError:
    print("MemoryError: Not enough memory to create this object.")

# IndentationError:-IndentationError is a Python exception that occurs
# when your code is not properly indented.

try:
    print("hello")
# print("hello")

except:
    print("Something went wron")

# RuntimeError:-RuntimeError is a general-purpose Python exception that
# occurs when an error happens that doesn’t fall into other specific categories.

try:
    raise RuntimeError("This is a runtime error")
except RuntimeError:
    print("Caught a RuntimeError!")


# StopIteration  :- is a Python exception that occurs when you try to
# get the next item from an iterator, but the iterator is exhausted.

try:
    my_list = [1, 2, 3]
    it = iter(my_list)

    # Consume all items plus one extra
    print(next(it))  # 1
    print(next(it))  # 2
    print(next(it))  # 3
    print(next(it))  # Raises StopIteration
except StopIteration:
    print("StopIteration caught: No more items in iterator")


# ==============================================================================

try:
    a = float(input("Enter num1="))
    b = float(input("Enter num2="))

    c = a / b

except ValueError:
    print("Please enter valid number")

except ZeroDivisionError:
    print("Division by zero is not allowed")

else:
    print("Result",c)
    print("programe executed succesfully!!")
finally:
    print("Good Bye")

# ===================================================================================

try:
    num1 = int(input("Enter num1="))
    num2 = int(input("Enter num2="))
    op = input("Enter operation(+,-,*,/):")

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        result = num1 / num2
    else:
        print("Invalid choice")

except ValueError:
    print("Please enter valid number")

except ZeroDivisionError:
    print("Division by zero is not allowed")

else:
    print("Result:",result)
finally:
    print("programe is finished!!")