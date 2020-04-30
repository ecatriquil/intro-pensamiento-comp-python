user_1_name = input('Ingresa tu nombre: ')
user_1_age = int(input('Ingresa tu edad: '))

user_2_name = input('Ingresa tu nombre: ')
user_2_age = int(input('Ingresa tu edad: '))

if user_1_age > user_2_age:
    print(f'{user_1_name} es mayor que {user_2_name}')
elif user_2_age > user_1_age:
    print(f'{user_2_name} es mayor que {user_1_name}')
else:
    print(f'{user_1_name} y {user_2_name} tienen la misma edad!')
    