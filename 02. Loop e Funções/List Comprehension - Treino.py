### List Comprehension

# Criação de uma iteração (baseado no for) e armazenamento dos resultados em uma lista


# Imprime  os numeros ate 10 - retorne x, para cada valor de x no intervalo 0 a 10

lista1 = [1,2,3,4,5,6,7,8,9,10]
lista2 = []
for valor in lista1:
    lista2.append(valor)

print(lista2)
del lista2

lista1 = [1,2,3,4,5,6,7,8,9,10]
lista2 = [valor for valor in lista1]
lista3 = [valor for valor in range(1,11,1)]

print(lista2)
print(lista3)


# Uso de Condicionais para filtrar os resultados

lista1 = [1,2,3,4,5,6,7,8,9,10]
lista2 = []
for valor in lista1:
    if valor >= 5:
        lista2.append(valor)

print(lista2)

lista1 = [1,2,3,4,5,6,7,8,9,10]
lista2 = [valor for valor in lista1 if valor >= 3]

print(lista2)

lista1 = [1,2,3,4,5,6,7,8,9,10]
lista2 = [valor for valor in lista1 if (valor <= 3 or valor >= 6)]

print(lista2)


# Uso de Condicionais para apresentar os resultados

lista1 = [1,2,3,4,5,6,7,8,9,10]
lista2 = [valor*3 if valor < 6 else valor for valor in lista1]

print(lista2)

lista1 = [1,2,3,4,5,6,7,8,9,10]
lista2 = [valor*2 if valor < 6 else valor for valor in lista1 if valor >= 3]

print(lista2)

lista1 = [1,2,3,4,5,6,7,8,9,10]
lista2 = ["Reprovado" if valor < 6 else "Aprovado" for valor in lista1]

print(lista2)

# Uso de calculos e funções dentro do processo

def potencia(val, pot):
    return val**pot


lista2 = [valor**2 for valor in range(1,101,1) if valor < 20 and valor % 2 == 0]

print(lista2)
del lista2

lista2 = [potencia(valor, 2) for valor in range(1,101,1) if (valor < 20 and valor % 2 == 0)]

print(lista2)


# Uso de dois loops - produto cartesiano

lista1 = []

for i in range(1,11,1):
    for j in range(1,6,1):
        lista1.append([i,j])

print(lista1)

lista1 =  [[i,j] for i in range(1,11,1) for j in range(1,6,1)]

print(lista1)


# Uso conjunto das possibilidades

lista1 = [[i,j] if i <= 5 else [i*3,j*3] for i in range(1,11,1) for j in range(1,6,1)]
lista2 = [[i,j] if i <= 3 else [i*3,j*3] for i in range(1,11,1) for j in range(1,6,1) if j == i]
lista3 = [[i,j] if i <= 3 else [i*3,j*3]
          for i in range(1,11,1)
          for j in range(1,6,1) if j == i]
lista4 =  ["OK" if i == 4 else [i,j] for i in range(1,11,1) if i > 1 for j in range(1,6,1) if j == i]

print(lista1)
print(lista2)
print(lista3)
print(lista4)


# Mais de um valor retornado

lista1 = [11,22,30,41,50,66,72,85,92,100]
lista2 = []

for k,v in enumerate(lista1):
    print(k,v)
    lista2.append([k,v])

print(lista2)

lista2 = [[k,v] for k,v in enumerate(lista1)]
print(lista2)

lista2 = [f"{k}:{v}" for k,v in enumerate(lista1)]
print(lista2)

lista2 = [[k,"OK"] if v <= 50 else [k,"Falha"] for k,v in enumerate(lista1)]
print(lista2)


# Uso de strings

frase = "Eduardo Moreira Araújo"
numero = 2

nova_string = [
    frase[indice:indice + numero]
    for indice in range(0, len(frase), numero)
]

print(frase)
print(nova_string)