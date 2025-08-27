### What is OOP ?
"""
OOP stands for object-oriented programming
Python is an object oriented language, allowing you to structure your code using classes and objects for better organization and reusability.

### Advantages of OOP
Provides a clear structure to programs
Makes code easier to maintain, reuse, and debug
Helps keep your code DRY (Don't Repeat Yourself)
Allows you to build reusable applications with less code

when you create an object from a class, it inherits all the variables and function defined inside that class.
"""

# Example : Create a class
# use keyword : class
class MyClass:
    x = 5

p1 = MyClass()  # <-- here this p1 is an object of class.
print(p1.x)

"""
## The __init__() method
all classes have a method called __init__(), which is always executed when the class is being initiated.
use __init__() method to assign values to object properties, or other operations that are necessary to do when the object is being created.
"""

# Example : use __init__() method to assign values to class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
# the __init_() method will get automatically called everytime class is used to create new object.

"""
__str__() method -> controls what should return when class object is printed
without __str__() method class object .classname at some address is written.
"""
# example
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)
print(p1)       # <-- without __str__() this return when object created"<__main__.Person object at 0x15039e602100>"

# with using __str__()
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)
print(p1)           # <-- due to __str__() this return when class object created "John(36)"

# create methods inside class
# can create your own method inside objects. this methods belong to class.
# example
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
# the self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
# here self is just given word, you can name it any thing you just have to mention first in function parameters.
# example : replace self with myself
class Person:
    def __init_(myself, name, age):
        myself.name = name
        myself.age = age
    
    def func1(xyx):
        print("hello my name is : "+ xyz.name)

p1 = Person("Doe", 89)
p1.func1()

# modify object properties
# just use class object.
p1.age = 48

# delete object properties
# using del keyword with class object
del p1.age
# remember this not just delete age in p1.age but whole age property from p1 attribute.

# you can also delete object this way
del p1

# use pass statement if you have plan for class but not for now.
class Person:
    pass
# this way leaving an class empty will not give you error.






