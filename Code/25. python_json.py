"""
Python JSON
JSON is a syntax for storing and exchanging data.
JSON is text, written with javascripts object notation.

"""
# python has built in package for json
import json

# parse json - convert from json to python.
# is you have json string, you can parse it by using the json.loads() method.
# convert json to python --> result will be python dictionary.
import json

# some JSON:
x = '{ "name" : "john", "age" : 29, "city" : "Canada"}'

# parse json that is x
y = json.loads(x)

# return result
print(y["age"])

# Now let's do the reverse
# convert python to json
# using json.dumps()
import json

# python object(dict)
x = {
    "name" : "jane doe",
    "age" : 29,
    "city" : "NA",
}
# here difference between json and dict declaration is just comma surrounding curly bracket
# convert python to json
y = json.dumps(x)
print(y)

"""
you can convert python objects of the following types into JSon Strings.
dict, list, tuple, string, int, float, True, False, None
"""
# Example
import json

print(json.dumps({"name": "John", "age": 30}))      # --> result : object
print(json.dumps(["apple", "bananas"]))         # --> result : Array
print(json.dumps(("apple", "bananas")))         # --> result : Array
print(json.dumps("hello"))                  # --> result : String
print(json.dumps(42))                   # --> result : Number
print(json.dumps(31.76))                # --> result : Number
print(json.dumps(True))                 # --> result : true
print(json.dumps(False))                # --> result : false
print(json.dumps(None))                 # --> result : null

# convert a python object containing all the legal data types:
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

# format the Result
# above example print json and it will be messay and not easy to read, with no indentations and the line breaks
# to format json , use json.dumps() with parameters
json.dumps(x, indent=4)

# use seperators
json.dumps(x, indent=4, separators=(".", " = "))

# use sort_keys to order
json.dumps(x, indent=4, sort_keys=True)


