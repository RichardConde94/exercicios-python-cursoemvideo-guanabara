#faça um programa que leia dois números e mostre a soma entre eles.


print("A soma entre ",1, " e ",2, " é: ",3,sep="")
print()
print("A soma entre " + str(1) + " e " + str(2) + " é: " + str(3))
print()

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = n1 + n2

print("A soma entre ",n1," e ",n2," é: ",soma, sep="")
print()

print("A soma entre " + str(n1) + " e " + str(n2) + " é: " + str(soma))
print()

print("A soma entre {} e {} é: {}".format(n1,n2,soma))
print()

print(f"A soma entre {n1} e {n2} é: {soma}")
