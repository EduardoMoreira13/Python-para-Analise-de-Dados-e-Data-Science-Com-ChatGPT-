# GRÁFICOS VIA MATPLOTLIB


# PACOTES E DADOS

import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("dataset.csv")
print(df.columns)


# GRÁFICO DE COLUNAS - UNIDIMENSIONAL e CONTAGEM

x1 = [2,4,6,8,10] # categorias
y1 = [6,7,8,2,4] # contagem

plt.bar(x1, y1, label = 'Barras', color = 'green')
plt.legend()
plt.show()

contagem = df['Segmento'].value_counts()

# Plotando o gráfico de colunas
grafico = contagem.plot(kind = 'bar', color = 'green', width=0.8)

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



# GRÁFICO DE COLUNAS - UNIDIMENSIONAL e PROPORÇÃO

contagem = df['Segmento'].value_counts(normalize=True)

# Plotando o gráfico de colunas
grafico = contagem.plot(kind = 'bar', color = 'green', width=0.8)

# Adicionando rótulos e título
grafico.set_xlabel('\nCategoria', fontsize=14)  # Definindo tamanho da fonte do xlabel
grafico.set_ylabel('Contagem\n', fontsize=14)   # Definindo tamanho da fonte do ylabel
plt.title('Gráfico de Colunas - Proporção de Categorias', fontsize=16)
grafico.set_xticklabels(grafico.get_xticklabels(), rotation=0) # sem rotacao no eixo x
for indice, valor in enumerate(contagem): # rotulo de dados
    grafico.annotate(str(round(valor,3)), xy=(indice, valor), ha='center', va='bottom')

# Definindo os intervalos de y - vale pra x se necessário
intervalos_y = np.arange(0, 1, 0.1)  # Intervalos de 0.1 em 0.1
grafico.set_yticks(intervalos_y)

# Exibindo o gráfico
plt.show()



# GRÁFICO DE BARRAS - UNIDIMENSIONAL e CONTAGEM

contagem = df['Segmento'].value_counts()

# Plotando o gráfico de colunas
grafico = contagem.plot(kind = 'barh', color = 'green', width=0.8)

# Adicionando rótulos e título
grafico.set_ylabel('Categoria\n', fontsize=14)  # Definindo tamanho da fonte do ylabel
grafico.set_xlabel('\nContagem', fontsize=14)   # Definindo tamanho da fonte do xlabel
plt.title('Gráfico de Barras - Proporção de Categorias', fontsize=16)
grafico.set_yticklabels(grafico.get_yticklabels(), rotation=0) # sem rotacao no eixo x
for indice, valor in enumerate(contagem):
    grafico.annotate(f'{valor}', xy=(valor, indice), ha='left', va='center')

# Definindo os intervalos de y - vale pra x se necessário
intervalos_x = np.arange(0, contagem.max() * 1.1, 1000)  # Intervalos de 1000 em 1000
grafico.set_xticks(intervalos_x)

# Exibindo o gráfico
plt.show()



# GRÁFICO DE BARRAS  - UNIDIMENSIONAL e PROPORÇÃO

contagem = df['Segmento'].value_counts(normalize=True)

# Plotando o gráfico de colunas
grafico = contagem.plot(kind = 'barh', color = 'green', width=0.8)

# Adicionando rótulos e título
grafico.set_ylabel('Categoria\n', fontsize=14)  # Definindo tamanho da fonte do ylabel
grafico.set_xlabel('\nContagem', fontsize=14)   # Definindo tamanho da fonte do xlabel
plt.title('Gráfico de Barras - Proporção de Categorias', fontsize=16)
grafico.set_yticklabels(grafico.get_yticklabels(), rotation=0) # sem rotacao no eixo x
for indice, valor in enumerate(contagem):
    grafico.annotate(f'{valor:.3f}', xy=(valor, indice), ha='left', va='center')

# Definindo os intervalos de y - vale pra x se necessário
intervalos_x = np.arange(0, 1, 0.1)  # Intervalos de 0.1 em 0.1
grafico.set_xticks(intervalos_x)

# Exibindo o gráfico
plt.show()



# GRÁFICO DE BARRAS - SUBSTITUINDO UM GRÁFICO DE PIZZA

# Calculando as proporções
proporcoes = df['Segmento'].value_counts(normalize=True)

# Plotando uma única barra dividida em seções proporcionais
fig, ax = plt.subplots()
cores = ['blue', 'green', 'red']  # Cores para as seções
inicio = 0

# Adicionando cada seção à barra
for categoria, proporcao in proporcoes.items():
    ax.barh(0, proporcao, left=inicio, color=cores.pop(), label=categoria)
    inicio += proporcao

    # Adicionando rótulo de dados
    ax.annotate(f'{proporcao:.2f}', xy=(inicio - proporcao / 2, 0), xytext=(0, 5),
                textcoords='offset points', ha='center', va='bottom')

# Configurações do gráfico
plt.xlabel('Proporção', fontsize=14)
plt.ylabel('Categoria', fontsize=14)
plt.title('Proporção de Categorias', fontsize=16)
plt.xlim(0, 1)  # Limites do eixo x de 0 a 1
plt.ylim(-0.5, 0.5)  # Limites do eixo y para centralizar a barra
plt.legend(loc='lower right')  # Adiciona legenda


# Exibindo o gráfico
plt.show()

