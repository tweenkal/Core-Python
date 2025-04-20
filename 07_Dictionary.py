# 👉Dictionary :-
# 👉Dictionary is the combination of  the key value pair.
# 👉Dictionary is represent the {}.
# 👉Dictionary is the key is the unique and im-mutable means it can not
# change the value.

data = {1:'Twinkle' , 2:'Hinal' , 3:'Heli'}
print(data)

# 👉fetch the particular value means it use the key
print(data[2])

# 👉second way for the fetch the particular value using the get()
print(data.get(2))

print(data.get(4))  #here not give the error it is give the none.

#print(data[4])  #it is give to the error key error.

print(data.get(2,'Not found')) #here is present the index 1 in the dic means it is give the Hinal.

print(data.get(4,'Not found'))  #here is not present the index 4 in the dic then its give the not found.

# 👉Here make 2 list and combine to the dictionary

key = ['Twinkle','Hinal','Heli']
values = ['Python','Java','PHP']


#here zip() is used to the merge the two list and make the dictionary
# and dict() is the function of the dictionary
data = dict(zip(key,values))
print(data)

#👉 add key and value in dictionary
data['Monika'] = 'Css'
print(data)

# 👉Here fetch the value using key
print(data['Monika'])

print(data['Twinkle'])

# 👉Here delete the key for Monika
del data['Monika']
print(data)

# 👉Nested dictionary dictionary inside the list and dictionary
# inside the dictionary.

prog = {'Java' : 'Atom' , 'Css' : 'Vs' , 'Python' : ['Pycharm','IDLE','Jupiter'] , 'PHP' : 'Larawell' , 'C++' : {'Turbo c' , 'Vs code' , 'another'}}
print(prog)

# 👉fetch the particular value in this dictionary
print(prog['Python'])

# 👉fetch particular value using index
print(prog['Python'][2])

print(prog['Java'])

