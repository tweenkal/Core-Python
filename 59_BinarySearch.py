# 👉Binary Search:-
# 👉Binary search is all the values are sorted

# 👉Find the mid value:-
# 👉Mid = Lower + Upper / 2

# 👉If search value  is smaller then change the Upper bound
# 👉If search value is smaller then change upper bound and mid becomes
# new upper bound
# 👉If search value is bigger than  change lower bound and mid  becomes
# a new  lower bound

#          0,1 , 2, 3,4
# list = [10,20,30,40,50]

def binary(list,n):
    lower = 0
    upper = len(list)-1

    while lower <= upper:
        mid = (lower + upper) // 2

        if list[mid] == n:
            return mid
        elif list[mid] < n:
            lower = mid + 1
        else:
            upper = mid - 1

    return -1

list = [10,20,30,40,50]
n = 40
print(binary(list,n))




