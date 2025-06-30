# 👉Find factorial of the number using function

# 5! = 5 * 4 * 3 * 2 * 1
# 4! = 4 * 3 * 2 * 1

# n = int(input("Enter any number="))
#
# def fact():
#
#     if n < 0:
#         print("Invalid number")
#
#     else:
#         fact = 1

#
#         for i in range(1,n+1):
#             fact *= i
#         print(fact)
#
# fact()


# 👉Factorial using recursion

# n = int(input("Enter no="))
#
# def fact(x):
#
#     if n == 1:
#         return 1
#
#     return x * fact(n-1)
#
# result = fact(n)
# print(result)


# Print prime numbers between 1 and 10
# print("Prime numbers between 1 and 10 are:")
#
# for num in range(1, 11):
#     if num > 1:
#         # Check if number is prime
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             print(num)



x = ("apple","banana","cherry")
y = list(x)
y.append("orange")
y2 = tuple(y)
print(y2)