#!/usr/bin/env python
# coding: utf-8

# # <font color='blue'>Data Science Academy</font>
# 
# ## <font color='blue'>Fundamentos de Linguagem Python Para Análise de Dados e Data Science</font>
# 
# ## <font color='blue'>Projeto 2</font>
# 
# ## <font color='blue'>Análise Exploratória de Dados em Linguagem Python Para a Área de Varejo</font>

# ![DSA](imagens/projeto2.png)

# In[1]:


# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# In[2]:


# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt


# ## Carregando os Dados

# In[3]:


# Carrega o dataset
df_dsa = pd.read_csv('dados/dataset.csv')


# In[4]:


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

# In[13]:


# Primeiro filtramos o dataframe com os registros da categoria que desejamos
df_dsa_p1 = df_dsa[df_dsa['Categoria'] == 'Office Supplies']


# In[14]:


# Em seguida agrupamos por cidade e calculamos o total de valor_venda
df_dsa_p1_total = df_dsa_p1.groupby('Cidade')['Valor_Venda'].sum()


# In[15]:


# Então encontramos a cidade com maior valor de venda
cidade_maior_venda = df_dsa_p1_total.idxmax()
print("Cidade com maior valor de venda para 'Office Supplies':", cidade_maior_venda)


# In[16]:


# Para conferir o resultado
df_dsa_p1_total.sort_values(ascending = False)


# ## Pergunta de Negócio 2:
# 
# ### Qual o Total de Vendas Por Data do Pedido?
# 
# Demonstre o resultado através de um gráfico de barras.

# In[17]:


# Calculamos o total de vendas para cada data de pedido
df_dsa_p2 = df_dsa.groupby('Data_Pedido')['Valor_Venda'].sum()


# In[18]:


df_dsa_p2.head()


# Obs: Estamos aqui tratando data de pedido como variável categórica e não como série temporal. Se a pergunta fosse "ao longo do tempo" essa resposta não seria a ideal.

# In[19]:


# Plot
plt.figure(figsize = (20, 6))
df_dsa_p2.plot(x = 'Data_Pedido', y = 'Valor_Venda', color = 'green')
plt.title('Total de Vendas Por Data do Pedido')
plt.show()


# ## Pergunta de Negócio 3:
# 
# ### Qual o Total de Vendas por Estado?
# 
# Demonstre o resultado através de um gráfico de barras.

# In[20]:


# Agrupamos por estado e calculamos o total de vendas
df_dsa_p3 = df_dsa.groupby('Estado')['Valor_Venda'].sum().reset_index()


# In[21]:


# Plot
plt.figure(figsize = (16, 6))
sns.barplot(data = df_dsa_p3, 
            y = 'Valor_Venda', 
            x = 'Estado').set(title = 'Vendas Por Estado')
plt.xticks(rotation = 80)
plt.show()


# ## Pergunta de Negócio 4:
# 
# ### Quais São as 10 Cidades com Maior Total de Vendas?
# 
# Demonstre o resultado através de um gráfico de barras.

# In[22]:


# Agrupamos por cidade, calculamos o total de vendas e ordenamos listando somente os 10 primeiros registros
df_dsa_p4 = df_dsa.groupby('Cidade')['Valor_Venda'].sum().reset_index().sort_values(by = 'Valor_Venda',
                                                                                    ascending = False).head(10)


# In[23]:


df_dsa_p4.head(10)


# In[24]:


# Plot
plt.figure(figsize = (16, 6))
sns.set_palette('coolwarm')
sns.barplot(data = df_dsa_p4, 
            y = 'Valor_Venda', 
            x = 'Cidade').set(title = 'As 10 Cidades com Maior Total de Vendas')
plt.show()


# ## Pergunta de Negócio 5:
# 
# ### Qual Segmento Teve o Maior Total de Vendas?
# 
# Demonstre o resultado através de um gráfico de pizza.

# In[25]:


# Agrupamos por segmento e calculamos o total de vendas
df_dsa_p5 = df_dsa.groupby('Segmento')['Valor_Venda'].sum().reset_index().sort_values(by = 'Valor_Venda',
                                                                                      ascending = False)


# In[26]:


df_dsa_p5.head()


# In[27]:


