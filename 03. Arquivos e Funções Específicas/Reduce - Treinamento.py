# REDUCE

# A função reduce() em Python é uma função da biblioteca functools que aplica uma determinada
# função binária a pares consecutivos de elementos em uma estrutura de dados iterável
# (como uma lista, tupla ou outro objeto iterável), reduzindo-a a um único valor.

from functools import reduce

lista = [40, 10 , 40, 10, 20, 50, 70, 10]

def soma(a,b):
    x = a + b
    return x

print(reduce(soma, lista, 0)) # 0 é o valor inicial

print(reduce(lambda x,y: x+y, lista, 0)) # Uso da função lambda

max_find2 = lambda a,b: a if (a > b) else b # Uso da função lambda com condicionais
print(reduce(max_find2, lista))

