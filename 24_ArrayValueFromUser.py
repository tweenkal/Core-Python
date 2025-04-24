# 👉Ask user of length of the array and the enter value for the user
# and this is add the array by user.

from array import *

arr = array('i',[])

n = int(input("Enter the length of the array="))

for i in range(n):
    x = int(input("Enter the values="))
    arr.append(x)

print(arr)

# 👉if the user is enter the search of the number of value then it
# is compare to the array inside value this is match then print the
# index number of the value and this is not match then it is shift and y
# check the another value or the condition.

val = int(input("Enter the search of the number="))

k = 0
for i in arr:
    if i == val:
        print(k)
        break

    k += 1

# print(arr.index(val))

else:
    print("This value is not match for the array")

