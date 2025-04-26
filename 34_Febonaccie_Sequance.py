# 👉Fibonacci Seriece:-

# 0,1,1,2,3,5,8,13....
# 0+1=1 , 1+1=2 , 2+1=3 , 3+2=5 , 5+3=8 , 8+5=13....

n = int(input("Enter no="))

def feb(n):
    a = 0
    b = 1

    if n < 0:
        print(a)

    else:
        print(a)
        print(b)

        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)
feb(n)