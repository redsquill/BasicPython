"""
function
----------------------------------
def function_name(parameteres):
    docstring
    statements
"""


def welcome():
    """
    this function welcome to the person
    """
    print('Hello, Tahrin. Gooddmorning')


# calling function
welcome()
print(welcome.__doc__)


def welcome1(name):
    print(f'hello, {name}. Goodmorning!')


welcome1('Ashik')
welcome1('Shoeb')


def welcome2(name, msg):
    print(f'hello, {name}. {msg}!')


welcome2('Sajib', 'Good evening')
welcome2('Rahman', 'Good afternoon')

# Python arbitrary arguments


def welcome3(*names):
    for name in names:
        print('Hello ', name)


welcome3('Tahrin', 'Sajib', 'Ashik', 'Nayeem', 'Rahman')


def addition(x, y):
    print(x + y)


addition(3, 5)


def add(x, y):
    return (x + y)


result = add(4, 6)
print(result)


def sub(x, y):
    return (x - y)


print(sub(8, 3))


def multi(x, y):
    return (x * y)


print(multi(3, 4))


def div(x, y):
    return (x / y)


print(div(10, 3))


def double(x):
    return(x * 2)


print(double(3))
