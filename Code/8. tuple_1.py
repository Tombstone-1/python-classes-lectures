"""
# TUPLE
Tuples are used to store multiple items in a single variable.
Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
A tuple is a collection which is ordered and unchangeable.
denote with round brackets
"""

# Tuple
# items are ordered, unchangeable, and allow duplicate value.
# items are indexed, first element in index [0] and secon on [1], and soon.
# unchangeable means we cannot change, add, remove items after tuple been created.

# check tuple length. use len()
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# create tuple with one item.
thistuple = ("apple",)      # <-- is tuple , just because of this comma.
print(type(thistuple))

thistuple = ("apple")       # <-- Not tuple, it's simple string.
print(type(thistuple))

# tuple datatype and type of data it can contains.
tuple1 = ("apple", "banana", "cherry")      # <-- all strings
tuple2 = (1, 5, 7, 9, 3)                    # <-- all integer
tuple3 = (True, False, False)               # <-- all boolean
tuple1 = ("abc", 34, True, 40, "male")      # <-- all mix.

# tuple() constructer to make tuple.
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
# used tuple() constructor with bunch of strings as parameter.

# Access Tuple Items
# using index
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])     # output -- banana.

# Negative Indexing
# negative indexing means start from end. -1 refers to the last item, -2 refers to the second last item and so on.
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])        # output -- cherry.

# Range of indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])       # output - (cherry, orange, kiwi), remember 5 will not be included, means last position is not included.

# This example returns the items from the beginning to, but NOT included, "kiwi":
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

# This example returns the items from "cherry" and to the end:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

# Range of Negative Indexes
# This example returns the items from index -4 (included) to index -1 (excluded)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])  # output - ("orange", "kiwi", "melon")

# check if item exists. use 'in' keyword.
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")


# As you know you cannot change tuple value because its unchangeable.
# but there's workaround if you want to change tuple, convert to list then back to tuple.
x = ("apple", "banana", "cherry")
y = list(x)         # <-- using list() constructor
y[1] = "kiwi"
x = tuple(y)        # <-- using tuple() constructor
print(x)

# same as before if if you want to add, remove items you have to use this workaround.
# remember if you making tuple with only one item please a comma after , or else it will not be recognized as tuple.

# ADD items 
# list way
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

# Tuple way (you can add tuples to tuples)
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y      # <-- add tuple to other tuple.
print(thistuple)

# Remove Items
# List way.
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

# or delete tuple entirely. using del keyword.
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

#### UN-pack tuples
# when we create tuple by normally assigning value to it called packing.
# but in python we are also allowed to do unpacking , means getting tuple items as variable tuple.
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits       # here green, yellow, red are all variable which store "apple","banana", "cherry" respectivitly.
print(green)
print(yellow)
print(red)
# notes make sure when unpacking your number of variable should match with no. of items.
# if you do not know how many items you can just use (*) Asterisk.
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)        # print "apple"
print(yellow)       # print "banana"
print(red)          # print ["cherry", "strawberry", "raspberry"] because of asterisk.
# if asterisk is assign somewhere between, then python will assign value to asterisk variable until last variable matches with no. of items.
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)        # print apple
print(tropic)       # print ["mango", "papaya", "pineapple"]
print(red)          # print "pineapple", "cherry"

#### LOOP through Tuple.
# using for.
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

# using range() and len()
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

# using While loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

# TUPLE joins
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply tuples
# multiply content of tuple by given number using * operator. different from previous use of asterisk in unpacking
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)      # output  ["apple", "banana", "cherry", "apple", "banana", "cherry",]

# TUPLE Methods
"""
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found

"""



