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
x = int(input('Enter value for x: '))
y = int(input('Enter value for y: '))

if x > y:
    print("x is Greater than y")

elif x == y:
    print("Both are equal")

else:
    print("y is Greater than x")
