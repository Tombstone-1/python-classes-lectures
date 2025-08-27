# what is module 
# consider it as a library to import.

# create a module (remember to save it as .py) file named as greet_module.py
def greeting(name):
    print("hello, "+ name)

# import as module
# when using a function syntax : module_name.function_name
import greet_module

greet_module.greeting("johnson")    

# variable in modules
# module can also contain variable as list, dictionaries and so on.
# create a module_dict.py 
person = {
    "name" : "john"
    "age" : 36
    "country" : "somewhere"
}
# then import it on another file.
import module_dict

ele = module_dict.person["age"]
print(ele)

# renaming a module called aliasing. (to make calling easy)
import module_dict as DM

ele = DM.person["age"]
print(ele)

# you can make your module as well as make your own module.

# dir() -> a built in function to list all function and variable inside a module.
import platform

x = dir(platform)
print(x)
# dir() can be used on built-in as well as user defined module.

# using from keyword
# use this when you know what you want from inside a module then use from keyword.
# create your own module (mymodule.py)
def greeting(name):
    print("Hello, "+ name)

person = {
    "name":"hosefina"
    "age" : 46
    "country": "mexico"
}
# import it on other file.
from mymodule import greeting

greeting("manendez")

# using * asterisk
# when you want to import all variable and functions from module file.
from mymodule import *


