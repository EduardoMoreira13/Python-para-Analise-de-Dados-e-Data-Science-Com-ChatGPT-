# GRÁFICOS VIA MATPLOTLIB


# PACOTES E DADOS

import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("dataset.csv")
print(df.columns)


# GRÁFICO DE COLUNAS - BIDIMENSIONAL, COLUNAS JUSTAPOSTAS E CONTAGEM

x1 = [2,4,6,8,10]
y1 = [6,7,8,2,4]
x2 = [1,3,5,7,9]
y2 = [7,8,2,4,2]

plt.bar(x1, y1, label = 'Listas1', color = 'blue')
plt.bar(x2, y2, label = 'Listas2', color = 'red')
plt.legend()
plt.show()


contagem = df[['Segmento','Categoria']].value_counts()
cor = ['green','green','orange','orange','red','red','blue','blue','blue']

# Plotando o gráfico de colunas
grafico = contagem.plot(kind = 'bar', color = cor , width=0.8)

# Adicionando rótulos e título
grafico.set_xlabel('\nCategoria', fontsize=14)  # Definindo tamanho da fonte do xlabel
grafico.set_ylabel('Contagem\n', fontsize=14)   # Definindo tamanho da fonte do ylabel
plt.title('Gráfico de Colunas - Contagem de Categorias', fontsize=16)
grafico.set_xticklabels(grafico.get_xticklabels(), rotation=0) # sem rotacao no eixo x
for indice, valor in enumerate(contagem): # rotulo de dados
    grafico.annotate(str(valor), xy=(indice, valor), ha='center', va='bottom')

# Definindo os intervalos de y - vale pra x se necessário
intervalos_y = np.arange(0, contagem.max() * 1.1, 1000)  # Intervalos de 1000 em 1000
grafico.set_yticks(intervalos_y)

# Exibindo o gráfico
plt.show()


# GRÁFICO DE COLUNAS - BIDIMENSIONAL COM LEGENDA, COLUNAS SOBREPOSTAS E CONTAGEM

data1 = [30, 20, 10, 0, 0]
data2 = [20, 20, 20, 20, 0]
data3 = [50, 60, 70, 80, 100]

year = ["2015", "2016", "2017", "2018", "2019"]

plt.figure(figsize=(9, 7))
plt.bar(year, data3, color="green", label="Python")
plt.bar(year, data2, color="yellow", bottom=np.array(data3), label="JavaScript")
plt.bar(year, data1, color="red", bottom=np.array(data3) + np.array(data2), label="C++")

plt.legend(loc="lower left", bbox_to_anchor=(0.8, 1.0))
plt.show()