#crie um prorgrama que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.


#import math
from math import floor, trunc

num = float(input("Digite um número real: "))

print(f"A parte inteira de {num} é {floor(num)}")
print()

print(f"A parte inteira de {num} é {int(num)}")
print()

print(f"A parte inteira de {num} é {trunc(num)}")
