# Python inheritance
"""
Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.
"""

# Example - student class with inherit Person class.
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(f'first name : {self.firstname}, last name : {self.lastname}')

p1 = Person("john", "doe")
p1.printname()

class Student(Person):      # <-- that's how to right which class to inherit
    pass

S1 = Student("jane", "doe")
S1.printname()

# working of __init_() method in classes
# remember __init_() method is always there even if you did not define it.
# and if you define __init__() method in child class, it will no longer inherit from the parent class __init() method.
# to inherit from parent class do this.
# example
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(f'first name : {self.firstname}, last name : {self.lastname}')

p1 = Person("john", "doe")
p1.printname()

class Student(Person):
    def __init__(self, fname, lame):
        Person.__init__(self, fname, lname)     # <-- do this to inherit parent __init__method.

S1 = Student("mike", "olsen")
S1,printname()

# using super() function.
# using super method child class can inherit all method and its properties from parent class.
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)      # <-- do not need to use parent element name (person) here, just use super()
# notice also we did not use self parameter her.

x = Student("Mike", "Olsen")
x.printname()

# ADD extra properties.
# Example
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname):
        super.()__init__(fname, lname)
        self.graduationYear = 2019      # <-- by doing this all class entry will have 2019 as graduation year.

# lets see how to pass it as an variable from class instance.
# to do so just add another parameter in child class init method
class Person():
    def __init__(self,  fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, graduationyear):
        super().__init__(fname, lname)

s1 = Student("mike", "mudda", "2050")
s1.printname()

## Add Methods to student class.
class Person():
    def __init__(self,  fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)












