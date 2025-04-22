# 👉Give me the number is prime or not
# 👉prime number means it is only divisible by one and itself and is give me reminder 0 then ii is not a prime.

num = 7

for i in range(2,num):
    if num % i == 0:
        print("Not a Prime number")
        break

else:
    print("Prime Number")