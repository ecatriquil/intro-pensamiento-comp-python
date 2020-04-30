# contador_externo = 0
# contador_interno = 0

# while contador_externo < 5:
#     while contador_interno < 6:
#         print(contador_externo, contador_interno)
#         contador_interno += 1

#         if contador_interno >= 3:
#             break
#     contador_externo += 1
#     contador_interno = 0

# frutas = ['manzana', 'pera', 'mango']
# for fruta in frutas:
#     print(fruta)

iter('cadena') #cadena 
iter(['a', 'b', 'c']) #lista
iter(('a', 'b', 'c')) #tupla
iter({'a', 'b', 'c'}) #conjunto
iter({'a': 1, 'b': 2, 'c': 3}) #diccionario

#Todas regresan un objeto de tipo iterator

# frutas = ['manzana', 'pera', 'mango']
# iterador = iter(frutas)
# print(next(iterador))
# print(next(iterador))
# print(next(iterador))

estudiantes = {
    'mexico': 10,
    'colombia': 15,
    'puerto_rico': 4,
}

# for pais in estudiantes:
#     print(pais)

# for pais in estudiantes.keys():
#     print(pais)

# for numero_de_estudiantes in estudiantes.values():
#     print(numero_de_estudiantes)

for pais, numero_de_estudiantes in estudiantes.items():
    print(pais, numero_de_estudiantes)