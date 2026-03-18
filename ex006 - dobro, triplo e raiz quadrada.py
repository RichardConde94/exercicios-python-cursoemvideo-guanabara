#faça um programa que leia um numero e mostre na tela o seu dobro, triplo e sua raiz quadrada.


n1 = float(input("Digite um número: "))

dobro = n1 * 2
triplo = n1 * 3
raiz = n1 ** (1/2)

print("O dobro de ",n1," é ",round(dobro, 2), ", o triplo é ",round(triplo,2), " e a raiz quadrada é ", round(raiz,2),sep="")
print()

print("O dobro de " + str(round(n1, 2)) + " é " + str(round(dobro, 2)) + ", o triplo é " + str(round(triplo, 2)) + " e a raiz quadrada é " + str(round(raiz, 2)))
print()

print("O dobro de {:.2f} é {:.2f}, o triplo é {:.2f} e a raiz quadrada é {:.2f}".format(n1,dobro,triplo,raiz))
print()

print(f"O dobro de {n1:.2f} é {dobro:.2f}, o triplo é {triplo:.2f} e a raiz quadrada é {raiz:.2f}")
