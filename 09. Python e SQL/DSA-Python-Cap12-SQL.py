#!/usr/bin/env python
# coding: utf-8

# # <font color='blue'>Data Science Academy</font>
# 
# ## <font color='blue'>Fundamentos de Linguagem Python Para Análise de Dados e Data Science</font>
# 
# ## <font color='blue'>Análise de Dados com Python e Linguagem SQL</font>

# **Por Que a Linguagem SQL é Fundamental Para Profissionais de Dados?**
# 
# A Linguagem SQL (Structured Query Language) é fundamental para profissionais de dados por várias razões:
# 
# - **Padrão Universal**: SQL é uma linguagem padrão e amplamente aceita para gerenciamento e consulta de bancos de dados relacionais. Independentemente do sistema gerenciador de banco de dados (SGBD) utilizado, SQL é a linguagem comum para realizar consultas e manipulações de dados.
# 
# 
# - **Flexibilidade**: SQL permite criar consultas complexas e personalizadas, combinando dados de várias tabelas, filtrando informações e realizando operações de agregação e ordenação. Isso permite que os profissionais de dados extraiam informações valiosas a partir dos dados armazenados.
# 
# 
# - **Manipulação de Dados**: Além das consultas, SQL permite a inserção, atualização e exclusão de dados, bem como a definição de esquemas e gerenciamento de objetos de banco de dados, como tabelas, índices e visões.
# 
# 
# - **Controle de Acesso e Segurança**: SQL também oferece recursos para gerenciar o acesso e a segurança dos dados, permitindo aos profissionais de dados controlar quem pode acessar, modificar ou excluir informações no banco de dados.
# 
# 
# - **Alta Demanda no Mercado**: Profissionais de dados com habilidades em SQL estão em alta demanda, já que a linguagem é amplamente usada em várias áreas e setores. O conhecimento em SQL é uma habilidade essencial para cargos como <a href="https://www.datascienceacademy.com.br/bundle/formacao-analista-de-dados">Analista de Dados</a>, <a href="https://www.datascienceacademy.com.br/bundle/formacao-cientista-de-dados">Cientista de Dados</a>, <a href="https://www.datascienceacademy.com.br/bundle/formacao-engenheiro-de-dados">Engenheiro de Dados</a> e Administrador de Banco de Dados.
# 
# 
# - **Integração com Outras Ferramentas e Tecnologias**: SQL se integra facilmente com outras ferramentas e linguagens de programação, como Python, R, Java, entre outras. Isso permite que os profissionais de dados aproveitem o poder da Linguagem SQL em conjunto com outras tecnologias para analisar, visualizar e processar dados.
# 
# Dominar a linguagem SQL proporciona aos profissionais de dados uma base sólida para trabalhar com bancos de dados relacionais e extrair insights valiosos a partir deles. Aprender SQL é um passo essencial para qualquer pessoa que deseja ingressar ou progredir no campo da Análise e Ciência de dados. A Linguagem SQL é fundamental para profissionais de dados. 
# 
# **Onde Encontrar Material de Estudo?**
# 
# Além deste capítulo que estudaremos agora, veja onde encontrar material sobre SQL aqui na DSA:
# 
# - A Linguagem SQL (nível de introdução) é estudada em um capítulo inteiro no curso gratuito de <a href="https://www.datascienceacademy.com.br/course/microsoft-power-bi-para-business-intelligence-e-data-science">Microsoft Power BI Para Business Intelligence e Data Science</a>.
# 
# 
# - A Linguagem SQL é estudada em diversos Labs do curso <a href="https://www.datascienceacademy.com.br/course/power-bi-avancado-para-analise-de-dados-com-dax">Power BI Avançado Para Análise de Dados com DAX</a>.
# 
# 
# - A Linguagem SQL é estudada em detalhes no curso SQL Para Data Science, o primeiro da <a href="https://www.datascienceacademy.com.br/bundle/formacao-analista-de-dados">Formação Analista de Dados</a>.
# 
# 
# - A Linguagem SQL é estudada em 4 dos 6 cursos da <a href="https://www.datascienceacademy.com.br/bundle/formacao-cientista-de-dados">Formação Cientista de Dados</a> e usada em diversos Labs, Estudos de Caso, Mini-Projetos e Projetos.
# 
# 
# - A Linguagem SQL é estudada em um Lab completo no primeiro curso da <a href="https://www.datascienceacademy.com.br/bundle/formacao-engenheiro-de-dados">Formação Engenheiro de Dados</a> e usada nos projetos de diversos cursos da Formação.
# 
# 
# - A Linguagem SQL é estudada em um capítulo inteiro (nível avançado) no segundo curso da <a href="https://www.datascienceacademy.com.br/bundle/formacao-arquiteto-de-dados">Formação Arquiteto de Dados</a> e usada nos projetos de diversos cursos da Formação.
# 
# 
# - No curso de Excel Avançado, (curso de bônus gratuito e exclusivo para os alunos das Formações DSA) há um Lab demonstrando passo a passo como usar SQL dentro do Excel.

