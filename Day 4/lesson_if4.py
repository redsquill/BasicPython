"""
if condition : 
    True  statement
elif condition 2:
    Another Statement
else :
    False statement     

Relational/Comparisional Operator Operatior
equal to    ==
Greater Than    >
Grater Than or Equal to >=
Less Than   <
Less Than or Equal to   <=
Not equal to    !=
"""
x = float(input('Enter value for x: '))
y = float(input('Enter value for y: '))

if x > y:
    print(f"{x} is Greater than {y}")

elif x == y:
    print("Both are equal")

else:
    print(f"{y} is Greater than {x}")
