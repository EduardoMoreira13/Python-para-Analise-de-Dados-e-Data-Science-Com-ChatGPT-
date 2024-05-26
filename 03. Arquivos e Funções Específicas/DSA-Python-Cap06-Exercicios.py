# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# ## Exercícios

# Exercício 1 - Crie uma lista de 3 elementos e calcule a terceira potência de cada elemento.

def potencia(x):
    return pow(x,3)

lista = [4,2,5]
calculo = list(map(potencia, lista))
calculo


# Exercício 2 - Reescreva o código abaixo, usando a função map(). O resultado final deve ser o mesmo!
palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil.'.split()
resultado = [[w.upper(), w.lower(), len(w)] for w in palavras]
for i in resultado:
    print (i)
    
palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil.'.split()

def string(x):
    return [x.upper(), x.lower(), len(x)]

resultado = list(map(string, palavras))
print(" \n",resultado)

print(" \n")
resultado = map(lambda w: [w.upper(), w.lower(), len(w)], palavras)
for i in resultado:
    print (i)


# In[ ]:


# Solução


# In[23]:


# Exercício 3 - Calcule a matriz transposta da matriz abaixo.
# Caso não saiba o que é matriz transposta, visite este link: https://pt.wikipedia.org/wiki/Matriz_transposta
# Matriz transposta é um conceito fundamental na construção de redes neurais artificiais, base de sistemas de IA.
matrix = [[1, 2],[3,4],[5,6],[7,8]]
print(matrix)

transpose = [[row[i] for row in matrix] for i in range(2)]
print(transpose)


# In[34]:


# Exercício 4 - Crie duas funções, uma para elevar um número ao quadrado e outra para elevar ao cubo. 
# Aplique as duas funções aos elementos da lista abaixo. 
# Obs: as duas funções devem ser aplicadas simultaneamente.
lista = [0, 1, 2, 3, 4]

def quadrado(x):
    return pow(x,2)

def cubo(x):
    return pow(x,3)

funcoes = [quadrado, cubo]

for i in lista:
    valor = map(lambda x: x(i), funcoes)
    print(list((valor)))


# In[71]:


# Exercício 5 - Abaixo você encontra duas listas. Faça com que cada elemento da listaA seja elevado 
# ao elemento correspondente na listaB.

from functools import reduce

listaA = [2, 3, 4]
listaB = [10, 11, 12]

def mult(a,b):
    x = a ** b
    return x

calculo = list(zip(listaA, listaB))
print(calculo)

for valor in range(0,3,1):
    print(" \n Resultado: ", float(reduce(mult, calculo[valor])))

print(" \n ---------------- \n")
    
for i in range(0,3,1):
    valor = calculo[i][0] ** calculo[i][1]
    print(" \n Resultado: ", float((valor)))
    
print(" \n ---------------- \n")


# Usando a funcao map
valor = list(map(lambda x: x[0] ** x[1], calculo))
print(valor)

listaA = [2, 3, 4]
listaB = [10, 11, 12]
list(map(pow, listaA, listaB))


# In[81]:


# Exercício 6 - Considerando o range de valores abaixo, use a função filter() para retornar 
# apenas os valores negativos.
intervalo = list(range(-5, 5))
print(intervalo)

list(filter(lambda x: x < 0, intervalo))


# In[84]:


# Exercício 7 - Usando a função filter(), encontre os valores que são comuns às duas listas abaixo.
a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]

list(filter(lambda x: x in b, a))


# In[103]:


# Exercício 8 - Considere os dois dicionários abaixo. 
# Crie um terceiro dicionário com as chaves do dicionário 1 e os valores do dicionário 2.
dict1 = {'a':1,'b':2}
dict2 = {'c':4,'d':5}

def trocaValores(d1, d2):
    dicTemp = {}
    
    for d1key, d2val in zip(d1,d2.values()):
        dicTemp[d1key] = d2val
    
    return dicTemp

dict3 = trocaValores(dict1, dict2)
print(dict3)


# In[104]:


# Exercício 9 - Considere a lista abaixo e retorne apenas os elementos cujo índice for maior que 5.
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for indice, valor in enumerate(lista):
    if indice < 5:
        continue
    else:
        print(valor)


# In[108]:


# Exercício 10 - Crie um regex em Python para extrair a palavra que aparece depois das palavras 
# Data e Science na frase: 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil.'
import re
texto = 'A Data Science Academy oferece os melhores cursos de análise de dados do Brasil.'

resultado = re.findall(r'Data Science (\w+)', texto)
print("A palavra após 'Data Science' é:", resultado[0])


# # Fim

# ### Obrigado
# 
# ### Visite o Blog da Data Science Academy - <a href="http://blog.dsacademy.com.br">Blog DSA</a>
