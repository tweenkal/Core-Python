# 👉While loop:-A while loop in Python is a control flow statement
# that allows you to repeat a block of code as long as a condition
# is True.

i = 1

while i <= 5:
    print("Hello",i)
    i += 1

# 👉This is print the reverse order

print('-----------')
i = 5

while i >= 1:
    print("Hello",i)
    i -= 1

# 👉end="" is used to the statement is not print the new line it is
# using end="" the statement is print the same line
print("------------")

i = 1
while i <= 5:
    print("Telesko ",end="")
    j = 1
    while j <= 4 :
        print("Rockes ",end="")
        j += 1
    i += 1
    print()


# 👉print the table for 6

a = 6
b = 1

while a <= 60:
    print("6 * " ,b,"=", a)
    a += 6
    b += 1


# 👉Task :- print 1 to 5 sum

a = 1
sum = 0

while a <= 5:
    sum += a
    a += 1
print(a)

