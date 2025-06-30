# print all prime number in interval
# it is divisible by itself

lower = int(input("Enter lower limit="))
upper = int(input("Enter upper limit="))

for i in range(lower,upper+1):
    if i > 1:
        for j in range(2,i):
            if i % 2 == 0:
                break
        else:
            print(i)

