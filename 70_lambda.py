# even or odoo using function
def evenodd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("odd")

evenodd(2)
evenodd(5)

# prime number using function

def prime(num):
    for i in range(2,num):
        if num % i == 0:
            print("Not prime")
            break
    else:
        print("prime")

prime(11)

# factorial using function
def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact *= i
    print(fact)

factorial(5)

#fibonaccie using function
def febonaccie(num):
    a = 0
    b = 1
    c = 0

    print(a)
    print(b)

    while c < num:
        c = a+b
        a = b
        b = c
        print(c)

febonaccie(10)

#string is pallindrom or not using function

def pallindrom(str):
    if str == str[::-1]:
        print("pallindrom")
    else:
        print("not pallindrom")

pallindrom("php")


# reverse string using function
def reverse(text):
    reverse_text = " "
    for i in text:
        reverse_text = i + reverse_text
    print(reverse_text)

reverse("hello")

# square of number using function
def square(n):
    c = n * n
    print(c)

square(5)
square(6)

#calculator using function
def calc(a,b):
    sum = a+b
    sub = a-b
    mul = a*b
    div = a/b
    mod = a%b

    print("sum=",sum)
    print("sub=",sub)
    print("mul=",mul)
    print("div=",div)
    print("mod=",mod)

calc(10,5)

# remove punctaion of string
# check anagram
# get unique value from list of dict
# create a dict from range
# sort list of tuples by second item


# lambda function
sum = lambda x,y: x+y
print(sum(5,4))

evenodd = lambda x: x % 2 == 0
print(evenodd(10))

square = lambda x: x * x
print(square(5))

# map , filter , reduce
# map:-Used when you want to apply a function to every item in a list (or iterable).
num = [1,2,3,4,5]
square = list(map(lambda x: x * x,num))
print(square)

# filter:-Used when you want to keep only the elements that match a condition.
num = [1,2,3,4,5,6]
even = list(filter(lambda x: x % 2 == 0,num))
print(even)

# reduce:-Used when you want to reduce a list to a single value by repeatedly applying a function.
# (It’s in the functools module.)
from functools import reduce
num = [1,2,3,4,5]
sum = reduce(lambda x,y : x + y,num)
print(sum)

num = [1,2,3,4,5]
mul = reduce(lambda x,y : x * y,num)
print(mul)


