# 👉List:-
# 👉List is similar to the array.
# 👉List is represent to the [].
# 👉Lis is mutable means it can change the value.
# 👉List is the different type like integer, float , string etc...

# in interview asked already this questions
#👉list inside list
list1 = [1,2,3,4,[5,6],7,8.0]
print(list1)
# output:-[1, 2, 3, 4, [5, 6], 7, 8.0]

student1 = ['Twinkle','Hinal','Jurali']
student2 = ['BCA','BCA','BCOM']
result = [dict(zip(student1, student2))]
print(result)
# output:-[{'Twinkle': 'BCA', 'Hinal': 'BCA', 'Jurali': 'BCOM'}]

# *************************************************************************

#👉create a list
thislist = ["apple", "banana", "cherry"]
print(thislist)
#output:-['apple', 'banana', 'cherry']

#👉list allow duplicate values
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
# output:-['apple', 'banana', 'cherry', 'apple', 'cherry']

#👉Print the number of items in the list:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
# output:-3

#👉String, int and boolean data types:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1,list2,list3)
print(list1)
print(list2)
print(list3)
# output:-['apple', 'banana', 'cherry'] [1, 5, 7, 9, 3] [True, False, False]
# ['apple', 'banana', 'cherry']
# [1, 5, 7, 9, 3]
# [True, False, False]

#👉A list with strings, integers and boolean values:
list1 = ["abc", 34, True, 40, "male"]
print(list1)
# output:-['abc', 34, True, 40, 'male']

#👉What is the data type of a list?
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
# output:-<class 'list'>

#👉Using the list() constructor to make a List:
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
# output:-['apple', 'banana', 'cherry']

#👉Print the second item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
# output:-banana

#👉Print the last item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
# output:-cherry

#👉Return the third, fourth, and fifth item:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
# output:-['cherry', 'orange', 'kiwi']

#👉This example returns the items from the beginning to, but NOT including, "kiwi":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
# output:-['apple', 'banana', 'cherry', 'orange']

#👉This example returns the items from "cherry" to the end:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
# output:-['cherry', 'orange', 'kiwi', 'melon', 'mango']

#👉This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
# output:-['orange', 'kiwi', 'melon']

#👉Check if "apple" is present in the list:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
# output:-Yes, 'apple' is in the fruits list

#👉Change the second item:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
# output:-['apple', 'blackcurrant', 'cherry']

#👉Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
# output:-['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

#👉Change the second value by replacing it with two new values:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
# output:-['apple', 'blackcurrant', 'watermelon', 'cherry']

#👉Change the second and third value by replacing it with one value:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
# output:-['apple', 'watermelon']

#👉Insert "watermelon" as the third item:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
# output:-['apple', 'banana', 'watermelon', 'cherry']

#👉append:-To add an item to the end of the list, use the append() method:
#👉Using the append() method to append an item:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
# output:-['apple', 'banana', 'cherry', 'orange']

#👉insert :-The insert() method inserts an item at the specified index:
#👉Insert an item as the second position:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
# output:-['apple', 'orange', 'banana', 'cherry']

#👉extend:-To append elements from another list to the current list, use the extend() method.
#👉Add the elements of tropical to thislist:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
# output:-['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

#👉The extend() method does not have to append lists, you can add any
# iterable object (tuples, sets, dictionaries etc.).
#👉Add elements of a tuple to a list:
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
# output:-['apple', 'banana', 'cherry', 'kiwi', 'orange']

#👉remove:-The remove() method removes the specified item.
#👉Remove "banana":
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
# output:-['apple', 'cherry']

#👉Remove the first occurrence of "banana":
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
# output:-['apple', 'cherry', 'banana', 'kiwi']

#👉remove all the banana in this list
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
while "banana" in thislist:
    thislist.remove("banana")
print(thislist)
# output:-['apple', 'cherry', 'kiwi']

#👉remove all the banana in this list using list compresion
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist = [item for item in thislist if item != "banana"]
print(thislist)
#output:-['apple', 'cherry', 'kiwi']

#👉pop() :-The pop() method removes the specified index.
#👉Remove the second item:
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
# output:-['apple', 'cherry']

#👉reverse:-Reverses the order of the list
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)
#output:-['cherry', 'banana', 'apple']

#👉Remove the last item:
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
# output:-['apple', 'banana']

#👉del :-  The del keyword can also delete the list completely.
#👉Remove the first item:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
# output:-['banana', 'cherry']

#👉Delete the entire list:
thislist = ["apple", "banana", "cherry"]
del thislist
# output:-['banana', 'cherry']

#👉clear :- The clear() method empties the list.
#👉Clear the list content:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
#output:-[]

#👉index:- Returns the index of the first element with the specified value
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)
# output:-2

#👉copy:-	Returns a copy of the list
#👉Copy the fruits list:
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()
print(x)
# output:-['apple', 'banana', 'cherry', 'orange']

#👉count:-Returns the number of elements with the specified value
#👉Return the number of times the value "cherry" appears in the fruits list:
fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry")
print(x)
# output:-1

#👉Print all items in the list, one by one:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
# output:-
# apple
# banana
# cherry

#👉Print all items by referring to their index number:
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
#output:-
# apple
# banana
# cherry

#👉Print all items, using a while loop to go through all the index numbers
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
# output:-
# apple
# banana
# cherry

#👉A short hand for loop that will print all items in a list:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
# output:-
# apple
# banana
# cherry

