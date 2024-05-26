## Exercícios

# Exercício 1 - Crie um objeto a partir da classe abaixo, chamado roc1, 
# passando 2 parâmetros e depois faça uma chamada aos atributos e métodos

from math import sqrt

class Rocket():
     
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def move_rocket(self, x_increment=0, y_increment=1):
        self.x += x_increment
        self.y += y_increment
        
    def print_rocket(self):
        print(self.x, self.y)
        

rocket = Rocket(x=100, y=50)
print(rocket.x)
print(rocket.y)

rocket.move_rocket(100, 50)
print(rocket.x)
print(rocket.y)

rocket.print_rocket()

print("\n")


# Exercício 2 - Crie uma classe chamada Pessoa() com os atributos: nome, cidade, telefone e e-mail. Use pelo menos 2
# métodos especiais na sua classe. Crie um objeto da sua classe e faça uma chamada a pelo menos um dos seus métodos
# especiais.

class Pessoa():

    def __init__(self, nome, cidade, telefone, email):
        self.nome = nome
        self.cidade = cidade
        self.telefone = telefone
        self.email = email

    def descricao(self):
        print(f"{self.nome} mora na cidade {self.cidade}, tem telefone: {self.telefone} e email: {self.email}")


    def escrita(self, idade = 0):
        self.idade = idade
        self.nome = self.nome.upper()
        print(f"O nome é igual a {self.nome} e a idade é igual a {self.idade}")

    def  __str__(self):
        return "O usuário " + self.nome + " mora na cidade " + self.cidade


pessoa1 = Pessoa("Eduardo","Brasília",6199998888, "eduardo_13hotmail.com")
print(pessoa1.nome)

pessoa1.descricao()
pessoa1.escrita(20)
print(str(pessoa1))

print("\n")


# Exercício 3 - Crie a classe Smartphone com 2 atributos, tamanho e interface e crie a classe MP3Player com os 
# atributos capacidade. A classe MP3player deve herdar os atributos da classe Smartphone.

class Smartphone():

    def __init__(self, tamanho = 'Grande', interface = 'Led'):
        self.tamanho = tamanho
        self.interface = interface

class MP3Player(Smartphone):

    def __init__(self, capacidade = 5, tamanho = 'Pequeno', interface = 'Led'):
        Smartphone.__init__(self, tamanho, interface)
        self.capacidade = capacidade

objeto1 = MP3Player(10, interface = "HD")

print(objeto1.tamanho)
print(objeto1.interface)
print(objeto1.capacidade)

