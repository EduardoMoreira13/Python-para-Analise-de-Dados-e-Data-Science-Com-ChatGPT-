# Exemplo com 1 parâmetro

def quadrado(x):
    return x ** 2


numeros = [1, 2, 3, 4, 5]
numeros_ao_quadrado = list(map(quadrado, numeros))
print(numeros)
print(numeros_ao_quadrado)

numeros_ao_quadrado = list(map(quadrado, numeros))
print(numeros)
print(numeros_ao_quadrado)

print("\n")


# Exemplo com 2 parâmetros

def multiplicar(x,y):
    return x * y

numeros1 = [1, 2, 3, 4, 5]
numeros2 = [8, 4, 1, 6, 5]
numeros_mult = list(map(multiplicar, numeros1, numeros2))
print(numeros1)
print(numeros2)
print(numeros_mult)

print("\n")


# Exemplos com lambda

numeros = [1, 2, 3, 4, 5]
numeros_ao_quadrado = list(map(lambda x: x**2, numeros))
print(numeros)
print(numeros_ao_quadrado)

numeros1 = [1, 2, 3, 4, 5]
numeros2 = [8, 4, 1, 6, 5]
numeros_mult = list(map(lambda x,y: x*y, numeros1, numeros2))
print(numeros1)
print(numeros2)
print(numeros_mult)


a = [1,2,3,4]
b = [5,6,7,8]
c = [9,10,11,12]

print(list(map(lambda x, y, z : x + y + z, a, b, c)))


print("\n")


# Exemplo com funções já existentes e que precisam de mais parâmetros - vetorização

# Definindo a lista de base e expoente
from itertools import repeat
bases = [2, 3, 4]
expoentes = repeat(2, 3)

# Usando map com pow para calcular potências
resultados = map(pow, bases, expoentes)

# Convertendo o resultado para uma lista
resultados_lista = list(resultados)

print(resultados_lista)  # Saída: [8, 9, 256]

