# if 3 > 2:
#     print('3 es mayor que 2')
# if 5 >= 10:
#     print('5 es menor o igual a 10')
# else:
#     print('5 no es mayor o igual que 10')

num_1 = int(input('Escoge un entero: '))
num_2 = int(input('Escoge otro entero: '))

if num_1 > num_2:
    print('El primer numero es mayor que el segundo')
elif num_1 < num_2:
    print('El segundo numero es mayor que el primero')
else:
    print('Ambos numeros son iguales')