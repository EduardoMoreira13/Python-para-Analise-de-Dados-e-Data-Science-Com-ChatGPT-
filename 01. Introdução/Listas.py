### Listas

lista_1 = ["arroz, frango, tomate, leite"]
lista_1
type(lista_1)

lista_2 = ["arroz", 'frango', "tomate", "leite"]
lista_2


lista_3 = [23, 300, "Estatistica",]
lista_3

item1 = lista_3[0]
item2 = lista_3[1]
item3 = lista_3[2]

print(item1,item2,item3)


# ### Deletando

del lista_2[3]


lista_2


### Listas dentro de Listas


listas = [[1,2,3],[10,15,14],[10.1,8.7,2.3]]

listas


a = listas[0]
a
a = listas[0][1]
a
b = listas[0] * 3
b 


### Concatenando Listas

lista_s1 = [34,32,56]
lista_s2 = [21,90,51]

lista_total = lista_s1 + lista_s2
lista_total


### Funcoes Built-in


lista_numeros = [10,20,50,-3.4]

# tamanho da lista

len(lista_numeros)

# valor maximo da lista

max(lista_numeros)

# valor minimo da lista

min(lista_numeros)


lista = ["1","2","3","4"]
lista


# Adicionando informacao

lista.append("5")
lista

lista.count('3')


# Lista Vazia

a = []
a.append(10)
a.append(50)
a


old = [20,30,50]
new_list = []

for item in old:
    new_list.append(item)

new_list


cidades = ["Recife","Manaus","Salvador"]
cidades.extend(["Fortaleza","Palmas"])
print(cidades)


cidades.index("Salvador")


# Insere e retira um elemento na lista em uma posicao especifica

print(cidades)
cidades.insert(2, 110)
print(cidades)
cidades.remove(110)
print(cidades)


# Inverter a lista

cidades.reverse()
cidades


lista = [34,32,56, 0, -3, -44, 100]
lista.sort()
lista

