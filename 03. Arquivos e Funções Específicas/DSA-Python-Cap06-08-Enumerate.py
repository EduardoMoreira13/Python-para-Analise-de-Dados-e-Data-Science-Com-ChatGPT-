#!/usr/bin/env python
# coding: utf-8

# # <font color='blue'>Data Science Academy</font>
# 
# ## <font color='blue'>Fundamentos de Linguagem Python Para Análise de Dados e Data Science</font>
# 
# ## <font color='blue'>Capítulo 6 - Função Enumerate</font>

# In[1]:


# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# ## Função Enumerate
# 
# A função enumerate() em Python é uma função que permite iterar sobre uma estrutura de dados (como uma lista, tupla ou outro objeto iterável). A função enumerate() retorna um objeto enumerado, que pode ser usado em loops para percorrer a estrutura de dados e acessar o contador e o valor de cada elemento.

# In[2]:


# Criando uma lista
seq = ['a','b','c']


# In[3]:


enumerate(seq)


# In[4]:


list(enumerate(seq))


# In[5]:


# Imprimindo os valores de uma lista com a função enumerate() e seus respectivos índices
for indice, valor in enumerate(seq):
    print (indice, valor)


# In[6]:


for indice, valor in enumerate(seq):
    if indice >= 2:
        break
    else:
        print (valor)


# In[7]:


lista = ['Marketing', 'Tecnologia', 'Business']


# In[8]:


for i, item in enumerate(lista):
    print(i, item)


# In[9]:


for i, item in enumerate('Data Science Academy'):
    print(i, item)


# In[10]:


for i, item in enumerate(range(10)):
    print(i, item)


# # FIM

# ### Obrigado
# 
# ### Visite o Blog da Data Science Academy - <a href="http://blog.dsacademy.com.br">Blog DSA</a>
