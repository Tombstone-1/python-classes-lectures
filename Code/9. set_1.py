# SETS
"""
sets are used to store multiple items in single variable.
set is one the built-in data types of python.
set is collection of unordered , mutable, unindexed items and not allow duplicate items.
frozenset is unmutable.
# one more thing sometimes you have heard that set are un mutable even though you can add remove items that because items inside set should be unchangeable.

denoted by {}
"""

# create a set
thisset = {"apple", "banana", "cherry"}
print(thisset)

# duplicate are not allowed , only first occurance would be return in set. rest will get ignore
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)      # output - {"apple", "banana", "cherry"} might not be same order but value will be same.

# Set considered (Boolean) True and (int) 1 as same, means duplicate and not allowed in set.
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)      # output - {"apple", "banana", "cherry", True, 2}
# same goes for (Boolean) False and (int) 0.

# Get length of set, using len()
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

# Set dataypes
set1 = {"apple", "banana", "cherry"}    # string
set2 = {1, 5, 7, 9, 3}                  # integer
set3 = {True, False, False}             # boolean
set1 = {"abc", 34, True, 40, "male"}    # all Mix.

# Using set() constructor.
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

# Acces Items
# access set is quite different from other datatype, as it does not contain index.
# use for and in keyword for this.
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

# check if something is present in set
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

# check if something not in set
thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)

# See Once Set created you cannot change (update) its items but can add, remove new items,
# ADD items using add() method.
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")       # <-- will get added but don't know where as its undordered.
print(thisset)

# ADD other iterable (list tuple dict) by using update() method.
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

# Remove Items using Remove() method
# if item to remove does not exist ,remove() will raise an error.
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# using discard() method
# if remove item does not exist, discard() will not raise error.
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

# you can also use pop() method, but since set is unordered we don't know which item will get remove.
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)            # <-- stores remove item.
print(thisset)

# using clear() method
# just like list clear() method will clear the list for items, making it empty set.
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# using del keyword
# this is delete entire set.
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)  #this will raise an error because the set no longer exists


### Looping through sets.
# using For.
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

### Join sets
# there are several methods to join.
"""
union() and update()    methods join all items from both sides.excluding all duplicates
intersection()          keeps only duplicates
symmetric_difference()  keep all items except duplicates
difference()            keep items from first set that are not in the other set.
"""

# using union() method
# union return new set with all items of both sets.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# you can also use | bitwise or operator, give same result as union().
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)
# remember | operator only allow to join set with seth not other like set with tuple list dict .

# join multiple set with union() method
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

# join set with tuple using union() method
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)

# using update() method
# update() method will insert items to other set. measn changes the original set.
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

# using intersection() method
# will return new set with items that is contained by both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

# same as union() method you can also use & bitwise and operator for intersection() and it will provide same result.
# & operator can be only use to join sets not other datatypes.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)

# using intersection_update() method.
# will keep duplicate but will changes in original set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)
print(set1)

# using difference() method.
# will return a new set containing only items from the first set that are not present on other set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)
print(set3)     # output - {"banna", "cherry"}

# using - operator same as difference() method. only for sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)

# using difference_update() method
# will keep only those value from first set that is not present in second set and return original set(first)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)
print(set1)

# using symmetric_difference() method 
# will exclude items that are present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
print(set3)

# using ^ operator same as symmetric_difference() method. only work for sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)

# using symmetric_difference_update() method
# same function as symmetric_difference, but instead of return new set , make changes in original one.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)
print(set1)


# set methods()
"""
isdisjoint()	 	Returns whether two sets have a intersection or not
issubset()		    Returns True if all items of this set is present in another set
issuperset()		Returns True if all items of another set is present in this set

"""