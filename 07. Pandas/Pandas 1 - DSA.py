# PANDAS: Excel em Python, manipulação de dados

import pandas as pd
import numpy as np

# Cria um dicionário e depois converta em um dataframe
dados = {'Estado': ['Santa Catarina', 'Rio de Janeiro', 'Tocantins', 'Bahia', 'Minas Gerais'],
         'Ano': [2004, 2005, 2006, 2007, 2008],
         'Taxa Desemprego': [1.5, 1.7, 1.6, 2.4, 2.7]}

df = pd.DataFrame(dados)
print(df.head(n = 10))
print("\n")

# Reorganizando as colunas
df = pd.DataFrame(dados, columns = ['Estado', 'Taxa Desemprego', 'Ano'])
print(df.head(n = 10))
print("\n")

# Criando outro dataframe com os mesmos dados anteriores, mas adicionando uma coluna
df2 = pd.DataFrame(dados,
                columns = ['Estado', 'Taxa Desemprego', 'Taxa Crescimento', 'Ano'],
                index = ['estado1', 'estado2', 'estado3', 'estado4', 'estado5'])
print(df2.head(n = 10))
print(df2.values)
print(df2.dtypes)
print(df2.columns)
print(df2['Estado'])
print(df2[ ['Taxa Desemprego', 'Ano'] ])
print(df2.index)
print("\n")

# Filtrando pelo índice
print(df2.filter(items = ['estado3'], axis = 0))
print("\n")

# Verificando existência de NA e substituindo valores
print(df2.isna())
print(df2.head(n = 10))
print(df2['Taxa Crescimento'].isna())
df2['Taxa Crescimento'] = np.arange(5.)
print(df2.head(n = 10))
print(df2['Taxa Crescimento'].isna())
print("\n")


# Resumo estatístico - summary

print(df2.describe())
print(df2['Taxa Crescimento'].describe())
print(df2[['Taxa Desemprego', 'Ano']].describe())
print("\n")


# Slicing de DataFrames do Pandas

print(df2['estado2':'estado4'])
print(df2[ df2['Taxa Desemprego'] < 2 ])
print(df2['Taxa Crescimento'])
print(df2[['Estado', 'Taxa Crescimento']])
print(df2[['Estado', 'Taxa Crescimento', 'Ano']])
print("\n")

