# NumPy: Cálculo matricial

import numpy as np

# Matriz identidade 5 x 5
arr5 = np.eye(5)
print(arr5)
print("\n")

# Matriz diagonal
arr6 = np.diag(np.array([1, 2, 3, 4]))
print(arr6)
print("\n")


# Criando matriz
arr9 = np.array( [ [1,2,3] , [4,5,6] ] )
print(arr9)
print("\n")

# Transposta por Array
print(arr9.transpose())
print("\n")

# Traço por Array
print(arr9.trace())
print("\n")

# Criação de Matriz por Matrix - A função matrix cria uma matriz a partir de uma lista de listas

lista = [[13,81,22], [0, 34, 59], [21, 48, 94]]

arr11 = np.matrix(lista)
print(arr11)
print("\n")

m1 = np.matrix(lista)
m2 = np.matrix(lista) + 5

# Indexação da matriz
print(arr11[0:2,2])
print("\n")

# Soma e Subtração
print(np.add(m1,m2))
print(m1 + m2)
print(np.subtract(m1,m2))
print(m1 - m2)
print("\n")

# Multiplicação por escalar
print(np.dot(m1,3))
print(m1 * 3)
print("\n")

# Matriz vezes a própria matriz ou multiplicação matricial
print(m1 ** 3)
print(m1 * m1 * m1) # não usar, elemento a elemento
print(m1 @ m1 @ m1) # usar, cálculo matricial
print(m1 ** 2)
print(m1 @ m2)
print(m1 * m2)
print(np.dot(m1,m2))
print("\n")

# Matriz Transposta
print(m1.transpose())
print("\n")

# Traço Matriz
print(m1.trace())
print("\n")

# Matriz raiz quadrada
print(np.power(m1, 1/2))
print("\n")

# Matriz inversa
print(np.linalg.inv(m1))
print("\n")

# Determinante Matriz
print(np.linalg.det(m1))
print("\n")

# Pegar a diagonal da matriz
diagonal = np.diag(m1)
print(diagonal)
print("\n")


# Calcular autovalores e autovetores
matriz = np.array([[1, 2],[3, 4]])
autovalores, autovetores = np.linalg.eig(matriz)

print("Autovalores:")
print(autovalores)

print("\nAutovetores:")
print(autovetores)
