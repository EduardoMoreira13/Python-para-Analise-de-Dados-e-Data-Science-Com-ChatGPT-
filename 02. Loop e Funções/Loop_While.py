### Loop While

# Usando while para imprimir os valores de 0 a 9

valor = 0
while valor < 10:
    print(valor)
    valor = valor + 1


# Usando o loop com else para finalizar o loop

valor = 0
while valor < 10:
    print(valor)
    valor += 1
else:
    print("Loop encerrado!")




# ### Pass, Break, Continue


# interromper um loop ou continuar o loop - break e pass


valor = 0
while valor < 10:
    if valor == 12:
        print("Loop encerrado!")
        break
    else:
        pass
    print(valor)
    valor = valor + 1
else:
    print("Loop encerrado!")



# continuar pulando valores - continue

for letra in "Python e zzz incrivel":
    if letra == "z":
        continue
    print(letra)


### Comando While e For juntos



# Encontrando numeros primos entre 2 e 30 usando loop e while


# armazenamento da lista

primos = []

for num in range(2, 31 ,1):
    
    # Variavel de Controle
    eh_primo = True
    
    # Verificando se o numero e primo
    i = 2
    while i <= num // 2:
        if num % i == 0:
            eh_primo = False
            break
        i += 1
           
    # Verificando se o numero e primo
    if eh_primo: primos.append(num)

# Imprimindo os valores
print(primos)

