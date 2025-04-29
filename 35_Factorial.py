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

n = int(input("Enter no="))

def fact(x):

    if n == 1:
        return 1

    return x * fact(n-1)

result = fact(n)
print(result)
