#!/usr/bin/env python
# coding: utf-8

# # <font color='blue'>Data Science Academy</font>
# 
# ## <font color='blue'>Fundamentos de Linguagem Python Para Análise de Dados e Data Science</font>
# 
# ## <font color='blue'>Capítulo 6 - Função Filter</font>

# In[ ]:


# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# ## Função Filter
# 
# A função filter() em Python é uma função que filtra elementos de uma estrutura de dados iterável (como uma lista, tupla ou outro objeto iterável) com base em uma determinada condição. A função filter() retorna um objeto filtro, que pode ser convertido em outra estrutura de dados, como uma lista, se necessário.

# In[1]:


# Criando uma função
def verificaPar(num):
    if num % 2 == 0:
        return True
    else:
        return False


# In[2]:


# Chamando a função e passando um número como parâmetro. Retornará 
# Falso de for ímpar e True se for par.
verificaPar(35)


# In[3]:


# Falso de for ímpar e True se for par.
verificaPar(10)


# In[4]:


lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]


# In[5]:


lista


# In[6]:


# A função filter() retorna um iterator
filter(verificaPar, lista)


# In[7]:


list(filter(verificaPar, lista))


# In[8]:


list(filter(lambda x: x%2==0, lista))


# In[9]:


list(filter(lambda num: num > 8, lista))


# # Fim

# ### Obrigado
# 
# ### Visite o Blog da Data Science Academy - <a href="http://blog.dsacademy.com.br">Blog DSA</a>
