# Projeto 2 - Parte 1

# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt


df_dsa = pd.read_csv('dados/dataset.csv')
print(df_dsa.head(10))
print(df_dsa.shape)
print(df_dsa.columns)

# Resumo estatístico da coluna com o valor de venda
print(df_dsa['Valor_Venda'].describe())

# Verificando se há registros duplicados
print(df_dsa[df_dsa.duplicated()])

# Verificando de há valores ausentes
print(df_dsa.isnull().sum())

# Pergunta de Negócio 1:

# Qual Cidade com Maior Valor de Venda de Produtos da Categoria 'Office Supplies'? Valor máximo

dados = df_dsa[ (df_dsa.Categoria == 'Office Supplies') ][['Cidade','Categoria','Valor_Venda']]

print(dados.sort_values(by='Valor_Venda', ascending=False).head(5))

dados_graf = dados.sort_values(by='Valor_Venda', ascending=False)[['Cidade','Valor_Venda']].head(5)

# Cria o gráfico de colunas
plt.barh(dados_graf['Cidade'], dados_graf['Valor_Venda'], color = 'skyblue')
plt.ylabel('Cidade\n')
plt.xlabel('\nValor de Venda (Dólar Americano)')
plt.title('5 Maiores Valores de Vendas da Categoria Office Supplies por Cidade')

# Adiciona rótulos aos dados
for i, valor in enumerate(dados_graf['Valor_Venda']):
    plt.text(valor, i, "  US$ " + str(valor).replace(".",","), ha='left', va='center')

# Mostra gráfico
plt.box(False)
plt.show()
print("\n")


# Qual Cidade com Maior Valor de Venda de Produtos da Categoria 'Office Supplies'? Total

dados = df_dsa[ (df_dsa.Categoria == 'Office Supplies') ]
dados = dados.groupby('Cidade')['Valor_Venda'].sum()
print(f"A cidade com o maior total de vendas foi: {dados.idxmax()}")
print("\n")
dados = dados.reset_index().rename(columns={'Cidade': 'Cidade', 'Valor_Venda': 'Total de Venda'})

print(dados.sort_values(by='Total de Venda', ascending=False).head(5))
dados_graf = dados.sort_values(by='Total de Venda', ascending=False).head(5)

# Cria o gráfico de colunas
plt.barh(dados_graf['Cidade'], dados_graf['Total de Venda'], color = 'skyblue')
plt.ylabel('Cidade\n')
plt.xlabel('\nValor de Venda (Dólar Americano)')
plt.title('5 Maiores Valores de Vendas da Categoria Office Supplies por Cidade')

# Adiciona rótulos aos dados
for i, valor in enumerate(dados_graf['Total de Venda']):
    plt.text(valor, i, "  US$ " + str(valor).replace(".",","), ha='left', va='center')

# Mostra gráfico
plt.box(False)
plt.show()
print("\n")


# Pergunta de Negócio 2: # não organizado por data

# Qual o Total de Vendas Por Data do Pedido? Demonstre o resultado através de um gráfico de barras.


dados = df_dsa.groupby('Data_Pedido')['Valor_Venda'].sum()
dados = dados.reset_index().rename(columns={'Data_Pedido': 'Data_Pedido', 'Valor_Venda': 'Total_Venda'})
print(dados)

# Cria o gráfico de colunas
plt.figure(figsize=(20,6))
dados.plot(x = 'Data_Pedido', y = 'Total_Venda', color = 'skyblue')
plt.ylabel('Total de Vendas US$\n')
plt.xlabel('\nData do Pedido')
plt.title('Total de Vendas Por Data do Pedido')

# Mostra gráfico
plt.box(False)
plt.show()
print("\n")

# Pergunta de Negócio 3:

# Qual o Total de Vendas por Estado? Demonstre o resultado através de um gráfico de barras.

dados = df_dsa.groupby('Estado')['Valor_Venda'].sum()
dados = dados.reset_index().rename(columns={'Estado': 'Estado', 'Valor_Venda': 'Total de Venda'})

