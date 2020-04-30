# Las listas son mutables
# a = [1,2,3]
# b = a
# print(id(a))
# print(id(b))

# c = [a,b]

# print(c)
# a.append(5)
# print(c)

# Clonar listas mediante list
# a = [1,2,3]
# b = list(a)

# print(a)
# print(b)

# print(id(a))
# print(id(b))

# Clonar listas mediante ::
# c = a[::]
# print(c)
# print(id(c))

my_list = list(range(10))
print(my_list)

# List comprenhesion
double = [i * 2 for i in my_list]
print(double)

pares = [i for i in my_list if i % 2 == 0]
print(pares)