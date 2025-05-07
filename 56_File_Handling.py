# 👉File handling:-
# 👉File is 2 different mode:- 1)character mode 2)binary mode

# 👉read file

# f = open("Mydata.txt","r")
# print(f.read())

# print only one line
# print(f.readline())
# print(f.readline())

# print the 4 character in line 1
# print(f.readline(4))

# 👉write file

# f1 = open("demo.txt","w")
# f1.write("world")

# 👉append file

# f1 = open("demo.txt","a")
# f1.write("Hello")

# 👉Read data and fetch data line by line

# f = open("Mydata.txt","r")
#
# f1 = open("demo1.txt","w")

# for i in f:
#     print(i)

# for i in f:
#     f1.write(i)

# 👉read binary file means read the image

# f = open("living room1.jpeg","rb")
# print(f.read())

# 👉write binary file means write the image
f = open("living room1.jpeg","rb")

f1 = open("abc.jpeg","wb")

for i in f:
    f1.write(i)