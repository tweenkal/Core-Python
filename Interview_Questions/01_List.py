# concatenate list using + operator
lis1 = [1,2,3,4]
lis2 = [5,6,7,8]
lis3 = lis1 + lis2
print(lis3)

# concatenate using extend operator
lis1 = [1,2,3,4,5]
lis2 = [6,7,8,9,10]
lis1.extend(lis2)
print(lis1)

# membership operator
a = ["apple","banana","mango","cherry"]
print("banana" in a)
print("papaya" in a)

# a list containing strings, numbers and another list
student = ['Jack', 32, 'Computer Science', [2, 4]]
print(student)

# an empty list
empty_list = []
print(empty_list)

# access 32 positive index
print(student[1])

# negative index
print(student[-1])

colors = ['Red', 'Black', 'Green']
print('Original List:', colors)

# change first item to purple
colors[1] = "purple"
print(colors)

# change third item to blue
colors[2] = "blue"
print(colors)


a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)

# output:-[['a', 'b', 'c'], [1, 2, 3]]
print(x[0])
# output:-['a', 'b', 'c']

print(x[0][1])
#output:- 'b'


# Program 22: Find max and min keys
scores = {"Alice": 90, "Bob": 75, "Charlie": 85}
print("Max key:", max(scores))  # Alphabetically largest
print("Min key:", min(scores))  # Alphabetically smallest


