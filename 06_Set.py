# 👉set:-
# 👉set is the collection of the unique elements.
# 👉set is the represent for the {}.
# 👉set is never follow the sequeance means it not follow the sequance.
# 👉set does not support for index.
# 👉set is simillar to the list the difference would be it not maintaine
# the sequance and its not support duplicate values.
# 👉Its not display the repeat value means the you are enter the
# {23,24,23,56,76} but it is a got the output for the here 23 is got
# only one time not a two time.

#👉create a set
thisset = {"apple", "banana", "cherry"}
print(thisset)
# output:-{'banana', 'cherry', 'apple'}

#👉Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
# output:-{'cherry', 'apple', 'banana'}

#👉True and 1 is considered the same value:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
# output:-{True, 2, 'banana', 'cherry', 'apple'}

#👉False and 0 is considered the same value:
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)
# output:-{True, 2, 'apple', 'banana', 'cherry'}

#👉Get the number of items in a set:
thisset = {"apple", "banana", "cherry"}
print(len(thisset))
# output:-3

#👉String, int and boolean data types:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)
# output:-{'banana', 'apple', 'cherry'}
# {1, 3, 5, 7, 9}
# {False, True}

#👉What is the data type of a set?
myset = {"apple", "banana", "cherry"}
print(type(myset))
# output:-<class 'set'>

#👉Using the set() constructor to make a set:
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
# output:-{'cherry', 'apple', 'banana'}

#👉Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
# output:_
# apple
# banana
# cherry

#👉Check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
# output:-True

#👉Check if "banana" is NOT present in the set:
thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)
# output:-False

#👉add :- Adds an element to the set
#👉Add an item to a set, using the add() method:
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
# output:-{'apple', 'cherry', 'banana', 'orange'}

#👉clear :- Removes all the elements from the set
#👉Remove all elements from the fruits set:
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)
# output:-set()

# 👉copy:-	Returns a copy of the set
# 👉 Copy the fruits set:
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)
# output:-{'apple', 'cherry', 'banana'}

# 👉difference:-	Returns a set containing the difference between two or more sets
# 👉 Return a set that contains the items that only exist in set x, and not in set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)
# output:-{'cherry', 'banana'}

# 👉 difference_update:-Removes the items in this set that are also included in another, specified set
#  👉Remove the items that exist in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)
# output:-{'cherry', 'banana'}

#  👉discard:-	Remove the specified item
#  👉Remove "banana" from the set:
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)
# output:-{'apple', 'cherry'}

# 👉intersection:-Returns a set, that is the intersection of two other sets
#  👉Return a set that contains the items that exist in both set x, and set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)
# output:-{'apple'}

#  👉intersection_update:-Removes the items in this set that are not present in other, specified set(s)
#  👉Remove the items that is not present in both x and y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)
# output:-{'apple'}

# 👉isdisjoint:-Returns whether two sets have a intersection or not
#  👉Return True if no items in set x is present in set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)
# output;-True

# 👉issubset:-Returns True if all items of this set is present in another set
# 👉Return True if all items in set x are present in set y:
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)
# output:-True

#  👉issuperset:-Returns True if all items of another set is present in this set
#  👉Return True if all items set y are present in set x:
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)
# output:-True

#  👉pop():-Removes an element from the set
#  👉Remove a random item from the set:
fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits)
# output:-{'apple', 'cherry'}

# 👉 remove:-removes the specified element
#  👉Remove "banana" from the set:
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)
# output:-{'apple', 'cherry'}

#  👉union:-Return a set containing the union of sets
#  👉Return a set that contains all items from both sets, duplicates are excluded:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z)
# output:-{'banana', 'cherry', 'google', 'microsoft', 'apple'}

#  👉update:-Update the set with the union of this set and others
#  👉Insert the items from set y into set x:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)
print(x)
#output:-{'google', 'microsoft', 'banana', 'cherry', 'apple'}