# NumPy: pacote para trabalhar com dados em forma de matrizes e realizar cálculos otimizados


# ARRAY: Estrutura multidimensional de armazenamento de dados

import numpy as dsa

arr1 = dsa.array([10, 21, 32, 43, 48, 15, 76, 57, 89])

print(arr1)
print(arr1.shape) # dimensões


# ACESSANDO E FATIANDO UM ARRAY

print(arr1[4])
print(arr1[1:4])
indices = [1, 2, 5, 6]
print(arr1[indices])

mask = (arr1 % 2 == 0) # A aplicação de uma função se torna vetorizada igual ao R
print(arr1[mask])


# ALTERANDO UM ELEMENTO DO ARRAY

print(arr1)
arr1[0] = 100
print(arr1)



