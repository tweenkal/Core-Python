# 👉Function :- Function is the block of the code then its only
# run it is called . you  make have the multiple statement.

# 👉Two types of function:-
# 1)Built-In function :- max(),min(),sqrt()
# 2)User define function

# 👉here it not define function for multiple time only this call the function multiple
# time


def greet():
    print("Hello")
    print("Good morning")

greet()
greet()

# 👉add two number using function

def add(a,b):
    c = a + b
    print(c)

add(10,20)

# 👉Using return

def add(a,b):
    c = a + b
    return c

result = add(10,50)
print(result)

# 👉In one function is add and sub

def add_sub(a,b):
    c = a + b
    d = a - b

    return c,d

result1,result2 = add_sub(10,40)
print(result1,result2)

# 👉Find Gometric mean using function and find the greater number

def gmean(a,b):

    c = (a * b) / (a + b)
    print(c)

def grater(a,b):
    if a > b:
        print("a is grater")
    else:
        print("b is grater")

grater(4,8)
gmean(4,8)


# 👉Using user input
number = int(input("Enter rollno="))
name = input("Enter name=")

def func(name,rollno):
    print("name is=",name)
    print("Roll no=",rollno)

func(number,name)

# 👉line by line print

def demo(*name):
    for i in name:
        print("my name is=",i)

demo("pqr","xyz","abc")

# 👉doc string

def demo():
    """
    This is the doc string
    """
    print("Thi is a function")

print(demo.__doc__)   # this is the print the docstring

# 👉here this is the execute the multiline comment using __doc__

def demo():
    print("Thi is a function")
    """
    This is the doc string
    """

print(demo.__doc__)   # this is the print the docstring

# This is the  get output None means is doc string is execute for before
# the function the first line not a after