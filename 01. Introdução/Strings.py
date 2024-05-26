#!/usr/bin/env python
# coding: utf-8

# ### Criacao de String

# In[1]:


"Ola Mundo"


# In[2]:


'Ola Mundo'


# In[3]:


"Ola 'Mundo'"


# In[6]:


print("Ola Mundo! \n Vamos aprender Python?")


# ### Indexacao de String

# In[8]:


s = "Data Science Academy"

print(s)


# In[9]:


s[0] # Indexacao comeca por 0


# In[10]:


s[1]


# In[11]:


s[100]


# In[12]:


s[0:]


# In[13]:


s[1:]


# In[14]:


s[:7]


# In[15]:


s[-1]


# In[16]:


s[:-1]


# In[21]:


s[-2:]


# In[18]:


s[1::]


# In[19]:


s[::2]


# In[20]:


s[::-1]


# In[22]:


s[-2:] * 3


# ### Funcoes Built-in de Strings

# In[23]:


s


# In[25]:


# Maiuscula

s.upper()


# In[26]:


# Minuscula

s.lower()


# In[27]:


# Divisao por espacos em branco

s.split()


# In[29]:


# Divisao especificada

s.split('e')


# In[30]:


# Primeira letra Maiuscula

s.capitalize()


# In[34]:


# Contagem de letras especificas

s.count("a")


# In[35]:


# Pergunta se o texto possui uma caracteristica especifica

s.islower()


# In[37]:


# Termina com

s.endswith("y")


# In[41]:


# Termina com

s.startswith("Dat")


# ### Comparacao entre strings

# In[44]:


"Python" == "R"


# In[47]:


"Python" == "Python"

