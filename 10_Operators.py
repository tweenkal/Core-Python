# 👉Operators:-
# 1)Arithmatic Operator
# 2)Assignment Operator
# 3)Logical Operator
# 4)Unary Operator
# 5)Relational Operator
# 6)Bitwise Operator

# 👉1)Arithmatic Operator :- + , - , * , / , %

x = 2
y = 3

# Addition
print(x + y)

# Subtraction
print(x - y)

# Multiplication
print(x * y)

# Division
print(x / y)

# Modular
print(x % y)

# 👉2)Assignment Operators :- = , += , -= , *= , /=  , %=
x = 2
x = x + 2
print(x)

x += 2
print(x)

x -= 2
print(x)

x *= 2
print(x)

x /= 2
print(x)

x %= 2
print(x)

# 👉Assign value in one line with two varibles
a,b = 4,3
print('a=',a)
print('b=',b)

# 👉3)Unary operator:-
n = 6
print(n)
print(-n)

n = -n
print(n)


# 👉4)Relational Operator :- < , > , <= , >= , == , !=
a = 2
b = 4

print(a < b)
print(a > b)
print(a <= b)

a = 4
print(a >= b)
print(a == b)

b = 2
print(a != b)


# 👉5)Logical Operators := &&(AND)  , ||(OR) , !(not)
c = 3
d = 5

# 👉And:-
print(c < 10 and d > 20)
print(c < 10 and d < 20)

# 👉OR
print(c < 10 or d > 20)
print(c > 10 or d > 20 )

# NOT :- 0 = 1 , 1 = 0
x = True
print(x)

print(not x)

y = False
print(y)
print(not y)

# 👉Bitwise Operator :- AND(&) , OR(||) , XOR(^) , Complement(~) or tilde ,
#                       left shift(<<) , right shift(>>)

# 👉Complement(~) :- means reverse for the binary format

print(~12)

# 👉AND(&) :-
print(12 & 13)  #12

# 👉OR( | ):-
print(12 | 13) #13

# 👉XOR(^) :-

# 0 0 0
# 1 0 1
# 0 1 1
# 1 1 0

print(12 ^ 13)   #1


# 👉Left shift(<<)
print(10 << 2)

# 👉Right shift(>>)
print(10 >> 2)


