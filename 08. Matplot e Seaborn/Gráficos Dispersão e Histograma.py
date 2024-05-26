# GRÁFICOS VIA MATPLOTLIB

# PACOTES E DADOS

import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pylab import *

df = pd.read_csv("dataset.csv")
print(df.columns)


# HISTOGRAMA
valores = df['Valor_Venda']
bins = list(range(0,600,100))
plt.hist(valores, bins, histtype = 'bar', rwidth = 0.95)
plt.show()


# GRÁFICO DE DISPERSÃO
x = [1,2,3,4,5,6,7,8]
y = [5,2,4,5,6,8,4,8]

plt.scatter(x, y, label = 'Pontos', color = 'r', marker = 'o')
plt.legend()
plt.show()








