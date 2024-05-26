#!/usr/bin/env python
# coding: utf-8

# ### Metodos
# 
# Tudo em Python e objeto. E cada objeto tem metodos (funcoes que podem ser executadas) e atributos (propriedades e caracteristicas).

# In[ ]:


# Objeto do tipo Lista

lista = []

type(lista)


# In[ ]:


# Metodos - aplicando funcoes

print(len(lista))

lista.append(1)

print(len(lista))


# In[ ]:


# Funcoes interessantes

help(lista.count)

dir(lista)