# ![DSA](imagens/dsa_cap12.png)

# In[1]:


# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# Para este capítulo usaremos o SQLite: https://sqlite.org/index.html

# In[2]:


import sqlite3


# In[3]:


sqlite3.sqlite_version


# In[4]:


import pandas as pd


# In[5]:


pd.__version__


# ## Conectando no Banco de Dados com Linguagem Python
# 
# Leia o manual em pdf no Capítulo 12 do curso com a descrição completa do que é a Linguagem SQL!

# In[6]:


# Conecta no banco de dados
con = sqlite3.connect('cap12_dsa.db')


# In[7]:


# Abre um cursor para percorrer os dados no banco de dados
cursor = con.cursor()


# In[8]:


# Query SQL para extrair os nomes das colunas no banco de dados
sql_query = """SELECT name FROM sqlite_master WHERE type = 'table';"""


# In[9]:


# Executa a query
cursor.execute(sql_query)


# In[10]:


# Visualiza o resultado
print(cursor.fetchall())


# > A query abaixo retorna todas as linhas e todas as colunas da tabela.

# In[11]:


# Cria uma instrução SQL
query1 = 'SELECT * FROM tb_vendas_dsa'


# In[12]:


# Executa a query no banco de dados
cursor.execute(query1)


# In[13]:


# List comprehension para visualizar os nomes das colunas
nomes_colunas = [description[0] for description in cursor.description]


# In[14]:


# Visualiza o resultado
print(nomes_colunas)


# In[15]:


# Retorna os dados da execução da query
dados = cursor.fetchall()


# In[16]:


# Visualiza os dados
dados


# ## Aplicando Linguagem SQL Direto no Banco de Dados com Linguagem Python

# > A query abaixo retorna a média de unidades vendidas.

# In[17]:


# Cria uma instrução SQL para calcular a média de unidades vendidas
query2 = 'SELECT AVG(Unidades_Vendidas) FROM tb_vendas_dsa'


# In[18]:


# Executa a query no banco de dados
cursor.execute(query2)


# In[19]:


# Visualiza o resultado
print(cursor.fetchall())


# > A query abaixo retorna a média de unidades vendidas por produto.

# In[20]:


# Cria uma instrução SQL para calcular a média de unidades vendidas por produto
query3 = 'SELECT Nome_Produto, AVG(Unidades_Vendidas) FROM tb_vendas_dsa GROUP BY Nome_Produto'


# In[21]:


# Executa a query no banco de dados
cursor.execute(query3)


# In[22]:


# Visualiza o resultado
cursor.fetchall()


# > A query abaixo retorna a média de unidades vendidas por produto se o valor unitario for maior do que 199.

# In[23]:


# Cria uma instrução SQL para calcular a média de unidades vendidas por produto,
# quando o valor unitário for maior que 199
query4 = """SELECT Nome_Produto, AVG(Unidades_Vendidas) 
            FROM tb_vendas_dsa 
            WHERE Valor_Unitario > 199 
            GROUP BY Nome_Produto"""


# In[24]:


# Executa a query no banco de dados
cursor.execute(query4)


# In[25]:


# Visualiza o resultado
cursor.fetchall()


# > A query abaixo retorna a média de unidades vendidas por produto se o valor unitario for maior do que 199 e somente se a média de unidades vendidas for maior do que 10.

# In[26]:


# Esta query está ERRADA!
query5 = """SELECT Nome_Produto, AVG(Unidades_Vendidas) 
            FROM tb_vendas_dsa 
            WHERE Valor_Unitario > 199 and AVG(Unidades_Vendidas) > 10
            GROUP BY Nome_Produto """


# In[27]:


# Executa a query no banco de dados
# cursor.execute(query5)


