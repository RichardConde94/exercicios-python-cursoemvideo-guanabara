#faça um programa que pergunte o nome de uma pessoa e faça uma mensagem de boas vindas.


nome = str(input("Digite o seu nome: ")).strip().title()

print("É um prazer te conhecer, ", nome, "!",sep="")
print()

print("É um prazer te conhecer, " + nome + "!")
print()

print("É um prazer te conhecer, {}!".format(nome))
print()

print(f"É um prazer te conhecer, {nome}!")