# Função para converter os dados em valor absoluto
def autopct_format(values): 
    def my_format(pct): 
        total = sum(values) 
        val = int(round(pct * total / 100.0))
        return ' $ {v:d}'.format(v = val)
    return my_format


# In[28]:


# Plot

# Tamanho da figura
plt.figure(figsize = (16, 6))

# Gráfico de pizza
plt.pie(df_dsa_p5['Valor_Venda'], 
        labels = df_dsa_p5['Segmento'],
        autopct = autopct_format(df_dsa_p5['Valor_Venda']),
        startangle = 90)

# Limpa o círculo central
centre_circle = plt.Circle((0, 0), 0.82, fc = 'white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Labels e anotações
plt.annotate(text = 'Total de Vendas: ' + '$ ' + str(int(sum(df_dsa_p5['Valor_Venda']))), xy = (-0.25, 0))
plt.title('Total de Vendas Por Segmento')
plt.show()


# ## Pergunta de Negócio 6 (Desafio Nível Baby):
# 
# ### Qual o Total de Vendas Por Segmento e Por Ano?

# In[29]:


df_dsa.head()


# In[30]:


# Convertemos a coluna de data para o tipo datetime para obter o formato adequado
df_dsa['Data_Pedido'] = pd.to_datetime(df_dsa['Data_Pedido'], dayfirst = True)


# In[31]:


df_dsa.dtypes


# In[32]:


# Extraímos o ano criando nova variável
df_dsa['Ano'] = df_dsa['Data_Pedido'].dt.year


# In[33]:


df_dsa.head()


# In[34]:


# Total de vendas por segmento e por ano
df_dsa_p6 = df_dsa.groupby(['Ano', 'Segmento'])['Valor_Venda'].sum()


# In[35]:


df_dsa_p6


# ## Pergunta de Negócio 7 (Desafio Nível Júnior):
# 
# Os gestores da empresa estão considerando conceder diferentes faixas de descontos e gostariam de fazer uma simulação com base na regra abaixo:
# 
# - Se o Valor_Venda for maior que 1000 recebe 15% de desconto.
# - Se o Valor_Venda for menor que 1000 recebe 10% de desconto.
# 
# ### Quantas Vendas Receberiam 15% de Desconto?

# In[36]:


# Cria uma nova coluna de acordo com a regra definida acima
df_dsa['Desconto'] = np.where(df_dsa['Valor_Venda'] > 1000, 0.15, 0.10)


# In[37]:


df_dsa.head()


# In[38]:


# Total por cada valor da variável
df_dsa['Desconto'].value_counts()


# In[39]:


print('No Total 457 Vendas Receberiam Desconto de 15%.')


# ## Pergunta de Negócio 8 (Desafio Nível Master):
# 
# ### Considere Que a Empresa Decida Conceder o Desconto de 15% do Item Anterior. Qual Seria a Média do Valor de Venda Antes e Depois do Desconto?

# In[40]:


# Criamos uma coluna calculando o valor de venda menos o desconto
df_dsa['Valor_Venda_Desconto'] = df_dsa['Valor_Venda'] - (df_dsa['Valor_Venda'] * df_dsa['Desconto'])


# In[41]:


df_dsa.head()


# In[42]:


# Filtrando as vendas antes do desconto de 15%
df_dsa_p8_vendas_antes_desconto = df_dsa.loc[df_dsa['Desconto'] == 0.15, 'Valor_Venda']


# In[43]:


# Filtrando as vendas depois do desconto de 15%
df_dsa_p8_vendas_depois_desconto = df_dsa.loc[df_dsa['Desconto'] == 0.15, 'Valor_Venda_Desconto']


# In[44]:


# Calcula a média das vendas antes do desconto de 15%
media_vendas_antes_desconto = df_dsa_p8_vendas_antes_desconto.mean()


# In[45]:


# Calcula a média das vendas depois do desconto de 15%
media_vendas_depois_desconto = df_dsa_p8_vendas_depois_desconto.mean()


# In[46]:


print("Média das vendas antes do desconto de 15%:", round(media_vendas_antes_desconto, 2))


# In[47]:


print("Média das vendas depois do desconto de 15%:", round(media_vendas_depois_desconto, 2))


# ## Pergunta de Negócio 9 (Desafio Nível Master Ninja):
# 
# ### Qual o Média de Vendas Por Segmento, Por Ano e Por Mês?
# 
# Demonstre o resultado através de gráfico de linha.

# In[48]:


# Extraímos o mês e gravamos em uma nova variável
df_dsa['Mes'] = df_dsa['Data_Pedido'].dt.month


# In[49]:


df_dsa.head()


# In[50]:


# Agrupamos por ano, mês e segmento e calculamos estatísticas de agregação
df_dsa_p9 = df_dsa.groupby(['Ano', 'Mes', 'Segmento'])['Valor_Venda'].agg([np.sum, np.mean, np.median])


# In[51]:


df_dsa_p9


# In[52]:


# Vamos extrair os níveis
anos = df_dsa_p9.index.get_level_values(0)
meses = df_dsa_p9.index.get_level_values(1)
segmentos = df_dsa_p9.index.get_level_values(2)


# https://seaborn.pydata.org/generated/seaborn.relplot.html

# In[53]:


# Plot
plt.figure(figsize = (12, 6))
sns.set()
fig1 = sns.relplot(kind = 'line',
                   data = df_dsa_p9, 
                   y = 'mean', 
                   x = meses,
                   hue = segmentos, 
                   col = anos,
                   col_wrap = 4)
plt.show()


# ## Pergunta de Negócio 10 (Desafio Nível Master Ninja das Galáxias):
# 
# ### Qual o Total de Vendas Por Categoria e SubCategoria, Considerando Somente as Top 12 SubCategorias? 
# 
# Demonstre tudo através de um único gráfico.

# In[54]:


df_dsa.head()


# In[55]:


# Agrupamos por categoria e subcategoria e calculamos a soma somente para variáveus numéricas
df_dsa_p10 = df_dsa.groupby(['Categoria',
                             'SubCategoria']).sum(numeric_only = True).sort_values('Valor_Venda',
                                                                                   ascending = False).head(12)


# In[56]:


# Convertemos a coluna Valor_Venda em número inteiro e classificamos por categoria
df_dsa_p10 = df_dsa_p10[['Valor_Venda']].astype(int).sort_values(by = 'Categoria').reset_index()


# Obs: Classificar o item acima por categoria é importante para preencher o gráfico com as subcategorias para cada categoria de forma ordenada.

# In[57]:


# Dataframe com categorias e subcategorias
df_dsa_p10


# In[58]:


# Criamos outro dataframe somente com os totais por categoria
df_dsa_p10_cat = df_dsa_p10.groupby('Categoria').sum(numeric_only = True).reset_index()


# In[59]:


# Dataframe com categorias 
df_dsa_p10_cat


# In[60]:


# Listas de cores para categorias
cores_categorias = ['#5d00de',
                    '#0ee84f',
                    '#e80e27']


# In[61]:


# Listas de cores para subcategorias
cores_subcategorias = ['#aa8cd4',
                       '#aa8cd5',
                       '#aa8cd6',
                       '#aa8cd7',
                       '#26c957',
                       '#26c958',
                       '#26c959',
                       '#26c960',
                       '#e65e65',
                       '#e65e66',
                       '#e65e67',
                       '#e65e68']


# In[62]:


# Plot

# Tamanho da figura
fig, ax = plt.subplots(figsize = (18,12))

# Gráfico das categorias
p1 = ax.pie(df_dsa_p10_cat['Valor_Venda'], 
            radius = 1,
            labels = df_dsa_p10_cat['Categoria'],
            wedgeprops = dict(edgecolor = 'white'),
            colors = cores_categorias)

# Gráfico das subcategorias
p2 = ax.pie(df_dsa_p10['Valor_Venda'],
            radius = 0.9,
            labels = df_dsa_p10['SubCategoria'],
            autopct = autopct_format(df_dsa_p10['Valor_Venda']),
            colors = cores_subcategorias, 
            labeldistance = 0.7,
            wedgeprops = dict(edgecolor = 'white'), 
            pctdistance = 0.53,
            rotatelabels = True)

# Limpa o centro do círculo
centre_circle = plt.Circle((0, 0), 0.6, fc = 'white')

# Labels e anotações
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.annotate(text = 'Total de Vendas: ' + '$ ' + str(int(sum(df_dsa_p10['Valor_Venda']))), xy = (-0.2, 0))
plt.title('Total de Vendas Por Categoria e Top 12 SubCategorias')
plt.show()


# # Fim
