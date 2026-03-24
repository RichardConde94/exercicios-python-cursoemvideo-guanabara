#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo,
#calcule e mostre o comprimento da hipotenusa.


from math import hypot

cateto_oposto = float(input("Digite o cateto oposto: "))
cateto_adjacente = float(input("Digite o cateto adjacente: "))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
#forma de resolver sem importação:
# hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** 0.5

print(f"A hipotenusa dos catetos é {hipotenusa:.2f}")
