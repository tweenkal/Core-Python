# 👉Zip function :- it is combine the 2 elements.

name = ('ABC','XYZ','PQR')
company = ('Goggle','MS','Apple')

zipped = list(zip(name,company))
print(zipped)

# This use for many data structure like tuple,dict etc...

for a,b in zipped:
    print(a,"=>",b)