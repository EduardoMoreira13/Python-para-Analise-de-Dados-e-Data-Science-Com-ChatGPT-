#!/usr/bin/env python
# coding: utf-8

# # <font color='blue'>Data Science Academy</font>
# 
# ## <font color='blue'>Fundamentos de Linguagem Python Para Análise de Dados e Data Science</font>
# 
# ## <font color='blue'>Manipulação de Dados com Pandas</font>

# ![DSA](imagens/dsa_cap10.png)

# In[1]:


# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# Guia de Usuário do Pandas:
# 
# https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html#user-guide

# In[2]:


# Instala a versão exata do pacote
get_ipython().system('pip install -q pandas==1.5.3')


# In[3]:


import pandas as pd


# In[4]:


pd.__version__


# ## Manipulando Dados em DataFrames do Pandas 

# In[5]:


# Cria um dicionário
dados = {'Estado': ['Santa Catarina', 'Rio de Janeiro', 'Tocantins', 'Bahia', 'Minas Gerais'], 
         'Ano': [2004, 2005, 2006, 2007, 2008], 
         'Taxa Desemprego': [1.5, 1.7, 1.6, 2.4, 2.7]}


# In[6]:


print(dados)


# In[7]:


# Importa a função DataFrame do Pandas
from pandas import DataFrame


# In[8]:


# Converte o dicionário em um dataframe
df = DataFrame(dados)


# In[9]:


# Visualiza as 5 primeiras linhas
df.head()


# In[10]:


type(df)


# In[11]:


# Reorganizando as colunas
DataFrame(dados, columns = ['Estado', 'Taxa Desemprego', 'Ano'])


# In[12]:


# Criando outro dataframe com os mesmo dados anteriores mas adicionando uma coluna
df2 = DataFrame(dados, 
                columns = ['Estado', 'Taxa Desemprego', 'Taxa Crescimento', 'Ano'], 
                index = ['estado1', 'estado2', 'estado3', 'estado4', 'estado5'])


# In[13]:


df2


# In[14]:


df2.values


# In[15]:


df2.dtypes


# In[16]:


df2.columns


# In[17]:


# Imprimindo apenas uma coluna do Dataframe
df2['Estado']


# In[18]:


# Linguagem Python é case sensitive
# df2['estado']


# In[19]:


# Imprimindo apenas duas colunas do Dataframe
df2[ ['Taxa Desemprego', 'Ano'] ]


# In[20]:


df2.index


# In[21]:


# Filtrando pelo índice
df2.filter(items = ['estado3'], axis = 0)


# ## Usando NumPy e Pandas Para Manipulação de Dados

# In[22]:


df2.head()


# In[23]:


df2.dtypes


# In[24]:


# Resumo estatístico do Dataframe
df2.describe()


# In[25]:


df2.isna()


# In[26]:


df2['Taxa Crescimento'].isna()


# In[27]:


# Importando o NumPy
import numpy as np


# In[28]:


# Usando o NumPy para alimentar uma das colunas do dataframe
df2['Taxa Crescimento'] = np.arange(5.)


# In[29]:


df2


# In[30]:


df2.dtypes


# In[31]:


df2['Taxa Crescimento'].isna()


# In[32]:


# Resumo estatístico do Dataframe
df2.describe()


# ## Slicing de DataFrames do Pandas

# In[33]:


df2


# In[34]:


df2['estado2':'estado4']


# In[35]:


df2[ df2['Taxa Desemprego'] < 2 ]


# In[36]:


df2['Taxa Crescimento']


# In[37]:


df2[['Estado', 'Taxa Crescimento']]


# In[38]:


df2[['Estado', 'Taxa Crescimento', 'Ano']]


# ## Preenchendo Valores Ausentes em DataFrames do Pandas
# 
# A função fillna() é usada para preencher os valores ausentes. A função oferece muitas opções. Podemos usar um valor específico, uma função agregada (por exemplo, média) ou o valor anterior ou seguinte.
# 
# Para esse exemplo usaremos a moda, a estatística que representa o valor que aparece mais vezes em uma variável.

# In[39]:


# Primeiro importamos um dataset
dsa_df = pd.read_csv("dataset.csv")


# In[40]:


dsa_df.head(15)


# In[41]:


dsa_df.isna().sum()


# In[42]:


# Extraímos a moda da coluna Quantity
moda = dsa_df['Quantidade'].value_counts().index[0]


