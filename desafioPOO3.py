class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")

nome = input()
idade = int(input())

inst = Pessoa(nome, idade)

inst.mostrar()

