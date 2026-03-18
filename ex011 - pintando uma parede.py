#Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.


altura = float(input("Digite uma altura em metros: "))
largura = float(input("Digite uma largura em metros: "))
area = altura * largura
tinta = area / 2

print(f"""Sua parede tem uma área total de {area:.2f}m² e serão necessários {tinta:.2f}l de tinta para pintá-la por completo.""")