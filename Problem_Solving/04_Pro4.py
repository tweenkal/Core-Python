# Swap two number using third variable

num1 = int(input("Enter num1="))
num2 = int(input("Enter num2="))

temp = num1
num1 = num2
num2 = temp

print("num1=",num1)
print("num2=",num2)

# without using third variable

x = int(input("Enter x="))
y = int(input("Enter y="))

x,y = y,x

print("x=",x)
print("y=",y)

# second method

x = int(input("Enter x="))
y = int(input("Enter y="))

x = x + y
y = x - y
x = x - y

print("x=",x)
print("y=",y)

# third method

x = int(input("Enter x="))
y = int(input("Enter y="))

x = x ^ y
y = x ^ y
x = x ^ y

print("x=",x)
print("y=",y)
