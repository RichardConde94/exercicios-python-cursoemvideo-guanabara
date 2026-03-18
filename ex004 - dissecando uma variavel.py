#faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele.


algo = input("Digite algo: ")

print("O tipo primitivo desse valor é: ", type(algo))
print("É um número ou letra? ", algo.isalnum())
print("É uma letra? ", algo.isalpha())
print("Está em minúsculo? ",algo.islower())
print("É um dígito? ",algo.isdigit())
print("É um número? ", algo.isnumeric())
print("É um algarismo decimal? ", algo.isdecimal())
print("É um espaço vazio? ", algo.isspace())
print("Está em maiúsculo? ", algo.isupper())
print("Está com as iniciais em maiúsculo? ", algo.istitle())
print("Você digitou: ", algo, sep="")