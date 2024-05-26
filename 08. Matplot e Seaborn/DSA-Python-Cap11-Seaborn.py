#!/usr/bin/env python
# coding: utf-8

# # <font color='blue'>Data Science Academy</font>
# 
# ## <font color='blue'>Fundamentos de Linguagem Python Para Análise de Dados e Data Science</font>
# 
# ## <font color='blue'>Visualização de Dados com Seaborn</font>

# ![DSA](imagens/dsa_cap11.png)

# In[1]:


# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# ## Statistical Data Visualization com Seaborn 

# https://seaborn.pydata.org/

# In[2]:


get_ipython().system('pip install -q seaborn==0.12.2')


# In[3]:


# Imports
import random
import numpy as np
import pandas as pd
import matplotlib as mat
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


np.__version__


# In[5]:


pd.__version__


# In[6]:


mat.__version__


# In[7]:


import seaborn as sea
sea.__version__


# ## Criando Gráficos com Seaborn

# In[8]:


# Carregando um dos datasets que vem com o Seaborn
dados = sea.load_dataset("tips")


# In[9]:


dados.head()


# In[10]:


# O método joinplot cria plot de 2 variáveis com gráficos bivariados e univariados
sea.jointplot(data = dados, x = "total_bill", y = "tip", kind = 'reg')


# In[11]:


# O método lmplot() cria plot com dados e modelos de regressão
sea.lmplot(data = dados, x = "total_bill", y = "tip", col = "smoker")


# In[12]:


# Construindo um dataframe com Pandas
df = pd.DataFrame()


# In[13]:


# Alimentando o Dataframe com valores aleatórios
df['idade'] = random.sample(range(20, 100), 30)
df['peso'] = random.sample(range(55, 150), 30)


# In[14]:


df.shape


# In[15]:


df.head()


# In[16]:


# lmplot
sea.lmplot(data = df, x = "idade", y = "peso", fit_reg = True)


# In[17]:


# kdeplot
sea.kdeplot(df.idade)


# In[18]:


# kdeplot
sea.kdeplot(df.peso)


# In[19]:


# distplot
sea.distplot(df.peso)


# In[20]:


# Histograma
plt.hist(df.idade, alpha = .3)
sea.rugplot(df.idade)


# In[21]:


# Box Plot
sea.boxplot(df.idade, color = 'm')


# In[22]:


# Box Plot
sea.boxplot(df.peso, color = 'y')


# In[23]:


# Violin Plot
sea.violinplot(df.idade, color = 'g')


# In[24]:


# Violin Plot
sea.violinplot(df.peso, color = 'cyan')


# In[25]:


# Clustermap
sea.clustermap(df)


# ## Usando Matplotlib, Seaborn, NumPy e Pandas na Criação de Gráfico Estatístico

# In[26]:


# Valores randômicos
np.random.seed(42)
n = 1000
pct_smokers = 0.2

# Variáveis
flag_fumante = np.random.rand(n) < pct_smokers
idade = np.random.normal(40, 10, n)
altura = np.random.normal(170, 10, n)
peso = np.random.normal(70, 10, n)

# Dataframe
dados = pd.DataFrame({'altura': altura, 'peso': peso, 'flag_fumante': flag_fumante})

# Cria os dados para a variável flag_fumante
dados['flag_fumante'] = dados['flag_fumante'].map({True: 'Fumante', False: 'Não Fumante'})


# In[27]:


dados.shape


# In[28]:


dados.head()


# In[29]:


# Style
sea.set(style = "ticks")

# lmplot
sea.lmplot(x = 'altura', 
           y = 'peso', 
           data = dados, 
           hue = 'flag_fumante', 
           palette = ['tab:blue', 'tab:orange'], 
           height = 7)

# Labels e título
plt.xlabel('Altura (cm)')
plt.ylabel('Peso (kg)')
plt.title('Relação Entre Altura e Peso de Fumantes e Não Fumantes')

# Remove as bordas
sea.despine()

# Show
plt.show()


# Conheça a Formação Análise Estatística. Os alunos aprendem a construir diversos gráficos para análise estatística em Linguagem R e Linguagem Python. Confira:
# 
# https://www.datascienceacademy.com.br/bundle/formacao-analise-estatistica

# # Fim

# 
# ### Obrigado
# 
# ### Visite o Blog da Data Science Academy - <a href="http://blog.dsacademy.com.br">Blog DSA</a>
# 
