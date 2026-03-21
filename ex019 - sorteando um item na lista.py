#um professor quer sortear um dos seus alunos para apagar o quadro.
#faça um programa que o ajude escrevendo o nome deles e o nome do escolhido.

from random import choice

aluno1 = str(input("Digite o nome do primeiro aluno: ")).capitalize()
aluno2 = str(input("Digite o nome do segundo aluno: ")).capitalize()
aluno3 = str(input("Digite o nome do terceiro aluno: ")).capitalize()
aluno4 = str(input("Digite o nome do quarto aluno: ")).capitalize()

lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(lista)

print(f"O aluno escolhido para apagar o quadro foi: {escolhido}")