# this is single line comment
"""
this is multiline comments

"""

x = 5
y = "John"
print(x)
print(y)

# variable are not needed to be declared with any type
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#casting (type cast your variable to any type you want)
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# if you want type of varibale
x = 5
y = "John"
print(type(x))
print(type(y))

# string should be either used with single or double quotes both have same effect.
x = "John"
# is the same as
x = 'John'

# variable are case sensitive
a = 4
A = "Sally"
#A will not overwrite a


"""
Now there are rules for variable decalaration.
1-> A variable name must start with a letter or the underscore character
2-> A variable name cannot start with a number.
3-> A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ).
4-> Variable names are case-sensitive (age, Age and AGE are three different variables).
5-> A variable name cannot be any of the Python keywords.

"""

# examples declarations. (legal ones.)
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# illegal ones
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# variable decalaretion case type.
# Camel Case
variableName = 5

# Pascal Case
VaribaleName = 5

# Snake case
varibale_name = 5

### Assign Multiple Values.
# python allows you to assign values to multiple variable in one lines.
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
# this will assign orange to x, banana to y, cherry to z.

# Now you can also assign same value to multiple variables.
x = y = z = "Orange"
print(x)
print(y)
print(z)
# this will assign orange to all three x,y,z

# Also if you have collection like list and tuple, pyhton allow you to extract the value into variables.
# this is called unpacking.
# example (unpack a list)
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Now there are various ways to Output a variable. will be required in future settings.
# simplest one.
x = "Python is awesome"
print(x)

# multiple in single print function.
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
# output -> Python is awesome # look how there is space even if we did not give one.

# multiple varibale concatinate to one.
# Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
# output -> Python is awesome

# using + to concatinate is for string and char only.
x = 5
y = 10
print(x + y)
# will give you addition.

# now if you try to do 
x = 5
y = "John"
print(x + y)
# python will give you an error saying combining string and integer.
# instead of that use this
x = 5
y = "John"
print(x, y)


# there local variable and there's global (its only matter of scope of varibale).
# example global and local variable
x = "awesome"   # <-- global variable (reachable from whole program)

def myfunc():
  x = "fantastic"   # <-- local variable (only inside this function).
  print("Python is " + x);   #output : fantastic

myfunc()
print("Python is " + x)   # output : awesome

# global keyword help to declare a variable global wherever they are.
def myfunc():
  global x          # <-- variable becomes global.
  x = "fantastic"

myfunc()
print("Python is " + x)     # output: fantastic.

