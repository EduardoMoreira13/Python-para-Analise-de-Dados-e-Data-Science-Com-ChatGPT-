import numpy as np

# A função array() cria um array NumPy
arr2 = np.array([10, 12, 30, 24, 5])
print(arr2)


# Usando Métodos ou Funções do array NumPy

print("Soma acumulada: ", arr2.cumsum(), np.cumsum(arr2))
print("Produto acumulado: ", arr2.cumprod(), np.cumprod(arr2))
print("Media: ", arr2.mean(), np.mean(arr2))
print("Soma: ", arr2.sum(), np.sum(arr2))
print("Maximo: ", arr2.max(), np.max(arr2))
print("Minimo: ", arr2.min(), np.min(arr2))
print("Desv. Padrao: ", arr2.std(), np.std(arr2))
print("Variancia: ", arr2.var(), np.var(arr2))
print("Arredondamento: ", arr2.round(decimals= 3))
print("Ordenação: ", arr2.sort())

# Usando Funções de outros pacotes em um array NumPy - algumas não funcionam para array

import statistics as stat

print("Media: ", stat.mean(arr2))
print("Soma: ", sum(arr2))
print("Maximo: ", max(arr2))
print("Minimo: ", min(arr2))
print("Ordenação: ", sorted(arr2))


# Outras funções chamando o pacote diretamente

arr3 = np.arange(0, 50, 5)
print(arr3)

arr4 = np.zeros(10)
print(arr4)

# Array de valores booleanos
arr7 = np.array([True, False, False, True])
print(arr7)

# Array de strings
arr8 = np.array(['Linguagem Python', 'Linguagem R', 'Linguagem Julia'])
print(arr8)

# A função linspace() do NumPy é usada para criar uma sequência de números igualmente espaçados dentro de um intervalo especificado.
# Essa função é amplamente utilizada em programação científica e matemática para gerar arrays de números para diversos fins, como gráficos,
# cálculos e simulações.

# O método linspace (linearly spaced vector) retorna um número de valores igualmente distribuídos no intervalo especificado.

print(np.linspace(0, 10))
print(np.linspace(1, 10, 10))


# A função logspace() do NumPy é usada para criar uma sequência de números igualmente espaçados em escala logarítmica
# dentro de um intervalo especificado. Essa função é amplamente utilizada em programação científica e matemática para
# gerar arrays de números para diversos fins, como gráficos, cálculos e simulações.

print(np.logspace(0, 5, 10))