# A moda em Estatística é uma medida de tendência central que representa o valor mais frequente em um conjunto de dados. 
# 
# A moda é especialmente útil quando queremos saber qual é o valor mais comum ou popular em um conjunto de dados, seja em uma distribuição unimodal (com apenas uma moda) ou em uma distribuição bimodal (com duas modas).
# 
# No entanto, a moda pode não ser tão representativa quanto outras medidas de tendência central, como a média e a mediana, especialmente em distribuições assimétricas ou quando há valores extremos. Por essa razão, é importante analisar diferentes medidas de tendência central e usar a que melhor se adequa aos objetivos da análise estatística.

# In[43]:


print(moda)


# In[44]:


# E por fim preenchemos os valores NA com a moda
dsa_df['Quantidade'].fillna(value = moda, inplace = True)


# In[45]:


dsa_df.isna().sum()


# ## Query (Consulta) de Dados no DataFrame do Pandas
# 
# Com o Pandas criamos dataframes, que são essencialmente tabelas. Como tal, podemos fazer consultas, ou simplesmente queries. E para isso usamos o método query(). Veja o exemplo abaixo:

# In[46]:


dsa_df.head()


# In[47]:


# Checamos os valores mínimo e máximo da coluna Valor_Venda
dsa_df.Valor_Venda.describe()


# O intervalo de vendas (Valor_Venda) é de 0.44 a 22638. Vamos fazer uma consulta e retornar todas as vendas dentro de um range de valores. Fazemos isso com a instrução abaixo:

# In[48]:


# Geramos um novo dataframe apenas com o intervalo de vendas entre 229 e 10000
df2 = dsa_df.query('229 < Valor_Venda < 10000')


# In[49]:


# Então confirmamos os valores mínimo e máximo
df2.Valor_Venda.describe()


# In[50]:


# Geramos um novo dataframe apenas com os valores de venda acima da média
df3 = df2.query('Valor_Venda > 766')


# In[51]:


df3.head()


# Consulta executada com sucesso!

# ## Verificando a Ocorrência de Diversos Valores em Uma Coluna
# 
# Em nosso conjunto de dados de exemplo temos a coluna Quantidade que representa a quantidade de itens vendidos em cada uma das vendas. Imagine que precisamos saber em quais vendas foram vendidos 5, 7, 9 ou 11 itens. 
# 
# Como aplicaríamos esse tipo de filtro ao nosso dataframe?
# 
# Fácil. O Pandas oferece o método isin() para checar diversos valores em uma coluna. Quem conhece Linguagem SQL já deve ter percebido que o método é o mesmo que a cláusula IN em SQL. Vamos ao exemplo.

# In[52]:


dsa_df.shape


# In[53]:


# Então aplicamos o filtro
dsa_df[dsa_df['Quantidade'].isin([5,7,9,11])]


# Na instrução acima estamos filtrando o dataframe chamado df, retornando todas as linhas onde a coluna Quantidade for igual aos valores 5, 7, 9 ou 11. Passamos uma lista de valores como argumento para o método isin().
# 
# Vamos deixar um pouquinho mais divertido. Se você executou a instrução acima, percebeu que foram retornadas 2.128 linhas. E se quisermos retornar somente 10 linhas? É só fatiar o resultado assim:

# In[54]:


# Shape
dsa_df[dsa_df['Quantidade'].isin([5,7,9,11])].shape


# In[55]:


dsa_df[dsa_df['Quantidade'].isin([5,7,9,11])][:10]


# O Pandas não é incrível? 😁

# ## Operadores Lógicos Para Manipulação de Dados com Pandas
# 
# Os operadores lógicos são excelentes para filtrar dataframes e retornar exatamente os dados que precisamos para nosso trabalho. Para conhecer mais sobre as regras dos operadores lógicos, acesse aqui:
# 
# https://pt.wikipedia.org/wiki/Operador_l%C3%B3gico

# Primeiro usaremos o operador lógico AND para checar duas condições. Serão retornados os registros quando as duas condições forem verdadeiras.

# In[56]:


# Filtrando as vendas que ocorreram para o segmento de Home Office e na região South
dsa_df[ (dsa_df.Segmento == 'Home Office') & (dsa_df.Regiao == 'South') ].head()


# Mas pode ser necessário checar duas condições e retornar os registros se pelo menos uma for verdadeira. Nesse caso usamos o operador OR, conforme abaixo.

# In[57]:


# Filtrando as vendas que ocorreram para o segmento de Home Office ou região South
dsa_df[(dsa_df.Segmento == 'Home Office') | (dsa_df.Regiao == 'South')].tail()


