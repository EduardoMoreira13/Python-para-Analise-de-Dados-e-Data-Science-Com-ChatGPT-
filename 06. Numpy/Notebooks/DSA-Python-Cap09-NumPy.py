# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# Importando o NumPy
import numpy as dsa

dsa.__version__


# In[4]:


# Instrução para instalar uma versão exata do pacote em Python
# !pip install numpy==1.22.2


# ### Criando Arrays NumPy

# In[5]:


# Array criado a partir de uma lista Python
arr1 = dsa.array([10, 21, 32, 43, 48, 15, 76, 57, 89])


# In[6]:


print(arr1)


# In[7]:


# Um objeto do tipo ndarray é um recipiente multidimensional de itens do mesmo tipo e tamanho
type(arr1)


# In[8]:


# Verificando o formato do array
arr1.shape


# Um array NumPy é uma estrutura de dados multidimensional usada em computação científica e análise de dados. O NumPy fornece um objeto de matriz N-dimensional (ou ndarray), que é uma grade homogênea de elementos, geralmente números, que podem ser indexados por um conjunto de inteiros.
# 
# Os arrays NumPy são mais eficientes do que as listas Python para armazenar e manipular grandes quantidades de dados, pois são implementados em Linguagem C e fornecem várias otimizações de desempenho. Além disso, o NumPy permite a fácil leitura e escrita de arquivos de dados, integração com outras bibliotecas Python e suporte a operações em paralelo usando várias CPUs ou GPUs.

# ![DSA](imagens/formatos.png)

# ### Indexação em Arrays NumPy

# In[9]:


print(arr1)


# In[10]:


# Imprimindo um elemento específico no array
arr1[4] 


# In[11]:


# Indexação
arr1[1:4] 


# In[12]:


# Indexação
arr1[1:4+1] 


# In[13]:


# Cria uma lista de índices
indices = [1, 2, 5, 6]


# In[14]:


# Imprimindo os elementos dos índices
arr1[indices] 


# In[15]:


# Cria uma máscara booleana para os elementos pares
mask = (arr1 % 2 == 0)


# In[16]:


mask


# In[17]:


arr1[mask]


# In[18]:


# Alterando um elemento do array
arr1[0] = 100


# In[19]:


print(arr1)


# In[20]:


# Não é possível incluir elemento de outro tipo
try:
    arr1[0] = 'Novo elemento'
except:
    print("Operação não permitida!")


# ### Funções NumPy

# In[21]:


# A função array() cria um array NumPy
arr2 = dsa.array([1, 2, 3, 4, 5])


# In[22]:


print(arr2)


# In[23]:


# Verificando o tipo do objeto
type(arr2)


# In[24]:


# Digite . e pressione a tecla Tab no seu teclado para visualizar os métodos disponíveis em objetos NumPy
arr2


# In[25]:


# Usando métodos do array NumPy
arr2.cumsum()


# In[26]:


arr2.cumprod()


# In[27]:


# Digite . e pressione a tecla Tab no seu teclado para visualizar as funções para manipular objetos NumPy
dsa


# In[28]:


# A função arange cria um array NumPy contendo uma progressão aritmética a partir de um intervalo - start, stop, step
arr3 = dsa.arange(0, 50, 5)


# In[29]:


print(arr3)


# In[30]:


# Verificando o tipo do objeto
type(arr3)


# In[31]:


# Formato do array
dsa.shape(arr3)


# In[32]:


print(arr3.dtype)


# In[33]:


# Cria um array preenchido com zeros
arr4 = dsa.zeros(10)


# In[34]:


print(arr4)


# In[35]:


# Retorna 1 nas posições em diagonal e 0 no restante
arr5 = dsa.eye(3)


# In[36]:


print(arr5)


# In[37]:


# Os valores passados como parâmetro, formam uma diagonal
arr6 = dsa.diag(dsa.array([1, 2, 3, 4]))


# In[38]:


print(arr6)


# In[39]:


# Array de valores booleanos
arr7 = dsa.array([True, False, False, True])


# In[40]:


print(arr7)


# In[41]:


# Array de strings
arr8 = dsa.array(['Linguagem Python', 'Linguagem R', 'Linguagem Julia'])


