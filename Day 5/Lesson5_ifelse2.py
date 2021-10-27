while True:

    print('Main Menu')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Disvison')
    print('5. Exit')
    print('Enter your selection: ',end = '')

    x = int(input())

    if x == 1:
        a = int(input('A: '))
        b = int(input('B: '))
        print(f'Addition is {a + b}')

    elif x == 2:
        a = int(input('A: '))
        b = int(input('B: '))
        print(f'Subtraction is {a - b}')

    elif x == 3:
        a = int(input('A: '))
        b = int(input('B: '))
        print(f'Multiplication is {a * b}')

    elif x == 4:
        a = int(input('A: '))
        b = int(input('B: '))
        print(f'Division is {a / b}')    

    elif x == 5:
        
        print('Thank you for using this application')
        break   # Exit from loop    

    else:
        print('Invalid selection') 
