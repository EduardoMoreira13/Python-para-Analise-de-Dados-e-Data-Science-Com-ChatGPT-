# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# ## Função Map

# A função map() em Python é uma função que aplica uma determinada função a cada elemento de uma estrutura
# de dados iterável (como uma lista, tupla ou outro objeto iterável). A função map() retorna um objeto que pode
# ser convertido em outra estrutura de dados, como uma lista, se necessário.

# In[2]:


# Função Python que retorna um número ao quadrado
def potencia(x):
    return x ** 2


# In[3]:


numeros = [1, 2, 3, 4, 5]


# In[4]:


numeros_ao_quadrado = list(map(potencia, numeros))


# In[5]:


print(numeros_ao_quadrado)


# In[6]:


# Criando duas funções

# Função 1 - Recebe uma temperatura como parâmetro e retorna a temperatura em Fahrenheit
def fahrenheit(T):
    return ((float(9)/5)*T + 32)

# Função 2 - Recebe uma temperatura como parâmetro e retorna a temperatura em Celsius
def celsius(T):
    return (float(5)/9)*(T-32)


# In[7]:


# Criando uma lista
temperaturas = [0, 22.5, 40, 100]


# In[8]:


# Aplicando a função a cada elemento da lista de temperaturas. 
# Em Python 3, a funçãp map() retornar um iterator
map(fahrenheit, temperaturas)


# In[9]:


# Função map() retornando a lista de temperaturas convertidas em Fahrenheit
list(map(fahrenheit, temperaturas))


# In[10]:


# Usando um loop for para imprimir o resultado da função map()
for temp in map(fahrenheit, temperaturas):
    print(temp)


# In[11]:


# Convertendo para Celsius
map(celsius, temperaturas)


# In[12]:


list(map(celsius, temperaturas))


# In[13]:


# Usando expressão lambda
map(lambda x: (5.0/9)*(x - 32), temperaturas)


# In[14]:


list(map(lambda x: (5.0/9)*(x - 32), temperaturas))


# In[15]:


# Somando os elementos de 2 listas
a = [1,2,3,4]
b = [5,6,7,8]


# In[16]:


list(map(lambda x,y:x+y, a, b))


# In[17]:


# Somando os elementos de 3 listas
a = [1,2,3,4]
b = [5,6,7,8]
c = [9,10,11,12]


# In[18]:


list(map(lambda x, y, z : x + y + z, a, b, c))


# # Fim

# ### Obrigado
# 
# ### Visite o Blog da Data Science Academy - <a href="http://blog.dsacademy.com.br">Blog DSA</a>
