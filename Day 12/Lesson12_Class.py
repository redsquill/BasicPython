"""
Class 
---------------------------------
A class is a blueprint for the object.

An object has two characterstic
1# Attribute
2# Behavior

General syntax of class
---------------------------------------
class ClassName(object):
    body of class'

"""


class Person(object):
    # Constructor
    def __init__(self, name, age) -> None:
        super().__init__()
        print("I'm from base class.")
        self.name = name
        self.age = age
        self.dob = '1997-07-22'

    def walk(self):
        print(f'{self.name} is now walking. ')

    def run(self):
        print(f'{self.name} is running. ')

    def show(self):
        print(f'I am {self.name}, {self.age} years old. ')


# creating class object
"""
P1 = Person('Shoaeb', 16)
P1.walk()
P1.show()

P2 = Person('Altabur', 12)
P2.show()
"""

# inheritence


class Student(Person):
    def __init__(self, name, age, fees) -> None:
        super().__init__(name, age)
        self.fees = fees

    def show(self):
        print(f'I am {self.name}, {self.age} years old & fees is {self.fees} ')


S1 = Student('Ashik', 24, 4000)

S1.show()
