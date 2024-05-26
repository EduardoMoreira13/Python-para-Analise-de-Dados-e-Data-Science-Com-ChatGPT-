#!/usr/bin/env python
# coding: utf-8

# # <font color='blue'>Data Science Academy</font>
# 
# ## <font color='blue'>Fundamentos de Linguagem Python Para Análise de Dados e Data Science</font>
# 
# ## <font color='blue'>Capítulo 6 - Tratamento de Erros e Exceções</font>

# In[1]:


# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# ## Erros e Exceções
# 
# Sempre leia as mensagens de erro. Erros fazem parte do processo de aprendizagem e vão acompanhar você na sua jornada em programação, em qualquer linguagem.
# 
# ![DSA](imagens/mensagem_erro.png)

# In[2]:


# Erro (leia a mensagem de erro)
print('Hello)


# In[3]:


# Erro (leia a mensagem de erro)
8 + 's'


# In[4]:


# Criando uma função
def numDiv (num1, num2):
    resultado = num1 / num2
    print(resultado)


# In[5]:


# Execução não gera erro
numDiv(4,2)


# In[6]:


# Execução gerando erro (leia a mensagem de erro)
numDiv(4,0)


# ## Try, Except, Finally

# In[7]:


8 + 's'


# In[8]:


# Utilizando try e except
try:
    8 + 's'
except TypeError:
    print("Operação não permitida")


# In[9]:


# Utilizando try, except e else
try:
    f = open('arquivos/testandoerros.txt','w')
    f.write('Gravando no arquivo')
except IOError:
    print ("Erro: arquivo não encontrado ou não pode ser salvo.")
else:
    print ("Conteúdo gravado com sucesso!")
    f.close()


# In[10]:


# Utilizando try, except e else
try:
    f = open('arquivos/testandoerros','r')
except IOError:
    print ("Erro: arquivo não encontrado ou não pode ser lido.")
else:
    print ("Conteúdo gravado com sucesso!")
    f.close()


# In[11]:


# Utilizando try, except, else e finally
try:
    f = open('arquivos/testandoerros.txt','w')
    f.write('Gravando no arquivo')
except IOError:
    print ("Erro: arquivo não encontrado ou não pode ser salvo.")
else:
    print ("Conteúdo gravado com sucesso!")
    f.close()
finally:
    print ("Comandos no bloco finally são sempre executados!")


# > Cada possibilidade de erro deve ser tratada no seu programa.

# In[12]:


def askint():
    try:
        val = int((input("Digite um número: ")))
    except:
        print ("Você não digitou um número!")
    finally:
        print ("Obrigado!")


# In[13]:


askint()


# In[14]:


def askint():
        try:
            val = int(input("Digite um número: "))
        except:
            print ("Você não digitou um número!")
            val = int(input("Tente novamente. Digite um número: "))
        finally:
            print ("Obrigado!")
        print (val) 


# In[15]:


askint()


# In[16]:


def askint():
    while True:
        try:
            val = int(input("Digite um número: "))
        except:
            print ("Você não digitou um número!")
            continue
        else:
            print ("Obrigado por digitar um número!")
            break
        finally:
            print("Fim da execução!")
        print (val) 


# In[17]:


askint()


# Uma lista completa de exceções em Python pode ser encontrada aqui:
# 
# https://docs.python.org/3.9/library/exceptions.html

# # Fim

# ### Obrigado
# 
# ### Visite o Blog da Data Science Academy - <a href="http://blog.dsacademy.com.br">Blog DSA</a>
