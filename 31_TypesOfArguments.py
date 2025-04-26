# 👉Types of argument:-
# 1)Formal argument
# 2)Actual argument:-
# Types of actual argument:-
# 1)position 2)keyword 3)default 4)variable length

def add(a,b):  #This is a formal argument
    c = a + b
    print(c)

add(4,5)  #This is the Actual argument

# 1)Position:-
def person(name,age):
    print(name)
    print(age)

person("Twinkle",21)

# here the name is position to twinkle and age is position to 21.

# 2)keyword:-means the mention the variable name itself.
def person(name,age):
    print(name)
    print(age)

person(name="Twinkle",age=21)  #<- name and age keyword

# here name and age is the keyword

# 3)default() :- default means the not passing the value.

def person(name,age=21):  #default argument
    print(name)
    print(age)

person('Twinkle')

# here i am pass the name for calling the function but not pass the age
# then got the error but i crating function age pass the age for the
# formal argument then it is work

# 4)variable length argument:-Variable-length arguments refer to a
# feature that allows a function to accept a variable number of arguments
# in Python.

def sum(a,*b):      # * means b access all the values

    c = 0
    for i in b:
       c = c + i
    print(c)

sum(4,5,7,8,9)


#  * means it is consider by-default tuple


def sum(n,*num):

    sum = 0
    for i in num:
        sum += i

    print(sum)

sum(10,20,30,40)

# 👉 **kwargs:-

# 👉keyword variable length argument :- means this variable are mentioned
# to the proper keyword

# here * is not support multiple keyword arguments that means
# is used to the ** .

def person(name,**data):
    print(name)

    for i,j in data.items():
        print(i,"=",j)

person('Twinkle',age=21,city='Ahemdabad',mob=8849016763)

