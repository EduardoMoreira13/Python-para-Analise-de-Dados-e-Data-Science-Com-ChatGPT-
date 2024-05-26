# Programação Orientada a objeto

class Vendedor():

    def __init__(self, nome): # Atributos e definição de valores iniciais
        self.nome = nome
        self.vendas = 0

    def vendeu(self, vendas):
        self.vendas = vendas

    def meta(self, meta):
        if self.vendas > meta:
            print(f"{self.nome} bateu a meta!")
        else:
            print(f"{self.nome} não bateu a meta!")


Vendedor1 = Vendedor("Eduardo") # Criação de uma instância
print(Vendedor1.nome)
Vendedor1.meta(500)
Vendedor1.vendeu(1000)
Vendedor1.meta(500)

Vendedor2 = Vendedor("Selma") # Criação de uma instância
print(Vendedor2.nome)
Vendedor2.meta(500)
Vendedor2.vendeu(300)
Vendedor2.meta(500)

# É possivel modularizar classes (separar o código)


# Manipulação de atributos de uma classe

print(hasattr(Vendedor1, "nome")) # Tem nome no objeto vendedor 1?
print(hasattr(Vendedor1, "vendas")) # Tem vendas no objeto vendedor 1?

print(getattr(Vendedor1, "nome")) # Retorne o nome no objeto vendedor 1?
print(getattr(Vendedor1, "vendas")) # Retorne as vendas no objeto vendedor 1?

print(getattr(Vendedor1, "nome")) # Retorne o nome no objeto vendedor 1?
print(getattr(Vendedor1, "vendas")) # Retorne as vendas no objeto vendedor 1?

setattr(Vendedor1, "nome", "Edu") # Definição ou alteração de um atributo?
print(getattr(Vendedor1, "nome")) # Retorne o nome no objeto vendedor 1?
setattr(Vendedor1, "vendas", 4500) # Definição ou alteração de um atributo?
print(getattr(Vendedor1, "vendas")) # Retorne as vendas no objeto vendedor 1?

delattr(Vendedor1, "nome") # deletando atributo
print(hasattr(Vendedor1, "nome")) # Tem nome no objeto vendedor 1?