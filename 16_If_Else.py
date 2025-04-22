# 👉If :- Here if is the block of the statement if condition is
# true the it is the execute the if statement otherwise is go out
# of the if statement .

if True:
    print("I am right")

print("Bye")

if False:
    print("I am not right")

print("Bye")

# 👉Find even number or odd number using the if condition

i = 5

if i % 2 == 0:
    print("Even")

if i % 2 != 0:
    print("Odd")

print("Bye")

# 👉If_Else :- here the if condintion is true it is the execute the if
# statement then condition is false then it is execute the else statement.

a = 3
if a % 2 ==0:
    print("Even")

else:
    print("Odd")

# 👉check the even and odd number it is number is even then check the
# number is greater then 5 but it is not a even number it is go out the
# if statement and print the else part.

# 👉Nested if:=

b = 4
if b % 2 == 0:
    print("Even")
    if b > 5:
        print("Greater")
    else:
        print("Not greater")

else:
    print("Odd")


# 👉Ladder if:- here if first condition is true the it is execute the
# if statement and not check the second condition it is go out of the
# if condition then it is first condition is false then it is jumping
# out of the second bloack and check the second condition then second
# condition is also false the it is jump to third condition here it is
# third condition is true then it ts execute this block and not jumping
# to the check other condition it is jumping out of the if statement.

i = 2

if i == 1:
    print("One")

elif i == 2:
    print("Two")

elif i == 3:
    print("Three")

elif i == 4:
    print("Four")

else:
    print("Wrong input")