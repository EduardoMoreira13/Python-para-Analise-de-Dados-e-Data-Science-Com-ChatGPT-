#!/usr/bin/env python
# coding: utf-8

# # <font color='blue'>Data Science Academy</font>
# 
# ## <font color='blue'>Fundamentos de Linguagem Python Para Análise de Dados e Data Science</font>
# 
# ## <font color='blue'>Capítulo 6 - Manipulação de Arquivos - Parte 2</font>

# In[1]:


# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# ## Manipulando Arquivos TXT
# 
# TXT é a extensão de arquivo para arquivos de texto puro. Um arquivo TXT é um arquivo de texto simples sem formatação, como negrito, itálico ou fontes diferentes. Ele pode ser aberto e editado com muitos aplicativos diferentes, incluindo editores de texto, processadores de texto e IDEs. Arquivos TXT são amplamente utilizados para armazenar dados de texto simples, como listas, notas e documentos de texto. Eles são universais e podem ser lidos em praticamente qualquer dispositivo ou sistema operacional.

# In[2]:


texto = "Cientista de Dados pode ser uma excelente alternativa de carreira.\n"
texto = texto + "Esses profissionais precisam saber como programar em Python.\n"
texto += "E, claro, devem ser proficientes em Data Science."


# In[3]:


print(texto)


# In[4]:


# Importando o módulo os
import os


# In[5]:


# Criando um arquivo 
arquivo = open(os.path.join('arquivos/cientista.txt'),'w')


# In[6]:


# Gravando os dados no arquivo
for palavra in texto.split():
    arquivo.write(palavra + ' ')


# In[7]:


# Fechando o arquivo
arquivo.close()


# In[8]:


# Lendo o arquivo
arquivo = open('arquivos/cientista.txt','r')
conteudo = arquivo.read()
arquivo.close()
print(conteudo)


# ### Usando a Expressão `with` 
# 
# O método close() é executado automaticamente.

# In[9]:


with open('arquivos/cientista.txt','r') as arquivo:
    conteudo = arquivo.read()


# In[10]:


print(len(conteudo))


# In[11]:


print(conteudo)


# In[12]:


with open('arquivos/cientista.txt','w') as arquivo:
    arquivo.write(texto[:19])
    arquivo.write('\n')
    arquivo.write(texto[28:66])


# In[13]:


# Lendo o arquivo
arquivo = open('arquivos/cientista.txt','r')
conteudo = arquivo.read()
arquivo.close()
print (conteudo)


# ## Manipulando Arquivos CSV 
# 
# CSV (Comma-Separated Values) é um formato de arquivo que armazena dados tabulares em formato de texto plano. Cada linha do arquivo CSV representa uma linha da tabela e as colunas são separadas por vírgulas. É amplamente utilizado para exportar e importar dados em diferentes aplicações, como planilhas e banco de dados. CSV é uma opção simples e universal para compartilhar dados, pois pode ser aberto e editado com muitos aplicativos diferentes, incluindo programas de planilha e editores de texto.

# In[14]:


# Importando o módulo csv
import csv


# In[15]:


with open('arquivos/numeros.csv','w') as arquivo:
    
    # Cria o objeto de gravação
    writer = csv.writer(arquivo)
    
    # Grava no arquivo linha a linha
    writer.writerow(('nota1', 'nota2', 'nota3'))
    writer.writerow((63,87,92)) 
    writer.writerow((61,79,76))
    writer.writerow((72,64,91))


# In[16]:


# Leitura de arquivos csv
with open('arquivos/numeros.csv', 'r', encoding='utf8', newline = '\r\n') as arquivo:
    
    # Cria o objeto de leitura
    leitor = csv.reader(arquivo)
    
    # Loop
    for x in leitor:
        print(x)


# In[17]:


# Gerando uma lista com dados do arquivo csv
with open('arquivos/numeros.csv','r') as arquivo:
    leitor = csv.reader(arquivo)
    dados = list(leitor)


# In[18]:


print(dados)


# In[19]:


# Impriminfo a partir da segunda linha
for linha in dados[1:]:
    print(linha)


# ## Manipulando Arquivos JSON (Java Script Object Notation )
# 
# JSON (JavaScript Object Notation) é um formato de dados de texto simples e leve que é utilizado para transmitir informações em aplicações web. É baseado em uma estrutura de objetos JavaScript e usa pares de chave-valor para representar dados. JSON é facilmente lido e escrito por máquinas e é amplamente utilizado como formato de intercâmbio de dados em aplicações web modernas.

# In[20]:


# Criando um dicionário
dict_guido = {'nome': 'Guido van Rossum',
              'linguagem': 'Python',
              'similar': ['c','Modula-3','lisp'],
              'users': 1000000}


# In[21]:


for k,v in dict_guido.items():
    print (k,v)


# In[22]:


# Importando o módulo JSON
import json


# In[23]:


# Convertendo o dicionário para um objeto json
json.dumps(dict_guido)


# In[24]:


# Criando um arquivo Json
with open('arquivos/dados.json','w') as arquivo:
    arquivo.write(json.dumps(dict_guido))


# In[25]:


# Leitura de arquivos Json
with open('arquivos/dados.json','r') as arquivo:
    texto = arquivo.read()
    dados = json.loads(texto)


# In[26]:


dados


# In[27]:


print(dados['nome'])


# ### Extração de Arquivo da Web

# In[28]:


# Imprimindo um arquivo JSON copiado da internet
from urllib.request import urlopen

response = urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode('utf8')
dados = json.loads(response)[0]


# In[29]:


dados


# In[30]:


print ('Título: ', dados['title'])
print ('URL: ', dados['url'])
print ('Duração: ', dados['duration'])
print ('Número de Visualizações: ', dados['stats_number_of_plays'])


# > Copiando o conteúdo de um arquivo para outro.

# In[31]:


# Nomes dos arquivos
arquivo_fonte = 'arquivos/dados.json'
arquivo_destino = 'arquivos/dados.txt'


# In[32]:


# Método 1
with open(arquivo_fonte,'r') as infile:
    text = infile.read()
    with open(arquivo_destino,'w') as outfile:
        outfile.write(text)  


# In[33]:


# Método 2
open(arquivo_destino,'w').write(open(arquivo_fonte,'r').read()) 


# In[34]:


# Leitura do arquivo txt
with open('arquivos/dados.txt','r') as arquivo:
    texto = arquivo.read()
    dados = json.loads(texto)


# In[35]:


print(dados)


# # FIM

# ### Obrigado
# 
# ### Visite o Blog da Data Science Academy - <a href="http://blog.dsacademy.com.br">Blog DSA</a>
