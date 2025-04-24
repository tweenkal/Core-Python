# 👉Variable :- Variable means it is the assign the value and it
# change the value.
# 👉Ever variable is some is the address

num = 23
print(num)
print(id(num))  #id means the find the address of the variable


# It give a same address for this variable
a = 10
b = a
print(a)
print(b)

# 👉In python is a multiple variable but get the same data it is get the
# point of the same box this is not give multiple boxes
# 👉python is the more memory efficent
print(id(a))
print(id(b))

print(id(10))

a = 9
print(a)
print(id(a))
print(id(b))

#👉 constant :- constant means the im-mutable it can not change the value.
PI = 3.14
print(PI)

# 👉type of variable
PI = 3.15
print(type(PI))