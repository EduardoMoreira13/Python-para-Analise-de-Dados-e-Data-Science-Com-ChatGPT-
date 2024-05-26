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


# ## Trabalhando com Polimorfismo de Classes em Python
# 
# Polimorfismo é um dos conceitos fundamentais da Programação Orientada a Objetos (POO). O polimorfismo permite que objetos de diferentes classes possam ser tratados de forma uniforme. Isso significa que um objeto pode ser tratado como se fosse um objeto de uma superclasse, mesmo que ele seja de uma subclasse.
# 
# Mais especificamente, o polimorfismo se refere à habilidade de um objeto responder de diferentes formas a uma mesma mensagem. Isso é possível porque as subclasses podem implementar métodos com o mesmo nome que os métodos da superclasse, mas com comportamentos diferentes.
# 
# Com o Polimorfismo, os mesmos atributos e métodos podem ser utilizados em objetos distintos, porém, com implementações lógicas diferentes.

# In[2]:


# Superclasse
class Veiculo:
    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        pass

    def frear(self):
        pass


# In[3]:


# Subclasse
class Carro(Veiculo):
    
    def acelerar(self):
        print("O carro está acelerando.")

    def frear(self):
        print("O carro está freando.")


# In[4]:


# Subclasse
class Moto(Veiculo):
    
    def acelerar(self):
        print("A moto está acelerando.")

    def frear(self):
        print("A moto está freando.")


# In[5]:


# Subclasse
class Aviao(Veiculo):
    
    def acelerar(self):
        print("O avião está acelerando.")

    def frear(self):
        print("O avião está freando.")

    def decolar(self):
        print("O avião está decolando.")


# In[6]:


# Cria os objetos
lista_veiculos = [Carro("Porsche", "911 Turbo"), Moto("Honda", "CB 1000R Black Edition"), Aviao("Boeing", "757")]


# In[7]:


type(lista_veiculos)


# In[8]:


# Loop
for item in lista_veiculos:
    
    # O método acelerar tem comportamento diferente dependendo do tipo de objeto
    item.acelerar()
    
    # O método frear tem comportamento diferente dependendo do tipo de objeto
    item.frear()

    # Executamos o método decolar somente se o o objeto for instância da classe Aviao
    if isinstance(item, Aviao):
        item.decolar()

    print("---")


# # Fim

# ### Obrigado
# 
# ### Visite o Blog da Data Science Academy - <a href="http://blog.dsacademy.com.br">Blog DSA</a>
