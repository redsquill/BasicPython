"""
while loop
-----------------------
init variable
while condition: 
    statements
    ...    
"""
i = 1
while i <= 50:
    print(i, end='\t')
    #i = i+1
    i += 5

print('\n\n')  # \n for new line
start = int(input('Enter start value: '))
stop = int(input('Enter stop value: '))
i = start

while i <= stop:
    # if i % 2 != 0:
    if i % 2 == 0:
        print(i, end='\t')

    i += 1
