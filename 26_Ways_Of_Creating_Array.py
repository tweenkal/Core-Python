# 👉6 way of creating the array.
# 1)array() 2)linspace() 3)logspace() 4)arange() 5)zeros() 6)ones()
# 👉find type of array used to dtype.

from numpy import *

# 1)array():=
arr = array([1,2,3,4,5])
print(arr)
print(arr.dtype)  #this is dtype is the array type


# if in array one element is the float then it is convert all element to the float.
arr = array([1,2,3,4,5.0])
print(arr)
print(arr.dtype)

# 👉here create the array and its int to convert to the float.

arr = array([1,2,3,4,5],float)
print(arr)
print(arr.dtype)

# 👉2)linspace() :- linspace is also have 3 parameters like
# start , stop and step. in linspace() is not a step it is divided into the part

# here it is divided into the 16 parts and got the float value.
arr = linspace(0,15,16)
print(arr)

# 👉arange() :- it is a 3 parameter start,stop and step here step
# is not a number of parts it is the steps.

# here it is not a number of part it is first of the print 1 and skip 2
# numbers and print 3 up to 10.
arr = arange(1,10,2)
print(arr)

# 👉logspace() is a NumPy function that generates evenly spaced
# numbers on a logarithmic scale — super handy for things like
# plotting data that spans several orders of magnitude.

arr = logspace(1,10,5)
print(arr)
print(arr[4])

# 👉zeros():-zeros() creates a new array filled entirely with 0s.
arr = zeros(5,int)
print(arr)  #[0. 0. 0. 0. 0.] and give me this int format then

# 👉ones():-ones() creates a new array filled entirely with 1s.
arr = ones(6)
print(arr)