# In[28]:


# Cria uma instrução SQL para calcular a média de unidades vendidas por produto,
# quando o valor unitário for maior que 199, mas somente se a média de unidades vendidas for maior que 10
query5 = """SELECT Nome_Produto, AVG(Unidades_Vendidas) 
            FROM tb_vendas_dsa 
            WHERE Valor_Unitario > 199 
            GROUP BY Nome_Produto 
            HAVING AVG(Unidades_Vendidas) > 10"""


# In[29]:


# Executa a query no banco de dados
cursor.execute(query5)


# In[30]:


# Visualiza o resultado
cursor.fetchall()


# In[31]:


# Fecha o cursor e encerra a conexão
cursor.close()
con.close()


# ## Aplicando Linguagem SQL na Sintaxe do Pandas com Linguagem Python

# In[32]:


# Conecta no banco de dados
con = sqlite3.connect('cap12_dsa.db')


# In[33]:


# Abre um cursor para percorrer os dados no banco de dados
cursor = con.cursor()


# > A query abaixo retorna todas as linhas e todas as colunas da tabela.

# In[34]:


# Cria uma instrução SQL
query = 'SELECT * FROM tb_vendas_dsa'


# In[35]:


# Executa a query no banco de dados
cursor.execute(query)


# In[36]:


# Retorna os dados da execução da query
dados = cursor.fetchall()


# In[37]:


dados


# In[38]:


type(dados)


# In[39]:


# Carrega os dados como dataframe do Pandas
df = pd.DataFrame(dados, columns = ['ID_Pedido', 
                                    'ID_Cliente', 
                                    'Nome_Produto',
                                    'Valor_Unitario',
                                    'Unidades_Vendidas',
                                    'Custo'])


# In[40]:


df.head()


# In[41]:


# Fecha o cursor e encerra a conexão
cursor.close()
con.close()


# > A query abaixo retorna a média de unidades vendidas.

# In[42]:


# Calcula a média de unidades vendidas
media_unidades_vendidas = df['Unidades_Vendidas'].mean()


# In[43]:


type(media_unidades_vendidas)


# In[44]:


print(media_unidades_vendidas)


# > A query abaixo retorna a média de unidades vendidas por produto.

# In[45]:


# Calcula a média de unidades vendidas por produto
media_unidades_vendidas_por_produto = df.groupby('Nome_Produto')['Unidades_Vendidas'].mean()


# In[46]:


# Visualiza os 10 primeiros resultados
print(media_unidades_vendidas_por_produto.head(10))


# > A query abaixo retorna a média de unidades vendidas por produto se o valor unitario for maior do que 199.

# In[47]:


# Retorna a média de unidades vendidas por produto se o valor unitario for maior do que 199.
df[df['Valor_Unitario'] > 199].groupby('Nome_Produto')['Unidades_Vendidas'].mean()


# > A query abaixo retorna a média de unidades vendidas por produto se o valor unitario for maior do que 199 e somente se a média de unidades vendidas for maior do que 10.

# In[48]:


# Alternativa A
df[df['Valor_Unitario'] > 199].groupby('Nome_Produto').filter(lambda x: x['Unidades_Vendidas'].mean() > 10)


# In[49]:


# Alternativa B
df[df['Valor_Unitario'] > 199].groupby('Nome_Produto') \
                              .filter(lambda x: x['Unidades_Vendidas'].mean() > 10) \
                              .groupby('Nome_Produto')['Unidades_Vendidas'].mean()


# ## Sintaxe SQL x Sintaxe Pandas
# 
# As duas instruções abaixo retornam o mesmo resultado!

# In[50]:


# Sintaxe SQL
query5 = """SELECT Nome_Produto, AVG(Unidades_Vendidas) 
            FROM tb_vendas_dsa 
            WHERE Valor_Unitario > 199 
            GROUP BY Nome_Produto 
            HAVING AVG(Unidades_Vendidas) > 10"""


# In[51]:


# Sintaxe Pandas
df[df['Valor_Unitario'] > 199].groupby('Nome_Produto') \
                              .filter(lambda x: x['Unidades_Vendidas'].mean() > 10) \
                              .groupby('Nome_Produto')['Unidades_Vendidas'].mean()


# # Fim

# 
# ### Obrigado
# 
# ### Visite o Blog da Data Science Academy - <a href="http://blog.dsacademy.com.br">Blog DSA</a>
# 
