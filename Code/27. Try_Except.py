## Python Try Except
"""
try - block lets you test a block of code for errors.
except - block lets you handle the error
else - block lets you execute code when there is no error
finally - block lets you execute code, regardless of the result of the try and except blocks

"""
# Exception handling
# normally python will raise error but this way you can handle error and let code keep executing.
# Example
try:
  print(x)
except:
  print("An exception occurred")

# here first try block will try to execute code normally when it raise error except block will handle.

# Example : Many Exceptions
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
# here x is not declared so it will definitely raise error,
# second block will see if the error it that specific one, if not
# third block will execute.

# using Else keyword
# it will get executed if no errors were raised:
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

# using finally keyword
# this block will execute regardless of error is raised or not.
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
# finally block can be useful to close any objects and clean up resource

# Example : try to open and write a file with no write access.
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

# in this example code did not able to write anything to file,
# so regardless of write or not , finally will close file.
# this way we need not to take tension about file being open.

# using raise keyword.
# we can also raise a particular error if a condition occurs.
# example : raise a error if x is lower than 0
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")

# you can also define what kind of error to raise.
x = "hello"

if not type(x) is int: 
  raise TypeError("Only integers are allowed")
# if type is not int raise an error.







