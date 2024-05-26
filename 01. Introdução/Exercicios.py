# Versão da Linguagem Python

from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.

numeros = [1,2,3,4,5,6,7,8,9,10]

print(numeros)

# Gerar uma sequência de 1 a 10 e convertê-la em uma lista
numeros = list(range(1, 11))

# Imprimir a lista
print(numeros)

# Usando compreensão de lista para gerar a sequência de 1 a 10
sequencia = [i for i in range(1, 11)]

# Imprimir a lista
print(sequencia)




# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela

lista = ["Eduardo", 10, 10.55, [14, "Ana"], (15, "Maria", 12.3)]

print(lista)



# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string

string1 = "Eduardo "
string2 = "Moreira"
string = string1 + string2

print(string)



# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do 
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla

tupla = (1, 2, 2, 3, 4, 4, 4, 5)
tupla.count(4)



# Exercício 5 - Crie um dicionário vazio e imprima na tela

dicionario = {}
print(dicionario)



# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela

dicionario = {"Eduardo":15, "Fernando":11, "Cris":43}
print(dicionario)



# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela
dicionario["Ana"] = 22
print(dicionario)

# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. 
# Um dos valores deve ser uma lista de 2 elementos numéricos. 
# Imprima o dicionário na tela.

dicionario = {"Eduardo":15, "Fernando":11, "Cris":[43,"Ok"]}

print(dicionario)

dicionario["Marcelo"] = [28, "Ok"]

print(dicionario)



# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista.

lista = ["Eduardo", (20, "Ok"), {"chave1":22,"chave2":23}, 20.678]
lista


# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
frase = 'Cientista de Dados é o profissional mais sexy do século XXI'

print(frase[1-1])
print(frase[18-1])

print(frase[1-1] + " , " + frase[18-1])

print(frase[0:18]) # 18 e exclusivo (0,17) da 1 a 18 posicao