print(dados.sort_values(by='Total de Venda', ascending=False).head(5))
dados_graf = dados.sort_values(by='Total de Venda', ascending=False)

# Cria o gráfico de colunas
plt.barh(dados_graf['Estado'], dados_graf['Total de Venda'], color = 'skyblue')
plt.ylabel('Estado\n')
plt.xlabel('\nTotal de Venda (Dólar Americano)')
plt.title('Total de Vendas da Categoria Office Supplies por Estado')

# Adiciona rótulos aos dados
for i, valor in enumerate(dados_graf['Total de Venda']):
    plt.text(valor, i, "  US$ " + str(valor).replace(".",","), ha='left', va='center')

# Mostra gráfico
plt.box(False)
plt.show()
print("\n")

# Gráfico seaborn
plt.figure(figsize = (16, 6))
sns.barplot(data = dados_graf, y = 'Total de Venda', x = 'Estado').set(title = 'Vendas Por Estado')
plt.xticks(rotation = 80)
plt.show()
print("\n")



# Pergunta de Negócio 4:

#  Quais São as 10 Cidades com Maior Total de Vendas? Demonstre o resultado através de um gráfico de barras.

dados = df_dsa.groupby('Cidade')['Valor_Venda'].sum()
print(f"A cidade com o maior total de vendas foi: {dados.idxmax()}")
print("\n")
dados = dados.reset_index().rename(columns={'Cidade': 'Cidade', 'Valor_Venda': 'Total de Venda'})

print(dados.sort_values(by='Total de Venda', ascending=False).head(10))
dados_graf = dados.sort_values(by='Total de Venda', ascending=False).head(10)

# Cria o gráfico de colunas
plt.barh(dados_graf['Cidade'], dados_graf['Total de Venda'], color = 'skyblue')
plt.ylabel('Cidade\n')
plt.xlabel('\nValor de Venda (Dólar Americano)')
plt.title('5 Maiores Totais de Vendas por Cidade')

# Adiciona rótulos aos dados
for i, valor in enumerate(dados_graf['Total de Venda']):
    plt.text(valor, i, "  US$ " + str(valor).replace(".",","), ha='left', va='center')

# Mostra gráfico
plt.box(False)
plt.show()
print("\n")

# Gráfico Seaborn
plt.figure(figsize = (16, 6))
sns.set_palette('coolwarm')
sns.barplot(data = dados_graf,
            y = 'Total de Venda',
            x = 'Cidade').set(title = 'As 10 Cidades com Maior Total de Vendas')
plt.show()




# Pergunta de Negócio 5:

# Qual Segmento Teve o Maior Total de Vendas?

dados = df_dsa.groupby('Segmento')['Valor_Venda'].sum()
print("\n")
print(f"O segmento com o maior total de vendas foi: {dados.idxmax()}")
print("\n")
dados = dados.reset_index().rename(columns={'Segmento': 'Segmento', 'Valor_Venda': 'Total de Venda'})

print(dados.sort_values(by='Total de Venda', ascending=False))
dados_graf = dados.sort_values(by='Total de Venda', ascending=False)


# Função para converter os dados em valor absoluto
def autopct_format(values):
    def my_format(pct):
        total = sum(values)
        val = int(round(pct * total / 100.0))
        return ' $ {v:d}'.format(v = val)
    return my_format

# Tamanho da figura
plt.figure(figsize = (16, 6))

# Gráfico de pizza
plt.pie(dados_graf['Total de Venda'],
        labels = dados_graf['Segmento'],
        autopct = autopct_format(dados_graf['Total de Venda']),
        startangle = 90)

# Limpa o círculo central
centre_circle = plt.Circle((0, 0), 0.82, fc = 'white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Labels e anotações
plt.annotate(text = 'Total de Vendas: ' + '$ ' + str(int(sum(dados_graf['Total de Venda']))), xy = (-0.25, 0))
plt.title('Total de Vendas Por Segmento')
plt.show()