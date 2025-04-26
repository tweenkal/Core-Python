#👉 Multidimensional array:-
from numpy import *

arr = array([
    [1,2,3,4,5,6],
    [4,5,6,7,8,9]
])

print(arr)
print(arr.dtype)  #it is the find the array datatype
print(arr.ndim)  #it is the number of dimension is two
print(arr.shape) #it is the define the number of row and column
print(arr.size) #it is define the number of size for this entire block

# 👉Convert the 2d array into the 1d array.
arr2 = arr.flatten()
print(arr2)

# 👉Convert single dimensional array to 3d Array
arr3 = arr2.reshape(3,4)  #in this parameter pass the number of row and column
print(arr3)

# 👉make the 3 array in 2 2d array for 3 values
arr3 = arr2.reshape(2,2,3)
print(arr3)

# 👉row matrix :- means single column multiple row
# 👉column matrix :- means multiple row single column

arr1 = array([
    [1,2,3,4],
    [5,6,7,8]
])

m = matrix(arr1)        #used the matrix function

print(m)

# 👉Second method

m = matrix('1 2 3 4 ; 5 6 7 8')
print(m)

# 👉Convert into 4 rows and 2 column matrix

m = matrix('1 2 ; 3 4 ; 5 6 ; 7 8')
print(m)

# 👉print diagonal elements means the cross 1 3 7

print(diagonal(arr1))  #[1 6]

# 👉multiplication of two matrix

m1 = matrix('1 2 3 ; 4 5 6 ; 7 8 9')
m2 = matrix('10 11 12 ; 13 14 15 ; 16 17 18')

m3 = m1 * m2
print(m3)


