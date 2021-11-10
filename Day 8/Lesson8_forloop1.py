"""
for loop
----------------
for item in colection : 
    statement

escape character  
----------------------
tab   \t
new line  \n
quotation  \"
backslash  \\
backspace   \b

"""
import time
for i in [1, 5, 7, 12]:
    print(i, end="\t")

print('\n')
print('-' * 80)
for x in range(11):
    print(x, end='\t')

print('\n')
print('-' * 80)
for x in range(20, 41):
    print(x, end='\t')

print('\n')
print('-' * 80)
for x in range(100, 49, -1):
    print(x, end='\t')

print('\n')
print('-' * 80)
for x in range(100, 49, -1):
    if x % 2 != 0:
        print(x, end='\t')

print('\n')
print('-' * 80)
for x in range(50, 101):
    if x % 2 == 0:
        print(x, end='\t')

print('\n')
print('-' * 80)
fruits = ["Banana", "Apple", "Mango", "Orange"]
count = 1
for i in fruits:
    print(f'{count}. {i}', end='\n')
    count += 1

"""r = ['i', ' ', 'l', 'o', 'v', 'e']"""
r = 'I Love My Mother'
for i in r:
    print(i, end=' ', flush=True)
    time.sleep(0)

print('\n')
print('-' * 80)
sum = 0
o = [2, 5, 10, 20, 50, 70]
for i in o:
    sum += i
print(sum)

"""
Syntax of List Comprehension
[expression for item in list]
"""

print('\n')
print('-' * 80)
number_list = [x for x in range(20)]
print(number_list)


print('\n')
print('-' * 80)
number_list = [x for x in range(20) if x % 2 == 0]
print(number_list)
# Alternative solution
print('\n')
print('-' * 80)
number_list = []
for x in range(20):
    if x % 2 == 0:
        number_list.append(x)
print(number_list)
