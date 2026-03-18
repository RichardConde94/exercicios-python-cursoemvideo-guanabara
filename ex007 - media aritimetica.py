#faça um programa que leia duas notas de um aluno e mostre na tela a sua media.


nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
media = (nota1 + nota2) / 2

print("A média das duas provas do aluno é: ", round(media,1), sep="")
print()

print("A média das duas provas do aluno é: " + str(round(media, 1)))
print()

print("A média das duas provas do aluno é: {:.1f}".format(media))
print()

print(f"A média das duas provas do aluno é: {media:.1f}")
