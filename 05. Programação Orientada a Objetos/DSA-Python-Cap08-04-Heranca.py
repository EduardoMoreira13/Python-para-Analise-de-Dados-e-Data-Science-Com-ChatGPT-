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


# ## Trabalhando com Herança de Classes em Python
# 
# Em Programação Orientada a Objetos (POO), a herança é um conceito que permite criar novas classes a partir de outras classes existentes, aproveitando os atributos e métodos da classe original e adicionando novos atributos e métodos específicos. 
# 
# A classe original é chamada de classe mãe ou superclasse e a nova classe criada é chamada de classe filha ou subclasse.
# 
# A herança é uma técnica importante em POO porque permite reutilizar o código de maneira eficiente. Em vez de criar uma nova classe do zero, a subclasse pode herdar todos os atributos e métodos da superclasse e adicionar apenas o que é necessário. Dessa forma, a subclasse pode se concentrar em fornecer funcionalidades adicionais sem precisar se preocupar com as características básicas da classe.
# 
# Na herança, uma subclasse pode herdar os atributos e métodos da superclasse e substituí-los ou estendê-los conforme necessário. Por exemplo, uma subclasse pode ter um método com o mesmo nome de um método da superclasse, mas com um comportamento diferente. 

# In[2]:


# Criando a classe Animal - Super-classe
class Animal:
    
    def __init__(self):
        print("Animal criado.")

    def imprimir(self):
        print("Este é um animal.")

    def comer(self):
        print("Hora de comer.")
        
    def emitir_som(self):
        pass


# In[3]:


# Criando a classe Cachorro - Sub-classe
class Cachorro(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print("Objeto Cachorro criado.")
    
    def emitir_som(self):
        print("Au au!")


# In[4]:


# Criando a classe Gato - Sub-classe
class Gato(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print("Objeto Gato criado.")
    
    def emitir_som(self):
        print("Miau!")


# In[5]:


# Criando um objeto (Instanciando a classe)
rex = Cachorro()


# In[6]:


# Criando um objeto (Instanciando a classe)
zeze = Gato()


# In[7]:


rex.emitir_som() 


# In[8]:


zeze.emitir_som() 


# In[9]:


# Executando o método da classe Cachorro (sub-classe)
rex.imprimir()


# In[10]:


# Executando o método da classe Animal (super-classe)
rex.comer()


# In[11]:


# Executando o método da classe Cachorro (sub-classe)
zeze.comer()


# # Fim

# ### Obrigado
# 
# ### Visite o Blog da Data Science Academy - <a href="http://blog.dsacademy.com.br">Blog DSA</a>
