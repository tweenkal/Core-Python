# 👉Pass List To a fucntion:-
# 👉here make a list for the even and odd number and this list is pass
# to the function and return the count of the element inside the list.

def count(lst):
    even = 0
    odd = 0

    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    return even,odd

lst = [1,2,3,5,6,7,7,8,2]
even,odd = count(lst)
# print("Even no=",even)
# print("Odd no=",odd)

# 👉it is a second method for proper format
#👉 here format is the function that is belongs to the string.

print("Even is : {} and Odd is : {}".format(even,odd))

