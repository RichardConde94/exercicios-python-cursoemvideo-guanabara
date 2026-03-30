#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.


salario = float(input("Qual o salário do funcionário? "))

if salario > 1250:
    novo_salario = salario + (salario * 10 / 100)
    print(f"O novo salário sera de R${novo_salario:.2f}")
else:
    novo_salario = salario + (salario * 15 / 100)
    print(f"O novo salário será de R${novo_salario:.2f}")
