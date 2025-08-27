## functions ##
"""
A function is a block of code which only runs when it is called.
you can pass data as args and kwargs, known as a parameters
function can also return data when assign return type.
"""

# syntax : def keyword for function.
"""
def function_name (args kwargs)
    statement
"""

# exmaple : create function
def my_function():
    print("print from function")

# calling an function.
my_function()

### Arguments 
"""
information can be passed into function.
From function perspective :-
arguments are that statement that you passed when calling the function
my_function(statement)  # <-- arguments

parameeter are that statement you passed when function is defined.
def my_function(statement):     # <-- statement.
"""

# example : arguments and parameter
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# number of argument (in normal case argument and parameter in function should match in number)
# not more not less, yes if default parameter used , then its a different case.
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

# Example : *args
# if not know how many argument will be passed in function then use * before parameter
# this way function will receive tuple of arguments and can access accordingly.
def my_function(*kids):     # < given only 1 parameter.
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")  # <-- passed 3 argument

# Arbitary Arguments are often called args in python documentations.
# Keyword Arguments are often called to kwargs python documentations.

# example : keyword arguments
# you can also send arguments with key = value syntax
# this way order of the arguments does not matter.
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")   # <-- key = value pair

# arbitrary keyword arguments, **kwargs
# not know how many keyword arguments , then use ** before parameter in function definition.
def my_function(**kid):     # <-- given only 1 parameter
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")    # <-- passed 2 key=value argument

# Example : Default Parameter Value.
# if call function without argument, it uses the default value.
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()           # <-- no argument passed so function will print norway cause of default value.
my_function("Brazil")

# Example : passing list as an argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
# passed list then recieve list
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# Example : return values
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

# Example : Pass statement
# if you need function to be empty for some reason then use pass statement.
def function():
    pass

# Example : Positional-only arguments means *args
# specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
# To specify that a function can have only positional arguments, add , / after the arguments:
# means , / after argument is for positional arguments only.
def my_function(x, /):
  print(x)

my_function(3)
# without , / you can send keyword arguments in place of positional arguments
# ex
def my_function(x):     # <-- in position arguments
  print(x)

my_function(x = 3)      # <-- send keyword argument
# but when add , / this you will get error if pass keyword argument
def my_function(x, /):
  print(x)

my_function(x = 3)      # <-- raise error

# Example : keyword-only Arguments
# *, before arguments means keyword only arguments and no positional argument.
def my_function(*, x):
  print(x)

my_function(x = 3)
# without *,  this you allowed to send argument as you like
def my_function(x):
  print(x)

my_function(3)
# but with *, this , function becomes keyword arguments only and if you send positional then it raise error.
def my_function(*, x):
  print(x)

my_function(3)

# Example : Combine Positional only and keyword -only argument
# Any argument before the / , are positional-only, and any argument after the *, are keyword-only.
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

# Example : Recursion function
# Python also accepts function recursion, which means a defined function can call itself.
# Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)















