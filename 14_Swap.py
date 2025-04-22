# 👉Swap two number using third variable

a = 4
b = 6

print("Before swapping")
print('a=',a)
print('b=',b)

print("After swapping")
temp = a
a = b
b = temp

print('a=',a)
print('b=',b)

# 👉Swap two number without using third variable

a = 5
b = 7

print("Before swapping")
print('a=',a)
print('b=',b)

print("After swapping")
a = a + b
b = a - b
a = a - b

print('a=',a)
print('b=',b)

# 👉Swap two number without using third variable(second method)

a = 5
b = 7

print("Before swapping")
print('a=',a)
print('b=',b)

print("After swapping")
a = a ^ b
b = a ^ b
a = a ^ b


# 👉Swap two number without using third variable(Third method)

a = 5
b = 7

print("Before swapping")
print('a=',a)
print('b=',b)

print("After swapping")
a,b = b,a

print('a=',a)
print('b=',b)