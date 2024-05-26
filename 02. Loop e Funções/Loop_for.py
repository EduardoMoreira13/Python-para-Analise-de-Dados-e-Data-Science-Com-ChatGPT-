### Loop for

# Criando uma tupla e imprimindo cada elemento na tela

tp = (2,3,4) 
for i in tp:
    print(i)


# Criando uma lista e imprimindo cada elemento na tela

lista = ["Eduardo", "Ana", "Fernando"]

for i in lista:
    print(i)

# Imprimindo os valores no intervalo de 0 a 5 (exclusive) e de 3 a 15 (exclusive) a cada 3 valores

for contador in range(0,5,1):
    print(contador)
    
for contador in range(3,15,3):
    print(contador)


# Imprimindo os numeros pares - for e if

lista = list(range(1,101,1))

for num in lista:
    if num % 2 == 0:
        print(num)


# Strings tambem sao sequencias

for letra in "Eduardo Moreira":
    print(letra)


# ### Loop Aninhado

lista1 = [0,1,2,3,4]
lista2 = [1,2,3]

# Loop externo
for elemento_lista1 in lista1:
    
    # Loop interno
    for elemento_lista2 in lista2:
        print("\n", elemento_lista1 * elemento_lista2)
        
    print("\n----")


# Some os numeros pares da primeira lista com os numeros pares da segunda lista

lista1 = [10, 16, 24, 39, 47]
lista2 = [32, 89, 47, 76, 12]
soma = 0

# Loop externo
for lista in [lista1,lista2]:
    
    # Loop interno
    for num in lista:
        
        if num % 2 == 0:
            soma += num
            
print("A soma dos numeros pares das duas listas e igual a", soma)


# In[ ]:


# Mais de um indice no comando for

dicionario = {"K1":23,"K2":30,"K2":33}

for k,v in dicionario.items():
    print(k,v)


# Loop em lista de listas (matrizes) para encontrar o maior numero

matriz = [[42,23,24],[100,215,114],[10.1,98.7,12.3]]
maiornum = 0


# Loop externo
for linha in matriz:
    
    # Loop interno
    for num in linha:
        
        # Condicional
        if num > maiornum:
            maiornum = num
            
print("Maior numero:", maiornum)
    
    







