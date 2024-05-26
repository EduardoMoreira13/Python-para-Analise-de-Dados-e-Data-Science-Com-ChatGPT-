### Condicional IF

# if

if 5 > 2:
    print("Verdadeiro")


# if com mais de uma condicao

if 5 > 20:
    print("Verdadeiro")
else:
    print("Falso")


# if com variavel

dia = "quarta"

if dia == "terca":
    print("Verdadeiro")
else:
    print("Falso")


# if com varias condicoes

numero = 10

if numero > 20:
    print("Verdadeiro")
elif numero == 20:
    print("Verdadeiro")
else:
    print("Falso")


# ### Operadores Relacionais

6 > 3
6 >= 3
6 < 3
6 <= 6
6 == 6
6 != 7


# ### Condicionais aninhados

idade = 17
nome = "Eduardo"


# In[31]:


if idade >=18:
    if nome == "Eduardo":
        print("Eduardo, maior de idade")
    else:
         print(nome, ", maior de idade")
else:
    if nome == "Eduardo":
        print("Eduardo, menor de idade")
    else:
         print(nome, ", menor de idade")


if (idade >=18) and (nome == "Eduardo"):
    print("Eduardo, maior de idade")
elif (idade < 18) and (nome == "Eduardo"):
    print("Eduardo, menor de idade")
elif (idade >= 18) and (nome != "Eduardo"):
    print(nome,", maior de idade")
else:
    print(nome,", menor de idade")


# ### Operadores Logicos - not, and, or


# Usando AND

nota = 80
disciplina = "Estatistica"

if (disciplina == "Estatistica") and (nota > 70):
    print("A sua nota em estatistica e:", nota)


# Usando OR

nota = 20
disciplina = "Estatistica"

if (disciplina == "Estatistica") or (disciplina == "Matematica"):
    print("A sua nota em", disciplina, "e:", nota)


# Usando NOT

nota = 80
disciplina = "Estatistica"

if (disciplina == "Estatistica") and (not nota < 70):
    print("A sua nota em estatistica e:", nota)
    
if disciplina == "Estatistica" and nota > 70:
    print("A sua nota em estatistica e:", nota)


# Usando IN

nota = 20
disciplina = ["Estatistica", "Matematica"]

if "Estatistica" in disciplina:
    print("A sua nota em Estatistica e:", nota)


# Usando NOT IN

nota = 20
disciplina = ["Ciencias", "Matematica"]

if "Estatistica" not in disciplina:
    print("A sua nota em Estatistica nao foi informada")



# Usando Placeholder

nota = 80
disciplina = 'Estatistica'
semestre = 2

if (disciplina == "Estatistica") and (nota > 70) and (semestre == 2):
    print("A sua nota em %s e %r referente ao semestre %r:" %(disciplina, nota, semestre))

