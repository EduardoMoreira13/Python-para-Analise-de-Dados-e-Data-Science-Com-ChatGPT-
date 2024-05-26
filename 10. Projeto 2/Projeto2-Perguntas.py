# Projeto 2

# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt


df_dsa = pd.read_csv('dados/dataset.csv')

# Shape
df_dsa.shape


# In[5]:


# Amostra dos dados
df_dsa.head()


# In[6]:


# Amostra dos dados
df_dsa.tail()


# ## Análise Exploratória

# In[7]:


# Colunas do conjunto de dados
df_dsa.columns


# In[8]:


# Verificando o tipo de dado de cada coluna
df_dsa.dtypes


# In[9]:


# Resumo estatístico da coluna com o valor de venda
df_dsa['Valor_Venda'].describe()


# In[10]:


# Verificando se há registros duplicados
df_dsa[df_dsa.duplicated()]


# In[11]:


# Verificando de há valores ausentes
df_dsa.isnull().sum()


# In[12]:


df_dsa.head()


# ## Pergunta de Negócio 1:
# 
# ### Qual Cidade com Maior Valor de Venda de Produtos da Categoria 'Office Supplies'?

# In[ ]:





# ## Pergunta de Negócio 2:
# 
# ### Qual o Total de Vendas Por Data do Pedido?
# 
# Demonstre o resultado através de um gráfico de barras.

# In[ ]:





# ## Pergunta de Negócio 3:
# 
# ### Qual o Total de Vendas por Estado?
# 
# Demonstre o resultado através de um gráfico de barras.

# In[ ]:





# ## Pergunta de Negócio 4:
# 
# ### Quais São as 10 Cidades com Maior Total de Vendas?
# 
# Demonstre o resultado através de um gráfico de barras.

# In[ ]:





# ## Pergunta de Negócio 5:
# 
# ### Qual Segmento Teve o Maior Total de Vendas?
# 
# Demonstre o resultado através de um gráfico de pizza.

# In[ ]:





# ## Pergunta de Negócio 6 (Desafio Nível Baby):
# 
# ### Qual o Total de Vendas Por Segmento e Por Ano?

# In[ ]:





# ## Pergunta de Negócio 7 (Desafio Nível Júnior):
# 
# Os gestores da empresa estão considerando conceder diferentes faixas de descontos e gostariam de fazer uma simulação com base na regra abaixo:
# 
# - Se o Valor_Venda for maior que 1000 recebe 15% de desconto.
# - Se o Valor_Venda for menor que 1000 recebe 10% de desconto.
# 
# ### Quantas Vendas Receberiam 15% de Desconto?

# In[ ]:





# ## Pergunta de Negócio 8 (Desafio Nível Master):
# 
# ### Considere Que a Empresa Decida Conceder o Desconto de 15% do Item Anterior. Qual Seria a Média do Valor de Venda Antes e Depois do Desconto?

# In[ ]:





# ## Pergunta de Negócio 9 (Desafio Nível Master Ninja):
# 
# ### Qual o Média de Vendas Por Segmento, Por Ano e Por Mês?
# 
# Demonstre o resultado através de gráfico de linha.

# In[ ]:





# Pergunta de Negócio 10 (Desafio Nível Master Ninja das Galáxias):

# Qual o Total de Vendas Por Categoria e SubCategoria, Considerando Somente as Top 12 SubCategorias?


# Demonstre tudo através de um único gráfico.

# In[ ]:





# # Fim
