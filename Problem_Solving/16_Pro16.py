# armstrong or not

# 153 = (1*1*1) + (5*5*5) + (3*3*3)
#     =  1 + 125 + 27
#     = 153 is the armstrong number

# 53  = (5*5) + (3*3)
#     = 25 + 9
#     = 34   is not armstrong number

num = int(input("Enter number="))
sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    cube = digit ** 3
    sum = sum + cube
    temp //= 10

if sum == num:
    print("it is armstrong number")
else:
    print("it is not armstrong number")


