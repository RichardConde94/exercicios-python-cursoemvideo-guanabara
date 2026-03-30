#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint


print("-=-="*15)
print("Vou escolher um número de 0 a 5.Tente adivinhar qual é. ")
print("-=-="*15)
computador = randint(0, 5)
usuario = int(input('Digite um número entre 0 e 5 e veja se acertou: '))
if usuario == computador:
    print("Parabéns! Você acertou!")
else:
    print("Você errou!")
print(f"Eu escolhi {computador} e você {usuario}")