# In[42]:


print(arr8)


# A função linspace() do NumPy é usada para criar uma sequência de números igualmente espaçados dentro de um intervalo especificado. Essa função é amplamente utilizada em programação científica e matemática para gerar arrays de números para diversos fins, como gráficos, cálculos e simulações.
# 
# O método linspace (linearly spaced vector) retorna um número de valores igualmente distribuídos no intervalo especificado. 

# In[43]:


print(dsa.linspace(0, 10))


# In[44]:


print(dsa.linspace(0, 10, 15))


# A função logspace() do NumPy é usada para criar uma sequência de números igualmente espaçados em escala logarítmica dentro de um intervalo especificado. Essa função é amplamente utilizada em programação científica e matemática para gerar arrays de números para diversos fins, como gráficos, cálculos e simulações.

# In[45]:


print(dsa.logspace(0, 5, 10))


# ### Manipulando Matrizes

# In[46]:


# Criando uma matriz
arr9 = dsa.array( [ [1,2,3] , [4,5,6] ] ) 


# In[47]:


type(arr9)


# In[48]:


print(arr9)


# In[49]:


print(arr9.shape)


# In[50]:


# Criando uma matriz 2x3 apenas com números "1"
arr10 = dsa.ones((2,3))


# In[51]:


print(arr10)


# In[52]:


# Lista de listas
lista = [[13,81,22], [0, 34, 59], [21, 48, 94]]


# In[53]:


# A função matrix cria uma matriz a partir de uma lista de listas
arr11 = dsa.matrix(lista)


# In[54]:


type(arr11)


# In[55]:


print(arr11)


# In[56]:


# Formato da matriz
dsa.shape(arr11)


# In[57]:


# Tamanho da matriz
arr11.size


# In[58]:


print(arr11.dtype)


# In[59]:


print(arr11)


# In[60]:


# Indexação da matriz
arr11[2,1]


# In[61]:


# Indexação da matriz
arr11[0:2,2]


# In[62]:


# Indexação da matriz
arr11[1,]


# In[63]:


# Alterando um elemento da matriz
arr11[1,0] = 100


# In[64]:


print(arr11)


# In[65]:


x = dsa.array([1, 2])  # NumPy decide o tipo dos dado
y = dsa.array([1.0, 2.0])  # NumPy decide o tipo dos dado
z = dsa.array([1, 2], dtype = dsa.float64)  # Forçamos um tipo de dado em particular


# In[66]:


print(x.dtype, y.dtype, z.dtype)


# In[67]:


arr12 = dsa.array([[24, 76, 92, 14], [47, 35, 89, 2]], dtype = float)


# In[68]:


print(arr12)


# O itemsize de um array numpy é um atributo que retorna o tamanho em bytes de cada elemento do array. Em outras palavras, o itemsize representa o número de bytes necessários para armazenar cada valor do array numpy.

# In[69]:


arr12.itemsize


# In[70]:


arr12.nbytes


# In[71]:


arr12.ndim


# ### Manipulando Objetos de 3 e 4 Dimensões com NumPy

# In[72]:


# Cria um array numpy de 3 dimensões
arr_3d = dsa.array([
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ],
    [
        [13, 14, 15, 16],
        [17, 18, 19, 20],
        [21, 22, 23, 24]
    ]
])


# In[73]:


print(arr_3d)


# In[74]:


arr_3d.ndim


# In[75]:


arr_3d.shape


# In[76]:


arr_3d[0, 2, 1]


# In[77]:


# Cria um array numpy de 4 dimensões
arr_4d = dsa.array([
    [
        [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20]
        ],
        [
            [21, 22, 23, 24, 25],
            [26, 27, 28, 29, 30],
            [31, 32, 33, 34, 35],
            [36, 37, 38, 39, 40]
        ],
        [
            [41, 42, 43, 44, 45],
            [46, 47, 48, 49, 50],
            [51, 52, 53, 54, 55],
            [56, 57, 58, 59, 60]
        ]
    ],
    [
        [
            [61, 62, 63, 64, 65],
            [66, 67, 68, 69, 70],
            [71, 72, 73, 74, 75],
            [76, 77, 78, 79, 80]
        ],
        [
            [81, 82, 83, 84, 85],
            [86, 87, 88, 89, 90],
            [91, 92, 93, 94, 95],
            [96, 97, 98, 99, 100]
        ],
        [
            [101, 102, 103, 104, 105],
            [106, 107, 108, 109, 110],
            [111, 112, 113, 114, 115],
            [116, 117, 118, 119, 120]
        ]
    ]
])