# O operador de negação é o contrário do primeiro exemplo.

# In[58]:


# Filtrando as vendas que não ocorreram para o segmento de Home Office e nem na região South
dsa_df[(dsa_df.Segmento != 'Home Office') & (dsa_df.Regiao != 'South')].sample(5)


# ## Agrupamento de Dados em DataFrames com Group By
# 
# A função Pandas Groupby é uma função versátil e fácil de usar que ajuda a obter uma visão geral dos dados. Isso torna mais fácil explorar o conjunto de dados e revelar os relacionamentos entre as variáveis.
# 
# O código a seguir agrupará as linhas com base nas combinações Segmento/Regiao/Valor_Venda e nos dará a taxa média de vendas de cada grupo.

# In[59]:


# Aplicamos o group by
dsa_df[['Segmento', 'Regiao', 'Valor_Venda']].groupby(['Segmento', 'Regiao']).mean()


# Na instrução acima, primeiro filtramos os dados extraindo 3 colunas: ['Segmento','Regiao','Valor_Venda']. Na sequência, agrupamos por duas colunas: ['Segmento','Regiao']. E então calculamos a média para a coluna que ficou foram do group by, nesse caso a coluna Sales.
# 
# O comportamento do group by com Pandas é o mesmo observado na Linguagem SQL.

# ## Agregação Múltipla com Group By
# 
# Vamos explorar mais a função groupby() pois temos diversas opções de sumarização dos dados de forma simples. No exemplo abaixo uniremos a função groupby() com a função agg() para realiza agregação múltipla.

# In[60]:


# Aplicamos o group by
dsa_df[['Segmento', 'Regiao', 'Valor_Venda']].groupby(['Segmento', 'Regiao']).agg(['mean', 'std', 'count'])


# Na instrução acima, primeiro filtramos os dados extraindo 3 colunas: ['Segmento','Regiao','Valor_Venda']. Na sequência, agrupamos por duas colunas: ['Segmento','Regiao']. E então agregamos os dados calculando a média, desvio padrão e contagem de elementos para a coluna que ficou fora do group by, nesse caso a coluna Valor_Venda.
# 
# A função agg() recebe como argumento uma lista de funções para agregação.

# ## Filtrando DataFrame do Pandas com Base em Strings
# 
# O Pandas oferece diversas funções para manipulação de strings. Começaremos com o filtros de strings com base nas letras iniciais e finais.

# In[61]:


dsa_df.head()


# In[62]:


# Filtramos o dataframe pela coluna Segmento com valores que iniciam com as letras 'Con'
dsa_df[dsa_df.Segmento.str.startswith('Con')].head()


# In[63]:


dsa_df.Segmento.value_counts()


# In[64]:


# Filtramos o dataframe pela coluna Segmento com valores que terminam com as letras 'mer'
dsa_df[dsa_df.Segmento.str.endswith('mer')].head()


# As funções startswith() e endswith() são muito úteis quando for necessário filtrar strings por caracteres que apareçam no começo e/ou final.

# ## Split de Strings em DataFrames do Pandas
# 
# Com Pandas podemos realizar diversas tarefas de split de strings dividindo uma coluna ou extraindo elementos do nosso interesse. Vamos ao exemplo!

# In[65]:


dsa_df.head()


# In[66]:


dsa_df['ID_Pedido'].head()


# Este é o formato dos dados da coluna "ID_Pedido":
# 
# - CA-2016-152156
# - US-2015-108966
# 
# Temos o país, o ano e o id do pedido. Vamos dividir essa coluna e extrair o ano para gravar em uma nova coluna:

# In[67]:


# Split da coluna pelo caracter '-'
dsa_df['ID_Pedido'].str.split('-')


# Observe que o resultado são as listas em Python. Para extrair o ano precisamos especificar o índice da posição que queremos extrair (em nosso caso a posição 2, logo, índice 1 em Python):

# In[68]:


dsa_df['ID_Pedido'].str.split('-').str[1].head()


# In[69]:


# Fazemos o split da coluna e extraímos o item na posição 2 (índice 1)
dsa_df['Ano'] = dsa_df['ID_Pedido'].str.split('-').str[1]


# In[70]:


# Então conferimos a nova coluna criada
dsa_df.head()


# ## Strip de Strings em DataFrames do Pandas
# 
# Cuidado para não confundir. Vimos o Split e agora veremos o Strip. São funções diferentes.
# 
# O Split divide a string. O Strip remove caracteres da string. Veja os exemplos.

