# Lists
# list are used to store multiple items in a single variable.
# list are on of 4 builtin data types of python use to store collection of data.
# denoted with square bracket []

# example.
thislist = ["apple", "banana", "cherry"]
print(thislist)

# list items are ordered, changeable, and duplicates.
# list items indexed from [0] and go on.

# Ordered 
# When we say that lists are ordered, 
# it means that the items have a defined order, and that order will not change.
# If you add new items to a list, the new items will be placed at the end of the list.

# changeable
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

# Allow Duplicates
# Since list are indexed, list can have items with same value.
# Example:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# List length. len()
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# list of many types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# list can contain many types
list1 = ["abc", 34, True, 40, "male"]

# you can use type on list to see datatype
mylist = ["apple", "banana", "cherry"]
print(type(mylist))     # output : class 'list'

# list() Constructor : can also use list() when creating new list
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


# Acces list items
# list are indexed, and can be acess easily by using it.
# example
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# first positive index is 0 and start from left side.
# whereas first negative index is -1 and start with right side. (start from end).
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# range of indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
# here search will start from index 2 i.e. cherry and end at index 5 (not included).
# so output, ["cherry", "orange", "kiwi"]


# slicing 
# ex 1
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
# start from begining and leave out 4 index.
# output : ["apple", "banana", "cherry", "orange"]

# ex 2
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
# start from index 2 and till very last.
# output : ["cherry", "orange", "kiwi", "melon", "mango"]

# negative slices ex.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# check if item exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# change item value
# to change list item refer to index value.
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# change a range of item values. means change item value between a particular range of indeces.
# ex -  change the value between banana and cherry with blackcurrant and watermelon.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# change the second value by replaceing it with two value,
# result will be two new value in second position and rest will be shifted to the right.
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
# length of the list will change if inserted item does not match the number of item replaced.
# if you insert same, same no. will get replaced.

# Change the second and third value by replacing it with one value:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# Append Items
# to add item to the end of the list, use append() method.
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Extend list. append elements of other lists.
# use extend()
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Add any iterable
# the extend() method does not have to append list only, you can also use tuple, set , dict.
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# remove list items. remove()
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
# if there is duplicate item list removes first occurance.

# remove Specified Index. pop()
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
# if you did not specify the index, the pop() removes the last item.
# remove() works with item values.
# pop() works with index.

# del keyword , yes this is a keyword and not a function.
# remove item with index and also the whole list.
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
# delete entire list
thislist = ["apple", "banana", "cherry"]
del thislist

# now you don't want to delete list
# use clear() , it clear the list items with deleting whole list.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# loop through list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# loop through the index number.
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

# looping using list comprehension.
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


### List Comprehension.
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# if not used list comprehension, then have to use for loop.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)       # <-- newlist.append() using for loop.

print(newlist)

# with list comprehension.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

# Syntax --> 
# newlist = [expression for item in iterable if condition == True] iterable means list, tuple, set, dict
# return new list without changing old.

# conditions based.
# The condition is like a filter that only accepts the items that evaluate to True.
# example -  only accept item that are not apple.
newlist = [x for x in fruits if x != "apple"]
# The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".

# with no if statement (condition is optional.)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)
# this will copy fruits list into new list

# using iterable
# The iterable can be any iterable object, like a list, tuple, set etc.
# you can even use range() to store 10 no. into newlist.
newlist = [x for x in range(10)]
# same but with condition
newlist = [x for x in range(10) if x < 5]

# you can also use Expression in iterable to change outcome of list.
newlist = [x.upper() for x in fruits]

# you can set similar outcome to all list items.
# for example change all elements of fruits list to apple.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['apple' for x in fruits]

# the expression can also contain ,not like a filter , but as a way to manipulate the outcome.
newlist = [x if x != "banana" else "orange" for x in fruits]
# return orange in place of banana.

# Sorting
# use sort() to sort list alphabetically. ascending by default.
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# sort numerically
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# now for descending sorting.
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

# Customize sort function.
# you can also Customize your own function by using the keyword argument (key = function)
# example : sort list based on how close the number is to 50
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
# output : [50, 65, 23, 82, 100]

# Case sensitive sorting 
# normal sort() function in sorting case sensitive word gives unexepected result.
# for this we use sort(key = str.lower)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
# output : ['banana', 'cherry', 'Kiwi', 'Orange']

# Reverse Order
# if you want to reverse the list regardless of alphebet order.
# user reverse() method.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
# output : ['cherry', 'Kiwi', 'Orange', 'banana']

#### List Copying.
# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1
# because: list2 will only be a reference to list1 changes made in list1 will automatically also be made in list2.

# Use copy() built in method
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Another way to make a copy is to use the built-in method list().
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# You can also make a copy of a list by using the ':' (slice) operator.
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]       # <-- [:] this is slice operator.
print(mylist)


#### Join Lists
# there serveral ways to join or concatenate, two or more lists in python.
# one of the easiest '+' operator.
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Another basic way to copy list. by append list 2 into list 1
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

# or use extend() method where the purpose is to add elements from one list to another list.
# extend()
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)


#### ALL DISCUSSED LIST METHODS ###
"""
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
"""





