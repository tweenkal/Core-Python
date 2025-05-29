# 👉Enumarate function:-
# 👉Enumarate function is the built-in function in python that allow you
# to loop over a sequance and get the index and value of each element in
# the sequance at the same time.

# marks = [12,34,56,67,54,34]
#
# for index,mark in enumerate(marks):
#     print(mark)
#
#     if index == 3:
#         print("mark")
#
#     index += 1

# 👉start with index 1

marks = [12,34,56,67,54,34]

for index,mark in enumerate(marks,start=1):
    print(mark)

    if index == 3:
        print("mark")

    index += 1

