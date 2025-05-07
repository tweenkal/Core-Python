# 👉Linear search:-
# 👉How to search element in a list

pos = -1

def search(list,n):
    i = 0

    while i<len(list):
        if list[i] == n:
            globals() ['pos'] = i
            return True
        i += 1

    return False

list = [4,5,6,7,8,9]
n = 5

if search(list,n):
    print("Found at",pos+1)
else:
    print("Not Found")