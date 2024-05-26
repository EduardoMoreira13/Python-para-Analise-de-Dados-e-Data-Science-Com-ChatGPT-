#!/usr/bin/env python
# coding: utf-8

# ### Funcao Range

# In[2]:


# Imprimindo numeros de 1 a 10
for i in range(1,11,1):
    print(i)
    

# Guardando valores dentro de uma lista
numeros = []

for i in range(1,11,1):
    numeros.append(i)
print(numeros)


# In[3]:


# Tamanho de lista pela funcao range

lista = ["Eduardo", "Ana", "Moreira", "Araujo"]
lista_tam = len(lista)

for i in range(0, lista_tam, 1):
    print(lista[i])

