#!/usr/bin/env python
# coding: utf-8

# ### List Comprehension
# 
# Loop dentro de uma lista (expressao for item in iterable if condicao == True)

# In[1]:


# Imprime  os numeros ate 10 - retorne x, para cada valor de x no intervalo 0 a 10 

[x for x in range(10)]



# In[3]:


# Imprime os numeros ate 10 com condicionais

lista_numeros = [x for x in range(10) if x < 5 and x > 0]
lista_numeros


# ### Dict Comprehension

# In[8]:


# Dict Comprehension - dicionarios

dict_alunos = {"Bob":65, "Edu":15, "Ana":22}

dict_alunos_status = {k:("Aprovado" if v > 70 else "Reprovado") for (k,v) in dict_alunos.items()}
dict_alunos_status


# In[ ]:




