# 👉List:-
# 👉List is similar to the array.
# 👉List is represent to the [].
# 👉Lis is mutable means it can change the value.
# 👉List is the different type like integer, float , string etc...

lis = [23,45,32,45,67]
print(lis)

print(lis[2])

print(lis[2:])

print(lis[-1])

print(lis[-5])

names = ['Twinkle','Hinal','Heli']
print(names)

mil = [lis , names]

print(mil)


# 👉append() : it is a in-built function in python its add the value
# at end of the list
print(lis)
lis.append(23)
print(lis)
#
# 👉clear():- clear is the used to clear of the list and give me empty list.
# lis.clear()
# print(lis)

# 👉insert() :- insert is the add the value for  between means it
# expects two argument 1)index 2)value.
lis.insert(2,34)
print(lis)

# 👉remove() :- it is remove the element in the list.
lis.remove(34)
print(lis)

# 👉pop():- it is the delete the element in the list and it expects
# the index number
lis.pop(2)
print(lis)

# 👉Two method in data structure of stack 1)push 2)pop
# 👉It is last in first out in stack.
# 1)push :-means add the element
# 2)pop :- delete the element

lis.pop()   #it is remove the last element in the list
print(lis)

# 👉del :- del command is used to delete multiple value
del lis[2:]
print(lis)

# 👉extend :- means the add the multiple value in the list means merge the list
lis.extend([23,24,67,54,35])
print(lis)

# 👉min() :- find the minimum number of the list
print(min(lis))

# 👉max() :- find the maximum number of the list
print(max(lis))

# 👉sum() :- find the number of sum of the list
print(sum(lis))

# 👉sort() :- sort means the all number is display to assending order.
lis.sort()
print(lis)


# 👉here it can change the value for index no 2 = 24 but i got
# the index no2 = 34.
print(lis)
lis[2] = 34
print(lis)