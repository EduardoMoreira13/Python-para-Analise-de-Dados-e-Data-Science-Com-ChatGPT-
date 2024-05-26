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


# Pergunta de Negócio 6 (Desafio Nível Baby):

# Qual o Total de Vendas Por Segmento e Por Ano?
print(df_dsa["Data_Pedido"].head(10))
df_dsa["Data"] = pd.to_datetime(df_dsa['Data_Pedido'], dayfirst = True)
# df_dsa["Data"] = df_dsa["Data_Pedido"].apply(lambda x: dt.datetime.strptime(x, '%d/%m/%Y'))
df_dsa["Ano"] = df_dsa["Data"].dt.year
dados = df_dsa.groupby(["Ano",'Segmento'])['Valor_Venda'].sum().reset_index()

print(dados.sort_values(by='Ano', ascending=True))


# Pergunta de Negócio 7 (Desafio Nível Júnior):

# Os gestores da empresa estão considerando conceder diferentes faixas de descontos e gostariam de fazer
# uma simulação com base na regra abaixo:

# - Se o Valor_Venda for maior que 1000 recebe 15% de desconto.
# - Se o Valor_Venda for menor que 1000 recebe 10% de desconto.

# Quantas Vendas Receberiam 15% de Desconto?

dados = df_dsa.copy()

dados["Desconto"] = np.where(dados['Valor_Venda'] > 1000, '15%', '10%')

dados.loc[dados['Valor_Venda'] > 1000, 'Valor Desconto'] = dados['Valor_Venda'] * 0.15
dados.loc[dados['Valor_Venda'] <= 1000, 'Valor Desconto'] = dados['Valor_Venda'] * 0.10

dados.loc[dados['Valor_Venda'] > 1000, 'Valor Final'] = dados['Valor_Venda'] * 0.85
dados.loc[dados['Valor_Venda'] <= 1000, 'Valor Final'] = dados['Valor_Venda'] * 0.90

print(dados[["ID_Pedido",'Valor_Venda',"Desconto","Valor Desconto","Valor Final"]].head(50))
print(dados.groupby("Desconto")["Desconto"].count())
print("\n")


# Pergunta de Negócio 8 (Desafio Nível Master):

# Considere Que a Empresa Decida Conceder o Desconto de 15% do Item Anterior.
# Qual Seria a Média do Valor de Venda Antes e Depois do Desconto?

print(dados.groupby("Desconto")["Valor_Venda"].mean())
print(dados.groupby("Desconto")["Valor Final"].mean())
print("\n")
antes = dados.groupby("Desconto")["Valor_Venda"].mean().reset_index().iloc[1, 1]
depois = dados.groupby("Desconto")["Valor Final"].mean().reset_index().iloc[1, 1]
print(f"Média antes: {antes:.3f}, Média depois: {depois:.3f}")
print("\n")


# Pergunta de Negócio 9 (Desafio Nível Master Ninja):
#
# Qual o Média de Vendas Por Segmento, Por Ano e Por Mês? Demonstre o resultado através de gráfico de linha.

df_dsa["Data"] = pd.to_datetime(df_dsa['Data_Pedido'], dayfirst = True)
df_dsa["Ano"] = df_dsa["Data"].dt.year
df_dsa["Mês"] = df_dsa["Data"].dt.month
dados = df_dsa.groupby(["Ano","Mês",'Segmento'])['Valor_Venda'].agg(["sum", "mean", "median"])

print(dados.sort_values(by=['Ano',"Mês"], ascending=[True,True]))

# Vamos extrair os níveis
anos = dados.index.get_level_values(0) # não pode ser usado no caso de reset_index()
meses = dados.index.get_level_values(1)
segmentos = dados.index.get_level_values(2)

# Plot Seaborn
plt.figure(figsize = (12, 6))
sns.set()
fig1 = sns.relplot(kind = 'line',
                   data = dados,
                   y = 'mean',
                   x = meses,
                   hue = segmentos,
                   col = anos,
                   col_wrap = 4)
plt.show()
print("\n")


# Pergunta de Negócio 10 (Desafio Nível Master Ninja das Galáxias):

# Qual o Total de Vendas Por Categoria e SubCategoria, Considerando Somente as Top 12 SubCategorias?

dados = df_dsa.copy()
top12 = dados.groupby("SubCategoria")["Valor_Venda"].sum().reset_index().sort_values(by="Valor_Venda", ascending=False).head(12)
print(top12)
print("\n")

dados = dados[dados.SubCategoria.isin(top12["SubCategoria"])]
dados = dados.groupby(['Categoria','SubCategoria'])["Valor_Venda"].sum().reset_index()
print(dados)
print("\n")

