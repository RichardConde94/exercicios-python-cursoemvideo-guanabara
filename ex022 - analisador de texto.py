# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras no total(sem considerar os espaços)
# Quantas letras tem o primeiro nome

nome = str(input("Digite seu nome completo: ")).strip().title()
print(f"Você digitou: {nome}")
separa = nome.split()

print(f"O seu nome em letras maiúsculas é {nome.upper()},\n"
      f"em letras minúsculas é {nome.lower()},\n"
      f"ao todo seu nome tem {len(nome) - nome.count(' ')} letras e\n"
      f"o primeiro nome tem {len(separa[0])} letras.")
