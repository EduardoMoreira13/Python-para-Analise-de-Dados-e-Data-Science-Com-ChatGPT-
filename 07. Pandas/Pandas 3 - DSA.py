# PANDAS: Excel em Python, manipulação de dados

import pandas as pd
import numpy as np

# Leitura do arquivo em excel
print("Leitura do arquivo em excel")
dsa_df = pd.read_csv("dataset.csv")
print(dsa_df.head(10))

# Filtramos o dataframe pela coluna Segmento com valores que iniciam com as letras 'Con'
dados = dsa_df[dsa_df.Segmento.str.startswith('Con')].head()
print(dados)

# Filtramos o dataframe pela coluna Segmento com valores que terminam com as letras 'mer'
dsa_df[dsa_df.Segmento.str.endswith('mer')].head()
print(dados)

# Split - separação de strings
print(dsa_df['ID_Pedido'].head())
dados = dsa_df['ID_Pedido'].str.split('-')
print(dados)
print(dados.str[1].head())

# Strip - remoção de espaço em branco ou strings específicas
dados = dsa_df['Data_Pedido'].str.lstrip('20')
print(dados)

# Replace - Substituir strings
print(dsa_df['ID_Cliente'])
dsa_df['ID_Cliente'] = dsa_df['ID_Cliente'].str.replace('CG', 'AX')
print(dsa_df['ID_Cliente'])

# CAT - Concatenar strings
dsa_df['Pedido_Segmento'] = dsa_df['ID_Pedido'].str.cat(dsa_df['Segmento'], sep = '-')
print(dsa_df['Pedido_Segmento'])

