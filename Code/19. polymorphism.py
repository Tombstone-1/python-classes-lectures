# Polymorphism means methods, functions operators with same name that can be executed on many objects or class.

# Class Polymorphism.
# where we can have multiple classes with the same method name.
# for example : we have three classes car, boat, plane and they all have a method called move().
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("drive!")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly")

car1 = Car("Ford", "Mustang")
boat1 = Boat("ibiza", "Touring 20")
plane1 = Plane("boieng", "747")

for x in (car1, boat1, plane1):
    x.move()
# having same method name yet no error raise and it is working properly for every class.

# let's use Inheritance with polymorphism
# here a parent class will get inherited by child class whose having same methods.
# so those method will get overide when called from particular class object.
# example :
# vehicle parent class will have 3 child class car, boat , plane

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("move from parent class")
    
class Car(Vehicle):
    pass

class Boat(Vehicle):
    # no need for init function as that will be done by parent class , having same parameters as required.
    def move(self):
        print("sail")

class Plane(Vehicle):
    def move(self):
        print("fly")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for obj in (car1, boat1, plane1):
    print(obj.brand)
    print(obj.model)
    obj.move()          # <-- this move method will get override for particular class.

# Output
"""
Ford
Mustang
move from parent class      <-- this move method from parent class 
Ibiza
Touring 20
sail                    <-- here it got override by class's own method.
Boeing
747
fly         <-- same for this.

"""