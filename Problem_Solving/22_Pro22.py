# merge two dictionary

# using operator
a = {1:'hello',2:'Python'}
b = {3:'By',4:'good'}

print(a | b)

# using ** operator
a = {1:'hello',2:'Python'}
b = {3:'By',4:'good'}

print({**a, **b})

# using copy and update method
a = {1:'hello',2:'Python'}
b = {3:'By',4:'good'}

c = a.copy()
c.update(b)
print(c)