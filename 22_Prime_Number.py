# 👉Give me the number is prime or not
# 👉prime number means it is only divisible by one and itself and is give me reminder 0 then ii is not a prime.

# num = 7
#
# for i in range(2,num):
#     if num % i == 0:
#         print("Not a Prime number")
#         break
#
# else:
#     print("Prime Number")


start = 10
end = 50


for num in range(start,end+1):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
                print(num)