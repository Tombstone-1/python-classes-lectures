# Boolean Values 
# booleans represent one to two value :True or False
# in programming you can evaluate any expression and can get boolean answer.

# example
print(10 > 9)   # return : True
print(10 == 9)  # return : False
print(10 < 9)   # return : False

# use boolean in an conditional statement.
# example (print correct msg based on bool output.)
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# Evaluate Value and Variable. bool() function.
# The bool() function allows you to evaluate any value, and give you True or False in return,
print(bool("Hello"))
print(bool(15))
### or ####
x = "Hello"
y = 15

print(bool(x))
print(bool(y))
# both output will be True.

### What Values are True.

# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.
# example.
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])


#### what vales are False.
# In fact, there are not many values that evaluate to False, 
# except empty values, such as (), [], {}, "", 
# the number 0, and the value None. And 
# of course the value False evaluates to False.
# example
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
# all value will return False.

# Boolean in class.
# One more value, or object in this case, evaluates to False
# and that is if you have an object that is made from a class with a __len__ function that returns 0 or False
# example :
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj)) # return False.  

# but return True if return 1 or True.
class myclass():
  def __len__(self):
    return 1

myobj = myclass()
print(bool(myobj))


### Function can return Boolean values.
def myFunction() :
  return True

print(myFunction())

# execute an function based on boolean return.
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

# Python also has many built-in functions that return a boolean value, 
# like the isinstance() function, which can be used to determine if an object is of a certain data type:
x = 200
print(isinstance(x, int))

