# GRÁFICOS VIA SEABORN


# PACOTES E DADOS
import random
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sea
import pandas as pd
import numpy as np

# Carregando um dos datasets que vem com o Seaborn
dados = sea.load_dataset("tips")
print(dados.head(10))

# O método joinplot cria plot de 2 variáveis com gráficos bivariados e univariados
sea.jointplot(data = dados, x = "total_bill", y = "tip", kind = 'reg')
plt.show()

# O método lmplot() cria plot com dados e modelos de regressão
sea.lmplot(data = dados, x = "total_bill", y = "tip", col = "smoker")
plt.show()

# Criando um dataframe
df = pd.DataFrame()

# Alimentando o Dataframe com valores aleatórios
df['idade'] = random.sample(range(20, 100), 30)
df['peso'] = random.sample(range(55, 150), 30)


# lmplot
sea.lmplot(data = df, x = "idade", y = "peso", fit_reg = True)
plt.show()

# kdeplot
sea.kdeplot(df.idade)
plt.show()

# kdeplot
sea.kdeplot(df.peso)
plt.show()

# distplot
sea.distplot(df.peso)
plt.show()

# Histograma
plt.hist(df.idade, alpha = .3)
sea.rugplot(df.idade)
plt.show()

# Box Plot
sea.boxplot(df.idade, color = 'm')
plt.show()

