# 👉Find factorial of the number using function

# 5! = 5 * 4 * 3 * 2 * 1
# 4! = 4 * 3 * 2 * 1

n = int(input("Enter any number="))

def fact():

    if n < 0:
        print("Invalid number")

    else:
        fact = 1

        for i in range(1,n+1):
            fact *= i
        print(fact)

fact()

