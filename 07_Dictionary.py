# 👉Dictionary :-
# 👉Dictionary is the combination of  the key value pair.
# 👉Dictionary is represent the {}.
# 👉Dictionary is the key is the unique and im-mutable means it can not
# change the value.

#👉in interview already ask this questions
student = [{'abc': 1, 'bca': 2, 'ddd': 3}]
result = list(student[0].values())
print(result)
# output:-[1, 2, 3]

#👉Here make 2 list and combine to the dictionary
#here zip() is used to the merge the two list and make the dictionary
# and dict() is the function of the dictionary

key = ['Twinkle','Hinal','Heli']
values = ['Python','Java','PHP']
data = dict(zip(key,values))
print(data)
# output:-{'Twinkle': 'Python', 'Hinal': 'Java', 'Heli': 'PHP'}

# *************************************************************************

#👉Create and print a dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
# output:-{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

#👉Print the "brand" value of the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
# output:-Ford

#👉Duplicate values will overwrite existing values:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
#"year": 1964 is added first.
# Then "year": 2020 comes — and replaces the earlier value.
# output:_{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

#👉Get the value of the "model" key:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)
#output:-Mustang

#👉copy:-Returns a copy of the dictionary
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.copy()
print(x)
# output:-{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

#👉fromkeys:-Returns a dictionary with the specified keys and value
#Create a dictionary with 3 keys, all with the value 0:
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)

#👉get :-Returns the value of the specified key
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.get("model")
print(x)
# output:-Mustang

#👉items:-Returns a list containing a tuple for each key value pair
#👉Return the dictionary's key-value pairs:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.items()
print(x)
# output:-dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

#👉keys:-Returns a list containing the dictionary's keys
#👉Return the keys:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.keys()
print(x)
# output:-dict_keys(['brand', 'model', 'year'])

#👉pop:-Removes the element with the specified key
#👉Remove "model" from the dictionary:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
print(car)
# output:-{'brand': 'Ford', 'year': 1964}

#👉popitem:-Removes the last inserted key-value pair
#👉Remove the last item from the dictionary:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.popitem()
print(car)
# output:-{'brand': 'Ford', 'model': 'Mustang'}

#👉setdefault:-Returns the value of the specified key. If the key does
# not exist: insert the key, with the specified value
# Get the value of the "model" item:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("model", "Bronco")
print(x)
# output:-Mustang

#👉del :- The del keyword removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
# output:-{'brand': 'Ford', 'year': 1964}

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict
# print(thisdict) #this will cause an error because "thisdict" no longer exists.


#👉update :- Updates the dictionary with the specified key-value pairs
#👉Insert an item to the dictionary:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.update({"color": "White"})
print(car)
# output:-{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'White'}

#👉values:-Returns a list of all the values in the dictionary
#👉Return the values:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.values()
print(x)
# output:-dict_values(['Ford', 'Mustang', 1964])

#👉clear :- Removes all the elements from the dictionary
#👉Remove all elements from the car list:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
print(car)
# output:-{}

#👉Make a change in the original dictionary, and see that the values list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change
# output:-dict_values(['Ford', 'Mustang', 1964])
# output:-dict_values(['Ford', 'Mustang', 2020])

#👉Add a new item to the original dictionary, and see that the values list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["color"] = "red"
print(x) #after the change
# output:-dict_values(['Ford', 'Mustang', 1964, 'red'])

#👉Check if "model" is present in the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

# output:-Yes, 'model' is one of the keys in the thisdict dictionary

#👉Change the "year" to 2018:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)
# output:-{'brand': 'Ford', 'model': 'Mustang', 'year': 2018}

#👉Update the "year" of the car by using the update() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)
# output:-{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

#👉add items in dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
# output;_{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

#👉Print all key names in the dictionary, one by one:
for x in thisdict:
  print(x)
#output:-
# brand
# model
# year
# color

#👉Print all values in the dictionary, one by one:
for x in thisdict:
  print(thisdict[x])
# output:-
# Ford
# Mustang
# 1964
# red

#👉You can also use the values() method to return values of a dictionary:
for x in thisdict.values():
  print(x)
# output:-
# Ford
# Mustang
# 1964
# red

#👉You can use the keys() method to return the keys of a dictionary:
for x in thisdict.keys():
  print(x)
# output:-
# brand
# model
# year
# color

#👉Loop through both keys and values, by using the items() method:
for x, y in thisdict.items():
  print(x, y)
# output:-
# brand Ford
# model Mustang
# year 1964
# color red

#👉nested dictionary
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)

# output:-{'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}

#👉Print the name of child 2:
print(myfamily["child2"]["name"])
# output:-Tobias




























