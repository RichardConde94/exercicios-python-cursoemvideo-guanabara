#Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.


nome = str(input("Digite um nome completo: ")).title().strip()
separa = nome.split()
print(f"Você escreveu {nome}\n"
      f"O primeiro nome é {separa[0]}\n"
      f"e o ultimo nome é {separa[-1]}")
