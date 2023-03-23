'''class Dog:
    def __int__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")
    def roll_over(self):
        print(f"{self.name} is rolled over")
my_dog = Dog()


my_dog.sit('lucy',77)
my_dog.roll_over()

'''
from Inheritance import *

class Person:
    name = " "
    age = " "
    default = " "
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.deafult = 5
    def display(self):
        print(f"{self.name} \n{self.age}")
    def read_default(self):
        print(f"{self.deafult}")
p1 = Person("John", 36)
p1.display()
p1.deafult = 44
p1.read_default()

j1 = java()
j1.__int__()
p1 = python()
p1.__int__()