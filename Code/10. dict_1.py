# Dictionarys
"""
dictionary are collection of ordered. changeable and do not allow duplicate keys.
denoted by {} and key value pairs.

# in python 3.6 or earlier, dictionary were unordered but after python 3.7 , dictionary are ordered.
"""

# create a dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# duplicates are not allowed
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020      # <-- will raise error key have to be unique.
}
print(thisdict)

# use len() to find len to items in dict.
print(len(thisdict))

# using dict() constructor. 
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

# Accesing dictiionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)

# same result with get() method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
print(x)

# using keys() method to get all keys inside dictionary,
x = thisdict.keys()

# updating dictionary also changes dictionary keys list return
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change

car["color"] = "white"
print(x) #after the change

# using values() method ,same as keys return all values list in dict.
x = thisdict.values()

# changing in dictionary value will also changes value list get by value() method.
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change

car["year"] = 2020
print(x) #after the change

# using items() method return each item (key value pair) in the dictionary as tuple is a list.
x = thisdict.items()

# changes in the dictionary will reflect in items list as well.
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change

car["year"] = 2020
car["color"] = "red"
print(x) #after the change

# check if key exists.
# using in keyword
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


####### change Dictionary items
# change dict item by refering to key 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

# update dictionary using update() method
# update() will update the dict with items given in its argument.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})     # <-- should be in key value pair inside a dict.

###### Adding items to Dictionary
# adding item canbe done by using a new key name and assigning a value in it.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

# update dictionary using update() method
# update() will update the dict with items given in its argument.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

#### Removing items from dictionary.
# using pop() method with specified key.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

# using popitem() method remove last item inserted (before python 3.7 random item used to get pop)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

# you can also use del keyword with specific key to remove.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

# And yes del keyword can delete whole dict as well so make sure what are you doing.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict        # <-- minor changed from item removal command.
print(thisdict) #this will cause an error because "thisdict" no longer exists.

# using clear() method empties whole dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

#### looping in dictionary
# using for loop
for x in thisdict:
  print(x)

# to print all values in dict
for x in thisdict:
  print(thisdict[x])

# you can also use values() to return only value from dict
for x in thisdict.values():
  print(x)

# using key() return key only from dict
for x in thisdict.keys():
  print(x)

# use items() to return key value pair from dict
for x, y in thisdict.items():
    print(x,' : ', y)



#### for copying dictionaries
"""
# You cannot copy a dictionary simply by typing dict2 = dict1,
# because: dict2 will only be a reference to dict1,
# and changes made in dict1 will automatically also be made in dict2.
"""
# using copy() method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# using dict() constructor
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)     # <-- dict() copies to mydict
print(mydict)

##### Nested Dictionaries
# dictionary, inside of dictionaries.
# example
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
# my family is a dict contains child1, child2, child3 dictionaries.

# you can also add this way
# create 2 dict seperately and then there reference inside a dictionary
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
myfamily = {
  "child1" : child1,
  "child2" : child2
}

# Access Items in nested Dictionary
print(myfamily["child1"]["year"])   # <-- use 2 [] brackets

# Loop through nested Dictionaries
# using items()
for key, value in myfamily.items():
  print(key)
  for inner_key in value:
    print(inner_key + ':', value[inner_key])


### additional Dictionary Methods
"""
fromkeys()	Returns a dictionary with the specified keys and value
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
"""




