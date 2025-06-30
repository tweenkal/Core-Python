# 👉Copying the array :- how to create another array for existing
# array


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

# 👉sum():-Sum of the array
arr = array([1,2,3,4,5])
print(sum(arr))

# 👉min():-min value in the array
arr = array([1,2,3,4,5])
print(min(arr))

# 👉concatenate the array
arr = array([1,2,3,4,5])
arr2 = array([6,7,8,9,10])
print(concatenate([arr,arr2]))

# 👉Copying array
# 👉Two different type of copy
# 1)shallowest copy 2)deep copy
# 1)shallowest copy :- it means it is the copy this elements but then
# both the elements but both the array are depended to each other.

# 2)deep copy:-deep copy means the two different elements it is not
# link to each other for any way.two different array and two different
# value not link each other

arr1 = array([1,2,3,4,5])
# 👉view() is a function of the create the array as a different location
arr2 = arr1.view() #here view() is used the shallow copy
arr2 = arr1.copy()  #here not change the both value only change the arr1 value means it is a deep copy
arr1[1] = 7  #here the i am change the arr1 value but it is by-default change the arr2 value means it is a shallowest copy
print(arr1,arr2)

# 👉address of the array
print(id(arr1))
print(id(arr2))

