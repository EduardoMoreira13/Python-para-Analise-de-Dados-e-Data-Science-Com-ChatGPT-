#!/usr/bin/env python
# coding: utf-8

# # <font color='blue'>Data Science Academy</font>
# 
# ## <font color='blue'>Fundamentos de Linguagem Python Para Análise de Dados e Data Science</font>
# 
# ## <font color='blue'>Capítulo 6 - Função Reduce</font>

# In[1]:


# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# ## Função Reduce
# 
# A função reduce() em Python é uma função da biblioteca functools que aplica uma determinada função binária a pares consecutivos de elementos em uma estrutura de dados iterável (como uma lista, tupla ou outro objeto iterável), reduzindo-a a um único valor.

# In[2]:


# Importando a função reduce do módulo functools
from functools import reduce


# In[3]:


from IPython.display import Image
Image('arquivos/reduce.png')


# In[4]:


# Criando uma lista
lista = [47, 11 , 42, 13]


# In[5]:


lista


# In[6]:


# Função 
def soma(a,b):
    x = a + b
    return x


# In[7]:


# Usando reduce com uma função e uma lista. A função vai retornar o valor máximo
reduce(soma, lista)


# In[8]:


# Criando uma lista
lst = [47, 11, 42, 13]


# In[9]:


# Usando a função reduce() com lambda
reduce(lambda x,y: x+y, lst)


# In[10]:


# Podemos atribuir a expressão lambda a uma variável
max_find2 = lambda a,b: a if (a > b) else b


# In[11]:


type(max_find2)


# In[12]:


# Reduzindo a lista até o valor máximo, através da função criada com a expressão lambda
reduce(max_find2, lst)


# # Fim

# ### Obrigado
# 
# ### Visite o Blog da Data Science Academy - <a href="http://blog.dsacademy.com.br">Blog DSA</a>
