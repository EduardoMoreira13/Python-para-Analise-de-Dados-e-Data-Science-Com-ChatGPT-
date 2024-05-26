### Funcões

# Definindo uma funcao

def primeiraFunc():
    print("Hello World")
    
primeiraFunc()


# Definindo uma funcao

def primeiraFunc():
    nome = "Eduardo"
    print("Hello %s" %(nome))
    
primeiraFunc()


# Definindo uma funcao com parametros

def segundaFunc(nome):
    print("Hello, %s!" %(nome))
    
segundaFunc("Eduardo Moreira")


# Funcao para imprimir numeros

def imprimenumeros(inferior, superior, salto):
    lista = []
    for i in range(inferior, superior + 1, salto):
        lista.append(i)
    print(lista)
    
imprimenumeros(0, 50, 2)


# Funcao com numero variavel de argumentos

def printvarinf(arg1, *vartuple):
    
    # Imprimindo o valor do primeiro argumento
    print("Parametro 1:", arg1)

    # Imprimindo os outros argumentos
    for item in vartuple:
        print("Parametro 1:", item)
    return;

printvarinf(10)
print("\n")
printvarinf("Eduardo", "Moreira", 10)


# ### Escopo Variavel - local e global


# Variavel Global

var_global = 10 

# Funcao
def multiplica_numeros(num1,num2):
    var_local = num1 * num2 # Variavel local
    print(var_local)


### Fazendo Split dos Dados

def split_string_palavras(text):
    return text.split(" ")


texto = "Separacao de palavras a partir de uma funcao"

split_string_palavras(texto)

