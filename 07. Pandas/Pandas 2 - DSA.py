# PANDAS: Excel em Python, manipulação de dados

import pandas as pd
import numpy as np

# Leitura do arquivo em excel
print("Leitura do arquivo em excel")
dsa_df = pd.read_csv("dataset.csv")
print(dsa_df.head(10))

# Contagem e substituição de NA
print("Contagem e substituição de NA")
print(dsa_df.isna().sum())
moda = dsa_df['Quantidade'].value_counts().index[0]
dsa_df.fillna({'Quantidade': moda}, inplace = True) # inplace salva no próprio arquivo
print(dsa_df.isna().sum())


# Query (Consulta) de Dados no DataFrame do Pandas
print("Query (Consulta) de Dados no DataFrame do Pandas")
print(dsa_df.head(10))
print(dsa_df.Valor_Venda.describe())
print(dsa_df["Valor_Venda"].describe())

df2 = dsa_df.query('229 < Valor_Venda < 10000')
print(df2.Valor_Venda.describe())

df3 = df2.query('Valor_Venda > 766')
print(df3.head(10))


# Filtro com o operador IN e NOT IN
print("Filtro com o operador IN e NOT IN")
dados = dsa_df[dsa_df['Quantidade'].isin([5,7,9,11])]
print(dados.head(10))

dados = dsa_df[~dsa_df['Quantidade'].isin([5,7,9,11])]
print(dados.head(10))


# Operadores Lógicos Para Manipulação de Dados com Panda
print("Operadores Lógicos Para Manipulação de Dados com Panda")
dados = dsa_df[ (dsa_df.Segmento == 'Home Office') & (dsa_df.Regiao == 'South') ].head() # AND
print(dados.head(10))

dados = dsa_df[(dsa_df.Segmento == 'Home Office') | (dsa_df.Regiao == 'South')].tail() # OR
print(dados.head(10))

dados = dsa_df[(dsa_df.Segmento != 'Home Office') & (dsa_df.Regiao != 'South')].sample(5) # Diferente
print(dados.head(10))

# Agregação por Group BY e AGG
print("Agregação por Group BY e AGG")
dados = dsa_df[['Segmento', 'Regiao', 'Valor_Venda']].groupby(['Segmento', 'Regiao']).mean()
print(dados)

dados = dsa_df[['Segmento', 'Regiao', 'Valor_Venda']].groupby(['Segmento', 'Regiao']).agg(['mean', 'std', 'count'])
print(dados)




