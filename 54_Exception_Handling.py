# 👉Exception handling:-
# 👉Errors:-
# 👉Three types of error:-
# 1)compile time error 2)logical error 3)run time error
# 👉that code have a multiple statements and one of the statement you
# have syntax error

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

# a = 5
# b = 0
# try:
#     print("Resource open")
#     print(a/b)
#
# except Exception as e:
#     print("hey do not divide the number of zero",e)
#
# finally:
#     print("Resource closed")


# 👉Second method

a = 8
b = 2

try:
    print("Resource open")
    print(a/b)
    k = int(input("Enter the number="))
    print(k)

except ZeroDivisionError:
    print("can not divide number by zero")

except ValueError:
    print("Invalid input")

except Exception as e:
    print("Something went wrong")

finally:
    print("Resource closed")