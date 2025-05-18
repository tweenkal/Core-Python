# 👉For loop:-A for loop in Python is used to iterate over a sequence
# (like a list, string, tuple, or a range of numbers). It repeats a
# block of code for each item in that sequence.for loop is work with sequance.
# for loop is print the statement one by one

x = ['Twinkle',20,90.0]

for i in x:
    print(i)


str = 'Twinkle'

for i in str:
    print(i)


# 👉range:- range function is print to the number of sequance it it
# 3 things 1)start point 2)end point 3)Iterative

# 👉print 1 to 10 number using the for loop
for i in range(1,11):
    print(i)

# 👉print the 11 to 20 number using for loop but iterative a 2 number.

for i in range(11,21,2):
    print(i)


# 👉print 20 to 11 for the reverse order

for i in range(20,10,-1):
    print(i)

# 👉it is print the 1 to 20 number but is not print the divisible by the 5.

for i in range(1,21):
    if i % 5 != 0:
        print(i)

# 👉hello print line by line

str = "hello"

for i in str:
    print(i)

# 👉for loop in list(Nested for):-

list1 = [1,2,3]
list2 = ["Python","React Js","PHP"]

for i in list1:
    for j in list2:
        print(i,j)

# 👉for loop:

for i in range(1,101,10):
    print(i)


for i in range(1,12,3):
    print(i)


for i in range(12):
    print("6 * ",i, "=" ,6 * i)
    if i == 10:
        break