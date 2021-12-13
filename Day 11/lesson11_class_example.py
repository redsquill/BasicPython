"""
Class 
---------------------------------------------------
A class is a blueprit for the object
A object has 2 characteristics 
A# Attributes
B# Behavior

Syntax:
class ClassName(object):
    snip
"""


class MyClass(object):
    """This is my  first class."""
    a = 10

    def myFunc(self):
        print('Hello Nafee')


print(MyClass.a)
print(MyClass.myFunc)
print(MyClass.__doc__)
print(MyClass.__name__)
print(MyClass.__base__)

# creatig class object
#objectname = classname()

x = MyClass()
x.myFunc()


class Parrot:
    # class attribute
    species = 'bird'

    # instace attribute/constructor
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


p1 = Parrot('Mithu', 1)
p2 = Parrot('Birb', 2)
print(f'{p1.name} is a {p1.__class__.species}')
print(f'{p2.name} is a {p2.__class__.species}')

print(f'{p1.name} is {p1.age} years old')
print(f'{p2.name} is {p2.age} years old')