#👉list compresion
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
# output:-['apple', 'banana', 'mango']

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
# output:-['apple', 'banana', 'mango']

#👉sort :- it is set the assending order
#👉Sort the list alphabetically:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
# output:-['banana', 'kiwi', 'mango', 'orange', 'pineapple']

#👉Sort the list numerically:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
# output:-[23, 50, 65, 82, 100]

#👉Sort the list descending:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
# output:_['pineapple', 'orange', 'mango', 'kiwi', 'banana']

#👉Sort the list descending:
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
# output:-[100, 82, 65, 50, 23]

#👉join :- join two list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
# output:-['a', 'b', 'c', 1, 2, 3]

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
# output:-['a', 'b', 'c', 1, 2, 3]

# find the sum of all numbers
numbers = [5, 10, 15, 20, 25]
sum = sum(numbers)
print(sum)
# output:-75

#Sort the list in reverse order.
numbers = [5, 10, 15, 20, 25]
numbers.sort(reverse=True)
print(numbers)
# output:-[25, 20, 15, 10, 5]

# Loop through the list and print the type of each item.
mixed = [1, "hello", 3.14, True]
for i in mixed:
  print(i)
#output:-
# 1
# hello
# 3.14
# True

# Access the number 4.
matrix = [[1, 2], [3, 4], [5, 6]]
a = matrix[1][1]
print(a)
# output:-4

# Add a new row: [7, 8].
matrix = [[1, 2], [3, 4], [5, 6]]
matrix.append([7,8])
print(matrix)
# output:-[[1, 2], [3, 4], [5, 6], [7, 8]]

#Flatten the list into a single list: [1, 2, 3, 4, 5, 6].
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [item for row in matrix for item in row]
print(flat)
# output:-[1, 2, 3, 4, 5, 6]


# Create a list [2, 2, 2, 2, 2]
a = [2] * 5

# Create a list [0, 0, 0, 0, 0, 0, 0]
b = [0] * 7

print(a)
print(b)
# output:-[2, 2, 2, 2, 2]
# [0, 0, 0, 0, 0, 0, 0]

# nested list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access element at row 2, column 3
print(matrix[1][2])
# output:-6

# list comprasion
# Create a list of squares from 1 to 5
squares = [x**2 for x in range(1, 6)]
print(squares)

#list traversal
arr = [54, 43, 2, 1, 5]
print(*arr)
# output:-54 43 2 1 5

#length of list
lis = [3,4,5,6,7]
print(len(lis))
# output:-5

#create list using range
r1 = 0
r2 = 10
li = list(range(r1,r2))
print(li)
# output:-[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# using list compresion
r1 = 0
r2 = 10
li = [i for i in range(r1, r2)]
print(li)
# output:-[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#Create a List of Tuples in Python
a = [1, 2, 3]
b = ['apple', 'orange', 'cherry']
res = list(zip(a, b))
print(res)
# output:-[(1, 'apple'), (2, 'orange'), (3, 'cherry')]

a = [[1, 'apple'], [2, 'orange'], [3, 'cherry']]
res = list(map(tuple, a))
print(res)
# output:-[(1, 'apple'), (2, 'orange'), (3, 'cherry')]

n = 5
a = [0] * n
print(a)
# output:-[0, 0, 0, 0, 0]

n = 5
a = list(range(n))
print(a)
# output:-[0, 1, 2, 3, 4]

#append 6 begning of the list
li = [1, 3, 4, 5, 7]
li.insert(0, 6)
print(li)
# output:-[6, 1, 3, 4, 5, 7]

li = [1, 3, 4, 5, 7]
li = [6] + li
print(li)
# output:-[6, 1, 3, 4, 5, 7]

# appending list to a list
a = [1, 2, 3]
a.append([4, 5])
print(a)
# output:-[1, 2, 3, [4, 5]]

# Append an element to the second sublist
a = [[1, 2], [3, 4]]
a[1].append(5)
print(a)
# output:-[[1, 2], [3, 4, 5]]

# Extend the list by adding multiple elements
a = []
a.extend([3,4,5])
print(a)

# remove duplicate from a list
a = [1, 2, 2, 3, 4, 4, 5]
a = list(set(a))
print(a)
# output:-[1, 2, 3, 4, 5]

# flatten list
# a = [[1, 2, 3], [4, 5], [6, 7]]
# # Using sum to flatten the list
# b = sum(a, [])
# print(b)
# output:-[1, 2, 3, 4, 5]


#find even number in list
nums = [1, 2, 3, 4, 5, 6]
evens = [x for x in nums if x % 2 == 0]
print(evens)
# output:-[2, 4, 6]

# union of list to set
a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]
result = sorted(set(a) | set(b))  # or: sorted(set(a + b))
print(result)
# output:-[1, 2, 3]

# intersection
arr1 = [1, 2, 3, 4]
arr2 = [2, 4, 6, 7, 8]
# Intersection using set
intersection = sorted(set(arr1) & set(arr2))
print(intersection)
# output:-[2, 4]

# merge two list and return one shorted list
# input:[1,2,4],[1,3,4]
# output:- [1,1,2,3,4,4]
a = [1,2,4]
b = [1,3,4]
merge = a+b
merge.sort()
print(merge)

# Input: [0,0,1,1,1,2,2,3,3,4]
# Output: [0,1,2,3,4] (length = 5)
nums = [0,0,1,1,1,2,2,3,3,4]
unique_nums = list(set(nums))
unique_nums.sort()
print(unique_nums)
print(len(unique_nums))

# ************************************************************************

