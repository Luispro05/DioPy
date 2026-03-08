class ConversorTemperatura:
    def celsius_para_fahrenheit(self, celsius):
        fahrenheit = (celsius * 9/5)+32
        return fahrenheit 

celsius = float(input())

conversor = ConversorTemperatura()

fahrenheit = conversor.celsius_para_fahrenheit(celsius)
print(fahrenheit)