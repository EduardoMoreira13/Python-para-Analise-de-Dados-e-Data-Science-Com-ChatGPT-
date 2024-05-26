#!/usr/bin/env python
# coding: utf-8

# # <font color='blue'>Data Science Academy</font>
# 
# ## <font color='blue'>Fundamentos de Linguagem Python Para Análise de Dados e Data Science</font>
# 
# ## <font color='blue'>Capítulo 6 - Função Zip</font>

# In[1]:


# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# ## Função Zip
# 
# A função zip() em Python é uma função que agrupa elementos de múltiplas estruturas de dados iteráveis (como listas, tuplas ou outros objetos iteráveis) juntos em pares. A função zip() retorna um objeto zip, que pode ser convertido em outra estrutura de dados, como uma lista ou dicionário, se necessário.

# In[2]:


# Criando duas listas
x = [1,2,3]
y = [4,5,6]


# In[3]:


# Unindo as listas. Em Python3 retorna um iterator
zip(x, y)


# In[4]:


# Perceba que zip retorna tuplas. Neste caso, uma lista de tuplas
list(zip(x,y))


# In[5]:


# Atenção quando as sequências tiverem número diferente de elementos
list(zip('ABCD', 'xy'))


# In[6]:


# Criando duas listas
a = [1,2,3]
b = [4,5,6,7,8]


# In[7]:


list(zip(a,b)) 


# In[8]:


# Criando 2 dicionários
d1 = {'a':1,'b':2}
d2 = {'c':4,'d':5}


# In[9]:


# Zip vai unir as chaves
list(zip(d1,d2))


# In[10]:


# Zip pode unir os valores (itens)
list(zip(d1, d2.values()))


# In[11]:


# Criando uma função para trocar valores entre 2 dicionários
def trocaValores(d1, d2):
    
    dicTemp = {}
    
    for d1key, d2val in zip(d1, d2.values()):
        dicTemp[d1key] = d2val
    
    return dicTemp


# In[12]:


trocaValores(d1, d2)


# # FIM

# ### Obrigado
# 
# ### Visite o Blog da Data Science Academy - <a href="http://blog.dsacademy.com.br">Blog DSA</a>
