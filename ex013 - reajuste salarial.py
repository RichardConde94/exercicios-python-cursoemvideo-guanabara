#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.


salario = float(input("Qual o salário? "))
novo_salario = salario + (salario * 15 / 100)

print(f"O salário vai aumentar de R${salario:.2f} para R${novo_salario:.2f}")
