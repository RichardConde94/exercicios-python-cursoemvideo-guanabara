# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e
# a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.


dias = int(input("Por quantos dias o carro ficou alugado? "))
km = float(input("Quantos quilômetros foram rodados durante o aluguel? "))
valor_dia = dias * 60
valor_km = km * 0.15

print(f"O valor a ser pago pelo aluguel será de R${valor_km + valor_dia:.2f}, sendo R${dias * 60:.2f} pelas diárias e R${valor_km:.2f} pela quilometragem rodada")
