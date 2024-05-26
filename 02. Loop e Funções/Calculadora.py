#!/usr/bin/env python
# coding: utf-8

# ### Calculadora

# In[19]:


print("\n************************ Calculadora em Python ************************\n")

print("Selecione o numero da operacao desejada:\n", "\n1 - Soma", "\n2 - Subtracão", 
      "\n3 - Multiplicacão", "\n4 - Divisão\n")

operacao = int(input('Digite sua opcão (1/2/3/4): '))
print(" ")

erro1 = "Operacao Invalida! \nPor favor, digite 1, 2, 3 ou 4 considerando os tipos de operacoes informadas."

while operacao not in range(1,5,1):
    print(erro1, "\n")
    operacao = int(input('Digite sua opcão (1/2/3/4): '))

num1 = float(input('Digite o primeiro numero: '))
print(" ")

num2 = float(input('Digite o segundo numero: '))
print(" ")

if operacao == 1:
    print("%r + %r =" %(num1,num2),  num1 + num2)
elif operacao == 2:
    print("%r - %r =" %(num1,num2),  num1 - num2)
elif operacao == 3:
    print("%r * %r =" %(num1,num2),  num1 * num2)
else:
    print("%r / %r =" %(num1,num2),  num1 / num2)


# In[8]:


print("\n************************ Calculadora em Python ************************\n")

print("Selecione o numero da operacao desejada:\n", "\n1 - Soma", "\n2 - Subtracão", 
      "\n3 - Multiplicacão", "\n4 - Divisão\n")

operacao = int(input('Digite sua opcão (1/2/3/4): '))
print(" ")

num1 = float(input('Digite o primeiro numero: '))
print(" ")

num2 = float(input('Digite o segundo numero: '))
print(" ")

erro1 = "Operacao Invalida! \nPor favor, digite 1, 2, 3 ou 4 considerando os tipos de operacoes existentes."

def add(x, y):
    return x + y
    
def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

if operacao == 1:
    print("%r + %r =" %(num1,num2),  add(num1, num2))
elif operacao == 2:
    print("%r - %r =" %(num1,num2),  subtract(num1, num2))
elif operacao == 3:
    print("%r * %r =" %(num1,num2), multiply(num1, num2))
elif operacao == 4:
    print("%r / %r =" %(num1,num2),  divide(num1, num2))
else: 
    print(erro1, "\n")
    


# In[ ]:





# In[ ]:




