# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# ## Exercícios - Loops e Condiconais


# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou 
# igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"

print("Dias da semana: \n", "\n1 - Domingo", "\n2 - Segunda-Feira", 
      "\n3 - Terca-Feira", "\n4 - Quarta-Feira", "\n5 - Quinta-Feira", "\n6 - Sexta-Feira", "\n7 - Sabado\n")

dia = int(input("Indique o dia da semana pelo seu respectivo numero indicado acima:"))

print("")
if dia in [1,7]:
    print("Hoje é dia de descanso!")
else:
    print("Você precisa trabalhar!")



# Exercício 2 - Crie uma lista de 5 frutas e verifique se a fruta 'Morango' faz parte da lista


lista1 = ["Banana", "Melao", "Abacaxi", "Uva", "Melancia"]
lista2 = ["Banana", "Melao", "Abacaxi", "Morango", "Uva"]

if "Morango" in lista1:
    print("A fruta Morango faz parte da lista 1")
else:
    print("A fruta Morango nao faz parte da lista 1")


if "Morango" in lista2:
    print("A fruta Morango faz parte da lista 2")
else:
    print("A fruta Morango nao faz parte da lista 2")



# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma 
# lista

tupla = (10,20,30,40)
valor = 2
lista = []

for numero in tupla:
    numero *= valor
    lista.append(numero)
    
print(lista)


# Exercício 4 - Crie uma sequência de números pares entre 100 e 150 e imprima na tela

valores = list(range(100, 151, 2))
print(valores)

for i in range(100, 151, 2):
    print(i)

for i in range(100, 151, 1):
    if i % 2 == 0:
        print(i)


# Exercício 5 - Crie uma variável chamada temperatura e atribua o valor 40. Enquanto temperatura for maior que 35, 
# imprima as temperaturas na tela

temperatura = 40

while temperatura > 35:
    print(temperatura)
    temperatura -= 1


# Exercício 6 - Crie uma variável chamada contador = 0. Enquanto counter for menor que 100, imprima os valores na tela,
# mas quando for encontrado o valor 23, interrompa a execução do programa

contador = 0

while contador < 100:
    if contador == 23:
        print(contador)
        break
    print(contador)
    contador += 1


# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20, 
# adicione à lista, apenas os valores pares e imprima a lista
  
numeros = list()
i = 4

while (i <= 20):
    numeros.append(i)
    i = i+2
print(numeros)


# Exercício 8 - Transforme o resultado desta função range em uma lista: range(5, 45, 2)
nums = range(5, 45, 2)

nums = list(nums)
print(nums)
type(nums)


nums = range(5, 45, 2)
lista = []

for val in nums:
    lista.append(val)
print(lista)


# Exercício 9 - Faça a correção dos erros no código abaixo e execute o programa. Dica: são 3 erros.
temperatura = float(input('Qual a temperatura? '))
if temperatura > 30:
    print('Vista roupas leves.')
else:
    print('Busque seus casacos.')


# Exercício 10 - Faça um programa que conte quantas vezes a letra "r" aparece na frase abaixo. Use um placeholder na
# sua instrução de impressão
# “A gratidão é a virtude das almas nobres. O quão feliz é uma pessoa depende da profundidade de sua gratidão.”

frase = "A gratidão é a virtude das almas nobres. O quão feliz é uma pessoa depende da profundidade de sua gratidão." 

contagem = 0

for letra in frase:
    if letra == "r" or letra == "R":
        contagem += 1

print("A quantidade de vezes que a letra r aparece na frase e igual a %r" %(contagem))


# Fim