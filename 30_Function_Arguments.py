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