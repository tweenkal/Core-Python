# access index of a list using for loop

# using enumerate method

list = [10,20,30,40,50]
for index,value in enumerate(list):
    print(index,value)


# i am starting the value 1
list = [10,20,30,40,50]
for index,value in enumerate(list,start=1):
    print(index,value)


# not using enumerate

for i in range(len(list)):
    value = list[i]
    print(i,value)