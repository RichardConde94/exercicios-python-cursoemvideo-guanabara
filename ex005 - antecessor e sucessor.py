#faça um programa que leia um numero e mostre na tela o seu antecessor e seu sucessor.


n1 = int(input("Digite um número: "))

print("O antecessor de ", n1," é ", n1-1, " e o sucessor de ",n1," é ",n1 + 1, sep="")
print()

print("O antecessor de " + str(n1) + " é " + str(n1-1) + " e o sucessor de " + str(n1) + " é " + str(n1+1))
print()

print("O antecessor de {} é {} e o sucessor de {} é {}".format(n1,n1-1,n1,n1+1))
print()

print(f"O antecessor de {n1} é {n1-1} e o sucessor de {n1} é {n1+1}")
