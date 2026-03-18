#faça um programa que leia uma medida em metros e mostre na tela a conversão para centímetros e milímetros


metros = float(input("Digite uma medida em metros: "))

centimetros = metros * 100
milimetros = metros * 1000

print("A conversão de ", round(metros, 2), "m para centímetros é ", round(centimetros, 1), "cm e para milímetros é ", round(milimetros, 1), "mm.",sep="")
print()

print("A conversão de " + str(round(metros, 2)) + "m para centímetros é " + str(round(centimetros, 1)) + "cm e para milímetros é " + str(round(milimetros, 1)) + "mm.")
print()

print("A conversão de {:.2f}m para centímetros é {:.1f}cm e para milímetros é {:.1f}mm.".format(metros,centimetros,milimetros))
print()

print(f"A conversão de {metros:.2f}m para centímetros é {centimetros:.1f}cm e para milímetros é {milimetros:.1f}mm.")
