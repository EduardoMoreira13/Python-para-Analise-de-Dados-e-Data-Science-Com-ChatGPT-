#!/usr/bin/env python
# coding: utf-8

# # <font color='blue'>Data Science Academy</font>
# 
# ## <font color='blue'>Fundamentos de Linguagem Python Para Análise de Dados e Data Science</font>
# 
# ## <font color='blue'>Capítulo 6 - Pacotes e Módulos</font>

# In[1]:


# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# ## Pacotes e Módulos
# 
# Em Python, um módulo é um arquivo (script) que contém código Python e pode ser importado em outros arquivos Python. Ele é usado para compartilhar funções, classes e variáveis entre arquivos.
# 
# Já um pacote é uma coleção de módulos organizados em uma estrutura de diretórios. Ele permite a divisão de um aplicativo em múltiplos módulos, o que facilita a manutenção e o desenvolvimento.
# 
# Visite o PyPi, repositório de pacotes da Linguagem Python: https://pypi.org/

# In[2]:


# Importando um pacote Python
import numpy


# In[3]:


# Verificando todos os métodos e atributos disponíveis no pacote
dir(numpy)


# In[4]:


# Usando um dos métodos do pacote Numpy
numpy.sqrt(25)


# In[5]:


# Importando apenas um dos métodos do pacote Numpy
from numpy import sqrt


# In[6]:


# Usando o método
sqrt(9)


# In[7]:


# Imprimindo todos os métodos do pacote numpy
print(dir(numpy))


# In[8]:


# Help do método sqrt do pacote Numpy
help(sqrt)


# In[9]:


import random


# In[10]:


random.choice(['Abacate', 'Banana', 'Laranja'])


# In[11]:


random.sample(range(100), 10)


# In[12]:


import statistics


# In[13]:


dados = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]


# In[14]:


statistics.mean(dados)


# In[15]:


statistics.median(dados)


# In[16]:


import os


# In[17]:


os.getcwd()


# In[18]:


print(dir(os))


# > Podemos trabalhar com módulos dos pacotes (quando disponíveis).

# In[19]:


# Importando o módulo request do pacote urllib, usado para trazer url's 
# para dentro do nosso ambiente Python
import urllib.request


# http://python.org

# In[20]:


# Variável resposta armazena o objeto de conexão à url passada como 
# parâmetro
resposta = urllib.request.urlopen('http://python.org')


# In[21]:


# Objeto resposta
print(resposta)


# In[22]:


# Chamando o método read() do objeto resposta e armazenando o código 
# html na variável html
html = resposta.read()


# In[23]:


# Imprimindo html
print(html)


# # Fim

# ### Obrigado
# 
# ### Visite o Blog da Data Science Academy - <a href="http://blog.dsacademy.com.br">Blog DSA</a>