# In[78]:


print(arr_4d)


# In[79]:


arr_4d.ndim


# In[80]:


arr_4d.shape


# In[81]:


arr_4d[0, 2, 1]


# In[82]:


arr_4d[0, 2, 1, 4]


# ### Manipulando Arquivos com NumPy

# In[83]:


import os
filename = os.path.join('dataset.csv')


# In[84]:


# No Windows use !more dataset.csv. Mac ou Linux use !head dataset.csv
get_ipython().system('head dataset.csv')
#!more dataset.csv


# In[85]:


# Carregando um dataset para dentro de um array
arr13 = dsa.loadtxt(filename, delimiter = ',', usecols = (0,1,2,3), skiprows = 1)


# In[86]:


print(arr13)


# In[87]:


type(arr13)


# In[88]:


# Carregando apenas duas variáveis (colunas) do arquivo
var1, var2 = dsa.loadtxt(filename, delimiter = ',', usecols = (0,1), skiprows = 1, unpack = True)


# In[89]:


# Gerando um plot a partir de um arquivo usando o NumPy
import matplotlib.pyplot as plt
plt.show(plt.plot(var1, var2, 'o', markersize = 6, color = 'red'))


# ### Análise Estatística Básica com NumPy

# In[90]:


# Criando um array
arr14 = dsa.array([15, 23, 63, 94, 75])


# Em Estatística, a média é uma medida de tendência central que representa o valor central de um conjunto de dados. É calculada somando-se todos os valores do conjunto de dados e dividindo-se pelo número de observações.

# In[91]:


# Média
dsa.mean(arr14)


# O desvio padrão é uma medida estatística de dispersão que indica o quanto os valores de um conjunto de dados se afastam da média. Ele é calculado como a raiz quadrada da variância, que é a média dos quadrados das diferenças entre cada valor e a média.
# 
# O desvio padrão é uma medida útil porque permite avaliar a variabilidade dos dados em torno da média. Se os valores estiverem próximos da média, o desvio padrão será baixo, indicando que os dados têm pouca variabilidade. Por outro lado, se os valores estiverem muito distantes da média, o desvio padrão será alto, indicando que os dados têm alta variabilidade.
# 
# O desvio padrão é amplamente utilizado em Análise e Ciência de Dados, para avaliar a consistência dos dados e comparar conjuntos de dados diferentes. É importante notar que o desvio padrão pode ser influenciado por valores extremos (outliers) e pode ser afetado por diferentes distribuições de dados.

# In[92]:


# Desvio Padrão (Standard Deviation)
dsa.std(arr14)


# A variância é uma medida estatística que quantifica a dispersão dos valores em um conjunto de dados em relação à média. Ela é calculada como a média dos quadrados das diferenças entre cada valor e a média.
# 
# A fórmula para o cálculo da variância é:
# 
# var = 1/n * Σ(xi - x̄)^2
# 
# Onde:
# 
# - var é a variância
# - n é o número de observações
# - Σ é o somatório
# - xi é o i-ésimo valor no conjunto de dados
# - x̄ é a média dos valores
# 
# A variância é uma medida útil para avaliar a variabilidade dos dados em torno da média. Se a variância for baixa, isso indica que os valores estão próximos da média e têm pouca variabilidade. Por outro lado, se a variância for alta, isso indica que os valores estão distantes da média e têm alta variabilidade.

# In[93]:


# Variância
dsa.var(arr14)


# Leia o manual em pdf no Capítulo 9 sobre quando usar variância e desvio padrão para análise de dados.

# ### Operações Matemáticas com Arrays NumPy

# In[94]:


arr15 = dsa.arange(1, 10)


# In[95]:


print(arr15)


# In[96]:


# Soma dos elementos do array
dsa.sum(arr15)


# In[97]:


# Retorna o produto dos elementos
dsa.prod(arr15)


# In[98]:


# Soma acumulada dos elementos
dsa.cumsum(arr15)


# In[99]:


# Cria 2 arrays
arr16 = dsa.array([3, 2, 1])
arr17 = dsa.array([1, 2, 3])


# In[100]:


# Soma dos arrays
arr18 = dsa.add(arr16, arr17)  


# In[101]:


print(arr18)  


# Para multiplicar duas matrizes NumPy, podemos usar a função dot() ou o operador @. Ambos os métodos executam a multiplicação matricial. É importante lembrar que, para que a multiplicação de matrizes possa ser executada, o número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz.
# 
# Há várias formas de multiplicar elementos de matrizes NumPy. A função dot() é um método bastante utilizado.

# In[102]:


# Cria duas matrizes
arr19 = dsa.array([[1, 2], [3, 4]])
arr20 = dsa.array([[5, 6], [0, 7]])


# In[103]:


arr19.shape


# In[104]:


arr20.shape


# In[105]:


print(arr19)


# In[106]:


print(arr20)


# In[107]:


# Multiplicar as duas matrizes
arr21 = dsa.dot(arr19, arr20)


# In[108]:


print(arr21)  


# ![DSA](imagens/dot.png)

# In[109]:


# Multiplicar as duas matrizes
arr21 = arr19 @ arr20


# In[110]:


print(arr21)  


# In[111]:


# Multiplicar as duas matrizes
arr21 = dsa.tensordot(arr19, arr20, axes = ((1),(0)))


# In[112]:


print(arr21)  


# ### Slicing (Fatiamento) de Arrays NumPy

# In[113]:


# Cria um array
arr22 = dsa.diag(dsa.arange(3))


# In[114]:


print(arr22)


# In[115]:


arr22[1, 1]


# In[116]:


arr22[1]


# In[117]:


arr22[:,2]


# In[118]:


arr23 = dsa.arange(10)


# In[119]:


print(arr23)


# In[120]:


# [start:end:step]
arr23[2:9:3] 


# In[121]:


# Cria 2 arrays
a = dsa.array([1, 2, 3, 4])
b = dsa.array([4, 2, 2, 4])


# In[122]:


# Comparação item a item
a == b


# In[123]:


# Comparação global
dsa.array_equal(arr22, arr23)


# In[124]:


arr23.min()


# In[125]:


arr23.max()


# In[126]:


# Somando um valor a cada elemento do array
dsa.array([1, 2, 3]) + 1.5


# In[127]:


# Cria um array
arr24 = dsa.array([1.2, 1.5, 1.6, 2.5, 3.5, 4.5])


# In[128]:


print(arr24)


# In[129]:


# Usando o método around
arr25 = dsa.around(arr24)


# In[130]:


print(arr25)


# In[131]:


# Criando um array
arr26 = dsa.array([[1, 2, 3, 4], [5, 6, 7, 8]])


# In[132]:


print(arr26)


# O método flatten() com NumPy é usado para criar uma cópia unidimensional (ou "achatada") de um array multidimensional. Isso significa que o método cria um novo array unidimensional, que contém todos os elementos do array multidimensional original, mas que está organizado em uma única linha. A ordem dos elementos no novo array unidimensional segue a ordem dos elementos no array multidimensional original.

# In[133]:


# "Achatando" a matriz
arr27 = arr26.flatten()


# In[134]:


print(arr27)


# In[135]:


# Criando um array
arr28 = dsa.array([1, 2, 3])


# In[136]:


print(arr28)


# In[137]:


# Repetindo os elementos de um array
dsa.repeat(arr28, 3)


# In[138]:


# Repetindo os elementos de um array
dsa.tile(arr28, 3)


# In[139]:


# Criando um array
arr29 = dsa.array([5, 6])


# In[140]:


# Criando cópia do array
arr30 = dsa.copy(arr29)


# In[141]:


print(arr30)


# O NumPy é estudado em detalhes em diversos cursos e Formações aqui na DSA, através de exercícios, laboratórios, estudos de caso, mini-projetos e projetos.

# # Fim

# 
# ### Obrigado
# 
# ### Visite o Blog da Data Science Academy - <a href="http://blog.dsacademy.com.br">Blog DSA</a>
# 
