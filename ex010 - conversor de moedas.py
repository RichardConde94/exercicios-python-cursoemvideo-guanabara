#faça um programa que leia um valor em real e mostre na tela a sua conversão para dólar.

real = float(input("Digite um valor em reais: "))
#considerando o valor do dólar em R$5,59
dolar = real / 5.59

print("O valor de R$", round(real, 2)," convertido para dólar é US$", round(dolar, 2), sep="")
print()

print("O valor de R$" + str(round(real, 2)) + " convertido para dólar é US$" + str(round(dolar, 2)))
print()

print("O valor de R${:.2f} convertido para dólar é US${:.2f}".format(real, dolar))
print()

print(f"O valor de R${real:.2f} convertido para dólar é US${dolar:.2f}")
