# 👉set:-
# 👉set is the collection of the unique elements.
# 👉set is the represent for the {}.
# 👉set is never follow the sequeance means it not follow the sequance.
# 👉set does not support for index.
# 👉set is simillar to the list the difference would be it not maintaine
# the sequance and its not support duplicate values.
# 👉Its not display the repeat value means the you are enter the
# {23,24,23,56,76} but it is a got the output for the here 23 is got
# only one time not a two time.

set = {23,56,43,23,78,65}
print(set)

# ****************************************************************
# add
set = {1,2,3,4}
set.add(5)
print(set)

# remove
set = {1,2,3,4}
set.remove(2)
print(set)

# pop
set = {1,2,3,4}
set.pop()
print(set)

# union
set1 = {1,2,3,4}
set2 = {2,3,4,5}
set3 = set1.union(set2)
print(set3)

# intersection
set1 = {1,2,3,4,5}
set2 = {2,3,4,5,6}

set3 = set1.intersection(set2)
print(set3)

# clear
set = {1,2,3,4}
set.clear()
print(set)

# copy
set = {1,2,3,4}
x = set.copy()
print(x)