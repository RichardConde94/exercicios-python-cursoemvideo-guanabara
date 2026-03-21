#O mesmo professor quer agora sortear a ordem de apresentação dos trabalhos desses 4 alunos.
# Em vez de escolher apenas um,o programa deve mostrar a lista completa em uma ordem aleatória.


from random import shuffle

aluno1 = str(input("Digite o nome do primeiro aluno: ")).capitalize()
aluno2 = str(input("Digite o nome do segundo aluno: ")).capitalize()
aluno3 = str(input("Digite o nome do terceiro aluno: ")).capitalize()
aluno4 = str(input("Digite o nome do quarto aluno: ")).capitalize()

lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)

print(f"A sequência de apresentação será: {lista}")
