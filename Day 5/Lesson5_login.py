u = input('Enter username: ')
p = input('Enter password: ')

if u.upper() == 'tamim'.upper() and p == '123':
    print(f'Welcome Mr. {u}')

elif u.upper() != 'tamim'.upper() and p == '123':
    print('Invalid username')

elif u.upper() == 'tamim'.upper() and p != '123':
    print('Invalid password')

else:
    print('username and password both are invalid!!!')