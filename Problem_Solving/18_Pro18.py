# sum of natural number
# natural numbers means the positive int number

num = int(input("Enter num="))

if num < 0:
    print("Please enter positive number")
else:
    sum = 0
    while num > 0:
        sum += num
        num -= 1

    print(sum)