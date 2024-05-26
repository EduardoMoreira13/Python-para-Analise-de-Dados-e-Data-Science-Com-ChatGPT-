# Lambda

# Construir funções que não precisam ser definidas, geralmente serão utilizadas poucas vezes

preco = 1500

def calcular(p, taxa): # Uso tradicional
    return p * taxa

print(f"{calcular(preco, 0.3):.2f}".replace(".",","))


calcular = lambda x,y: x * y # Uso de lamda

print(f"{calcular(preco,0.3):.2f}".replace(".",","))

calcular = lambda x: x * 0.3 # Uso de lamda

print(f"{calcular(preco):.2f}".replace(".",","))


# Uso com a função map

lista = [20,33,50,36,21,67,80,44,23,76]
lista2 = [valor*2 for valor in lista]
print(lista)
print(lista2)

lista2 = list(map(lambda x: x * 2, lista))
print(lista2)