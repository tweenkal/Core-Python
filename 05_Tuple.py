# 👉Tuple:-
# 👉Tuple is the simillar to the list.
# 👉Tuple is the collection of the values.
# 👉Tuple is the im-mutable means it can not change the value.
# 👉Tuple is the represent the ().
# 👉Tuple is the faster than the list

tup = (24,66,33,23,24,43)
print(tup)

print(tup[2])

print(tup[2:])

# 👉count() :- count is the count of the number and its expects to the
# one argoument.
print(tup.count(24))

#index() :- its a find the index number of the value in the tuple
print(tup.index(66))


# 👉tuple:-

# here coma is consider the tuple
tup = ('hello',)
print(tup)
print(type(tup))
b = 5,'hello'
print(type(b))


# 👉change the tuple

tup1 = ("Apple","Banana","Cherry","Mango","Rasbari")
print(tup1)

tup2 = list(tup1)
tup2.append("Orange")
print(tup2)

tup2[1] = "Banana1"
print(tup2)

tup3 = tuple(tup2)
print(tup3)