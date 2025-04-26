# 👉Recursion:- Recursion means it is a calling function by itself.

# import sys is the limit of the recursion
# 👉by-default recursion limit is the 1000

# 👉i am change limit for 1000 and set to the 2000 limit

import  sys

sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())  #getrecursionlimit() this function is give me the recursion of the limit

i = 0
def greet():
    global i
    i += 1
    print("Hello",i)
    greet()

greet()

