# 👉Anonymous function:=
# 👉It is means define function is without function name its called
# anonymous function and it is called a lambda function
# 👉This function is define the lambda expression.
# 👉It should have one expression and take multiple arguments.
# 👉Using lambda it is reduce the number of lines

#👉 addition of two number using lambda anonymous function

add = lambda a,b : a + b

result = add(3,4)
print(result)


# 👉Square of the number using lambda anonymous function

square = lambda a : a * a

result = square(5)
print(result)


# 👉Three function of use in lambda:-
# 1)Filter() 2)map() 3)Reduce()

# 1)Filter():-This is the in-built function in python.filter() is take
# the sequance.filter() takes two arguments function and iterable.
# filter() means make the parts .
# filter() is a built-in function in Python.
# It filters the items in an iterable based on whether they pass
# a True/False test.
# Only the elements that return True from the function are kept.
# It returns a filter object (which you usually convert into a
# list, tuple, etc.).

# 👉using filter() filter the even number.

nums = [2,4,3,5,4,6,7,9]

even = list(filter(lambda n : n % 2 == 0,nums))
print(even)

# 👉map() := map() is take the two parameter like function and iterative
# map() is a built-in function in Python.
# It applies a function to every item in an iterable (like a list, tuple,
# etc.) one by one.
# It returns a special object (a map object), which you can convert into
# a list, tuple, etc.

double = list(map(lambda n : n*2,even))
print(double)

# 👉reduce() :=reduce() function is belong to module as functools.
# reduce() applies a function to all elements of an iterable,
# one by one, to reduce it to a single value.
# It's like keep combining the elements until only one final result is left.

# 👉here sum of all double elements in using reduce.
from functools import reduce

sum = reduce(lambda a,b : a+b ,double)
print(sum)



