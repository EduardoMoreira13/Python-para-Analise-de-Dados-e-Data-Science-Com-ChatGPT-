#!/usr/bin/env python
# coding: utf-8

# # <font color='blue'>Data Science Academy</font>
# 
# ## <font color='blue'>Fundamentos de Linguagem Python Para Análise de Dados e Data Science</font>
# 
# ## <font color='blue'>Capítulo 6 - Manipulação de Arquivos - Parte 1</font>

# In[1]:


# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# ## Manipulação de Arquivos

# ### Lendo Arquivos

# In[2]:


# Abrindo o arquivo para leitura
arq1 = open("arquivos/arquivo1.txt", "r") # r = read


# In[3]:


type(arq1)


# In[4]:


# Lendo o arquivo
print(arq1.read())


# In[5]:


# Contar o número de caracteres
print(arq1.tell())


# In[6]:


# Lendo o arquivo
print(arq1.read())


# In[7]:


# Retornar para o iníco do arquivo
print(arq1.seek(0,0))


# In[8]:


# Lendo os primeiros 23 caracteres
print(arq1.read(23))


# In[9]:


# Lendo o arquivo
print(arq1.read())


# ### Gravando Arquivos

# In[10]:


# Abrindo arquivo para gravação
arq2 = open("arquivos/arquivo2.txt", "w") # w = write (sobreescrever)


# In[11]:


# Como abrimos o arquivo apenas para gravação, não podemos usar comandos de leitura.
print(arq2.read())


# In[12]:


# Gravando arquivo
arq2.write("Aprendendo a programar em Python.")


# In[13]:


arq2.close()


# In[14]:


# Lendo arquivo gravado
arq2 = open("arquivos/arquivo2.txt", "r")


# In[15]:


print(arq2.read())


# In[16]:


# Acrescentando conteúdo
arq2 = open("arquivos/arquivo2.txt", "a") # a = append (adicionar)


# In[17]:


arq2.write(" E a metodologia de ensino da Data Science Academy facilita o aprendizado.")


# In[18]:


arq2.close()


# In[19]:


arq2 = open("arquivos/arquivo2.txt", "r")


# In[20]:


print(arq2.read())


# In[21]:


# Retornando ao início do arquivo para leitura
arq2.seek(0,0)


# In[22]:


print(arq2.read())


# ### Abrindo Dataset em Linha Única

# Este arquivo abaixo foi obtido no site de dados abertos do governo da cidade de Chicago, nos EUA: 
# 
# https://data.cityofchicago.org/

# In[5]:


f = open('arquivos/salarios.csv', 'r')


# In[6]:


data = f.read()


# In[7]:


rows = data.split('\n')


# In[26]:


print(rows)


# ### Dividindo Um Arquivo em Colunas

# In[27]:


f = open('arquivos/salarios.csv', 'r')


# In[28]:


data = f.read()


# In[29]:


rows = data.split('\n')


# In[30]:


full_data = []


# In[31]:


type(rows)


# In[32]:


for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)


# In[33]:


print(full_data)


# ### Contando as Linhas de Um arquivo

# In[34]:


f = open('arquivos/salarios.csv', 'r')


# In[35]:


data = f.read()


# In[36]:


rows = data.split('\n')


# In[37]:


full_data = []


# In[38]:


for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)


# In[39]:


count = 0
for row in full_data:
    count += 1   # Equivalente a: count = count + 1


# In[40]:


print(count)


# ### Contando o Número de Colunas de Um Arquivo

# In[41]:


f = open('arquivos/salarios.csv', 'r')
data = f.read()
rows = data.split('\n')
full_data = []


# In[42]:


for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)
    first_row = full_data[0]
count = 0


# In[43]:


for column in first_row:
    count = count + 1
    
# Outra solução possível
# for column in full_data[0]:
#     count = count + 1


# In[44]:


print(count)


# ### Gravando Arquivo Pelo Jupyter Notebook

# In[45]:


get_ipython().run_cell_magic('writefile', 'arquivos/arquivo3.txt', 'Este arquivo foi gerado pelo Jupyter Notebook.\nPodemos gerar quantas linhas quisermos e o Jupyter grava no arquivo final.\n')


# In[46]:


arq3 = open("arquivos/arquivo3.txt", 'r')


# In[47]:


arq3.read()


# In[48]:


# Estamos no final do arquivo e não há mais nada para ler
arq3.read()


# In[49]:


# Retornando ao início do arquivo
arq3.seek(0)


# In[50]:


arq3.seek(0)
arq3.readlines()


# In[51]:


# Podemos usar um loop for para ler o arquivo
for line in open('arquivos/arquivo3.txt'):
    print(line)


# ## Importando um Dataset com Pandas

# In[52]:


import pandas as pd


# In[53]:


pd.__version__


# In[54]:


arquivo = "arquivos/salarios.csv"


# In[55]:


df = pd.read_csv(arquivo)


# In[56]:


df.head()


# In[57]:


df['Position Title'].value_counts()


# # Fim

# ### Obrigado
# 
# ### Visite o Blog da Data Science Academy - <a href="http://blog.dsacademy.com.br">Blog DSA</a>
