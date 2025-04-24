# 👉Copying the array :- how to create another array for existing array


from numpy import *

# 👉here add the 5 element after the array
arr = array([1,2,3,4,5])
arr = arr + 5
print(arr)

# 👉here addition of two array
# here 1+6=7 , 2+7=9 etc....it is also called the vectorized operations.
arr1 = array([1,2,3,4,5])
arr2 = array([6,7,8,9,10])

arr3 = arr1 + arr2
print(arr3)

# 👉sin() :- find the sin() of the array
arr = array([1,2,3,4,5])
print(sin(arr))

# 👉cos() :- cos of the array
arr = array([1,2,3,4,5])
print(cos(arr))

# 👉log() :- log of the array
arr = array([1,2,3,4,5])
print(log(arr))

#👉sqrt() :- it is square of the array
arr = array([1,2,3,4,5])
print(sqrt(arr))

# 👉max() :- find the max element in this array
arr = array([1,2,3,4,5])
print(max(arr))


# 👉sort() :- it is a sequance of the array
arr = array([3,2,4,6,1,5])
print(sort(arr))

