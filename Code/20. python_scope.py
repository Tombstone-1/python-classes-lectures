# local scope - inside a block or for a particular function or class.

# example local scope:
def myfunc():
  x = 300          # <-- only accessible by function
  print(x)

myfunc()

# Example global scope:
x = 300             # <-- here it can be accessed by any function or anywhere through out program.

def myfunc():
  print(x)

myfunc()
print(x)

"""
if you operate same named variable but one is local to the function and one is global then python
will treat it as 2 separate variable and local one will only be used inside of that function or block.
"""

# if you want to make local variable global
# do that by using global keyword next to variable.
def myfunc():
  global x
  x = 300

myfunc()
print(x)
# this can initialize a local variable as global 
# but if you have a global variable and you want to make changes to that
# not to the local one (as they have same name) use global keyword and that variable name.
# Example
x = 300

def myfunc():
  global x
  x = 200

myfunc()
print(x)
# this will be change value of global variable.

# Non local keyword
# it is used to work with variable inside nested functions.
# make variable belong to the outer function.
# example:
def myfunc1():
    x = 'jane'
    def myfunc2():
        nonlocal x
        x = 'hello'
    myfunc2()           # <-- here value will get changed to hello
    return x
print(myfunc1)
# here second function declared it as nonlocal means variable does not belong to him.
# so even different value is getting assign in the second function, variable belong to first function got changed .

# if nonlocal was not used then output would be jane, as function 2 only define a new local variable to it that does not have any effect on first function.


