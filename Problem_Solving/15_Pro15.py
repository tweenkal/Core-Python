# Fibonacci sequance

# 0 + 1= 1, 1+1=2 , 2+1=3, 3+2=5 , 3+5=8 etc...

num = int(input("Enter no="))
a = 0
b = 1
c = 0

print(a)
print(b)

for i in range(1,num+1):
    c = a + b
    a = b
    b = c

    print(c)
