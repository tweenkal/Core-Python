# 👉Array is the similar to the list but one difference you need to all
# the value have same type.
# 👉here all the value have a same type
# 👉array in python we not have the fixed size
# 👉array is not a by default this import the module for import array
# 👉 * means is work for the all function
# 👉In array is used to the buffer_info() function this give the size
# of the array
# 👉different different method in the array like insert,append ,reverse
# ,remove,pop,clear etc..

# 👉signed int(i) : it is access the positive and negative number both.
# 👉unsigned int(I) :- it is access only the positive number not a negative number.

from array import *

# 👉Signed int :- 'i'
# array = array('i',[10,-20,30,-40,50])
# print(array)

# 👉unsigned int :- 'I'
# array = array('I',[10,20,49,50,90])
# print(array)
# print(type(array))

# 👉Give me the size of the array.it give me two things first is the
# address of the array and second is the size of the array.
val = array('i',[10,20,-30,40,-50])
print(val)
print(val.buffer_info())

# 👉Give me the typecode of the array like 'i','I','f','F' etc....
print(val.typecode)   #i

# 👉print the value one by one
print(val[2])

# 👉print the all element line by line.
for i in range(5):
    print(val[i])

# 👉length of the array
for i in range(len(val)):
    print(val[i])

for e in val:
    print(e)

# 👉old value of the is coming to the new array here fetch the one-one
# value and assigning to the array

newarray = array(val.typecode,(a for a in val))

for e in newarray:
    print(e)

# 👉print the square of the number in array.
newarray = array(val.typecode,(a*a for a in val))

for e in newarray:
    print(e)

# 👉using while loop

i = 0
while i<len(newarray):
    print(newarray[i])
    i+=1

# 👉Give me the reverse of the array.
val.reverse()
print(val)

# 👉print character in array.
# 👉print character using unicode 'u'.

ch = array('u',['a','b','c','d','e'])
print(ch)

for i in range(5):
    print(ch[i])