# In[71]:


dsa_df.head(3)


# In[72]:


dsa_df['Data_Pedido'].head(3)


# A coluna 'Data_Pedido' é a data de envio do produto no formato YYYY-MM-DD. Imagine que seja necessário deixar o ano apenas com 2 dígitos sem alterar o tipo da variável. Fazemos isso com a função lstrip(), ou seja, left strip.

# In[73]:


# Vamos remover os dígitos 2 e 0 à esquerda do valor da variável 'Data_Pedido'
dsa_df['Data_Pedido'].str.lstrip('20')


# Como não usamos o inplace = True a mudança é somente na memória e não altera o dataframe. Podemos usar ainda as funções rstrip() e strip() com diferentes variações de strip de strings.

# In[74]:


dsa_df['Data_Pedido'].head(3)


# ## Replace de Strings em DataFrames do Pandas
# 
# Se for necessário substituir caracteres dentro de uma string o Pandas oferece uma função para isso também.
# 
# Por exemplo, vamos substituir 2 caracteres em uma das colunas.

# In[75]:


dsa_df.head()


# In[76]:


# Substituímos os caracteres CG por AX na coluna 'ID_Cliente'
dsa_df['ID_Cliente'] = dsa_df['ID_Cliente'].str.replace('CG', 'AX')


# In[77]:


dsa_df.head()


# E pronto. Fácil assim.

# ## Combinação de Strings em DataFrames do Pandas
# 
# A função cat() pode ser usada para concatenar strings em um dataframe do Pandas.
# 
# Vamos criar uma nova coluna concatenando as colunas “ID_Pedido” e “Segmento” com o separador “-”.

# In[78]:


dsa_df.head()


# In[79]:


# Concatenando strings
dsa_df['Pedido_Segmento'] = dsa_df['ID_Pedido'].str.cat(dsa_df['Segmento'], sep = '-')


# In[80]:


dsa_df.head()


# ## Construção de Gráficos a Partir de DataFrames do Pandas
# 
# Vimos até aqui diversas funcionalidades do Pandas que tornam o processo de manipulação de dados realmente simples. E para concluir este capítulo vamos estudar as opções que o Pandas oferece para criação de gráficos diretamente a partir de dataframes, sem a necessidade de usar qualquer outra biblioteca. 
# 
# Acompanhe os exemplos.

# In[81]:


# Instala a versão exata do Scikit-learn
get_ipython().system('pip install -q scikit-learn==1.2.1')


# In[82]:


import sklearn
sklearn.__version__


# In[83]:


# Vamos começar importando o dataset iris do Scikit-learn
from sklearn.datasets import load_iris
data = load_iris()


# In[84]:


# E então carregamos o dataset iris como dataframe do Pandas
import pandas as pd
df = pd.DataFrame(data['data'], columns = data['feature_names'])
df['species'] = data['target']
df.head()


# In[85]:


# Para criar um gráfico de linhas com todas as variáveis do dataframe, basta fazer isso:
df.plot()


# In[86]:


# Que tal um scatter plot com duas variáveis? 
df.plot.scatter(x = 'sepal length (cm)', y = 'sepal width (cm)')


# In[87]:


# E mesmo gráficos mais complexos, como um gráfico de área, pode ser criado:
columns = ['sepal length (cm)', 'petal length (cm)', 'petal width (cm)', 'sepal width (cm)']
df[columns].plot.area()


# In[88]:


# Calculamos a média das colunas agrupando pela coluna species e criamos um gráfico de barras com o resultado
df.groupby('species').mean().plot.bar()


# In[89]:


# Ou então, fazemos a contagem de classes da coluna species e plotamos em um gráfico de pizza
df.groupby('species').count().plot.pie(y = 'sepal length (cm)')


# A lista de possibilidades é imensa. Aqui tem muitos outros exemplos:
# 
# https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html
# 

# In[90]:


# Gráfico KDE (Kernel Density Function) para cada variável do dataframe
df.plot.kde(subplots = True, figsize = (8,8))


# In[91]:


# Boxplot de cada variável numérica
columns = ['sepal length (cm)', 'petal length (cm)', 'petal width (cm)', 'sepal width (cm)']
df[columns].plot.box(figsize = (8,8))


# O Pandas é uma verdadeira caixa de ferramentas para manipulação de dados em Python.

# # Fim

# ### Obrigado
# 
# ### Visite o Blog da Data Science Academy - <a href="http://blog.dsacademy.com.br">Blog DSA</a>
