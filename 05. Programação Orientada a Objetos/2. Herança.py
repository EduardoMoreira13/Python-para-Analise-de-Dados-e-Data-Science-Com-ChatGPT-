# Criando a classe Animal - Super-classe
class Animal():

    def __init__(self):
        print("Animal criado.")

    def imprimir(self):
        print("Este é um animal.") # Serve para todos os animais

    def comer(self):
        print("Hora de comer.") # Serve para todos os animais

    def emitir_som(self): # Será especificado na sub-classe
        pass


# Criando a classe Cachorro - Sub-classe
class Cachorro(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Objeto Cachorro criado.")

    def emitir_som(self):
        print("Au au!")


# Criando a classe Gato - Sub-classe
class Gato(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Objeto Gato criado.")

    def emitir_som(self):
        print("Miau!")


# Criando um objeto (Instanciando a classe)
rex = Cachorro()


# Criando um objeto (Instanciando a classe)
zeze = Gato()
rex.emitir_som()
zeze.emitir_som()


# Executando o método da classe Cachorro (sub-classe)
rex.imprimir()


# Executando o método da classe Animal (super-classe)
rex.comer()


# Executando o método da classe Cachorro (sub-classe)
zeze.comer()