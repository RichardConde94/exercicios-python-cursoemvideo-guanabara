# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.


celcius = float(input("Digite a temperatura em graus Celsius: "))
fahrenheit = celcius * 1.8 + 32

print(f"A temperatura de {celcius:.1f}ºC convertida para Fahrenheit é: {fahrenheit:.1f}ºF")


# o inverso

fahrenheit = float(input("Digite a temperatura em graus Farenheit: "))
celcius = (fahrenheit - 32) / 1.8

print(f"A temperatura de {fahrenheit:.1f}ºF convertida para Celcius é: {celcius:.1f}ºC")