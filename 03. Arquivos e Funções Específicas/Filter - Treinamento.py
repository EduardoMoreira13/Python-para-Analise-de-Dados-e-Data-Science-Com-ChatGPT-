# FILTER

# O map aplica uma função em toda a estrutura e te retorna o mesmo número de elementos
# dessa estrutura (podemos usar condicional ou não).

# O filter aplica a função, mas só retorna os elementos que atendem uma condição de verdadeiro

lista = [1,2,3,4,5,6,7,8,9,10]

def funcao(x):
    if x <= 5:
        return x*100
    else:
        return x*10

print(list(map(funcao, lista)))

def funcao(x):
    if x <= 5:
        return True
    else:
        return False

print(list(filter(funcao, lista)))

print(list(filter(lambda num: num <= 5, lista)))


# filter() é projetada para filtrar os elementos de um único iterável com base em uma
# função de filtro fornecida.