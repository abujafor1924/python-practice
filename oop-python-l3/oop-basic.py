"""
 basic Oop subject:
 1. class
 2. object
 3. inheritance (Object Behaviour)
 4. abstraction
 5. polymorphism
 6. Encapsulation
 7. Constractor (self drive)

"""


# Basic Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# basic Object
p1 = Person("John", 36)


# Basic Inheritance
# define a superclass
# class super_class:
# attributes and method definition

# inheritance
# class sub_class(super_class):
# attributes and method of super_class
# attributes and method of sub_class

class Animal:
    # attribute and method of the parent class
    name = ""

    def eat(self):
        print("I can eat")


# inherit from Animal
class Dog(Animal):

    # new method in subclass
    def display(self):
        # access name attribute of superclass using self
        print("My name is ", self.name)


# create an object of the subclass
labrador = Dog()

# access superclass attribute and method
labrador.name = "Rohu"
labrador.eat()

# call subclass method
labrador.display()

# basic abstraction
# Python program demonstrate
# abstract base class work
from abc import ABC, abstractmethod


class Car(ABC):
    def mileage(self):
        pass


class Tesla(Car):
    def mileage(self):
        print("The mileage is 30kmph")


class Suzuki(Car):
    def mileage(self):
        print("The mileage is 25kmph ")


class Duster(Car):
    def mileage(self):
        print("The mileage is 24kmph ")


class Renault(Car):
    def mileage(self):
        print("The mileage is 27kmph ")

    # Driver code


t = Tesla()
t.mileage()

r = Renault()
r.mileage()

s = Suzuki()
s.mileage()
d = Duster()
d.mileage()


# Class Polymorphism
# Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.
# For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move():
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")


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
        print("Fly!")


car1 = Car("Ford", "Mustang")  # Create a Car class
boat1 = Boat("Ibiza", "Touring 20")  # Create a Boat class
plane1 = Plane("Boeing", "747")  # Create a Plane class

for x in (car1, boat1, plane1):
    x.move()


# basic Encapsulation
# Python program for demonstrating protected members
# first, we will create the base class
class Base1:
    def __init__(self):
        # the protected member
        self._p = 78

    # here, we will create the derived class


class Derived1(Base):
    def __init__(self):
        # now, we will call the constructor of Base class
        Base1.__init__(self)
        print("We will call the protected member of base class: ",
              self._p)

        # Now, we will be modifing the protected variable:
        self._p = 433
        print("we will call the modified protected member outside the class: ",
              self._p)


obj_1 = Derived1()

obj_2 = Base1()

# here, we will call the protected member
# this can be accessed but it should not be done because of convention
print("Access the protected member of obj_1: ", obj_1._p)

# here, we will access the protected variable outside
print("Access the protected member of obj_2: ", obj_2._p)



# Basic Constructor
class Employee:
    def __init__(self, name, id):
        self.id = id
        self.name = name

    def display(self):
        print("ID: %d \nName: %s" % (self.id, self.name))


emp1 = Employee("John", 101)
emp2 = Employee("David", 102)

# accessing display() method to print employee 1 information

emp1.display()

# accessing display() method to print employee 2 information
emp2.display()