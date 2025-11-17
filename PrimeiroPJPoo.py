class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("plim plim..")

    def parar(self):
        print("Parando bicicleta ...")
        print("Biclicleta parada!!")

    def correr(self):
        print("Vrummm...")

    #def __str__(self):
        #return f"Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"                

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f"{chave}={valor}" for chave, valor in self.__dict__.items()])}"


B1 = Bicicleta("vermelha", "caloi", 2022, 600)
B1.buzinar()
B1.correr()
B1.parar()
print(B1)