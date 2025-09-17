# 👉Function arguments and function parameters must be different.
# 👉pass by value and pass by reference:-

def update(x):
    print(id(x))
    x = 8
    print(id(x))
    print("x=",x)

a = 10
print(id(a))
update(a)
print("a=",a)  #here updating value for x is not affecting for a and it is pass by value and pass by reference.

# 👉pass by value and pass by reference:-
# 👉here pass by value is only passing the value not a pass by addressing
# 👉but pass by reference is passing the address for itself.


# 👉difference between print and return:=
# 👉print is th show the output and print the statement but return is
# store the statement

# many type of function argument
# default argument
#keyword argument
# required argument
# arbitary argument

# default argument:-If no value is passed, the function uses the default value.
def greet(name="Guest"):
    print("Hello,", name)

# Calling with an argument
greet("Alice")   # Output: Hello, Alice

# Calling without an argument (uses default)
greet()          # Output: Hello, Guest

# keyword argument:-You call the function by specifying parameter names.
def greet(name,age):
    print("name=",name)
    print("age=",age)

greet(age=21,name="twinkle")

# arbitary argument:-Use *args when you don’t know how many positional
# arguments will be passed.its like a tuple
def info(*args):
    for i in args:
        print(i)

info("alice",25,"bca")

# keyword arbitary argument:-Use **kwargs when you don’t know how many
# keyword arguments will be passed.its like a dictionary.
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

show_info(name="Alice", age=25)



