#faça um programa que leia um numero e mostre na tela a sua tabuada.


n1 = int(input("Digite um número para ver sua tabuada: "))

print("A tabuada de ", n1," é: ", sep="")

print(n1, " x 1 = ", n1 * 1, sep="")
print(n1, " x 2 = ", n1 * 2, sep="")
print(n1, " x 3 = ", n1 * 3, sep="")
print(n1, " x 4 = ", n1 * 4, sep="")
print(n1, " x 5 = ", n1 * 5, sep="")
print(n1, " x 6 = ", n1 * 6, sep="")
print(n1, " x 7 = ", n1 * 7, sep="")
print(n1, " x 8 = ", n1 * 8, sep="")
print(n1, " x 9 = ", n1 * 9, sep="")
print(n1, " x 10 = ", n1 * 10, sep="")
print()


print("A tabuada de " + str(n1) + " é: ")

print(str(n1) + " x 1 = " + str(n1 * 1))
print(str(n1) + " x 2 = " + str(n1 * 2))
print(str(n1) + " x 3 = " + str(n1 * 3))
print(str(n1) + " x 4 = " + str(n1 * 4))
print(str(n1) + " x 5 = " + str(n1 * 5))
print(str(n1) + " x 6 = " + str(n1 * 6))
print(str(n1) + " x 7 = " + str(n1 * 7))
print(str(n1) + " x 8 = " + str(n1 * 8))
print(str(n1) + " x 9 = " + str(n1 * 9))
print(str(n1) + " x 10 = " + str(n1 * 10))
print()


print("A tabuada de {} é: ".format(n1))

print("{} x 1 = {}".format(n1, n1 * 1))
print("{} x 2 = {}".format(n1, n1 * 2))
print("{} x 3 = {}".format(n1, n1 * 3))
print("{} x 4 = {}".format(n1, n1 * 4))
print("{} x 5 = {}".format(n1, n1 * 5))
print("{} x 6 = {}".format(n1, n1 * 6))
print("{} x 7 = {}".format(n1, n1 * 7))
print("{} x 8 = {}".format(n1, n1 * 8))
print("{} x 9 = {}".format(n1, n1 * 9))
print("{} x 10 = {}".format(n1, n1 * 10))
print()


print(f"A tabuada de {n1} é: ")

print(f"""
{n1} x 1 = {n1*1}
{n1} x 2 = {n1*2}
{n1} x 3 = {n1*3}
{n1} x 4 = {n1*4}
{n1} x 5 = {n1*5}
{n1} x 6 = {n1*6}
{n1} x 7 = {n1*7}
{n1} x 8 = {n1*8}   
{n1} x 9 = {n1*9}
{n1} x 10 = {n1*10}""")
