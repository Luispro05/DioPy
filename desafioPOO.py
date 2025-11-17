class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0
    
    def acelerar(self, incremento):
        self.velocidade += incremento

    def frear(self, decremento):
        self.velocidade -= decremento
        if self.velocidade < 0:
            self.velocidade = 0
    
    def mostrar_velocidade(self):
        print(f"velocidade atual:{self.velocidade} km/h")

meu_carro = Carro("Honda", "Civic", 2018)
meu_carro.acelerar(120)
meu_carro.mostrar_velocidade()