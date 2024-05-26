#!/usr/bin/env python
# coding: utf-8

# # <font color='blue'>Data Science Academy</font>
# 
# ## <font color='blue'>Fundamentos de Linguagem Python Para Análise de Dados e Data Science</font>
# 
# ## <font color='blue'>Introdução à Programação Orientada a Objetos</font>

# In[1]:


# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# ## Objetos

# Em Python, Tudo é Objeto!

# In[2]:


# Criando uma lista
lst_num = ["Data", "Science", "Academy", "Nota", 10, 10]


# In[3]:


# A lista lst_num é um objeto, uma instância da classe lista em Python
type(lst_num)


# In[4]:


print(type([]))


# In[5]:


lst_num.count(10)


# In[6]:


# Usamos a função type, para verificar o tipo de um objeto
print(type(10))
print(type([]))
print(type(()))
print(type({}))
print(type('a'))


# In[7]:


# Criando um novo tipo de objeto chamado Carro
class Carro(object):
    pass


# In[8]:


# Instância do Carro
ferrari = Carro()


# In[9]:


print(type(ferrari))


# In[10]:


# Criando uma classe
class Estudantes:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota


# In[11]:


# Criando um objeto chamado Estudante1 a partir da classe Estudantes
Estudante1 = Estudantes("Bob", 12, 9.5)


# In[12]:


# Atributo da classe Estudante, utilizado por cada objeto criado a partir desta classe
Estudante1.nome


# In[13]:


# Atributo da classe Estudante, utilizado por cada objeto criado a partir desta classe
Estudante1.idade


# In[14]:


# Atributo da classe Estudante, utilizado por cada objeto criado a partir desta classe
Estudante1.nota


# In[15]:


# Criando uma classe
class Funcionarios:
    
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def listFunc(self):
        print("Funcionário(a) " + self.nome + " tem salário de R$" + str(self.salario) + " e o cargo é " + self.cargo)


# In[16]:


# Criando um objeto chamado Func1 a partir da classe Funcionarios
Func1 = Funcionarios("Mary", 20000, "Cientista de Dados")


# In[17]:


# Usando o método da classe
Func1.listFunc()


# In[18]:


print("**** Usando atributos *****")


# In[19]:


hasattr(Func1, "nome")


# In[20]:


hasattr(Func1, "salario")


# In[21]:


setattr(Func1, "salario", 4500)


# In[22]:


hasattr(Func1, "salario")


# In[23]:


getattr(Func1, "salario")


# In[24]:


delattr(Func1, "salario")


# In[25]:


hasattr(Func1, "salario")


# # Fim

# ### Obrigado
# 
# ### Visite o Blog da Data Science Academy - <a href="http://blog.dsacademy.com.br">Blog DSA</a>
