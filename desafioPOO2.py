class Calculadora:

    def soma(self, num1, num2):
        return num1 + num2

    def sub(self, num1, num2):
        return num1 - num2   
    
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

calc = Calculadora()

resultado = calc.soma(num1, num2)
print(resultado)