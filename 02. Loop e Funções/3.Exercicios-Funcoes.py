# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


## Exercícios - Métodos e Funções


# Exercício 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20 (a função não recebe parâmetro) 
# e depois faça uma chamada à função para listar os números 

def imprimevalores():
    print(list(range(2,21,2)))

imprimevalores()

def imprimevalores():
    print([x for x in range(2,21,2)])

imprimevalores()


# Exercício 2 - Crie uam função que receba uma string como argumento e retorne a mesma string em letras maiúsculas.
# Faça uma chamada à função, passando como parâmetro uma string

def letra_maiuscula(letra):
    letra = letra.upper()
    return letra

letra_maiuscula("Eduardo Moreira Araujo")


# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e 
# imprima a lista

def lista_add(l1, l2):
    return (l1 + l2)

lista1 = [1,3,4,5]
lista2 = ["Eduardo", "Moreira"]

lista_add(lista1, lista2)


# Exercício 4 - Crie uma função que receba um argumento formal e uma possível lista de elementos. Faça duas chamadas 
# à função, com apenas 1 elemento e na segunda chamada com 4 elementos


def lista_add(valor, *lista):

    # Imprimindo o valor do primeiro argumento
    print("elementos:", valor)

    # Imprimindo os outros argumentos
    for item in lista:
        print("elementos:", item)
    return;

valor1 = 15
lista1 = ["Eduardo", "Moreira", 23, 77.88]

lista_add(valor1)

lista_add(lista1)



# Exercício 5 - Crie uma função anônima e atribua seu retorno a uma variável chamada soma. A expressão vai receber 2 
# números como parâmetro e retornar a soma deles

soma = lambda num1,num2: num1 + num2

soma(5, 34)
soma(-10, 11)


# Exercício 6 - Execute o código abaixo e certifique-se que compreende a diferença entre variável global e local
total = 0

def soma( arg1, arg2 ):
    total = arg1 + arg2; 
    print ("Dentro da função o total é: ", total)
    return total;

soma(10,20);
print ("Fora da função o total é: ", total)



# Exercício 7 - Abaixo você encontra uma lista com temperaturas em graus Celsius
# Crie uma função anônima que converta cada temperatura para Fahrenheit
# Dica: para conseguir realizar este exercício, você deve criar sua função lambda, dentro de uma função 
# (que será estudada no próximo capítulo). Isso permite aplicar sua função a cada elemento da lista
# Como descobrir a fórmula matemática que converte de Celsius para Fahrenheit? Pesquise!!!

Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda x: (9/5) * x + 32, Celsius)

print (list(Fahrenheit))



# Exercício 8 - Crie uma list comprehension que imprima o quadrado dos números de 1 a 10
[x**2 for x in range(1,11)]


# Exercício 9 - Crie uma list comprehension que imprima as palavras com a letra a no nome
lista = ["maça", "coiote", "banana", "terreno", "Python"]

teste1 = [palavra for palavra in lista]
print(teste1)

teste2 = [palavra for palavra in lista if ("a" in palavra)]
print(teste2)


# Exercício 10 - Crie uma list comprehension que imprima os números menores que 5 em um intervalo de 1 a 10

intervalo = range(1,11,1)
teste = [valores for valores in intervalo if (valores < 5)]
print(teste)

# Fim


