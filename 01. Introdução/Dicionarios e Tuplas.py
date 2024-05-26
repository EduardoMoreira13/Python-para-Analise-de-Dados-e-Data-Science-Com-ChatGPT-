### Dicionarios e Tuplas


# Listas possuem elementos independentes

lista = ["Eduardo", 25, "Ana", 23, "Fernando", 30]
lista


# Dicionarios possuem elementos dependentes, ou seja, temos um conjunto de informacoes para cada elemento

dicionario = {"Eduardo":25, "Ana":23, "Fernando":30}
print(dicionario)
dicionario["Eduardo"]


dicionario = {1:(25,4,8), 2:(23,7,8), 3:(30,7,7)}
dicionario
dicionario[1]


# Adicionar uma informacao

dicionario = {"Eduardo":25, "Ana":23, "Fernando":30}
dicionario["Marcelo"] = 28
print(dicionario)


# Deixar um dicionario vazio

dicionario.clear()
print(dicionario)


# Deletar um dicionario

del dicionario
# print(dicionario)


# Obter Valores do dicionario

dicionario = {"Eduardo":25, "Ana":23, "Fernando":30}

dicionario.values()


# Obter tamanho do dicionario

dicionario = {"Eduardo":25, "Ana":23, "Fernando":30}

len(dicionario)


# Obter items do dicionario

dicionario = {"Eduardo":25, "Ana":23, "Fernando":30}

dicionario.items()


# Atualizar e copiar o dicionario

dicionario1 = {"Eduardo":25, "Ana":23, "Fernando":30}
dicionario2 = {"Angela":23, "Marina":18}

dicionario1.update(dicionario2)
print(dicionario1)
dicionario1


# Dicionario Vazio

dicionario = {}
dicionario["Eduardo"] = 23
dicionario


# Dicionario contendo listas

dicionario = {"Lista1":[25,30,"Eduardo"], "Lista2":[22,30,"Ana"], "Lista3":[34,22,"Eddie",36]}
dicionario


dicionario["Lista1"]
dicionario["Lista1"][2]


# Selecao de elemento e aplicando funcoes

dicionario["Lista1"][2] = dicionario["Lista1"][2].upper()

dicionario


# Duas operacoes ao mesmo tempo

# dicionario["Lista1"][0] = dicionario["Lista1"][0] - 2
print(dicionario["Lista1"][0])
dicionario["Lista1"][0] -=2
print(dicionario["Lista1"][0])


### Dicionarios Aninhados

# Criando dicionarios aninhados

dicionario = {"Key1": {"Key2":{"Key3":"Aninhada"}}}
dicionario


dicionario['Key1']['Key2']['Key3']


# ### Tuplas - estruturas sem alteracao


tupla = ("Eduardo", 25, "Ana", 23, "Fernando", 30) 
tupla


# Deletando uma tupla

del tupla
#tupla


# Conversao em uma lista

tupla = ("Eduardo", 25, "Ana", 23, "Fernando", 30) 
tupla = list(tupla)
type(tupla)

