#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

#A condição para que 3 retas formem um triangulo é: cada um dos lados deve ser menor que a soma dos outros dois.


reta1 = int(input("Digite o tamanho da primeira reta: "))
reta2 = int(input("Digite o tamanho da segunda reta: "))
reta3 = int(input("Digite o tamanho da terceira reta: "))

if reta1 < reta2 + reta3 and reta2 < reta3 + reta1 and reta3 < reta2 + reta1:
    print("As retas podem formar um triângulo")
else:
    print("As retas não podem formar um triângulo")