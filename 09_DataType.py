#👉Data type :-
# 1)None 2)Numeric 3)List 4)Tuple 5)Set 6)String 7)Range 8)Dictionary or mapping

# 👉1)None :- None means not assign any value in the variable

#👉 2)Numeric :- Numeric is four type 1)int 2)float 3)complex 4)bool

# 👉Integer
num = 2
print(type(num))

num1 = 2.3
print(type(num1))

num3 = 4+2j
print(type(num3))

# 👉 Convert the float value into the integer
a = 2.4
b = int(a)
print(b)
print(type(b))

# 👉Convert the int value into the float

d = float(b)
print(d)
print(type(d))

# 👉Convert the float value into the integer
k = 6
c = complex(b,k)
print(c)

# 👉Boolean :- boolean is the give two values True or False
# 👉 In python the True = 1 and False = 0
bool = b < k
print(bool)
print(type(bool))

bool = b > k
print(bool)

# 👉 In python the True = 1 and False = 0
print(int(True))

print(int(False))

# 👉List , Tuple , String , Set , Range is the under of the sequance.

# 👉List:-
lis = [2,4,5,6,7]
print(type(lis))

# 👉set:-
set = {2,4,5,6,7}
print(type(set))

# 👉string:-
str = "Twinkle"
print(type(str))

# 👉Tuple:-
tup = (2,3,4,5,6)
print(type(tup))

# 👉Range : it is iterate between the values.
print(range(10))

# 👉Convert range into the list
print(list(range(10)))

#👉Here the number is start  2 to 10 and difference is 2.
print(list(range(2,10,2)))
print(type(range(10)))

# 👉Dictionary :- Dictionary is also called the mapping it is the huge amount of the data
# and it is fetch to very fast and efficient way here every value is
# assign the key

dict = {'Twinkle':'Real me9' , 'Hinal' : 'Oppo' , 'Heli' : 'Samsung'}
print(dict)

# 👉got the all key in the dictionary
print(dict.keys())

# 👉got all the values in the dictionary
print(dict.values())

# 👉fetch the pertcular value means fetch the Hinal's phone
print(dict['Hinal'])

print(dict.get('Twinkle'))